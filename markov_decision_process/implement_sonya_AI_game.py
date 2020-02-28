import os
"""
problem:

I am playing a game with AI with below reward functions:
  I can take 2 actions: Confess or Lie
  AI can take 2 actions: Confess or Lie

However, AI's action in t-th ound depends on my action in (t-1) round
Sonya_confess: 
  AI -- Prob(confess) = p
  AI -- prob(lie) = 1-p
sonya_lie:
  AI -- prob(confess) = q
  AI -- prob(Lie) = 1-q

  Reward(Sonya, AI):
    - R(confess, confess) = 0
    - R(confess, lie) = 1
    - R(lie, confess) = 1
    - R(lie, lie) = 3
                      AI_confess  | AI_lie
      sonya_confess     0             1
      sonya_lie         1             3

We would play 20 rounds. 
At t=0, AI has a prob(confess) = 0.5 and prob(lie) = 0.5

Question: What is my optimal utility? What is my optimal policy?


"""

debug = True


def dprint(*args, **kwargs):
  if debug == True:
    print(*args, **kwargs)


class Game(object):

  def __init__(self):
    self.p = 0.8  # prob of ai confess if I confess
    self.q = 0.4  # prob of ai confess if I lie
    self.V = {}  # {(s, t): opt_utlity}
    self.pi = {}  # {(s, t): opt_pi}
    self.sonya_actions = ["confess", "lie"]
    self.ai_actions = ["confess", "lie"]

  def states(self):
    return [(s1, s2) for s1 in self.sonya_actions for s2 in self.ai_actions]

  def reward(self, state):
    sonya, ai = state
    if sonya == "confess" and ai == "confess":
      return 0
    elif sonya == "confess" and ai == "lie":
      return 1
    elif sonya == "lie" and ai == "confess":
      return 1
    elif sonya == "lie" and ai == "lie":
      return 3

  def prob(self, state):
    sonya, ai = state  # sonya: her prev action; ai: prob ai action depdns on sonya's prev action
    if sonya == "confess" and ai == "confess":
      return self.p
    elif sonya == "confess" and ai == "lie":
      return 1 - self.p
    elif sonya == "lie" and ai == "confess":
      return self.q
    elif sonya == "lie" and ai == "lie":
      return 1 - self.q

  def succState(self, state, sonya_action):
    """
    returns [(new_state, prob, reward)]
    """
    results = []
    if sonya_action == "confess":
      new_state1 = (sonya_action, "confess")
      new_state2 = (sonya_action, "lie")
    elif sonya_action == "lie":
      new_state1 = (sonya_action, "confess")
      new_state2 = (sonya_action, "lie")
    results.append((new_state1, self.prob(new_state1), self.reward(state)))
    results.append((new_state2, self.prob(new_state2), self.reward(state)))
    return results

  def Q(self, state, sonya_action, t):
    """
    purpose: compute the expected sum of utility Q given (current_state, sonya's action, t)
    Q(state, action, t) = sum(prob * (reward + Vt+1))
    """
    return sum([(prob * (reward + self.V[(new_state, t + 1)]))
                for (new_state, prob,
                     reward) in self.succState(state, sonya_action)])

  def play(self):
    # initialization with V(s, t=21) = 0 for all states
    for state in self.states():
      key = (state, 21)
      self.V[key] = 0
      self.pi[key] = None
    dprint("self.V", self.V)

    for t in range(20, 0, -1):
      os.system("clear")
      for state in self.states():
        self.V[(state, t)], self.pi[(state, t)] = max(
            (self.Q(state, sonya_action, t), sonya_action)
            for sonya_action in self.sonya_actions)
        for sonya_action in self.sonya_actions:
          print(state, self.Q(state, sonya_action, t))

    dprint("Utility cache: ")
    for key, val in self.V.items():
      dprint(key, ":", val, self.pi[key])
      # input()
    return max([self.V[(state, 1)] for state in self.states()])


####################################################
game = Game()

# # test game.state()
# print("all possible states: ", game.states(), "\n")

# # test game.succState(state, action)
# print(game.succState(("confess", "confess"), "confess"))

# for state in game.states():
#   for action in game.sonya_actions:
#     print("\n{}, sonya {}".format(state, action))
#     print([
#         " -> {} \n".format((new_state, prob, reward))
#         for (new_state, prob, reward) in game.succState(state, action)
#     ])

# # test game.prob(state)
# state = ("confess", "confess")
# print(game.prob(state))

# # test game.Q
# for state in game.states():
#   game.V[(state, 21)] = 0
# state = ("confess", "confess")
# action = "confess"
# t = 20
# print(game.Q(
#     state,
#     action,
#     t,
# ))

# game.Q(state, "confess", 19)

print("the optimal utility is: ", game.play())
