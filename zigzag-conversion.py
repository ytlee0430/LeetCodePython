class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if len(s) < 2 or numRows == 1:
            return s
        resultArray = ["" for i in range(numRows)]
        downward = False
        current_index = 0
        for i in range(len(s)):
            if i % (numRows-1) == 0:
                downward = not downward
            resultArray[current_index] += s[i]
            if downward:
                current_index += 1
            else:
                current_index -= 1
        return "".join(resultArray)
