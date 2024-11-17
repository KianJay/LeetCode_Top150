class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = [char for char in s if char.isalnum()]
        j, i = 0 , len(s) -1
        while j < i :
            if s[j] != s[i]:
                return False
            j+=1
            i-=1
        return True
            
