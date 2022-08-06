
class LongestSubWithoutRepChar:
    def lengthOfLongestSubstringTest(self, s: str) -> int:
        # len 0
        # len 1
        # len >= 2
        if(len(s) < 1):
            return 0
        if(len(s) == 1):
            return 1
        else:
            substringDict, maxSubstringDict, substring = {}, {}, ''
            i = 0
            while(i < len(s)):
                currchar = s[i]
                get = substringDict.get(s[i])
                if(get is None):
                    substringDict[s[i]] = i # index
                    substring = substring + s[i]
                    i += 1
                else:
                    # remove current char from substringdict
                    k = substringDict[s[i]]+1
                    j = 0
                    while(substring[j] != s[k]): # remove all chars from dict
                        del substringDict[substring[j]]
                        j += 1
                    substring = substring[j:]
                if(i == len(s)):
                    break;
                if(len(substringDict)>len(maxSubstringDict)):
                    maxSubstringDict = substringDict.copy()
                
        return len(maxSubstringDict)

    def lengthOfLongestSubstring(self, s: str) -> int:
        substring = ''
        substringDict = {}
        
    
    def testAnswer(self, answer:int, expected:int):
        return answer == expected