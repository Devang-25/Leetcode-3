import os

##############
# Markov Decision Process MDP
"""
Transportation Problem:
- There are N stations. 
- starting from station1. 
- you have two actions: 1) walk (reward: -1); 2) tram (reward: -2)
- Walk would take you to next station: s -> s+1
- Tram would take you 2*station: s -> 2s

- There is a probability that if you take tram, the tram might fail and thus you stay at the original station.

describe this problem in the class below. 


Thought: 
Q: What functions do I need? 
"""


class TransportationMDP(object):
  walkCost = 1.5
  tramCost = 2
  failProb = 0.05

  def __init__(self, N):
    self.N = N  # num of stations

  def startState(self):
    return 1

  def isEnd(self, state):
    return state == self.N

  def actions(self, state):
    actions = []
    if state + 1 <= self.N:
      actions.append("walk")
    if state * 2 <= self.N:
      actions.append("tram")
    return actions

  def succProbState(self, state, action):
    """
    - given a state and an action, compute the successor states (or future state) with corresponding probability
    
    Return:
    (new_state, prob, reward):
      new_state = new state I end up
      prob = T(s, a, s')
      reward = R(s, a, s')
    """
    results = []
    if action == "walk":
      results.append((state + 1, 1, -self.walkCost))
    elif action == "tram":
      results.append((2 * state, 1 - self.failProb, -self.tramCost))
      results.append((state, self.failProb, -self.tramCost))
    return results

  def discount(self):
    return 1.0

  def states(self):
    return range(1, self.N + 1)


############################################################
# implement the iterative Policy Evalution Algorithm
# percy called this as Inference Algorithm


def valueIteration(mdp):
  V = {}  #{state: estimated opt utility}
  pi = {}  #{state: estimated pi_opt}

  # def Q(state, action):
  #   """
  #   purpose: calcuate the sum of the expected utility of a particular action
  #   mdp.succProbstate(state, action) = [(new_state, prob, reward)]
  #   """
  #   q = 0
  #   for (new_state, prob, reward) in mdp.succProbState(state, action):
  #     q += prob * (reward + mdp.discount() * V[new_state])
  #   return q

  def Q(state, action):
    """
    purpose: calcuate the sum of the expected utility of a particular action
    mdp.succProbstate(state, action) = [(new_state, prob, reward)]
    """
    return sum(prob * (reward + mdp.discount() * V[new_state])
               for (new_state, prob,
                    reward) in mdp.succProbState(state, action))

  # Initialize all V[state] = 0
  for state in mdp.states():
    V[state] = 0

  # start the iteration
  while True:
    newV = {}
    os.system("clear")
    for state in mdp.states():
      if mdp.isEnd(state):
        newV[state], pi[state] = 0, None
      else:
        newV[state], pi[state] = max(
            (Q(state, action), action) for action in mdp.actions(state))
      print("state:{}, newV[{}]:{}, policy[{}]:{}".format(
          state, state, newV[state], state, pi[state]))
    input()

    # check for convergence
    # if converge, we break from this while loop
    if max(abs(V[state] - newV[state]) for state in mdp.states()) < 1e-10:
      break

    V = newV


############################################################
# implement the iterative Value Iteration Algorithm
# percy called this as Inference Algorithm

###############
# testing the mdp model
mdp = TransportationMDP(20)
# print(mdp.isEnd(10))
# print(mdp.actions(5))
# print(mdp.actions(6))
# print("(new_state, prob, reward): ", mdp.succProbState(5, "tram"))

valueIteration(mdp)