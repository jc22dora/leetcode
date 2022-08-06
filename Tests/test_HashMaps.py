
from ..HashMaps.SetMatrixZeros import SetMatrixZeros
from ..HashMaps.LongestSubstringWithoutRepeatingCharacters import LongestSubWithoutRepChar
from ..HashMaps.IntersectionOfTwoLinkedLists import IntersectionOfTwoLL, ListNode
from ..HashMaps.IsomoprhicStrings import IsomorphicStrings
from ..HashMaps.HappyNumber import Solution
from ..HashMaps.IntegerToRoman import Solution

def test_isHappy():
    # NOT DONE
    testcase1 = 19
    expected1 = ""
    testcase2 = ""
    expected2 = ""
    testcase3 = ""
    expected3 = ""
    solution = Solution()
    assert(solution.isHappy(testcase1)==expected1)

def test_intToRoman():
    solution = Solution()
    testcase1 = 3
    expected1 = "III"
    testcase2 = 58
    expected2 = "LVIII"
    testcase3 = 1994
    expected3 = "MCMXCIV"
    assert(solution.intToRoman(testcase1) == expected1)
    assert(solution.intToRoman(testcase2) == expected2)
    assert(solution.intToRoman(testcase3) == expected3)

def test_intersectionOfTwoLinkedLists():
    # NOT DONE
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node5 = ListNode(5)
    node6 = ListNode(6)
    node7 = ListNode(7)
    node8 = ListNode(8)
    node9 = ListNode(9)

    #testcase1a = ListNode(4, ListNode(1, ListNode(8, ListNode(4, ListNode(5)))))
    testcase1a = node4
    testcase1a.next = node1
    testcase1a.next = node8
    testcase1a.next = node4
    testcase1a.next = node5
    testcase1b = node5
    testcase1b.next = node6
    testcase1a.next = node1
    testcase1a.next = node8
    testcase1a.next = node4
    testcase1a.next = node5
    #testcase1b = ListNode(5, ListNode(6, ListNode(1, ListNode(8, ListNode(4, ListNode(5))))))
    expected1 = ""
    testcase2 = ""
    expected2 = ""
    testcase3 = ""
    expected3 = ""
    solution = IntersectionOfTwoLL()
    assert(solution.getIntersectionNode(testcase1a, testcase1b) == expected1)
def test_isomorhpicStrings():
    testcase1s = "egg"
    testcase1t = "add"
    expected1 = True
    testcase2s = "abcdefghijklmnopqrstuvwxyzva"
    testcase2t = "abcdefghijklmnopqrstuvwxyzck"
    expected2 = False
    testcase3s = "badc"
    testcase3t = "baba"
    expected3 = False
    solution = IsomorphicStrings()
    assert(solution.isIsomorphic(testcase1s, testcase1t) == expected1)
    assert(solution.isIsomorphic(testcase2s, testcase2t) == expected2)
    assert(solution.isIsomorphic(testcase3s, testcase3t) == expected3)
def test_letterCombinations():
    pass
def test_longestSubstringWithoutRepeatingCharacters():
    solution = LongestSubWithoutRepChar()
    testcase1 = "abcabcbb"
    expected1 = 3
    testcase2 = "dvdf"
    expected2 = 3
    testcase3 = "abdcvdf"
    expected3 = 5
    
    assert(solution.lengthOfLongestSubstring(testcase1), expected1)
    assert(solution.lengthOfLongestSubstring(testcase2), expected2)
    assert(solution.lengthOfLongestSubstring(testcase3), expected3)
def test_letterCombinations():
    pass
def test_LRUCache():
    pass
def test_setMatrixZeros():
    testcase1 =  [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
    expected1 = [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
    testcase2 = [[1,1,1],[1,0,1],[1,1,1]]
    expected2 = [[1,0,1],[0,0,0],[1,0,1]]
    testcase3 = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
    expected3 = [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
    solution = SetMatrixZeros()
    assert(solution.setZeroes(testcase1) == expected1)
    assert(solution.setZeroes(testcase2) == expected2)
    assert(solution.setZeroes(testcase3) == expected3)