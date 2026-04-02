class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        top,bot = 0, len(matrix) - 1

        while top<=bot: 
            row = (top + bot) // 2

            if matrix[row][-1] < target:
                top = row + 1
                print(f"top = {top}")
            elif matrix[row][0] > target:
                bot = row - 1
            else:
                break
        row = matrix[row]
        print(row)

        l,r = 0, len(row) - 1

        while l <= r:
            m = (l+r) // 2

            if row[m] < target:
                l = m + 1
            elif row[m] > target:
                r = m - 1
            elif row[m] == target:
                return True
        return False

            