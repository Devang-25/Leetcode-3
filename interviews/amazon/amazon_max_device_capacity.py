"""
第二题略难。
给一个device capacity，一串 list of foreground application, 一串background application, 然后每个application是个tuple： (id, size)。 求所有总size加起来不超过device  capacity的foreground和background application的pair。比如你有foreground application: [[1, 2], [3, 4]], background application: [[4, 1], [5, 6]]， 总的capacity是8，那么答案就是 [[1, 5]] 因为 [1,2 ] 和[5,6] 组合起来刚好能撑满整个capacity。要求返回所有满足pair id。

Time Complexity: O(N log N)
- sort list O(N log N)
- for each foreground / forward_routes: do one binary search O(logN) => N * O(LogN) = O(N log N)


"""

def device_capacity(foreground, background, max_device_capacity):
  """
  input foreground: list(tuple(int)), eg. [id, size]]
  input background: list(tuple(int)), eg. [[id, size]]
  max_device_capacity = int
  """
  max_available_device_cap = -float("inf")
  max_ids = []

  # sort both foreground and background
  foreground.sort(key=lambda x: x[1])
  background.sort(key=lambda y: y[1])

  print(foreground, background)

  for foreground_i, foreground_size in foreground:
    print("foreground", foreground_i, foreground_size)
    if foreground_size > max_device_capacity:
      continue

    max_background_size = max_device_capacity - foreground_size

    # use bineary search to search max_background_size:
    start = 0
    end = len(background) - 1

    while start <= end:
      mid = (start + end) // 2

      background_size = background[mid][1]
      background_i = background[mid][0]
      total_size = foreground_size + background_size

      if total_size <= max_device_capacity:
        if total_size == max_available_device_cap:
          max_ids.append((foreground_i, background_i))
          print("1", max_ids)
        elif total_size > max_available_device_cap:
          max_available_device_cap = total_size
          max_ids = [(foreground_i, background_i)]
          print("2", max_ids)

      if background_size == max_background_size:
        print("break")
        break

      elif background_size < max_background_size:
        start = mid + 1
        print("right")

      elif background_size > max_background_size:
        end = mid - 1
        print("left")

  return max_ids


############ test case 1 ###########

# foreground = [[3, 4], [1, 2]]
# background = [[4, 1], [5, 6]]
# max_device_capacity = 8
# # return [[1,5]] b/c 2 + 6 = 8

############ test case 2 ###########
# foreground = [[1,3000],[2,5000],[3,4000],[4,10000]]
# background = [[1,2000],[2,3000],[3,4000]]
# max_device_capacity = 11000
# # return [[2, 3]]

############ test case 3 ###########
foreground = [[3, 4], [1, 2], [2, 3]]
background = [[4, 1], [5, 6], [8, 5]]
max_device_capacity = 8
# return [[1,5], [2, 8]] b/c 2 + 6 = 8


print(device_capacity(foreground, background, max_device_capacity))
