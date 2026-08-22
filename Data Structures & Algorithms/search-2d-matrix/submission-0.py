class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows_start=cols_start=0
        rows_end = len(matrix)-1
        cols_end = len(matrix[0])-1
        while rows_start<=rows_end:
            midrow = rows_start + (rows_end-rows_start)//2
            if matrix[midrow][0] <= target <= matrix[midrow][cols_end]:
                cols_start = 0
                cols_end_inner = cols_end
                while cols_start<=cols_end_inner:
                    midcol = cols_start + (cols_end_inner - cols_start)//2
                    if target == matrix[midrow][midcol]:
                        return True
                    if target < matrix[midrow][midcol]:
                        cols_end_inner=midcol-1
                    else:
                        cols_start=midcol+1
                return False
            elif target < matrix[midrow][0]:
                rows_end=midrow-1
            else:
                rows_start=midrow+1
        
        return False
