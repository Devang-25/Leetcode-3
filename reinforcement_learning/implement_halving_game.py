"""
pauå™œrpose: using reinforcement learning to implement Having Game

Game:
- Start with a number N
- players take turns either decrementing N or replacing it with [N/2]
- The player that is left with 0 wins.


"""


class HalvingGame(object):

  def __init__(self, N):
    self.N = N

  # state = (player, number)
  def startState(self):
    return (+1, self.N)

  def isEnd(self, state):
    player, number = state
    return (number == 0)

  def actions(self, state):
    player, number = state
    return ["-", "/"]

  def succ(self, state, action):
    player, number = state

    if action == "-":
      return (-player, number - 1)
    elif action == "/":
      return (-player, int(number / 2))

  def utility(self, state):
    """
    agent's utility at the end state s
    agent: +1; if agent wins, agent gain +inf
    opponent: -1; if opponent wins, agent utility -inf

    """
    player, number = state
    return player * float("inf")

  def player(self, state):
    player, number = state
    return player


##############################################################################
# Modeling of Different Policies


def simplePolicy(game, state):
  action = "-"
  print("simple policy: state {} --> action {}".format(state, action))
  return action


def humanPolicy(game, state):
  # print("agent")
  while True:
    print("human policy: Enter a move for the state {} --> action ".format(
        state,))
    action = input().strip()
    # print("{}".format(action))
    if action in game.actions(state):
      return action


def minimaxPolicy(game, state):

  def recurrance(state):
    # return a a tuple (utility of the state, the action that give that uility)
    # if it is the base case, then just return the utility of the state
    print("state", state)
    if game.isEnd(state):
      return (game.utility(state), None)

    candidates = [(recurrance(game.succ(state, action))[0], action)
                  for action in game.actions(state)]

    print("candidates", candidates)
    player = state[0]
    if player == +1:
      return max(candidates)
    elif player == -1:
      return min(candidates)

  utility, action = recurrance(state)
  print("minimax policy: state {}, action {} with utility {}".format(
      state, action, utility))
  return action


####################################################################
# play the game

# choose a policy for human play (or called as agent) and opponent
policies = {
    +1: humanPolicy,
    # -1: simplePolicy,
    -1: minimaxPolicy,
}

game = HalvingGame(N=15)
state = game.startState()
# print("successor state after start state \n", game.succ(state, "/"))

while not game.isEnd(state):
  player = game.player(state)
  policy = policies[player]
  # ask policy to make a move
  action = policy(game, state)
  # advance the state
  state = game.succ(state, action)  # succ() return (player, number)
print("final utility of game is {}".format(game.utility(state)))