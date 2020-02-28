import os
import random
from collections import defaultdict
import math
import numpy as numpy
from numpy.random import choice

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
    """
    purpose: given a state, return all the posiisble action of that state
    """
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
    """
    purpose: check if a state is and end state
    """
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
    """
    purpose: given the state and action, return the reward

    Note: usually reward also depends on the new state,
          but in this blackjack, action already decide the reward.
    """
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

    # dprint("Results are: ")
    # for result in results:
    #   dprint(result)

    return results

  # Compute set of states reachable from startState.  Helper function for
  # MDPAlgorithms to know which states to compute values and policies for.
  # This function sets |self.states| to be the set of all states.
  def computeStates(self):
    """
    purpose: starting from the startState, compute all the possible states
    """
    self.states = set()
    queue = []
    # print("check type", type(self.startsState()))
    self.states.add(self.startState())
    queue.append(self.startState())
    while len(queue) > 0:
      state = queue.pop()
      for action in self.actions(state):
        for prob, reward, newState in self.succProbState(state, action):
          if newState not in self.states:
            self.states.add(newState)
            queue.append(newState)
    dprint("%d states" % len(self.states))
    dprint("states:", self.states)


###################  Q-Learning with Feature Extraction ##########


class QLearningWithFeatureExtraction(BlackJack):

  def __init__(self, cardValues, multiplicity, threshold, peekCost, discount,
               epsilon, maxIterations, numTrials):
    super().__init__(cardValues, multiplicity, threshold, peekCost)

    self.discount = discount
    self.epsilon = epsilon
    self.weights = defaultdict(float)
    self.iterations = 0
    self.maxIterations = maxIterations
    self.numTrials = numTrials

    # self.Q_opt = defaultdict(float) 

    # dprint("super inital weight", self.weights)

  def get_action(self, state):
    """
    purpose: decide when to take a random action and when to take an action tht maximize your utility
    """
    self.iterations += 1
    # dprint("state to get action", state)
    if random.random() < self.epsilon:
      dprint("random action",)
      return random.choice(self.actions(state))
    else:
      dprint("max aciton",)
      # results = [
      #     (self.Q(state, action), action) for action in self.actions(state)
      # ]
      # dprint("all possible Q and action", results)
      return max(
          (self.Q(state, action), action) for action in self.actions(state))[1]

  def eta(self):
    """
    purpose: update your learning rate eta based on the number of iterations
    """
    return 1.0 / math.sqrt(self.iterations)

  def feature_extraction(self, state, action):
    """
    purpose: given the state and action of blackjack game, return the feature function φ(s, a),
    where state = (total, nextCard, counts)

    Rule for features:
    -- Indicator for the action and the current total (1 feature).
    -- Indicator for the action and the presence/absence of each face value in the deck.
          Example: if the deck is (3, 4, 0, 2), then your indicator on the presence of each card is (1, 1, 0, 1)
          Note: only add this feature if the deck is not None.
    -- Indicators for the action and the number of cards remaining with each face value (len(counts) features).
          Note: only add these features if the deck is not None.
    """
    total, next_card, counts = state

    features = [((action, total), 1)]
    if counts is not None:
      presence = tuple(1 if count else 0 for count in counts)
      features.append(((action, presence), 1))
    for face_value, count in enumerate(counts):
      feature = ((action, face_value, count), 1)
      features.append(feature)
    return features

  def Q(self, state, action):
    """
    purpose: given a state and action, return the estimated optimal Q (Q_est_opt) for that state and action.
    
    procedure:
      - use the state and action to get the feature (self.feacture_extracion(state, action))
      - for each (f, v): 
        - get w: self.weights[f]
        - Q_est_opt(s,a) = w * v
      - return Q_est_opt(s, )
    
    return: float

    note: if the state is endstate, its Q is 0.
    """
    if self.isEnd(state):
      return 0

    for f, v in self.feature_extraction(state, action):
      w = self.weights[f]
      Q = w * v
    return Q

  def update_weight(self, state, action, reward, new_state):
    """
    purpose: update the weight based on (state, action, reward, new_state)
 
    procuedue:
    - for (state, action) -- extract --> features: [(feature, val), (feacture, val)....]
    - for each pair of (feature, val):
      - update weight of that speciifc feacture:
        w[f] = w - eta(Q_est_opt(s, a) - (reward + discount * V_est_opt(new_state)))*feacture_value
    
    Note:
      if state is endState(), no need to update
    """
    # dprint("initial weight", self.weights)

    if self.isEnd(state):
      dprint("update weight but state {} is end state".format(state))
      return
    eta = self.eta()
    Q_est_opt = self.Q(state, action)
    V_est_opt = max(self.Q(new_state, action) for action in self.actions(state))
    target = reward + self.discount * V_est_opt

    for (feature, val) in self.feature_extraction(state, action):
      self.weights[feature] -= eta * (Q_est_opt - target) * val

  def train(self):
    os.system("clear")
    for trail in range(self.numTrials):
      dprint("trail: {}".format(trail))
      state = self.startState()
      for i in range(self.maxIterations):
        dprint("\ntrai:{}, iteration:{}".format(trail, i))
        dprint("state", state)
        if self.isEnd(state):
          dprint("end state")
          break
        action = self.get_action(state)
        dprint("action", action)
        # [(prob, reward, new_state)]
        transitions = self.succProbState(state, action)
        if len(transitions) == 0:
          self.update_weight(state, action, 0, None)
          break

        p = [prob for (prob, reward, new_state) in transitions]
        # dprint('candidates\n', candidates)
        i = choice(len(transitions), p=p)
        prob, reward, new_state = transitions[i]
        dprint("reward:{}, new_state:{}".format(reward, new_state))

        # update weight using the reward and new_state
        self.update_weight(state, action, reward, new_state)

        state = new_state


##################### Initial the Game ###################

cardValues = list(range(1, 14))
multiplicity = 4
threshold = 6
peekCost = 1
discount = 1.0
epsilon = 0.2
maxIterations = 1000
numTrials = 10

############ testing the BlackJack Game Mechanism ########
game = BlackJack(cardValues, multiplicity, threshold, peekCost)

# game.computeStates()
# print("all the possible state", game.states)

############### Testing the Q-learning with Feature Extraction Function #########

ql = QLearningWithFeatureExtraction(cardValues, multiplicity, threshold,
                                    peekCost, discount, epsilon, maxIterations,
                                    numTrials)
# state = ql.startState()

# action = ql.get_action(state)
# print(action)

# features = ql.feature_extraction(state, action)
# for (f, v) in features:
#   print(f, "|", v, "|", ql.weights[f])

# results = ql.succProbState(state, action)  # [(prob, reward, new_state)]

# # udpate weights
# prob, reward, new_state = results[0]
# print("state:{}, action:{}, prob:{}, reward:{}, new_state:{}".format(
#     state, action, prob, reward, new_state))

# ql.update_weight(state, action, reward, new_state)

# print(ql.isEnd((4, None, None)))

ql.train()
print("weights\n")
for f, val in ql.weights.items():
  print("f:{}, val:{}, Q:{}".format(
      key,
      val,
  ))
