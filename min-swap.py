class Solution:
    def minSwaps(self, s: str) -> int:
        startZero = {"1": 0, "0": 0}
        startOne = {"1": 0, "0": 0}
        isOdd = True
        for str in s:
            if isOdd:
                if str == "1":
                    startZero[str] += 1
                else:
                    startOne[str] += 1
            else:
                if str == "0":
                    startZero[str] += 1
                else:
                    startOne[str] += 1
            isOdd = not isOdd

        if (startZero["1"] == startZero["0"]) or (startOne["1"] == startOne["0"]):
            return min(startZero["1"], startOne["1"])

        return -1

Solution().minSwaps("100")