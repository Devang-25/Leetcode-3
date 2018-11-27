"""
Given an unsorted array of integers arr and a number s, write a function findArrayQuadruplet that finds four numbers (quadruplet) in arr that sum up to s. Your function should return an array of these numbers in an ascending order. If such a quadruplet doesn’t exist, return an empty array.

Note that there may be more than one quadruplet in arr whose sum is s. You’re asked to return the first one you encounter (considering the results are sorted).

Explain and code the most efficient solution possible, and analyze its time and space complexities.

"""



from collections import defaultdict
import itertools

def find_array_quadruplet1(arr, s):
    sum_cache = defaultdict(list)
    for num1, num2 in itertools.combinations(sorted(arr), 2):
        sum_cache[num1 + num2].append((num1, num2))
    for key1 in sum_cache:
        key2 = s - key1
        if key2 in sum_cache:
            i, j = sum_cache[key1][0]
            l, m = sum_cache[key2][0]
            if all([arr.count(ele) >= (i, j, l, m).count(ele) for ele in (i, j, l, m)]) == True:
                return [i, j, l, m]
    return []


  # sorted(arr)
# sum1(i, j) and sum2(l, m)
# i is from 0 to n-4
# j is from i+1 to n-3:
# search l,m using low, high pointers at j+1, n-1:
# if l+m < sum2: low++
# if l+m > sum2: high--
# if l+m == sum2, return i, j, l, m
# else, return []

############################################
# method_2

def find_array_quadruplet(arr, s):
    """
    input arr: array
    input s: int
    rtype: list
    """
    # corner case:
    if len(arr) < 4:
        return []

    arr.sort()
    n = len(arr)
    for i in range(0, n-3):
        for j in range(i+1, n-2):
            r = s - arr[i] - arr[j]
            low = j+1
            high = n-1
            while low < high:
                if arr[low] + arr[high] == r:
                    return [arr[i], arr[j], arr[low], arr[high]]
                elif arr[low] + arr[high] > r:
                    high -= 1
                else:
                    low += 1
    return []

# arr.sort -> n(logn)
# 2 for-loop + 1 while-loop = n^3
# thus time complexity: n^3
