from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digitsToLettersMap = {
            1: [],
            2: ["a","b","c"],
            3: ["d","e","f"],
            4: ["g","h","i"],
            5: ["j","k","l"],
            6: ["m","n","o"],
            7: ["p","q","r","s"],
            8: ["t","u","v"],
            9: ["w","x","y","z"],
        }
        length = len(digits)
        combinations = [digits]*self.getCombinationLength(digits, digitsToLettersMap)
        i = len(combinations)
        while(i > 0):
            combinations
    def getCombinationLength(self, digits:str, map) -> int:
        if(digits == ""): return 0
        else:
            length = 1
            for i in range(len(digits)):
                length *= len(map[int(digits[i])])
            return length

if __name__ == "__main__":
    solution = Solution()
    solution.letterCombinations("234")
    testcase1 = ""
    expected1 = ""
    testcase2 = ""
    expected2 = ""
    testcase3 = ""
    expected3 = ""