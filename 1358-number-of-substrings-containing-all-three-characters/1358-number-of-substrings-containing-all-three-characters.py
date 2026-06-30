class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        start,result=0,0
        count = {'a': 0, 'b': 0, 'c': 0}
        for end in range(len(s)):
            count[s[end]]+=1
            while all(count.values()):
                count[s[start]]-=1
                start+=1
            result+=start
        return result
            
        