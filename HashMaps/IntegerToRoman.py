class Solution:
    def intToRoman(self, num: int) -> str:
        romanDict = {
            "M": 1000,
            "CM": 900,
            "D": 500,
            "CD": 400,
            "C": 100,
            "XC": 90,
            "L": 50,
            "XL": 40,
            "X": 10,
            "IX": 9,
            "V": 5,
            "IV": 4,
            "I": 1
        }
        romanKeys = list(romanDict.keys())
        string = ''
        tempKeys = romanKeys
        while(num):
            if(num < romanDict[tempKeys[0]] ):
                tempKeys.pop(0)
            else:
                string += tempKeys[0]
                num -= romanDict[tempKeys[0]]
        return string

if __name__ == "__main__":
    solution = Solution()
    
    testcase1 = 3
    testcase2 = 58
    testcase3 = 1994
    print(solution.intToRoman(testcase1))
    print(solution.intToRoman(testcase2))
    print(solution.intToRoman(testcase3))