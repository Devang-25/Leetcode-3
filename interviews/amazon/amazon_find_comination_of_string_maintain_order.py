"""
https://www.1point3acres.com/bbs/forum.php?mod=viewthread&tid=504192&highlight=%D1%C7%C2%E9%2Bvo

给两个string, 要求保证每个string内部相对顺序不变的情况下，输出所有可能的组合.
比如 s1 = “AB”  s2 = “CD” 输出ABCD ACBD ACDB CABD CADB CDAB

fn(s1, s2) = [s1[0] + tail for tail in fn(s1[1:], s2)] +
             [s2[0] + tail for tail in fn(s1, s2[1:])] +
"""


def all_combinations(s1, s2):

  # print('s1:{}, s2:{}'.format(s1, s2))
  """
  inputs:
    t1: List[str]
    t2: List[str]
  outputs:
    r: List[str]

  """
  # print("\n")
  # print("t1:{}, t2:{}".format(t1, t2))

  if not s1:
    return [s2]

  if not s2:
    return [s1]

  l = all_combinations(s1[1:], s2)
  left = [s1[0] + s for s in l]
  # print("l:{}, t1:{}, left:{}".format(l, t1[0], left))

  r = all_combinations(s1, s2[1:])
  right = [s2[0] + s for s in r]
  # print("r:{}, t2:{}, right:{}".format(r, t2[0], right))

  return left + right


######## test case 1 ######
s1 = "AB"
s2 = ""
# AB

r = all_combinations(s1, s2)
print("r", r)

######## test case 2 ######
s1 = "A"
s2 = "C"
# AC, CA

r = all_combinations(s1, s2)
print("r", r)

######## test case 3 ######

s1 = "AB"
s2 = "CD"

r = all_combinations(s1, s2)
print("r", r)
# ABCD ACBD ACDB CABD CADB CDAB