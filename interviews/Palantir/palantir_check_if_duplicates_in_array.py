"""
Check if a given array contains duplicate elements within k distance from each other

Given an unsorted array that may contain duplicates. Also given a number k which is smaller than size of array. Write a function that returns true if array contains duplicates within k distance.


Examples:

Input: k = 3, arr[] = {1, 2, 3, 4, 1, 2, 3, 4}
Output: false
All duplicates are more than k distance away.

Input: k = 3, arr[] = {1, 2, 3, 1, 4, 5}
Output: true
1 is repeated at distance 3.

Input: k = 3, arr[] = {1, 2, 3, 4, 5}
Output: false

Input: k = 3, arr[] = {1, 2, 3, 4, 4}
Output: true

"""

from collections import defaultdict


def check_duplicates(arr, k):
  """
    input:
        arr: list[int]
        k: int

    output:
        bool

    """

  cache = defaultdict(list)

  for i, ele in enumerate(arr):
    if len(cache[ele]) >= 1:
      if i - cache[ele][-1] <= k:
        return True
    cache[ele].append(i)
  return False


k = 3
arr = [1, 2, 3, 4, 1, 2, 3, 4]
# False

assert check_duplicates(arr, k) == False

arr = [1, 2, 3, 1, 4, 5]
assert check_duplicates(arr, k) == True

arr = []
assert check_duplicates(arr, k) == False
