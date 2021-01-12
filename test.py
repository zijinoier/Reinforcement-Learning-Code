import gym
# import sys
# sys.path.append('./env/')

import gym_foo

env = gym.make('GridWorld-v0')  # 参数为环境的id

obs = env.reset()
env.render()
a = input("input:")
