class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s
        
        lists = [[] for _ in range(numRows)]
        count = 0
        direction = 0
        
        for char in s:
            lists[count].append(char)

            if count == 0:
                direction = 1
            elif count == numRows - 1:
                direction = -1

            count += direction
        
        result = "".join("".join(row) for row in lists)
        return result