"""  # O(NLogN)
  # arr = [1, 4, 5, 2, 3, 7, 8, 6, 10, 9]
  # arr = [1, 4, 5, 2]
#    k + index + k
# i=0: 0 + k = 0 + 2
# len(arr) - k times  * (2k + 1) == > O(N-k)* log(2K+1) < O(N*log(N))"""

# min heap

import heapq

def sort_k_messed_array(arr, k):
  """
  input arr: array of int
  input k: int
  output results: list of int, my sorted list
  """
  # heap = heapq.heapify(list(arr[:k])) # heap = [1, 4]
  heap = []
  for j in range(k):
    heapq.heappush(heap, arr[j])
  print(heap)
  results = []
  for i in range(k, len(arr)): # kth = 2th = 5
    heapq.heappush(heap, arr[i])
    min_ele = heapq.heappop(heap)
    results.append(min_ele)

  return results


arr1 = [1, 4, 5, 2, 3, 7, 8, 6, 10, 9]
k = 2

print(sort_k_messed_array(arr1, 2))




  
