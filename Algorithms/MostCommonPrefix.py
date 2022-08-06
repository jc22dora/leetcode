from typing import List


class MostCommonPrefix:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        pfx  = ""
        for j in range(len(strs[0])):
            pfd = {}
            curr = ""
            for i in range(len(strs)):
                if(j>len(strs[i])-1): break
                if(pfd.get(strs[i][j])):
                    pfd[strs[i][j]] += 1
                else:
                    curr = strs[i][j]
                    pfd[strs[i][j]] = 1
            if(not curr): break
            if(pfd[curr] != len(strs)): break
            pfx += curr
            
        return pfx

    