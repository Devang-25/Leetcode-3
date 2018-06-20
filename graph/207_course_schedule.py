class Solution(object):
        def canFinish_topological_sort(self, num_courses, prerequisites):
        """
        :type num_courses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        seen = set()
        taken = set()
        after_pre_dict = { i: [] for i in range(num_courses)}
        for after, pre in prerequisites:
            after_pre_dict[after].append(pre)

        def take(after):
            if after in taken:
                return True
            pres = after_pre_dict.get(after)
            if not pres:
                taken.add(after)
                return True

            if after in seen:
                return False
            seen.add(after)

            if all(take(pre) for pre in pres):
                taken.add(after)
                return True
            return False

        return all(take(course) for course in range(num_courses))

    def canFinish2(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype bool
        """
        num_prereq_need = [0] * numCourses
        further_courses = [[] for x in range(numCourses)]
        # print(further_courses)

        # organize the data into the num_preqreq_need & further_courses
        for pair in prerequisites:
            # course = pair[0]
            # prerequisite = pair[1]
            num_prereq_need[pair[0]] += 1
            further_courses[pair[1]].append(pair[0])

        # start up initial state for courses and flag
        courses = set(range(numCourses))
        update = True
        # while we have remove an course from the courses
        # we reach the flag = True
        while update and len(courses):
            update = False
            remove_list = []
            for x in courses:
                if num_prereq_need[x] == 0:
                    for child in further_courses[x]:
                        num_prereq_need[child] -= 1
                    remove_list.append(x)
                    update = True

            # the reason for building remove_list
            # instead of change courses in the spot
            # b/c during the iteration of courses,
            # we can NOT change the set
            for x in remove_list:
                courses.remove(x)
        return len(courses) == 0

test1 = [[1, 2], [2, 0], [0, 1]] # False
test2 = [[1, 2], [2, 0]] # True
test3 = [[1, 2], [0, 2]] # True

print(Solution().canFinish(3, test1))
print(Solution().canFinish(3, test2))
print(Solution().canFinish(3, test3))
