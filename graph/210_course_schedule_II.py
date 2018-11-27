from collections import defaultdict
import collections

class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        #
        course_pre = defaultdict(set)
        neighbor = defaultdict(set)
        result = []
        count = 0

        for course, pre in prerequisites:
            course_pre[course].add(pre)
            neighbor[pre].add(course)

        q = collections.deque([c for c in range(numCourses) if c not in course_pre])

        while q:
            pre = q.popleft()
            result.append(pre)
            count += 1
            for course in neighbor[pre]:
                course_pre[course].remove(pre)
                if not course_pre[course]:
                    q.append(course)

        return result if  count == numCourses else []
