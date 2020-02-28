"""
https://leetcode.com/problems/meeting-rooms-ii/

Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms required.

Example 1:

Input: [[0, 30],[5, 10],[15, 20]]
Output: 2
Example 2:

Input: [[7,10],[2,4]]
Output: 1


"""

# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e


class Solution(object):

  def minMeetingRooms(self, intervals):
    """
    :type intervals: List[Interval]
    :rtype: int
    """
    intervals = sorted(intervals, key=lambda x: (x.start, x.end))  # ON(logN)
    end_times = set()
    self.rooms = 0

    for interval in intervals:
      # print("interval", interval.start, interval.end)
      r = [interval.start >= end_time for end_time in end_times]
      # print("r:{}".format(r), any(r))
      if any(r):
        for end_time in end_times:
          if end_time <= interval.start:
            end_times.remove(end_time)
            break
      else:
        self.rooms += 1
      end_times.add(interval.end)
      # print("self.rooms", self.rooms, end_times)

    return self.rooms