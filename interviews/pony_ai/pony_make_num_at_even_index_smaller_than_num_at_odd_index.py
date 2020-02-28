'''
给我一个int数组，让我最后把奇数index的值都比偶数位的大。实在想不出O(n)的解，就直接说我不会，

- like [1,2,3,4,5,6,7,8]要变成[1,5,2,6,3,7,4,8]这种形式，但是我也不知道是不是我理解错了

Rearrange array such that even index elements are smaller and odd index elements are greater
Given an array, rearrange the array such that :

If index i is even, arr[i] <= arr[i+1]
If index i is odd, arr[i] >= arr[i+1]

https://www.geeksforgeeks.org/rearrange-array-even-index-elements-smaller-odd-index-elements-greater/

Time Complexity: O(N)



'''


def even_smaller_than_odd(nums):
  """
  input nums: list of int
  output results: list of int
  """
  for i in range(len(nums)-1):
    print("i", i, "i/2", int(i/2))
    if (i % 2) == 0: # i is even, then even smaller
      if nums[i] > nums[i + 1]:
        nums[i], nums[i + 1] = nums[i + 1], num[i]
        print("1", nums)
    elif (i % 2) != 0: # i is odd, then should be bigger
      if nums[i] < nums[i + 1]:
        nums[i], nums[i + 1] = nums[i + 1], nums[i]
        print("2", nums)
  return nums

nums = [2, 3, 4, 5]
# [2, 4, 3, 5]
print(even_smaller_than_odd(nums))

"""
O(N) Solution
We will go from left to right from A[1] to A[N]. If at any position, our inequality condition is unsatisfied, we will make a swap of i and i + 1 entries.

Sample Execution:
Let A = [4, 3, 5, 1, 2].
If we are first element (i = 1): A[1] <= A[2] is not satisfied, so we will swap A[1] and A[2].
So A will now become: [3, 4, 5, 1, 2]
Now we are at second element (i = 2): A[2] >= A[3] is not satisfied, so we will swap A[2] and A[3].
So A will now become: [3, 5, 4, 1, 2]
Now we are at third element (i = 3): A[3] <= A[4] is not satisfied, so we will swap A[3] and A[4].
So A will now become: [3, 5, 1, 4, 2]
Now we are at fourth element (i = 4): A[4] >= A[5] is satisfied, so we dont need to swap.
So A will remain as it is: [3, 5, 1, 4, 2]

Proof Of Correctness: 
Assume that a, b, c, be the leftmost(Ordered from A[1] to A[N], A[1] is leftmost, A[N] is rightmost) elements of the array A for which condition is not satisfied. Let us assume that a be the elements which just precedes b. (ie order of occurrence of elements is a, b, c)
Let us suppose we want b >= c. (a <= b).
According to our assumption, a <= b is already satisfied, but b >= c is not satisfied (ie b < c)
Now on swapping b and c, our new order of elements will be a, c, b.
Note that now in this order a <= c(because a <= b < c).
and we have c >= b. (because c > b).

We can handle the second case in the exactly similar way too (Case when a >= b is satisfied but b <= c is not satisfied). This case is left for readers to prove.

Complexity: O(N):
For each index i from 1 to N, we can make at most 1 swap, Swap operation is constant operation, Hence we will only make total O(N) operations.
"""
