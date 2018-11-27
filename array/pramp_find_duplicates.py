"""

Find The Duplicates
Given two sorted arrays arr1 and arr2 of passport numbers, implement a function findDuplicates that returns an array of all passport numbers that are both in arr1 and arr2. Note that the output array should be sorted in an ascending order.

Let N and M be the lengths of arr1 and arr2, respectively. Solve for two cases and analyze the time & space complexities of your solutions: M ≈ N - the array lengths are approximately the same M ≫ N - arr2 is much bigger than arr1.

Example:

input:  arr1 = [1, 2, 3, 5, 6, 7], arr2 = [3, 6, 7, 8, 20]

output: [3, 6, 7] # since only these three values are both arr.

"""
# recursive
def find_duplicates(arr1, arr2):

    result = []

    if len(arr1) >= len(arr2):
        long = arr1
        short = arr2
    else:
        short = arr1
        long = arr2
    print(long, short)

    def recursive_search(ele, search_list):
        start = 0
        end = len(search_list) - 1
        print("search_list", search_list)
        if end >= start:
            mid = (start + end) // 2
            if ele == search_list[mid]:
                return ele
            elif ele > search_list[mid]:
                print("ele >", ele, search_list[mid])
                return recursive_search(ele, search_list[mid+1: end+1])
            else:
                print("ele <", ele, search_list[mid])
                return recursive_search(ele, search_list[start : mid])
        return None


    for ele in short:
        find = recursive_search(ele, long)
        print(ele, find)
        if find:
            result.append(find)
    return result

def find_duplicates_iterative(arr1, arr2):

    result = []

    if len(arr1) >= len(arr2):
        long = arr1
        short = arr2
    else:
        short = arr1
        long = arr2

    for ele in short:
        start = 0
        end = len(long) - 1
        while start <= end:
            mid = (start + end) // 2
            if ele == long[mid]:
                result.append(ele)
                break
            elif ele > long[mid]:
                start = mid+1
            else:
                end = mid-1

    return result


def find_duplicates2(arr1, arr2):

    result = []

    if len(arr1) >= len(arr2):
        long = set(arr1)
        short = arr2
    else:
        short = arr1
        long = set(arr2)

    for ele in short:
        if ele in long:
            result.append(ele)
    return result

 # time complexity case 1: if M >>> N:  O(N*(log(M))), when M is super large, this method wins
# time complexity case 2: (M ≈ N), M appxo= N: O(M+N)
