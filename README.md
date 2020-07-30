# Introduction

## Riga Data Science Club
Riga Data Science Club is a non-profit organization to share ideas, experience and build machine learning projects together.

Our goal is to drive progress in the machine learning and artificial intelligence field.

- Follow us on [LinkedIn](https://www.linkedin.com/company/riga-ds-club)
- Join us [here](https://rigadsclub.com/join-us)

## Current Meetup: Reinforcement Learning Basics
The purpose of the meetup and this repository is to give basic understanding of Reinforcement Learning by practice. 
We are going to use [gym](https://gym.openai.com/) learning environment to do experiments, so make sure Python 3.6+ is installed with all other necessary packages as described in #Setup
 

# Setup
The following setup instructions are partially copied from OpenAI spinning up [resource](https://spinningup.openai.com/en/latest/user/installation.html) 
Feel free to use python environment manager of your choice or direct python installation.

## Anaconda
Download and install Anaconda. Follow the installation instructions for Anaconda [here](https://docs.continuum.io/anaconda/install/). 
Then create a conda Python 3.6 env for organizing packages for the purpose of this meetup:
```
conda create -n gym python=3.6
```
To use Python from the environment you just created, activate the environment with:
```
conda activate gym
```

## Installing OpenMPI

### Ubuntu
```
sudo apt-get update && sudo apt-get install libopenmpi-dev
```

### Mac OS X
```
brew install openmpi
```

## Installing Spinning Up
```
git clone https://github.com/openai/spinningup.git
cd spinningup
pip install -e .
```

# Q-learning
What’s ‘Q’?
The ‘q’ in q-learning stands for quality. Quality in this case represents how useful a given action is in gaining some future reward.

# Policy Gradient
The key idea underlying policy gradients is to push up the probabilities of actions that lead to higher return, and push down the probabilities of actions that lead to lower return, until you arrive at the optimal policy.
# Resources
1. Andrej Karpahy: [Deep Reinforcement Learning: Pong from Pixels](http://karpathy.github.io/2016/05/31/rl/)

2. Justin Francis: [Introduction to reinforcement learning and OpenAI Gym](https://www.oreilly.com/radar/introduction-to-reinforcement-learning-and-openai-gym/)

3. Charel van Hoof [Learn by example Reinforcement Learning with Gym](https://www.kaggle.com/charel/learn-by-example-reinforcement-learning-with-gym)

4. Ashish Rana: [Introduction: Reinforcement Learning with OpenAI Gym](https://towardsdatascience.com/reinforcement-learning-with-openai-d445c2c687d2)

5. Arthur Juliani:
    - [Simple Reinforcement Learning with Tensorflow Part 0: Q-Learning with Tables and Neural Networks](https://medium.com/emergent-future/simple-reinforcement-learning-with-tensorflow-part-0-q-learning-with-tables-and-neural-networks-d195264329d0)
    - [Simple Reinforcement Learning in Tensorflow: Part 1 - Two-armed Bandit](https://medium.com/@awjuliani/super-simple-reinforcement-learning-tutorial-part-1-fd544fab149)
    - [Simple Reinforcement Learning with Tensorflow: Part 2 - Policy-based Agents](https://medium.com/@awjuliani/super-simple-reinforcement-learning-tutorial-part-2-ded33892c724)
 
6. Satwik Kansal, Brendan Martin: [Reinforcement Q-Learning from Scratch in Python with OpenAI Gym](https://www.learndatasci.com/tutorials/reinforcement-q-learning-scratch-python-openai-gym/)

7. Andre Violante: [Simple Reinforcement Learning: Q-learning](https://towardsdatascience.com/simple-reinforcement-learning-q-learning-fcddc4b6fe56)

8. Amanda Iglesias Moreno: [Reinforcement learning framework and toolkits (Gym and Unity)](https://towardsdatascience.com/reinforcement-learning-framework-and-toolkits-gym-and-unity-1e047889c59a)

9. Aneek Das[Introduction to Q-Learning](https://towardsdatascience.com/introduction-to-q-learning-88d1c4f2b49c)