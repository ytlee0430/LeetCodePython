class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        tl = len(needle)
        for i in range(len(haystack)):
            s = haystack[i:i+tl]
            if s == needle:
                return i
        return -1