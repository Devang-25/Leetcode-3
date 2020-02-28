"""
https://leetcode.com/discuss/interview-question/207687/Optimally-utilized-travel-distance

max travel distance is : 11000
forward route list : [[1,3000],[2,5000],[3,4000],[4,10000]]
backward route list : [[1,2000],[2,3000],[3,4000]]

return a list of list: [[ids], ...] where they have the maximum travel distance while not exceed the given max_travel distance

"""
# ON(logN) Solution

def optimize_travel_distance(forward_routes, backward_routes, max_travel_distance):
    forward_routes.sort()
    backward_routes.sort()

    my_max_distance = 0
    max_ids = []

    for forward_i, forward_trip in forward_routes:
      if forward_trip > max_travel_distance:
        continue

      max_backward_trip = max_travel_distance - forward_trip
      # gap = -float("inf")
      start = 0
      end = len(backward_routes) - 1
      while start <= end:
        mid = (start + end) // 2
        total = backward_routes[mid][1] + forward_trip

        if total <= max_travel_distance:
          if total > my_max_distance:
            my_max_distance = total
            max_ids = [(forward_i, backward_routes[mid][0])]
            # print("max ids 1", max_ids)
          elif total == my_max_distance:
            max_ids.append((forward_i, backward_routes[mid][0]))
            # print("max ids 2", max_ids)

        if backward_routes[mid][1] == max_backward_trip: # assume each backward_trip is distinct
            break
        elif backward_routes[mid][1] > max_backward_trip:
          end = mid - 1
        elif backward_routes[mid][1] < max_backward_trip:
          start = mid + 1

    return max_ids

################# test case 1 ###################

# max_travel_distance = 11000
# forward_routes = [[1,3000],[2,5000],[3,4000],[4,10000]]
# backward_routes = [[1,2000],[2,3000],[3,4000]]
# # return [[2, 3]]

########### test case 2 ########
forward_routes = [[3, 4], [1, 2]]
backward_routes = [[4, 1], [5, 6]]
max_travel_distance = 8
# return [[1,5]]


############ test case 3 ###########
# foreground = [[3, 4], [1, 2], [2, 3]]
# background = [[4, 1], [5, 6], [8, 5]]
# max_device_capacity = 8
# # return [[1,5], [2, 8]] b/c 2 + 6 = 8

max_ids = optimize_travel_distance(forward_routes, backward_routes, max_travel_distance)

print(max_ids)

##################################
# O(N^2) Solution
def optimize_travel_distance(forward_routes, backward_routes, max_travel_distance):
  max_distance = 0
  ids = []
  for i in forward_routes:
      for j in backward_routes:
        temp = forward_routes[i][1] + backward_routes[j][1]
        if temp > max_distance:
          max_distance = temp
          ids = [(i, j)]
        else:
          ids.append((i, j))
  return ids
