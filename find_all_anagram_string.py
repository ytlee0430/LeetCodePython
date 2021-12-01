from collections import Counter
from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        p_length = len(p)
        s_length = len(s)
        result = []
        p_dict = Counter(p)
        s_dict = Counter(s[:len(p)])

        index = 0
        while index < s_length - p_length + 1:
            if s_dict == p_dict:
                result.append(index)
            s_dict[s[index]] -= 1
            if index + p_length < s_length:
                s_dict[s[index + p_length]] += 1
            if s_dict[s[index]] == 0:
                s_dict.pop(s[index], None)
            index += 1
        return result


Solution().findAnagrams("abab", "ab")
