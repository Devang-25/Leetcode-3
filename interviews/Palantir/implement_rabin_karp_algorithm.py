def rabin_karp(pattern, text):
  results = []  # [int] is [index]
  # hash pattern
  prime = 3
  # harsh pattern
  pattern_key = sum([
      ord(l) * (prime**order) for l, order in zip(pattern, range(len(pattern)))
  ])
  print("pattern", pattern_key)

  substring = text[:len(pattern) - 1]
  substring_key = sum([
      ord(l) * (prime**order)
      for l, order in zip(substring, range(len(pattern) - 1))
  ])

  i = len(pattern) - 1
  while i < len(text):
    # print("[{}]:{}".format(i, text[i])) if i < len(text) else print(
    #     "[{}]".format(i))
    substring += text[i]
    # print("substring", substring)

    substring_key += ord(text[i]) * (prime**(len(pattern) - 1))
    # print("substring key", substring_key)

    if substring_key == pattern_key and if_match(substring, pattern):
      print("found")
      # pattern = "abc" (012), i = 2, append 2-3+1=0: i
      results.append(i - len(pattern) + 1)

    # update: remove first letter; divide by prime
    substring_key -= ord(substring[0])
    substring_key /= prime
    substring = substring[1:]

    i += 1

  return results


def if_match(substring, pattern):
  assert len(substring) == len(pattern)

  i = 0
  while i < len(pattern):
    if substring[i] != pattern[i]:
      return False
    i += 1

  return True


pattern = "abc"
text = "abcabc"
r = rabin_karp(pattern, text)
print(r)

pattern = "abc"
text = "abcacb"
r = rabin_karp(pattern, text)
print(r)

pattern = ""
text = "abcacb"
r = rabin_karp(pattern, text)
print(r)

pattern = "a"
text = ""
r = rabin_karp(pattern, text)
print(r)
