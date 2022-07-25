from collections import defaultdict
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counts = defaultdict(int)
        for n in nums:
            counts[n] += 1
            
        for n, count in counts.items():
            if count > len(nums) // 2:
                return n
if __name__ == "__main__":
    testcase1 = [1]
    expected1 = 1
    testcase2 = ""
    expected2 = ""
    testcase3 = ""
    expected3 = ""
    solution = Solution()
    solution.majorityElement(testcase1)
    print(solution.majorityElement(testcase1) == expected1)
    print(solution.majorityElement(testcase2) == expected2)
    print(solution.majorityElement(testcase3) == expected3)