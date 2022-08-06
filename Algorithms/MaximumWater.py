from typing import List


class MaximumWater:
    def maxArea(self, height: List[int]) -> int:
        maxArea = 0
        i, j = 0, len(height)-1
        while(i<j):
            maxArea = max(min(height[i], height[j])*(j-i), maxArea)
            if(height[i] < height[j]): i += 1
            else: j-=1 
        return maxArea
