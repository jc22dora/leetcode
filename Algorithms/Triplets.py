from typing import List


class Triplets:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if(len(nums) == 3):
            if(sum(nums) == 0): return [nums]
            else: return []
        else:
            nums.sort()
            triplets = []
            for i in range(len(nums)):
                j = i + 1
                k = len(nums) - 1

                while(j < k):
                    if(nums[j] + nums[k] > -nums[i]): 
                        k -= 1
                    elif(nums[j] + nums[k] < -nums[i]):
                        j += 1
                    else:
                        triplets.append([nums[j], nums[k], nums[i]])
                        j+=1
                        k-=1
                        while j < k and nums[j] == nums[j - 1]:
                            j += 1
        return triplets

            
    