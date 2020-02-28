"""
problem: 
There are three players:
1) agent: who try with pi_max strategy
2) opp: who try with pi_min strategy
3) coin: who is 1/2

game: you pick a bin (1, 2, 3), then for 1/2 chance the coin would choose to rotate the bin. 
Then from the rotated order of bins, opp would pick a value. 

problem: compute the V_expectminimax
"""

import random

debug = True


def dprint(*args, **kwargs):
  if debug:
    print(*args, **kwargs)


class Game(object):

  def __init__(self):
    self.A = (-50, 50)
    self.B = (1, 3)
    self.C = (-5, 15)

    # players
    self.agent = "agent"
    self.coin = "coin"
    self.opp = "opp"

    # pick the specific number agent pick for a bin
    self.pick = None

  def statestate(self):
    return (self.agent, [self.A, self.B, self.C], self.pick)

  def isEnd(self, state):
    player, bins, pick = state
    return (player == None)

  def succ(self, state):
    """
    purpose: input state and action, output: future state (player, bins)
    """
    player, bins, pick = state

    if player == self.agent:
      action = self.agentPolicy(state)
      return (self.coin, bins, action)

    elif player == self.coin:
      future_state = (self.opp, bins, pick)
      action = self.coinPolicy()
      dprint("Coin {}".format(action))
      if action == "rotate":
        bins = bins[1:] + [bins[0]]
      return (self.opp, bins, pick)

    elif player == self.opp:
      return (None, None, min(bins[pick]))

  def coinPolicy(self):
    """
    return an action for the coin
    """
    n = random.random()
    if n < 0.5:
      return "rotate"
    else:
      return "No rotate"

  def agentPolicy(self, state):
    player, bins, pick = state
    assert player == self.agent
    V = []
    """
    V_i = 1/2 (min of original bin) + 1/2 (min of rotated bin)
    """
    bins = bins + [bins[0]]
    for i in range(len(bins) - 1):
      V_i = (1 / 2) * (min(bins[i])) + (1 / 2) * (min(bins[i + 1]))
      V.append(V_i)
    dprint("expected V_expectminimax: ", V)
    dprint("The max among V_expectiminimax is: ", max(V))
    return V.index(max(V))

  def play(self):
    state = self.statestate()
    dprint("start game: bins", state[1])
    while True:
      player = state[0]
      if player == None:
        break
      new_state = self.succ(state)
      state = new_state
    return state[2]


game = Game()
print("the final V agent get is: {}".format(game.play()))
