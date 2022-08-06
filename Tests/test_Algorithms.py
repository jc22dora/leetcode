from Algorithms.MaximumWater import MaximumWater
from Algorithms.MostCommonPrefix import MostCommonPrefix
from Algorithms.RemoveElement import RemoveElement
from Algorithms.Triplets import Triplets
def test_maxArea():
    testcase1 = [1,8,6,2,5,4,8,3,7]
    expected1 = 49
    testcase2 = [1,1]
    expected2 = 1
    testcase3 = ""
    expected3 = ""
    solution = MaximumWater()
    assert(solution.maxArea(testcase1) == expected1)
    assert(solution.maxArea(testcase2) == expected2)

def test_longestCommonPrefix():
    testcase1 = ["flower","flow","flight"] 
    expected1 = "fl"
    testcase2 = ["dog","racecar","car"]
    expected2 = ""
    testcase3 = ["a"]
    expected3 = "a"
    testcase4 = [""]
    expected4 = ""
    testcase5 = ["",""]
    expected5 = ""
    testcase6 = ["", "b"]
    expected6 = ""
    testcase7 = ["reflower","flow","flight"]
    expected7 = ""
    testcase8 = ["abab","aba",""]
    expected8 = ""
    testcase9 = ["ab", "a"]
    expected9 = "a"
    testcase10= ["flower","flower","flower","flower"] 
    expected10 = "flower"
    testcase11 = ["a", "b"]
    expected11= ""
    solution = MostCommonPrefix()
    
    assert(solution.longestCommonPrefix(testcase1) == expected1)
    assert(solution.longestCommonPrefix(testcase2) == expected2)
    assert(solution.longestCommonPrefix(testcase3) == expected3)
    assert(solution.longestCommonPrefix(testcase4) == expected4)
    assert(solution.longestCommonPrefix(testcase5) == expected5)
    assert(solution.longestCommonPrefix(testcase6) == expected6)
    assert(solution.longestCommonPrefix(testcase7) == expected7)
    assert(solution.longestCommonPrefix(testcase8) == expected8)
    assert(solution.longestCommonPrefix(testcase9) == expected9)
    assert(solution.longestCommonPrefix(testcase10) == expected10)
    assert(solution.longestCommonPrefix(testcase11) == expected11)

def test_removeElement():
    solution = RemoveElement()
    testcase1 = [[3,2,2,3], 3]
    expected1 = 2
    testcase2 = [[0,1,2,2,3,0,4,2], 2]
    expected2 = 5

    assert(solution.removeElement(testcase1[0],testcase1[1]) == expected1)
    assert(solution.removeElement(testcase2[0],testcase2[1]) == expected2)

def test_threeSum():
    # DONE BUT NEED TO MODIFY TEST
    testcase1 = [-1,0,1,2,-1,-4]
    expected1 = [[-1,-1,2],[-1,0,1]]
    testcase2 = ""
    expected2 = ""
    testcase3 = ""
    expected3 = ""
    solution = Triplets()
    assert(solution.threeSum(testcase1) == expected1)
    assert(solution.threeSum(testcase2) == expected2)
    assert(solution.threeSum(testcase3) == expected3)