class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # dict: key = letter, value = latest index of that letter
        # longest: record the longest word

        # if ele in visited: update (1)start (2)index of that els
        # if ele NOT visited: update (1)put ele into visited (2)calculate and update the longest

        longest = 0
        visited = {}
        start = -1
        for i, c in enumerate(s):
            if c in visited and start < visited[c]:
                start = visited[c]
            else:
                longest = max(longest, i - start)
            visited[c] = i
        return longest
