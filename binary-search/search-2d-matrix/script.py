from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        columns = len(matrix[0])
        left = 0
        right = rows * columns - 1
        while left <= right:
            middle = ((right - left) // 2) + left
            middle_row = middle // columns
            middle_column = middle - middle_row * columns
            if matrix[middle_row][middle_column] == target:
                return True
            elif matrix[middle_row][middle_column] < target:
                left = middle + 1
            else:
                right = middle - 1
        return False



class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        columns = len(matrix[0])
        left = 0
        right = rows * columns - 1
        while left <= right:
            middle = ((right - left) // 2) + left
            middle_row = middle // columns
            middle_column = middle - middle_row * columns
            if matrix[middle_row][middle_column] < target:
                left = middle + 1
            elif matrix[middle_row][middle_column] > target:
                right = middle - 1
            else:
                return True
        return False

# matrix = [[1,2,4,8],[10,11,12,13],[14,20,30,40]] 
# target = 10

# matrix=[[1,3,5,7],[10,11,16,20],[23,30,34,60]]
# target=3

# matrix=[[1]]
# target=2

matrix=[[1,2,4,8],[10,11,12,13],[14,20,30,40]]
target=10

x = Solution()
print(x.searchMatrix(matrix, target))