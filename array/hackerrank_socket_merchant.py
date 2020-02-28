from collections import Counter


def sockMerchant(n, ar):
  """
  inputs:
    n: int
    ar: a list of int
  
  output:
    result: number of pair of matching socks

  """

  socks_counter = Counter(ar)

  pairs_of_socks = 0

  for color in socks_counter:
    pairs_of_socks += (socks_counter[color] // 2)

  return pairs_of_socks


n = 8
ar = [1, 2, 1, 2, 1, 3, 2, 3]

r = sockMerchant(n, ar)
print("result", r)
