from typing import List


class RemoveElement:
    def removeElement(self, nums: List[int], val: int) -> int:
        i,k = 0, 0
        if(len(nums) < 2 and val not in nums): return len(nums) 
        while(i < len(nums)-k):
            if(nums[i] == val):
                k += 1
                nums[i] = nums[len(nums)-k]
            else:
                i += 1
        return len(nums)-k

    