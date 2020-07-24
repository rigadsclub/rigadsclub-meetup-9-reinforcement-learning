import gym
import matplotlib.pyplot as plt
env = gym.make("SpaceInvadersNoFrameskip-v4")
env.render()
print("Observation space:", env.observation_space)
print(env.env.get_action_meanings())
input("Press Enter to continue...")