class Solution:
    def isHappy(self, n: int) -> bool:
        dict = {}
        while(True):
            sum = 0
            for i in range(len(str(n))):
                sum += int(n[i])**2 
            if(dict.get(sum)): return False
            elif(sum == 1): return True
            else: 
                dict[sum] = 1
                n = sum 

if __name__ == "__main__":
    testcase1 = 19
    expected1 = ""
    testcase2 = ""
    expected2 = ""
    testcase3 = ""
    expected3 = ""
    solution = Solution()
    solution.isHappy(testcase1)