class Solution:
    def makeFancyString(self, s: str) -> str:
        s = s.lower()
        result = s[:2]
        for char in s[2:]:
            if not (char==result[-1]==result[-2]):
                result += char
        return result