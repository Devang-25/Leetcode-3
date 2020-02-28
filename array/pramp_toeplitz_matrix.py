def checkFirstRow(arr):
  for col in range(0, len(arr[0])):
    prev = arr[0][col]
    r = 1
    c = col + 1
    while 0 <= r < len(arr) and 0 <= c < len(arr[0]):
      ele = arr[r][c]
      if ele != prev:
        return False
      r += 1
      c += 1
  return True


def checkFirstCol(arr):
  for row in range(1, len(arr)):
    prev = arr[row][0]
    r = row + 1
    c = 1
    while 0 <= r < len(arr) and 0 <= c < len(arr[0]):
      ele = arr[r][c]
      if ele != prev:
        return False
      r += 1
      c += 1
  return True


def isToeplitz(arr):
  """
  @param arr: int[][]
  @return: bool
  """
  if checkFirstRow(arr) and checkFirstCol(arr):
    print(checkFirstRow(arr), checkFirstCol(arr))
    return True
  return False


arr = [[8, 8, 8, 8, 8], [8, 8, 8, 8, 9], [8, 8, 8, 8, 8], [8, 8, 8, 8, 8],
       [8, 8, 8, 8, 8]]

arr = [[4, 0], [9, 4]]
print("row", checkFirstRow(arr))
print("col", checkFirstCol(arr))
print("result", isToeplitz(arr))