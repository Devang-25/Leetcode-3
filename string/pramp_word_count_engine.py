"""
Word Count Engine
Implement a document scanning function wordCountEngine, which receives a string document and returns a list of all unique words in it and their number of occurrences, sorted by the number of occurrences in a descending order. If two or more words have the same count, they should be sorted according to their order in the original sentence. Assume that all letters are in english alphabet. You function should be case-insensitive, so for instance, the words “Perfect” and “perfect” should be considered the same word.

The engine should strip out punctuation (even in the middle of a word) and use whitespaces to separate words.

Analyze the time and space complexities of your solution. Try to optimize for time while keeping a polynomial space complexity.

Examples:

input:  document = "Practice makes perfect. you'll only
                    get Perfect by practice. just practice!"

output: [ ["practice", "3"], ["perfect", "2"],
          ["makes", "1"], ["youll", "1"], ["only", "1"],
          ["get", "1"], ["by", "1"], ["just", "1"] ]"""

from collections import defaultdict
import string

def word_count_engine(document):
  """
  input document: str
  return output: list[[str, int]]
  decending order

  # split
  # take out the puction
  # change to lower cases
  # iter: count , store
  """

  data = document.lower()
  data = ''.join(c for c in data if c not in string.punctuation)
  data = data.split()
  print(data)

  counter_dict = defaultdict(int)

  for ele in data:
    counter_dict[ele] += 1
  print(counter_dict.items())

  #print(data.index("youll"))
  result = sorted(counter_dict.items(), key=lambda x: (x[1], -data.index(x[0])), reverse=True)
  print('result', result)
  final_result = []

  for (key, value) in result:
    pair = [key, str(value)]
    final_result.append(pair)

  return final_result

a = "Practice makes perfect, you'll get perfecT by practice. just practice! just just just!!"
b = "To be, or not to be, that is the question:"

word_count_engine(b)
