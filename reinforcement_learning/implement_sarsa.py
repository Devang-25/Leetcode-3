"""
purpose: implement a SARSA (bootstrap: meaning update bit by bit)

game: 
start_state: you have a start state s_0
action: [stay, quit]
states: [in, end]

need to figure out: 
- T(s, a, s'): the transition function. 
  Q: how to update? 
    - T_esimate  = #times(s, a, s') occur / #times (s, a)
- R(s, a, s'): the reward.
  Q: how to figure out? how to update?
  - R_estimate = r in (s, a, r, s')

state: IN ----- action: stay ----> T: (in, stay)
    <--- T(in, stay, in)?reward? -                    
  |                                |
  |                                |
action: quit                  prob(end)? reward? 
  |                                |
  |                                |
T(in, quit) ----prob(end)? Reward?  ----> state: END


data: 
[in; stay, 4, in; stay, 4, in; stay, 4, in; stay, 4, end;]
[in; stay, 4, in; stay, 4, end;]
[in; stay, 4, end;]

Analysis: 
- update the utility Q(s, a) directly and iteratively (just like gradient descient).


"""

import os
import re
from collections import defaultdict

debug = True


def dprint(*args, **kwargs):
  if debug:
    print(*args, **kwargs)


class SARSA(object):

  def __init__(self):
    self.inState = "in"
    self.endState = "end"

    self.stay = "stay"
    self.quit = "quit"

    self.count = {}  #{(state, action): count_of(state, action)}
    self.eta = {}  # {(state, action): float}
    self.Q = {}  # {(state, action): estimate_Q}

    # initilization for estimating Reward and Transition Function
    """
    - for each epoch, 
    """
    for state in self.states():

      self.count[state] = {}
      self.eta[state] = {}
      self.Q[state] = {}
      for action in self.actions():
        self.count[state][action] = 0
        self.eta[state][action] = 0
        self.Q[state][action] = 0

  def states(self):
    return [self.inState, self.endState]

  def actions(self):
    return [self.stay, self.quit]

  def discount(self):
    return 1.0

  def update_eta(self, epoch):
    """
    input:
      epoch: str "in; stay, 4, in; stay, 4, end"
    return: None
    """
    epoch = re.split("; |, ", epoch)
    dprint("epoch", epoch)
    i = 0
    state, action, reward, new_state = epoch[i], epoch[i + 1], int(
        epoch[i + 2]), epoch[i + 3]
    self.eta[state][action] = 1 / (1 + self.count[state][action])
    self.count[state][action] += 1
    dprint("count", self.count)
    dprint("eta", self.eta)

  def update_Q(self, epoch):
    epoch = re.split(", |; ", epoch)
    i = 0
    state, action, reward, new_state = epoch[i], epoch[i + 1], int(
        epoch[i + 2]), epoch[i + 3]
    if new_state != self.endState:
      new_action = epoch[i + 4]
    else:
      new_action = self.stay
    eta = self.eta[state][action]
    Q = self.Q[state][action]
    dprint("eta:{}, Q:{}, reward:{}, Q_estimate:{}".format(
        eta, Q, reward, self.Q[new_state][new_action]))
    utility = reward + (self.discount() * self.Q[new_state][new_action])
    self.Q[state][action] = (1 - eta) * Q + eta * utility

  def estimate_mdp(self, data):
    """
    purpose: process the data and estimate the Reward and Transtion Function. 
    """

    for epoch in data:
      os.system("clear")
      self.update_eta(epoch)
      # dprint("eta", self.eta)
      self.update_Q(epoch)
      dprint("Q", self.Q)
      input()


################################################################################

data = [
    "in; stay, 4, end",
    "in; stay, 4, in; stay, 4, in; stay, 4, in; stay, 4, end",
    "in; stay, 4, in; stay, 4, end",
]

data = [
    "in; stay, 4, in; stay, 4, in; stay, 4, in; stay, 4, end",
    "in; stay, 4, in; stay, 4, end",
    "in; stay, 4, end",
    "in; quit, 100, end",
    "in; stay, 4, in; stay, 100, end",
]

# mc = ModelBasedMonteCarlo()
model = SARSA()
model.estimate_mdp(data)
