import gym

def fixed_strategy(observation):
    # Based on the observation, decide which action to take
    cart_position, cart_velocity, pole_angle, pole_angular_velocity = observation
    
    # If the pole is leaning to the left, push the cart to the left
    # If the pole is leaning to the right, push the cart to the right
    if pole_angle < 0:
        return 0
    else:
        return 1

env = gym.make("CartPole-v1")
observation = env.reset()
score = 0

for _ in range(1000):
    env.render()
    action = fixed_strategy(observation)
    observation, reward, terminated, truncated, _ = env.step(action)
    score += reward
    if terminated or truncated:
        observation = env.reset()
        print('done, score=', score)
        score = 0

env.close()
