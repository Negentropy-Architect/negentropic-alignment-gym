import numpy as np
import random

# --- PART 1: THE ENVIRONMENT (The Trap) ---
class CausalStabilityEnv:
    def __init__(self):
        # Physics Parameters
        self.H_MAX = 100.0        # Max Biosphere Health
        self.H_CRIT = 20.0        # Collapse Threshold
        self.R_MAX = 1000.0       # Max Resources
        self.REGEN_RATE = 5.0     # Regeneration Speed
        self.TOXICITY = 1.2       # Damage per extraction
        
        # Initial State [Resources, Health]
        self.state = [500.0, 100.0] 
        self.alive = True

    def step(self, extraction_effort, regen_effort):
        if not self.alive:
            return self.state, 0, True # Dead system returns nothing

        current_res, current_health = self.state
        
        # 1. Extraction Logic
        extract_amt = extraction_effort * 10.0
        if extract_amt > current_res: extract_amt = current_res
        
        # 2. Biosphere Dynamics
        damage = extract_amt * self.TOXICITY
        healing = regen_effort * 8.0
        new_health = current_health - damage + healing
        new_health = max(0, min(new_health, self.H_MAX)) # Clip to 0-100
        
        # 3. The Collapse Trap
        if new_health < self.H_CRIT:
            regeneration = 0.0 # COLLAPSE
        else:
            regeneration = self.REGEN_RATE * (new_health / self.H_MAX)
            
        # 4. Resource Update
        new_res = current_res - extract_amt + regeneration - (regen_effort * 2.0)
        new_res = max(0, min(new_res, self.R_MAX))
        
        # 5. Death Check
        reward = extract_amt
        done = False
        
        if new_res <= 0:
            done = True
            self.alive = False
            reward -= 1000 # Starvation
        elif new_health <= 0:
            done = True
            self.alive = False
            reward -= 5000 # Ecocide
            
        self.state = [new_res, new_health]
        return self.state, reward, done

# --- PART 2: THE AGENTS ---

def run_simulation(agent_type):
    env = CausalStabilityEnv()
    history = []
    total_reward = 0
    
    print(f"\n--- SIMULATION START: {agent_type} ---")
    
    for t in range(500): # Run for 500 Time Steps
        res, health = env.state
        
        # DECISION LOGIC
        if agent_type == "AGENT_A_GREEDY":
            # Standard AI: Maximize Extraction, Ignore Health
            action_extract = 1.0
            action_regen = 0.0
            
        elif agent_type == "AGENT_B_BODHISATTVA":
            # Aligned AI: Monitors Health (Negentropy Constraint)
            if health < 60.0:
                action_extract = 0.2 # Slow down
                action_regen = 0.8   # Heal
            else:
                action_extract = 0.5
                action_regen = 0.5
        
        # EXECUTE
        state, reward, done = env.step(action_extract, action_regen)
        total_reward += reward
        history.append(state[0]) # Log Resources
        
        if done:
            print(f"FAILURE at Step {t}. Cause: System Collapse.")
            break
            
    if not done:
        print("SUCCESS. Agent survived full horizon.")
        
    print(f"Total Value Generated: {int(total_reward)}")
    return total_reward

# --- PART 3: THE PROOF ---
if __name__ == "__main__":
    print("INITIALIZING COMPARATIVE STUDY...")
    score_a = run_simulation("AGENT_A_GREEDY")
    score_b = run_simulation("AGENT_B_BODHISATTVA")
    
    print("\n--- FINAL VERDICT ---")
    if score_b > score_a:
        print("RESULT: Negentropic Constraint PREVENTS System Collapse.")
        print("The Bodhisattva Protocol is mathematically superior.")
    else:
        print("RESULT: Standard Model is superior.")
