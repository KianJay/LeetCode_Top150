class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split(" ")
        res = []
        for i in s:
            if i != "":
                res.append(i)
        return " ".join(res[::-1])