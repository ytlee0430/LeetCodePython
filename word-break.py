from typing import List


class Solution:
    _end = '_end_'
    _trie = None

    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        def make_trie(words):
            root = dict()
            for word in words:
                current_dict = root
                for w in word:
                    current_dict = current_dict.setdefault(w, {})
                current_dict[self._end] = self._end
            return root

        self._trie = make_trie(wordDict)

        def find_word(answers, answer, str, start, end, current_trie):
            if end == len(str):
                if self._end in current_trie:
                    if answer == "":
                        new_answer = str[start:end]
                    else:
                        new_answer = f"{answer} {str[start:end]}"
                    answers.append(new_answer)
                return

            if self._end in current_trie:
                if answer == "":
                    new_answer = str[start:end]
                else:
                    new_answer = f"{answer} {str[start:end]}"
                find_word(answers, new_answer, str, end, end, self._trie)

            if str[end] not in current_trie:
                return

            find_word(answers, answer, str, start, end + 1, current_trie[str[end]])

        result = []
        find_word(result, "", s, 0, 0, self._trie)
        return result

Solution().wordBreak("bb", ["a","b","bbb","bbbb"])
