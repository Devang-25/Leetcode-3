class Solution(object):

  def areSentencesSimilarTwo(self, words1, words2, pairs):
    """
    :type words1: List[str]
    :type words2: List[str]
    :type pairs: List[List[str]]
    :rtype: bool
    """
    self.word_dict = {}
    self.pairs = pairs

    self.process()

    if len(words1) != len(words2):
      return False

    for w1, w2 in zip(words1, words2):
      if w1 == w2:
        continue
      # if (w1 or w2) not in self.word_dict:
      #   return False
      p1 = self.find_parent(w1)
      p2 = self.find_parent(w2)
      if p1 != p2:
        return False

    return True

  def process(self):
    for pair in self.pairs:
      w1, w2 = pair[0], pair[1]
      if w1 not in self.word_dict:
        self.word_dict[w1] = w1
      if w1 in self.word_dict and w2 not in self.word_dict:
        parent = self.find_parent(self.word_dict[w1])
        self.word_dict[w2] = parent
      elif w1 in self.word_dict and w2 in self.word_dict:
        p1 = self.find_parent(self.word_dict[w1])
        p2 = self.find_parent(self.word_dict[w2])
        self.union(p1, p2)

  def find_parent(self, w):
    if w not in self.word_dict:
      return None
    elif self.word_dict[w] == w:
      return w
    else:
      return self.find_parent(self.word_dict[w])

  def union(self, x, y):
    x_set = self.find_parent(x)
    y_set = self.find_parent(y)
    if x_set != y_set:
      self.word_dict[x_set] = y_set


#########################

s = Solution()

# words1 = ["great", "acting", "skills"]
# words2 = ["fine", "drama", "talent"]
# pairs = [["great", "fine"], ["drama", "acting"], ["skills", "talent"]]

# r = s.areSentencesSimilar(words1, words2, pairs)
# print("result", r)

# words1 = ["great", "acting", "skills"]
# words2 = ["fine", "painting", "talent"]
# pairs = [["great", "fine"], ["drama", "acting"], ["skills", "talent"]]

# r = s.areSentencesSimilar(words1, words2, pairs)
# print("result", r)

# words1 = ["great"]
# words2 = ["doubleplus", "good"]
# pairs = [["great", "doubleplus"]]

# r = s.areSentencesSimilar(words1, words2, pairs)
# print("result", r)

words1 = ["an", "extraordinary", "meal"]
words2 = ["a", "good", "dinner"]
pairs = [["great", "good"], ["extraordinary", "good"], ["well", "good"],
         ["wonderful", "good"], ["excellent", "good"], ["fine", "good"],
         ["nice", "good"], ["any", "one"], ["some", "one"], ["unique", "one"],
         ["the", "one"], ["an", "one"], ["single", "one"], ["a", "one"],
         ["truck", "car"], ["wagon", "car"], ["automobile", "car"],
         ["auto", "car"], ["vehicle", "car"], ["entertain", "have"],
         ["drink", "have"], ["eat", "have"], ["take",
                                              "have"], ["fruits", "meal"],
         ["brunch", "meal"], ["breakfast", "meal"], ["food", "meal"],
         ["dinner", "meal"], ["super", "meal"], ["lunch", "meal"],
         ["possess", "own"], ["keep", "own"], ["have", "own"],
         ["extremely", "very"], ["actually", "very"], ["really", "very"],
         ["super", "very"]]

r = s.areSentencesSimilar(words1, words2, pairs)
print("result", r)