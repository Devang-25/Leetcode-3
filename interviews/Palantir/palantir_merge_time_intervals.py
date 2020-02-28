"""
Given a collection of intervals, merge all overlapping intervals.

Example 1:

Input: [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].


Results = [[1,6]]
# [1,3] [2, 6] ==> [[1, 6]]
# [1, 6] [8, 10] ==> merge = True, [1,10] # r  / merge = False, [8,10]
  if merge: # merage
  # results.del([-1])
  # results.append(r)

  # elif not merge: # no merge
  # results.append(r)


1)  [item for item in merge_results]
2)  merge_results
"""



def merge_intervals(intervals):
  """
  input intervals: [[int]]

  output results type: [[int]]
  """


  if not intervals:
    return []

  results = []
  results.append(intervals[0])


  for i in range(1, len(intervals)):
    merge, r = check_merge(results[-1], intervals[i])
    if merge:
      results.pop()
    results.append(r)

  return results



def check_merge(r_interval, interval):
  """
  inputs:
  r_interval : [int]
  interval : [int]

  output:
  merge: bool
  r : [int]
  """
  s1, e1 = r_interval
  s2, e2 = interval

  if e1 >= s2:
    return (True, [s1, e2])

  elif e1 < s2:
    return (False, [s2, e2])



# intervals = [[1,3],[2,6]]
# intervals = [[1,3],[2,6],[8,10],[15,18]]

intervals = [[1, 3], [3, 6]]

print(merge_intervals(intervals))
