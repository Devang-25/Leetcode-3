"""
For a markov decision progress (MDP) problem, change the original transition function T(s, a, s') to:
T'(s, a, s') = 1/2T(s, a, s') + 1/2(1/|{s":T(s, a, s") > 0}|).

Let:
V1 = expected utility of orignal mdp with T(s, a, s')
V2 = expected utility of new mdp with T'(s, a, s'). 

Problem:
Is it alwasy true that V1(start_state) >= V2(start_state)? 
If not true, please give an counter example. 


Thought:
- It is not always true that V1(start_state) >= V2(start_state). 
- Reason: 
  - the new T'(s, a, s') kind like did a normalization of the orignal transition function T(s, a, s'). 
  - New new T'(s, a, s') add a positive fix number to each of the original transition prob for each node;
  - this make the orignal higher T() smaller, and originally smaller T() bigger. 
  - and if the higher T has a lower Reward, and 
  - smaller T has a larger reward, than T' would increase the prob for the bigger reward and lower the prob for the smaller reward

"""


class MDP(object):

  def __init__(self):
    self.V = {}

    for i in range(1, 4):
      self.V[i] = 0

  def startState(self):
    return 0

  def states(self):
    return [0, 1, 2, 3]

  def actions(self):
    return ["action"]

  def T(self, state, modified=False):
    # transitional function
    if not modified:
      if state == 1:
        return 0.5
      elif state == 2:
        return 0.25
      elif state == 3:
        return 0.25
    elif modified:
      return (0.5 * self.T(state) + 0.5 * (1 / 3))

  def R(self, state):
    if state == 1:
      return 10
    if state == 2:
      return 100
    if state == 3:
      return 100

  def succProbState(self, state, action, modified):
    """
    (prob, reward, s')
    """
    results = []
    if state == 0:
      results.append((self.T(1, modified=modified), self.R(1), 1))
      results.append((self.T(2, modified=modified), self.R(2), 2))
      results.append((self.T(3, modified=modified), self.R(3), 3))
    return results

  def Q(self, state, action, modified):
    return sum((prob * (reward + self.V[future_state])
                for prob, reward, future_state in self.succProbState(
                    state, action, modified)))


mdp = MDP()

##### test code block ###########
# print(mdp.R(2))
# print(mdp.T(1, modified=False))
# print(mdp.T(1, modified=True))
# print(mdp.Q(0, "action"))

V1 = mdp.Q(0, "action", False)
V2 = mdp.Q(0, "action", True)
print("V1:{}, V2:{}".format(V1, V2))