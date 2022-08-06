from typing import List


class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        if(len(people) <= 1): return people
        queue = []
        people.sort()
        i = 0
        while(people):
            if(people[i][1]>people[i+1][1]):
                popped = people[i+1]
                people[i+1] = people[i]
                people[i] = popped
                i = 0
            else:
                i += 1
                
if __name__ == "__main__":
    testcase1 = [[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]
    expected1 = [[5,0],[7,0],[5,2],[6,1],[4,4],[7,1]]
    testcase2 = ""
    expected2 = ""
    testcase3 = ""
    expected3 = ""
    solution = Solution()
    print(solution.reconstructQueue(testcase1) == expected1)
    print(solution.reconstructQueue(testcase2) == expected2)
    print(solution.reconstructQueue(testcase3) == expected3)