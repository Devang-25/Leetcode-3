"""
worst case time complexity:
O(N*logN).
b/c I have to sort the freq_cache[freq] list before append to result
"""

from typing import List
from collections import defaultdict


class Solution:

  def topKFrequent(self, words: List[str], k: int) -> List[str]:
    word_counter = defaultdict(int)
    freq_cache = defaultdict(list)
    results = []

    for word in words:
      word_counter[word] += 1

    for word, freq in word_counter.items():
      freq_cache[freq].append(word)

    for freq in range(len(words), 0, -1):
      if freq in freq_cache:
        freq_cache[freq].sort()
        results += freq_cache[freq]

    return results[:k]


words = ["i", "love", "leetcode", "i", "love", "coding"]
k = 2
s = Solution()
r = s.topKFrequent(words, k)
print(r)

##############
"""
Use max heap to implement:
  - push (freq, w) into the max_heap
  - so heap would first sort based on feq, then on word alphebatically

"""

from collections import defaultdict
import heapq

# class MaxHeap:

#   def __init__(self):
#     self.max_heap = []

#   def push(self, item):
#     word, freq = item
#     heapq.heappush(self.max_heap, (-freq, word))

#   def pop(self):
#     freq, word = heapq.heappop(self.max_heap)
#     return (word, -freq)

#   def peek(self):
#     freq, word = self.max_heap[0]
#     return (word, -freq)


class Solution:

  def topKFrequent(self, words: List[str], k: int) -> List[str]:
    # step1: build counter word
    word_counter = defaultdict(int)

    for w in words:
      word_counter[w] += 1

    # step2: use min_heap to store top k
    min_heap = []
    for w, freq in word_counter.items():
      if len(min_heap) < k:
        heapq.heappush(min_heap, (freq, w))
      else:
        min_freq, min_w = min_heap[0]
        if freq > min_freq:
          heapq.heappop(min_heap)
          heapq.heappush(min_heap, (freq, w))

    # step3: append into results
    results = []

    while min_heap:
      freq, w = heapq.heappop(min_heap)
      results = [w] + results

    return results
