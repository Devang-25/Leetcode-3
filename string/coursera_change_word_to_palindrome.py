'''
Input:
letter = [
  "abc",
  "abcc"
]

rule:
- each time you can only change down a letter by one step
- eg: c -> b -> a


output: array

'''


#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'mystery' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts STRING_ARRAY letter as parameter.
#

def mystery(letter):

  def process(word):
    i = 0
    j = len(word) - 1
    steps = 0
    while i < j:
      steps += abs(ord(word[i]) - ord(word[j]))
      i += 1
      j -= 1
    return steps

  results = []
  for item in letter:
    steps = process(item)
    results.append(steps)

  return results


letter = [
  "abc",
  "abcc"
]

print(mystery(letter))
