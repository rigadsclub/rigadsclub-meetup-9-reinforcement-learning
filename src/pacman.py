import gym
env = gym.make("MsPacmanNoFrameskip-v4")
env.render()
print(env.action_space)
print(env.env.get_action_meanings())
print(env.observation_space)
input("Press Enter to continue...")