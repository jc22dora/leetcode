from Recursion.Fibonacci import Fibonacci
from Recursion.RemoveElements import OddEven, PalindromeLinkedList, RemoveElements
from ..Recursion.ReverseLinkedList import ListNode, ReverseList


def test_fib():
    testcase1 = 4
    expected1 = 3
    testcase2 = 5
    expected2 = 5
    testcase3 = 6
    expected3 = 8
    solution = Fibonacci()
    assert(solution.fib(testcase1) == expected1)
    assert(solution.fib(testcase2) == expected2)
    assert(solution.fib(testcase3) == expected3)

def test_removeElement():
    solution = RemoveElements()
    testcase1 = ListNode().createTestCase([1,2,3,4,5, 6])
    testcase1 = solution.removeElements(testcase1, 3)
    expected1 = ListNode().createTestCase([5,4,3,2,1])
    testcase2 = ""
    expected2 = ""
    testcase3 = ""
    expected3 = ""

def test_isPalindrome():
    palin = PalindromeLinkedList()
    testcase1 = ListNode().createTestCase([1,2,2,1])
    expected1 = True
    print(palin.isPalindrome(testcase1) == expected1)

def test_oddEven():
    solution = OddEven()
    pass
def test_reverseList():
    solution = ReverseList()
    testcase1 = ListNode().createTestCase([1,2,3,4,5])
    testcase1 = solution.reverseList(testcase1)
    expected1 = ListNode().createTestCase([5,4,3,2,1])
    testcase2 = ""
    expected2 = ""
    testcase3 = ""
    expected3 = ""
    
    assert(solution.checkTest(testcase1, expected1))
    #assert(solution.reverseList(testcase2) == expected2)
    #assert(solution.reverseList(testcase3) == expected3)