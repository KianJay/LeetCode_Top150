class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        dic_pattern = {}
        dic_s = {}
        words = s.split(" ")

        # 패턴과 단어의 길이가 다르면 False 반환
        if len(pattern) != len(words):
            return False

        for i in range(len(pattern)):
            p = pattern[i]
            w = words[i]

            if p not in dic_pattern:
                dic_pattern[p] = w

            if w not in dic_s:
                dic_s[w] = p

            if dic_pattern[p] != w or dic_s[w] != p:
                return False

        return True

