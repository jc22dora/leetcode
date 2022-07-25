class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        sDict, tDict = {}, {}
        if(len(s) != len(t)):
            return False
        elif(len(s) <= 1):
            return True
        else:
            for i in range(len(s)):
                if(sDict.get(s[i]) is None and tDict.get(t[i]) is None):
                    sDict[s[i]] = t[i]
                    tDict[t[i]] = s[i]
                else:
                    if(t[i] != sDict.get(s[i])): return False

            return True


        
                
if __name__ == "__main__":
    testcase1s = "egg"
    testcase1t = "add"
    expected1 = True
    testcase2s = "abcdefghijklmnopqrstuvwxyzva"
    testcase2t = "abcdefghijklmnopqrstuvwxyzck"
    expected2 = False
    testcase3s = "badc"
    testcase3t = "baba"
    expected3 = False
    solution = Solution()
    print(solution.isIsomorphic(testcase1s, testcase1t) == expected1)
    print(solution.isIsomorphic(testcase2s, testcase2t) == expected2)
    print(solution.isIsomorphic(testcase3s, testcase3t) == expected3)