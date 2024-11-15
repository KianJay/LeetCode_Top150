class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s_list = s.split()
        s_last_str = len(s_list[-1])
        return s_last_str
        #make it list  and return len(n[:-1])