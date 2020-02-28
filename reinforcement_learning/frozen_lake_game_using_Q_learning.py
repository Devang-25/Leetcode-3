"""
https://medium.com/swlh/introduction-to-reinforcement-learning-coding-q-learning-part-3-9778366a41c0

purpose: use Q-leanring algorithm to play or to figure out the optimal value V_opt from the game)

Education: 

- generate a random action:
env.action_space.sample()

- take an action:
  env.step(action)
  Returns observation, reward, done, info.


- render the environement:
env.reset()


Matrix size:
Q: 16x4 matrix
b/c there map is 4x4, but every grid has 4 possibility of states (start, frozen, hot, destination).
You don't know the state of each grid when you start the game.
So you estimate there are 16 possible state, 
and with each state, you could possibly has 4 action: 0, 1, 2, 3: left, right, down, up.
Total: 16 * 4

action:
0: left
1: right
2: down
3: up

For every state F, the agent gets 0 reward, 
for state H it gets -1 reward as in state H the agent will die and 
upon reaching the goal, the agent gets +1 reward.

"""

import gym
import os
import numpy as np
import pickle

debug = True


def dprint(*args, **kwargs):
  if debug:
    print(*args, **kwargs)


env = gym.make('FrozenLake-v0')
env.render()

epsilon = 0.9  # the chance I would choose a random action
# epsilon = 0.0 # no exploration
total_episodes = 10000
max_steps = 100

eta = 0.81  # or you can call it learning_rate in the example
discount = 0.96

dprint("states:{}, actions:{}".format(env.observation_space.n,
                                      env.action_space.n))

# initilize Q to be all zeros
Q = np.zeros((env.observation_space.n, env.action_space.n))
dprint("inital Q", Q)


def choose_action(state):
  if np.random.uniform(0, 1) < epsilon:
    action = env.action_space.sample()
    # dprint("random action", action)
  else:
    action = np.argmax(Q[state, :])
    # dprint("max action", action)
  return action


def learn(state, action, reward, future_state):
  """
  utility = rewared + discount * V_estimate(s')
  V_estimate(s') = max(Q[s', :])
  Q_estimate(s, a) = (1 - eta)*Q_estimate(s, a)  + eta * utility
  """
  utility = reward + discount * np.max(Q[future_state, :])
  Q[state, action] = (1 - eta) * Q[state, action] + eta * utility


def run():
  for episode in range(total_episodes):
    state = env.reset()

    if episode == 0:
      env.render()

    t = 0

    while t < max_steps:
      """
      1) choose an action
      2) take the action
      3) learn/update with new info
      4) check if already reach the destination: if done: break
      5) count step size: t+= 1
      """
      env.render()
      action = choose_action(state)
      # dprint("action:", action)
      future_state, reward, done, info = env.step(action)
      learn(state, action, reward, future_state)

      state = future_state

      t += 1

      if done:
        break
    # dprint("episode:{}, step_size:{}".format(episode, t))
  dprint("latest Q:\n", Q)

  with open("frozenLake_qTable.pkl", 'wb') as f:
    pickle.dump(Q, f)


########################################################################
# test choose_action()
# dprint("all space", env.observation_space)
# dprint(choose_action(1))
# dprint(choose_action(2))

# # learn()
# dprint(learn(0, 1, 3, 2))
# dprint("result Q\n", Q)

os.system("clear")
run()