"""
https://www.1point3acres.com/bbs/forum.php?mod=viewthread&tid=506802&highlight=%D1%C7%C2%E9Vo

给两个team数组，数组元素是team player 的分数。问如何swap两队的队员使得两队分数最balance（队员分数和相差最小）。

"""


class Solution:

  def balance(self, team1, team2):
    """
    inputs:
      team1: list[int]
      team2: list[int]
    
    outputs:
      team1: list[int]
      team2: list[int]
    """

    # sort tema1 and team2 together:
    team1.sort()
    team2.sort()

    i = 0
    j = 0
    while i < len(team1) - 1 and j < len(team2) - 1:
      if team1[i] < team2[j]:
        target = team1[i]
        if team1[i + 1] < team2[j]:
          team1[i + 1], team2[j] = team2[j], team1[i + 1]
      elif team2[j] < team1[i]:
        target = team2[j]
        if team2[j] < team1[i]:
          team2[j + 1], team1[i] = team1[i], team2[j + 1]
      i += 1
      j += 1
      continue


team1 = [2, 3]
team2 = [4, 6]
total = 5 + 10 = 15
15 / 2 = 7
15 - 7 = 8
"""
t1 = [2, 3, 8]
t2 = [4, 6, 7]

state1:
i = 0
j = 0
min = 2
compare: 3 vs 4 --> 3 < 4--> 3 swap 4
swap:
t1 = [2, 4, 8]
t2 = [3, 6, 7]

state2: 
i = 0
j = 0
min = 2 
compare: compare 4 vs 6
since 4 < 6:
swap: 4 with 6
t1 = [2, 6, 8] : 16
t2 = [3, 4, 7] : 18

state3: 
i = 1
j = 1
min = 4
compare: 6 vs 7
since: 7 > 6: 
no swap.





###############
t1 = [2, 3, 8] 13
t2 = [4, 6, 7] 17 
# return:
# team1[2, 6, 7]  15
# team2[3, 4, 8]  15



##########

t1 = [2, 3, 8] 13
t2 = [4, 6, 7] 17 
diff = 5 / 2= 2.5

t1 = [4, 3, 8] 15
t2 = [2, 6, 7] 15


"""