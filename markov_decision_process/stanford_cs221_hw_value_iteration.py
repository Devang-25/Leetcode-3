"""
link: https://web.stanford.edu/class/cs221/assignments/blackjack/index.html

Problem 1: Value Iteration
In this problem, you will perform the value iteration updates manually on a very basic game just to solidify your intuitions about solving MDPs. 

The set of possible states in this game is {-2, -1, 0, 1, 2}. 

You start at state 0, and if you reach either -2 or 2, the game ends. At each state, you can take one of two actions: {-1, +1}.

If you're in state s and choose -1:
You have an 80% chance of reaching the state s−1.
You have a 20% chance of reaching the state s+1.

If you're in state s and choose +1:
You have a 70% chance of reaching the state s+1.
You have a 30% chance of reaching the state s−1.

If your action results in transitioning to state -2, then you receive a reward of 20. 
If your action results in transitioning to state 2, then your reward is 100. 
Otherwise, your reward is -5. Assume the discount factor γ is 1.

[3 points] Give the value of Vopt(s) for each state s after 0, 1, and 2 iterations of value iteration. Iteration 0 just initializes all the values of V to 0. Terminal states do not have any optimal policies and take on a value of 0.
[3 points] What is the resulting optimal policy πopt for all non-terminal states?

"""

import os

debug = True


def dprint(*args, **kwargs):
  if debug == True:
    print(*args, **kwargs)


class Game(object):

  def __init__(self):
    self.p = 0.8  #prob of reach s-1 if action is -1.
    self.q = 0.3  # prob of reach s+1 if action is +1
    self.V = {}  # {state: opt_reward}
    self.pi = {}  # {state: opt_action}

    # initialization
    for state in self.states():
      self.V[state] = 0
    print("init", self.V)

  def states(self):
    return [-2, -1, 0, 1, 2]

  def actions(self):
    return [-1, 1]

  def isEnd(self, state):
    return (state == 2) or (state == -2)

  def reward(self, new_state):
    if new_state == 2:
      return 100
    elif new_state == -2:
      return 20
    else:
      return -5

  def discount(self):
    return 1.0

  def succState(self, state, action):
    """
    return [(prob, reward, new_state)] given state, action

    rule:
      If you're in state s and choose -1:
      You have an 80% chance of reaching the state s−1.
      You have a 20% chance of reaching the state s+1.

      If you're in state s and choose +1:
      You have a 70% chance of reaching the state s+1.
      You have a 30% chance of reaching the state s−1.
    """
    # assert ((state != 2) and (state != -2))
    results = []
    if action == -1:
      results.append((self.p, self.reward(state - 1), state - 1))
      results.append((1 - self.p, self.reward(state + 1), state + 1))
    elif action == 1:
      results.append((self.q, self.reward(state + 1), state + 1))
      results.append((1 - self.q, self.reward(state - 1), state - 1))
    return results

  def Q(self, state, action):
    return sum((
        prob * (self.reward(new_state) + self.discount() * self.V[(new_state)]))
               for (prob, reward, new_state) in self.succState(state, action))

  def valueIteration(self):

    while True:
      os.system("clear")
      newV = {}
      for state in self.states():
        if self.isEnd(state):
          newV[state], self.pi[state] = 0, None
        else:
          newV[state], self.pi[state] = max(
              (self.Q(state, action), action) for action in self.actions())
          print("state:{}, V_opt:{}, pi_opt:{}".format(state, newV[state],
                                                       self.pi[state]))
      input()

      # converge condition
      if max(self.V[state] - newV[state] for state in self.states()) < 1e-10:
        break
      self.V = newV


game = Game()

# test game.states()
print(game.states())

print(game.isEnd(-2))
print(game.isEnd(2))

print("all possible actionss are:", game.actions())

# test game.succState()
# print(game.succState(2, 1))
# print(game.succState(-2, 1))
# print(game.succState(0, 1))

# test game.Q()
# print(game.Q(1, +1))

game.valueIteration()
