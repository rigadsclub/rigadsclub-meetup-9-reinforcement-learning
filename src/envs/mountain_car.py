import gym
from time import sleep

env = gym.make('MountainCarContinuous-v0')
observation = env.reset()

while True:
    env.render()
    action = env.action_space.sample()
    observation, reward, done, info = env.step(action)
    print("Observation:", observation, "Reward:", reward, "Done:", done)
    sleep(0.08)
    if done:
        break
