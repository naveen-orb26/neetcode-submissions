class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        grid = defaultdict(set)
        for i in range(9):
            for j in range(9):
                val = board[i][j]
                idx = (i//3,j//3)
                if val==".":
                    continue
                if val in rows[i] or val in cols[j] or val in grid[idx]:
                    return False
                rows[i].add(val)
                cols[j].add(val)
                grid[idx].add(val)

      
        return True
                    