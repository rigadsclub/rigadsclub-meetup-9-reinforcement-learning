import gym
from IPython.display import clear_output
from time import sleep
import os

env = gym.make('Taxi-v3')
env.reset()
env.s = 328
#env = gym.make("MountainCarContinuous-v0")
#env.render()
#print(env.action_space)
#print(env.env.get_action_meanings())
#print(env.observation_space)


def clear():
    os.system('clear')


def print_frames(frames):
    for i, frame in enumerate(frames):
        clear_output(wait=True)
        print(frame['frame'])
        print(f"Timestep: {i + 1}")
        print(f"State: {frame['state']}")
        print(f"Action: {frame['action']}")
        print(f"Reward: {frame['reward']}")
        sleep(.1)


done = False

epochs = 0
penalties, reward = 0, 0

frames = [] # for animation


while not done:
    action = env.action_space.sample()
    state, reward, done, info = env.step(action)

    if reward == -10:
        penalties += 1

    # Put each rendered frame into dict for animation
    frames.append({
        'frame': env.render(mode='ansi'),
        'state': state,
        'action': action,
        'reward': reward
    }
    )

    epochs += 1

print_frames(frames)

input("Press Enter to continue...")