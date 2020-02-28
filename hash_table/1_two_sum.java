import java.util.*;

class Solution {
  public int[] twoSum(int[] nums, int target) {
    HashMap<Integer, Integer> d = new HashMap();
    int[] result = new int[2];

    for (int i = 0; i < nums.length; i++) {
      int m = target - nums[i];
      System.out.println(d.containsKey(m));
      if (d.containsKey(m)) {
        result[0] = i;
        result[1] = d.get(m);
        break;
      }
      d.put(nums[i], i);
    }
    return result;
  }
}