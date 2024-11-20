class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        dic_s = {}
        dic_t = {}
        for i in range(len(s)):
            if s[i] not in dic_s:
                dic_s[s[i]] = i

            if t[i] not in dic_t:
                dic_t[t[i]] = i
            
            if dic_s[s[i]] != dic_t[t[i]]:
                return False
        return True