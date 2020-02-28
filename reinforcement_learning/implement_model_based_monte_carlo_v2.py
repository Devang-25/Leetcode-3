"""
purpose: implement a model_based monte carlo game

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

1st iteration: 
following the policy pi_(stay): 
- I choose action "stay" 4 times. 
- 3 times I reached state (s') "in"
- 1 times I reached state (s') "out"
- so the T_estimate:
  T_estimate(s, a, s') = T_estimate(in, stay, in) = 3/4
  T_estimate(s, a, s') = T_estimate(in, stay, end) = 1/4
- Reward_esimate:
  R_estimate(s, a, s') = R_estimate(in, stay, in) = $4
  R_estimate(s, a, s') = R_estimate(in, stay, out) = $4

2nd iteration:
- following the policy pi_(stay):
- update the T_estimate(s, a, s') and R_estimate(s, a, s'):
  - T_estimate(s, a, s') = T_estimate(in, stay, in) = 4/6
  - T_estimate(s, a, s') = T_estimate(in, stay, end) = 2/6
  - R_estimate(s, a, s') = R_estimate(in, stay, in) = $4
  - R_estimate(s, a, s') = R_estimate(in, stay, end) = $4


3rd iteration:
- following the policy pi_(stay):
- update the T_estimate(s, a, s') and R_estimate(s, a, s'):
  - T_estimate(s, a, s') = T_estimate(in, stay, in) = 5/7
  - T_estimate(s, a, s') = T_estimate(in, stay, end) = 3/7
  - R_estimate(s, a, s') = R_estimate(in, stay, in) = $4
  - R_estimate(s, a, s') = R_estimate(in, stay, end) = $4

eventually, the estimate converge to true value after a million time.
The result would be pretty accurate after a million time.
"""

import os
import re
from collections import defaultdict

debug = True


def dprint(*args, **kwargs):
  if debug:
    print(*args, **kwargs)


class ModelBasedMonteCarlo(object):

  def __init__(self):
    self.inState = "in"
    self.endState = "end"

    self.stay = "stay"
    self.quit = "quit"

    self.T_estimate = {}
    self.R_estimate = {}
    self.count = {}

    # initilization for estimating Reward and Transition Function
    """
    - first count all the occurance of (state, action, new_state) and (sate, action): self.count
    - then use self.count to compute estimate T(s, a, s') and R(s, a, s')
    """
    for state in self.states():
      self.T_estimate[state] = {}
      self.R_estimate[state] = {}
      self.count[state] = {}
      for action in self.actions():
        self.T_estimate[state][action] = {}
        self.R_estimate[state][action] = {}
        self.count[state][action] = {}
        for future_state in self.states():
          self.T_estimate[state][action][future_state] = 0.0
          self.R_estimate[state][action][future_state] = 0.0
          self.count[state][action][future_state] = 0.0
          self.count[state][action]["None"] = 0.0

  def states(self):
    return [self.inState, self.endState]

  def actions(self):
    return [self.stay, self.quit]

  def update_T(self, epoch):
    """
    inputs:
    data epoch: str "in; stay, 4, in; stay, 4, in; stay, 4, in; stay, 4, end;"

    update all the relavent T(s, a, s') in self.T

    return: None
    """
    epoch = re.split("; |, ", epoch)
    dprint("epoch", epoch)
    for i in range(0, len(epoch) - 1, 3):
      dprint(epoch[i], epoch[i + 1], epoch[i + 2], epoch[i + 3])
      state, action, reward, future_state = epoch[i], epoch[i + 1], epoch[
          i + 2], epoch[i + 3]
      self.count[state][action]["None"] += 1
      self.count[state][action][future_state] += 1
      # dprint(state, action, future_state, ":",
      #        self.count[state][action]["None"],
      #        self.count[state][action][future_state])

    # update
    dprint("updated count", self.count)
    for state in self.states():
      for action in self.actions():
        for future_state in self.states():
          if self.count[state][action]["None"] != 0.0:
            self.T_estimate[state][action][future_state] = self.count[state][
                action][future_state] / self.count[state][action]["None"]
            # self.R_estimate[state][action][future_state] = reward

  def update_R(self, epoch):
    """
    inputs:
    data str: "in; stay, 4, in; stay, 4, in; stay, 4, in; stay, 4, end;"

    update all the relavent R(s, a, s') in self. R

    return: None
    """
    epoch = re.split("; |, ", epoch)
    dprint("epoch", epoch)
    for i in range(0, len(epoch) - 1, 3):
      # dprint(epoch[i], epoch[i + 1], epoch[i + 2], epoch[i + 3])
      state, action, reward, future_state = epoch[i], epoch[i + 1], epoch[
          i + 2], epoch[i + 3]

      self.R_estimate[state][action][future_state] = float(reward)

  def estimate_mdp(self, data):
    """
    purpose: process the data and estimate the Reward and Transtion Function. 
    """

    for epoch in data:
      self.update_R(epoch)
      self.update_T(epoch)


