"""
Given an array of integers arr, you’re asked to calculate for each index i the product of all integers except the integer at that index (i.e. except arr[i]). Implement a function arrayOfArrayProducts that takes an array of integers and returns an array of the products.

Solve without using division and analyze your solution’s time and space complexities.

Examples:

input:  arr = [8, 10, 2]
output: [20, 16, 80] # by calculating: [10*2, 8*2, 8*10]

input:  arr = [2, 7, 3, 4]
output: [84, 24, 56, 42] # by calculating: [7*3*4, 2*3*4, 2*7*4,

"""

import numpy as np

def array_of_array_products(arr):
  if len(arr) <= 1:
    return []

  n = len(arr)
  left_array = [1] * n
  right_array = [1] * n
  # left array
  for i in range(1, n):
    left_array[i] = left_array[i-1] * arr[i-1]
  # right array
  for j in range(n-2, -1, -1):
    right_array[j] = right_array[j+1] * arr[j+1]
  
  return [l*r for l,r in zip(left_array, right_array)]
  #return [left_array[i] * right_array[i] for i in range(n)]
  # return list(np.array(left_array) * np.array(right_array))
