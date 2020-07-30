import gym
import numpy as np
import tensorflow as tf
env = gym.make('FrozenLake-v0')
# The grid with 4x4 gives 16 possible states, hence we have an array of 16 states.
inputs = tf.placeholder(shape=[1, 16],dtype=tf.float32)
# Each state has 4 possible outcomes, hence we have 16x4 matrix with weights uniformly distributed
weights = tf.Variable(tf.random_uniform([16,4],0,0.1))
# Find the dot product of inputs and the weights
Q1 = tf.matmul(inputs,weights)
# The next state will be the opted based on the argmax function.
output = tf.argmax(Q1,1)