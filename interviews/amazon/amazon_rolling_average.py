"""
例11： Rolling Average (2019.1)


input： [1,3,5,7,8] size =2
output: [2.0,4.0,6.0,7.5]

"""

def rolling_average(nums, size):
  if size == 0:
    return "division by 0"


  rolling_avg = []
  for i in range(len(nums) - size + 1):
    rolling_avg.append((sum(nums[i:i+size]))/size)
  return rolling_avg

# nums = [1,3,5,7,8]
# size = 2
#output: [2.0,4.0,6.0,7.5]

nums = [1,3,5,7,8]
size = 0

print(rolling_average(nums, size))
