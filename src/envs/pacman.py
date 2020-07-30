import gym
from time import sleep

env = gym.make('MsPacmanNoFrameskip-v4')
observation = env.reset()

while True:
    env.render()
    action = env.action_space.sample()
    observation, reward, done, info = env.step(action)
    print("Observation:", observation, "Reward:", reward, "Done:", done)
    sleep(0.05)
    if done:
        break



