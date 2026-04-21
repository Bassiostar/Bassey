import random

def simulate_probability(trials=100000):
    basket = ['R'] * 1 + ['B'] * 6 + ['W'] * 3
    
    first_ball_white_count = 0
    both_balls_white_count = 0
    
    for _ in range(trials):
        first_draw = random.choice(basket)
        
        if first_draw == 'W':
            first_ball_white_count += 1
            
            second_draw = random.choice(basket)
            
            if second_draw == 'W':
                both_balls_white_count += 1
                
    if first_ball_white_count == 0:
        return 0
        
    return both_balls_white_count / first_ball_white_count
probability = simulate_probability()
print(f"Simulated Probability: {probability:.4f}")
print(f"Theoretical Probability: {3/10}")