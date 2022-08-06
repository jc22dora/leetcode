class IsomorphicStrings:
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


        
        
    