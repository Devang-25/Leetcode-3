"""
A sorted array of distinct integers shiftArr is shifted to the left by an unknown offset and you don’t have a pre-shifted copy of it. For instance, the sequence 1, 2, 3, 4, 5 becomes 3, 4, 5, 1, 2, after shifting it twice to the left.

Given shiftArr and an integer num, implement a function shiftedArrSearch that finds and returns the index of num in shiftArr. If num isn’t in shiftArr, return -1. Assume that the offset doesn’t equal to 0 (i.e. assume the array is shifted at least once) or to arr.length - 1 (i.e. assume the shifted array isn’t fully reversed).

Explain your solution and analyze its time and space complexities.

Example:

input:  shiftArr = [9, 12, 17, 2, 4, 5], num = 2
# shiftArr is the outcome of shifting [2, 4, 5, 9, 12, 17]
# three times to the left

output: 3 # since it’s the index of 2 in arr

"""

def shifted_arr_search(shiftArr, num):
    """
    # find the pivot point: find array[i-1] > array[i]
    # search in subarray:
        # compare num with shiftArr[0]
        # if num < shiftArr[0] => search (pivot, len(array))
        # if num > shiftArr[0] => search in (array[0], pivot-1)
    """

    pivot = find_pivot_point(shiftArr)
    if pivot == 0 or num < shiftArr[0]:
        return search_num(shiftArr, pivot, len(shiftArr), num) # from (pivot, len(arr))
    return search_num(shiftArr, 0, pivot-1, num) # search from (arr[0], pivot-1)

def find_pivot_point(arr):
    begin = 0
    end = len(arr)
    while begin <= end:
        mid = (begin + end) // 2
        if arr[mid - 1] > arr[mid]:
            return mid
        if arr[begin] < arr[mid - 1]:
            begin = mid + 1
        else:
            end = mid - 1

    # if the pivot point is at the index#0
    return 0

def search_num(arr, begin, end, num):
    while begin <= end:
        mid = (begin + end) // 2
        if arr[mid] == num:
            return mid
        elif num < arr[mid]:
            end = mid - 1
        else:
            begin = mid + 1
    # if can NOT find the num
    return -1

list1 = [2]
list2 = [1, 2]
list3 = [2, 1]
list4 = [0, 1, 2, 3, 4, 5]
shifted_arr_search(list1, 2)
shifted_arr_search(list2, 2)
shifted_arr_search(list3, 1)

"""
Time Complexity: the time complexity of findPivotPoint is O(log((N)) since it’s essentially a slightly modified version of the binary search algorithm. The time complexity of binarySearch is obviously O(log((N)) as well. The total time complexity is therefore O(log((N)).

"""
