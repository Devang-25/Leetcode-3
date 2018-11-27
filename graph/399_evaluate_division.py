"""
Equations are given in the format A / B = k, where A and B are variables represented as strings, and k is a real number (floating point number). Given some queries, return the answers. If the answer does not exist, return -1.0.

Example:
Given a / b = 2.0, b / c = 3.0.
queries are: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ? .
return [6.0, 0.5, -1.0, 1.0, -1.0 ].

The input is: vector<pair<string, string>> equations, vector<double>& values, vector<pair<string, string>> queries , where equations.size() == values.size(), and the values are positive. This represents the equations. Return vector<double>.

According to the example above:

equations = [ ["a", "b"], ["b", "c"] ],
values = [2.0, 3.0],
queries = [ ["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"] ].
The input is always valid. You may assume that evaluating the queries will result in no division by zero and there is no contradiction.


"""

class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[list[str]]
        :type values: List[flat]
        :type queries: List[List[str]]
        """
        # make each pair of equations into dictionary
        quot = collections.defaultdict(dict)
        # zip functon take O(1) time time complexity
        for (num, den), val in zip(equations, values):
            quot[num][den] = val
            quot[den][num] = 1 / val
            quot[num][num] = quot[den][den] = 1.0
        # a/b * b/c = a/ c => quote[a][c]
        for a, b, c in itertools.permutations(quot, 3):
            if b in quot[a] and c in quot[b]:
                quot[a][c] = quot[a][b] * quot[b][c]
        return [quot[num].get(den, -1.0) for num, den in queries]


equations = [ ["a", "b"], ["b", "c"] ]
values = [2.0, 3.0]
queries = [ ["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"] ]

s = Solution()
s.calcEquation(equations, values, queries)
