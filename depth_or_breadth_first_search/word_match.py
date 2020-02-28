from typing import List
from collections import Counter

# class Token:
# def is_word(self) -> bool: pass
# def word(self) -> str: pass
# def choice(self) -> List[str]: pass


class Token:

  def __init__(self, data):
    self.data_ = data
    self.is_word_ = type(data) == str

  def is_word(self) -> bool:
    return self.is_word_

  def word(self) -> str:
    assert self.is_word()
    return self.data_

  def choice(self) -> List[str]:
    assert not self.is_word()
    return self.data_


class Match:

  def match(self, query: List[Token], doc: List[str]) -> bool:
    """Returns true if doc matches all tokens in the query.

    Rules:
    - matching is unordered.
    - if a token is a word, it needs to be in the doc
    - if a token is a choice of words, one of the words needs to be in the doc.

    query = [
      ['hello', 'world'],
      'hello',
    ]

    doc = ['hello', 'world']
    """
    self.query = query
    self.cache = {}  # key: index of token, value: index of matching word
    self.doc = Counter(doc) # key: word, value: count
    
    return self.recursion(0)

  def recursion(self, i):
    print("i:", i)
    if i == len(self.query):
      return True
    token = self.query[i]
    if token.is_word():
      check, key = self.check_word_in_doc(i)
      print("word", check, key)
    elif not token.is_word():
      check, key = self.check_choice_in_doc(i)
      print("choice", check, key)
    if check:
      self.cache[i] = key
      return self.recursion(i + 1)
    elif i == 0 and not check:
      print("i==0 and not check")
      return False
    elif not check:
      # go back to previous layer until you have reache a layer with choice Token
      # try other word in that choice token
      print("return to previous level")
      return self.recursion(i - 1)

  def check_word_in_doc(self, i):
    """
    return bool and index of word
    """
    word = self.query[i].word()
    if i in self.cache:
      self.doc[word] += 1
    if word in self.doc and self.doc[word] > 0:
      self.doc[word] -= 1
      return True, 0
    return False, None

  def check_choice_in_doc(self, i):
    """
    return true if choice in doc else False and match word index

    if i is in self.cache:
      # then the new match word must has a greater value than existing key
    """
    choice = self.query[i].choice()

    if i not in self.cache:
      for index, word in enumerate(choice):
        if word in self.doc and self.doc[word] > 0:
          self.doc[word] -= 1
          return True, index
      return False, None

    old_index = self.cache[i]
    old_word = choice[old_index]
    self.doc[old_word] += 1

    for index in range(old_index + 1, len(choice)):
      word = choice[index]
      if word in self.doc and self.doc[word] > 0:
        self.doc[word] -= 1
        return True, index
      return False, None


token1 = Token(["hello", "world"])
token2 = Token("hello")

query = [token1, token2]

doc = ["hello", "world"]

m = Match()
result = m.match(query, doc)
print("result", result)
print(m.cache)
