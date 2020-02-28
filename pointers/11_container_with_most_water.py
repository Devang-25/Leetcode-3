class Solution(object):
    def maxArea(self, heightMap):
        """
        :type heightMap: List[List[int]]
        :rtype: int
        """
        def computeArea(l, r):
            area = min(heightMap[l], heightMap[r]) * (r - l)
            return area
        
        if not heightMap or len(heightMap) == 1:
            return 0
        
        l = 0
        r = len(heightMap) - 1
        # max_water = min(heightMap[l], heightMap[r]) * r
        
        while l < r:
            if heightMap[l] <= heightMap[r]: # move the r pointer
                l += 1
                if heightMap[l] > heightMap[l - 1]:
                    water = min(heightMap[l], heightMap[r]) * (r - l)
            elif heightMap[l] > heightMap[r]: 
                r -= 1
                if heightMap[r] > heightMap[r+1]:
                    water = min(heightMap[l], heightMap[r]) * (r - l)
            if water > max_water:
                max_water = water
                print("l", l, "r", r)
        
        return max_water
    
    
heightMap = []
heightMap = [1]
heightMap = [0, 2]
heightMap = [1, 5, 0, 5, 1]
heightMap = [1,8,6,2,5,4,8,3,7]
heightMap = [2,3,4,5,18,17,6]

s = Solution()
r = s.maxArea(heightMap)
print("result", r)             