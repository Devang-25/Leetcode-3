class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        bracket_dict = {"(": ")",
                            "{": "}",
                            "[":"]"}
        target = []

        if not s:
            return True

        if len(s) % 2 != 0:
            return False

        for bracket in s:
            if bracket in bracket_dict:
                target.append(bracket_dict[bracket])
            if bracket not in bracket_dict:
                if not target:
                    return False
                if bracket == target[-1]:
                    target.pop()
                else:
                    return False
        return True if not target else False

Solution().isValid("({}){}")
Solution().isValid("")