class MDP(ModelBasedMonteCarlo):

  def __init__(self):
    # this inherit all the properties from parent class
    # ModelBasedMonteCarlo.__init__(self)

    # super() inherit all the property and methods from parent class
    super().__init__()

    self.inState = "in"
    self.endState = "end"

    self.stay = "stay"
    self.quit = "quit"

    self.V = {}
    self.pi = {}

    # initialization
    for state in self.states():
      self.V[state] = 0

  def startState(self):
    return self.inState

  def is_endState(self, state):
    return state == self.endState

  def states(self):
    return [self.inState, self.endState]

  def actions(self):
    return [self.stay, self.quit]

  def action(self, state):
    if state == self.inState:
      return [self.stay, self.quit]

  def T(self, state, action, future_state):
    return self.T_estimate[state][action][future_state]

  def R(self, state, action, future_state):
    return self.R_estimate[state][action][future_state]

  def succProbState(self, state, action):
    """
    return [(prob, reward, new_state)]
    return []

    """
    results = []
    new_states = [
        key for key in self.T_estimate[state][action].keys()
        if self.T_estimate[state][action][key] != 0.0
    ]
    for new_state in new_states:
      prob = self.T(state, action, new_state)
      reward = self.R(state, action, new_state)
      results.append((prob, reward, new_state))
    return results

  def Q(self, state, action):
    return sum(
        (prob * (reward + self.V[new_state])
         for prob, reward, new_state in self.succProbState(state, action)))

  def value_iteration_using_estimate_mdp(self, state):
    """
    purpose: compute optimal utility (Q or V) and policy pi using the value_iteration algroithm and your estimated mdp

    return: 
    - self.V: it is a dict given state: {state: int}
    - self.pi: it is a dict given state: {state: action}
    """
    while True:
      newV = {}
      # os.system("clear")
      for state in self.states():
        if self.is_endState(state):
          newV[state], self.pi[state] = 0, None
        else:
          newV[state], self.pi[state] = max(
              (self.Q(state, action), action) for action in self.action(state))
      if max(
          abs(newV[state] - self.V[state]) for state in self.states()) <= 1e-10:
        break
      self.V = newV


################################################################################

data = [
    "in; stay, 4, in; stay, 4, in; stay, 4, in; stay, 4, end",
    "in; stay, 4, in; stay, 4, end",
    "in; stay, 4, end",
]

data = [
    "in; stay, 4, in; stay, 4, in; stay, 4, in; stay, 4, end",
    "in; stay, 4, in; stay, 4, end",
    "in; stay, 4, end",
    "in; quit, 100, end",
    "in; stay, 4, in; stay, 100, end",
]

# mc = ModelBasedMonteCarlo()
model = MDP()
print("Utility dict", model.V)
print("R", model.R_estimate)
print("T", model.T_estimate)
print("Count", model.count)

# print(model.startState())

# print(model.is_endState("end"))
# print(model.is_endState("in"))

# print(model.states())
# print(model.action("in"))
# print(model.action("end"))

# process epoch
model.update_T(data[0])
# print("count", model.count, "\n")
# print("T_estimate", model.T_estimate, "\n")
model.update_R(data[0])
# print("R_estimate", model.R_estimate, "\n")

# test self.probSuccState()
# print(model.succProbState("in", "stay"))
# print(model.succProbState("in", "quit"))

# print(model.Q("in", "stay"))

model.estimate_mdp(data)
print(model.T)
print("count", model.count, "\n")
print("T_estimate", model.T_estimate, "\n")
print("R_estimate", model.R_estimate, "\n")

state = model.startState()
model.value_iteration_using_estimate_mdp(state)
print("V:", model.V)
print("policy", model.pi)
