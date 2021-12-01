# """
# This is Master's API interface.
# You should not implement it, or speculate about its implementation
# """
class Master:
    def __init__(self, secret):
        self.secret = secret
        self.count = 0

    def guess(self, word: str) -> int:
        def countMatch(w1):
            count = 0
            for i in range(6):
                if w1[i] == self.secret[i]:
                    count += 1
            return count
        self.count += 1
        if self.count > 9:
            return 1000
        return countMatch(word)

from typing import List
from random import randrange

class Solution:
    def findSecretWord(self, wordlist: List[str], master: 'Master') -> None:
        def countMatch(w1, w2):
            count = 0
            for i in range(6):
                if w1[i] == w2[i]:
                    count += 1
            return count


        while len(wordlist) > 0:
            index = randrange(len(wordlist))
            matchs = master.guess(wordlist[index])
            if matchs == 6:
                return

            i = index + 1
            while i < len(wordlist):
                compare_matched = countMatch(wordlist[index], wordlist[i])
                if compare_matched != matchs:
                    wordlist.remove(wordlist[i])
                    continue
                i += 1
            wordlist.remove(wordlist[index])
        return






Solution().findSecretWord(["wichbx","oahwep","tpulot","eqznzs","vvmplb","eywinm","dqefpt","kmjmxr","ihkovg","trbzyb","xqulhc","bcsbfw","rwzslk","abpjhw","mpubps","viyzbc","kodlta","ckfzjh","phuepp","rokoro","nxcwmo","awvqlr","uooeon","hhfuzz","sajxgr","oxgaix","fnugyu","lkxwru","mhtrvb","xxonmg","tqxlbr","euxtzg","tjwvad","uslult","rtjosi","hsygda","vyuica","mbnagm","uinqur","pikenp","szgupv","qpxmsw","vunxdn","jahhfn","kmbeok","biywow","yvgwho","hwzodo","loffxk","xavzqd","vwzpfe","uairjw","itufkt","kaklud","jjinfa","kqbttl","zocgux","ucwjig","meesxb","uysfyc","kdfvtw","vizxrv","rpbdjh","wynohw","lhqxvx","kaadty","dxxwut","vjtskm","yrdswc","byzjxm","jeomdc","saevda","himevi","ydltnu","wrrpoc","khuopg","ooxarg","vcvfry","thaawc","bssybb","ccoyyo","ajcwbj","arwfnl","nafmtm","xoaumd","vbejda","kaefne","swcrkh","reeyhj","vmcwaf","chxitv","qkwjna","vklpkp","xfnayl","ktgmfn","xrmzzm","fgtuki","zcffuv","srxuus","pydgmq"] ,Master("ccoyyo"))