class Solution:
    def trap(self, height: List[int]) -> int:
        maxLeft = 0
        maxRight = 0
        l, r = 0, len(height)-1        
        totalWater = 0

        while l < r:
            print(totalWater)
            if height[l] <= height[r]:
                maxLeft = max(maxLeft, height[l])
                totalWater += max(maxLeft - height[l],0)
                l += 1
            else:
                maxRight = max(maxRight, height[r])
                totalWater += max(maxRight - height[r],0)
                r -= 1

        return totalWater

                

