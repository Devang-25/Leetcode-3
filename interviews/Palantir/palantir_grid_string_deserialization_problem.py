"""
要做的就是根据run length encoding压缩成的一个字符串，复原一个6 * 7 grid。输入有可能invalid，invalid的话输出empty 6*7 grid

"""

# s = '12W1B12W3B24W1B14W'
# nums_set = set(["1","2","3","4","5","6", "7", "8", "9", "0"])

def parse(s):
  if s[-1].isdigit():
    return "invalid input"

  results = ""
  count = 0
  for c in s:
    if c.isdigit():
      count = count * 10 + int(c)
    else:
      char = c
      if count:
        results += char * count
      else:
        results += char
      count = 0
  return results

# def parse(s):
#   if s[-1].isdigit():
#     return "invalid input"

#   results = ""
#   i = 0
#   while i < len(s):
#     # print("i", i)
#     nums_str = ""
#     if s[i].isdigit():
#       while s[i].isdigit():
#         nums_str += s[i]
#         i += 1

#     char = s[i]
#     i += 1

#     if not nums_str:
#       results += char
#     else:
#       print("int", int(nums_str))
#       results += (char * int(nums_str))
#   return results

def print_decoding(result):
  # 6 * 7 grid
  for i in range(6):
    row = [i for i in result[i*7: (i+1)*7]]
    print("|{}|".format("|".join(row)))

def check_gravity(result):
  rows = [[i for i in result[i*7: (i+1)*7]] for i in range(6)]
  cols = zip(*rows)
  # print("rows", rows)
  # print("col", list(cols))

  for col in cols:
    meet_char = False
    for c in col:
      if c != "_":
        meet_char = True
      if c == "_" and meet_char:
        return False
  return True


def run_length_decoding(s):
  print("string", s)
  result_str = parse(s)
  # print("s:    {}\nresult: {}".format(s, result_str))
  if result_str == "invalid input" or len(result_str) != 42:
    return "Invalid Input"

  # print the results
  print_decoding(result_str)

  if_gravity = check_gravity(result_str)
  return if_gravity



s = "7s35a"
# print(parse(s))
print(run_length_decoding(s))
# string 7s35a
# |s|s|s|s|s|s|s|
# |a|a|a|a|a|a|a|
# |a|a|a|a|a|a|a|
# |a|a|a|a|a|a|a|
# |a|a|a|a|a|a|a|
# |a|a|a|a|a|a|a|
# True

s = "41s"
# print(parse(s))
print(run_length_decoding(s))
# string 41s
# Invalid Input


s = "abcdefgabcdefgabcdefgabcdefgabcdefgabcdefg"
assert len(s) == 42
# print(parse(s))
print(run_length_decoding(s))

# string abcdefgabcdefgabcdefgabcdefgabcdefgabcdefg
# |a|b|c|d|e|f|g|
# |a|b|c|d|e|f|g|
# |a|b|c|d|e|f|g|
# |a|b|c|d|e|f|g|
# |a|b|c|d|e|f|g|
# |a|b|c|d|e|f|g|
# True

s = "abcdefgabcdefgabcdefgabcdefgabcdefg7_"
# assert len(s) == 42
# print(parse(s))
print(run_length_decoding(s))

# string abcdefgabcdefgabcdefgabcdefgabcdefg7_
# |a|b|c|d|e|f|g|
# |a|b|c|d|e|f|g|
# |a|b|c|d|e|f|g|
# |a|b|c|d|e|f|g|
# |a|b|c|d|e|f|g|
# |_|_|_|_|_|_|_|
# False

s = "abcdefgabcdefgabcdefgabcdefgabcdefg_bcdefg"
# assert len(s) == 42
# print(parse(s))
print(run_length_decoding(s))

# string abcdefgabcdefgabcdefgabcdefgabcdefg_bcdefg
# |a|b|c|d|e|f|g|
# |a|b|c|d|e|f|g|
# |a|b|c|d|e|f|g|
# |a|b|c|d|e|f|g|
# |a|b|c|d|e|f|g|
# |_|b|c|d|e|f|g|
# False
