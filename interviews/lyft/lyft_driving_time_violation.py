"""
- write a function to determinte whether a driver is allowed to enter a drive mode

- drive is NOT allowed to drive a total of 12 hours without 8 hours break

- input: a list of driver shrifts as [[start, end], [start, end]]
- the star and end time are integers relative lyft launch

- input current time: int, time since lyft launch

return bool


+++++++++++++

True example:
# 9 hours break, 1 hour drive, 2 hours break, 10 hours driver
# history = [(9, 10), (12, 22)]
cur_time = 24


"""

# brutal force:
def can_drive(history, cur_time):
  drive = 0
  i = len(history) - 1
  last_start = cur_time
  while i >= 0:
    rest = last_start - history[i][1]
    drive += history[i][1] - history[i][0]
    if rest >= 8:
      return True
    if drive >= 12:
      return False
    last_start = history[i][0]
    i -= 1
  return True
  # while rest < 8 or drive < 12:



history = [(9, 10), (12, 22)]
current_time = 24
# True

# history = [(0,4), (5, 9), (10, 14), (15, 19), (20, 24)]
# current_time = 24
# False

print(history)
print(can_drive(history, current_time))
