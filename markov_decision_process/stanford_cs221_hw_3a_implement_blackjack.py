import os
import random

debug = True


def dprint(*args, **kwargs):
  if debug:
    print(*args, **kwargs)


class BlackJack(object):

  def __init__(self, cardValues, multiplicity, threshold, peekCost):
    """
    cardValues: list of integers (face values for each card included in the deck) eg: [1, 2, 3]
    multiplicity: single integer representing the number of cards with each face value
    threshold: maximum number of points (i.e. sum of card values in hand) before going bust
    peekCost: how much it costs to peek at the next card
    """
    self.cardValues = cardValues
    self.multiplicity = multiplicity
    self.threshold = threshold
    self.peekCost = peekCost
    self.cards = (self.multiplicity,) * len(self.cardValues)

    self.take = "take"
    self.peek = "peek"
    self.quit = "quit"

    self.peeked = False

  def startState(self):
    """
    state: (totalCardValueInHand, nextCardIndexIfPeeked, deckCardCounts)
    """
    return (0, None, (self.multiplicity,) * len(self.cardValues))

  def actions(self, state):
    totalCardValueInHand, nextCardIndexIfPeeked, deckCardCounts = state
    if totalCardValueInHand > self.threshold:
      return []
    elif totalCardValueInHand == self.threshold:
      return [self.quit]
    elif totalCardValueInHand < self.threshold and self.peeked == None:
      return [self.take, self.peek, self.quit]
    elif totalCardValueInHand < self.threshold and not self.peeked:
      return [self.take, self.quit]

  def isEnd(self, state):
    totalCardValueInHand, nextCardIndexIfPeeked, deckCardCounts = state
    if totalCardValueInHand > self.threshold:
      dprint("busted")
      return True
    # check if no more cards:
    # any():  any of the card still left
    # if not(any of the card is left)
    if not deckCardCounts:
      return True
    if not (any(deckCardCounts)):
      dprint("no more cards")
      return True
    return False

  def R(self, state, action):
    totalCardValueInHand, nextCardIndexIfPeeked, deckCardCounts = state
    if action == self.quit:  # only need to look at current state
      if totalCardValueInHand <= self.threshold:
        return totalCardValueInHand
      elif totalCardValueInHand > self.threshold:
        return 0
    elif action == self.peek:  # only need future state
      return -self.peekCost
    else:
      return 0

  def succProbState(self, state, action):
    """
    return: [(prob, reward, future_state)]
    """
    totalCardValueInHand, nextCardIndexIfPeeked, deckCardCounts = state
    results = []
    # print("deckCardCount", deckCardCounts)

    # 如果是EndState
    if totalCardValueInHand > self.threshold:
      prob = 1.0
      future_state = (0, None, None)
      # results.append((prob, 0, future_state))

    elif not deckCardCounts:
      future_state = (totalCardValueInHand, None, None)

    elif not (any(deckCardCounts)):  #没有牌了
      prob = 1.0
      future_state = (totalCardValueInHand, None, None)
      # results.append((prob, self.R(state, action), future_state))

    # if self.isEnd(state):
    #   return results

    # 如果不是endState()
    # 如果action是拿牌，上一轮没有peek, 还有牌
    elif action == self.take and (
        nextCardIndexIfPeeked == None) and deckCardCounts:
      for i in range(len(deckCardCounts)):
        if deckCardCounts[i] > 0:
          prob = deckCardCounts[i] / sum(deckCardCounts)
          deckCardCounts_new = list(deckCardCounts[:])
          deckCardCounts_new[i] -= 1
          future_state = (totalCardValueInHand + self.cardValues[i], None,
                          tuple(deckCardCounts_new))
          results.append((prob, self.R(state, action), future_state))

    # 如果action是拿牌，上一轮peeked
    elif action == self.take and type(nextCardIndexIfPeeked) == int:
      deckCardCounts[nextCardIndexIfPeeked] -= 1
      prob = 1.0
      future_state = (
          totalCardValueInHand + self.cardValues[nextCardIndexIfPeeked], None,
          tuple(deckCardCounts))
      results.append((prob, self.R(state, action), future_state))

    # action要看牌，没看过牌， 还有牌
    elif (not self.peeked) and (action == self.peek) and any(deckCardCounts):
      for i in range(len(deckCardCounts)):
        if deckCardCounts[i] > 0:
          prob = deckCardCounts[i] / sum(deckCardCounts)
          deckCardCounts_new = list(deckCardCounts[:])
          deckCardCounts_new[i] -= 1
          future_state = (totalCardValueInHand, i, tuple(deckCardCounts_new))
          results.append((prob, self.R(state, action), future_state))
      self.peeked = True

    elif action == self.quit:
      prob = 1.0
      future_state = (totalCardValueInHand, None, None)
      results.append((prob, self.R(state, action), future_state))

    dprint("Results are: ")
    for result in results:
      dprint(result)
    return results

  # Compute set of states reachable from startState.  Helper function for
  # MDPAlgorithms to know which states to compute values and policies for.
  # This function sets |self.states| to be the set of all states.
  def computeStates(self):
    self.states = set()
    queue = []
    print("check type", type(self.startState()))
    # self.states.add(self.startState())
    queue.append(self.startState())
    while len(queue) > 0:
      state = queue.pop()
      for action in self.actions(state):
        for prob, reward, newState in self.succProbState(state, action):
          if newState not in self.states:
            self.states.add(newState)
            queue.append(newState)
    print("%d states" % len(self.states))
    print("states:", self.states)


cardValues = list(range(1, 14))
multiplicity = 4
threshold = 4
peekCost = 1

game = BlackJack(cardValues, multiplicity, threshold, peekCost)
# print(game.startState())

# state = (2, None, (1, 0, 1))
# print(game.isEnd(state))
# state = (5, None, (0, 0, 0))
# print(game.isEnd(state))
# state = (0, None, None)
# print(game.isEnd(state))
# state = (4, None, (0, 0, 0))
# print(game.isEnd(state))

# state = (5, None, (0, 0, 0))
# print(game.R(state, game.quit))

# state = (4, None, (0, 0, 0))
# print(game.R(state, game.quit))

# state = (4, None, None)
# print(game.R(state, game.quit))

# state = (3, 0, (1, 1, 1))
# print(game.R(state, game.peek))

state = game.startState()
print(type(state))
print("start state", state)
# game.succProbState(state, game.take)
# game.succProbState(state, game.peek)
# print(game.succProbState(state, game.peek))

# state = (0, 0, [1, 1, 1])
# game.succProbState(state, game.take)
# print(game.succProbState(state, game.take))

game.computeStates()