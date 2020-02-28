from collections import defaultdict

class Solution(object):
    def totalFruit(self, tree):
        """
        :type tree: List[int]
        :rtype: int

        find the longest window that has only two type of int in it

        dynamic programming:
        the most amount you can collect started with
        """
        i = 0
        j = 0

        cur_basket = defaultdict(int) # {type: count}

        fruits_type = 0
        max_fruits = 0
        I, J = 0, 0

        while i <= j and j < len(tree):
            if fruits_type <= 2:
                # j += 1
                fruit = tree[j]
                cur_basket[fruit] += 1
                print("add fruit {}".format(j), cur_basket)

                if cur_basket[fruit] == 1:
                    fruits_type += 1

                if fruits_type <= 2:
                    if  (j - i + 1) > max_fruits:
                        max_fruits = (j - i + 1)
                        print("max fruit", i, j, max_fruits)
                        I, J = i, j

                elif fruits_type > 2:
                    while fruits_type > 2:
                        fruit = tree[i]
                        cur_basket[fruit] -= 1
                        print("deduct", cur_basket)
                        if cur_basket[fruit] == 0:
                            fruit_type -= 1
                            i += 1
            j += 1

        return max_fruits

inputs = [1,2,1]
s = Solution()
print(s.totalFruit(inputs))
