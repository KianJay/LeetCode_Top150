class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        dic = {}

        for char in magazine:
            if char not in dic:
                dic[char] = 1
            else:
                dic[char] += 1
        
        for char in ransomNote:
            if char in dic and dic[char] > 0:
                dic[char] -= 1
            else:
                return False
        return True