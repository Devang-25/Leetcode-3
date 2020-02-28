class Solution:

  def pathSum(self, nums):
    self.nums = nums
    self.all_sums = 0

    root_val = self.parse(nums[0])
    self.helper([root_val], 1)
    return self.all_sums

  def helper(self, prev_level_sums, index, level):
    if index >= len(self.nums):
      # assert len(prev_level_sums) == 8
      for s in prev_level_sums:
        self.all_sums += s
      return

    # cur_level = self.nums[index:index + len(prev_level_sums) + 1]
    # end_index = max(1, index + 2 * len(prev_level_sums))
    cur_level = self.nums[index:index + 2 * len(prev_level_sums)]
    cur_level_sums = []

    i = 0
    # assert len(cur_level) == 2 * len(prev_level_sums)
    for s in prev_level_sums:
      sum1 = s + self.parse(cur_level[i])
      sum2 = s + self.parse(cur_level[i + 1])
      cur_level_sums += [sum1, sum2]
      i += 2

    # assert len(cur_level_sums) == 2 * len(prev_level_sums)
    print("prev_level_sums:{}, cur_level_sums:{}".format(
        prev_level_sums, cur_level_sums))
    self.helper(cur_level_sums, index + 2 * len(prev_level_sums))

  def parse(self, num):
    level = int(str(num[0]))``
    val = int(str(num)[2])
    return val


nums = [113, 215, 221]
s = Solution()
r = s.pathSum(nums)
print("nums", nums, "r", r)

nums = [113, 221]
s = Solution()
r = s.pathSum(nums)
print("nums", nums, "r", r)
