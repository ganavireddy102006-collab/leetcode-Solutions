class Solution(object):
    def solveNQueens(self, n):
        res=[]
        board=[['.']*n for _ in range(n)]
        def backtrack(r):
            if r==n:
                res.append([''.join(row)for row in board])
                return
            for c in range(n):
                if all(board[i][c]=='.'and   abs(r-i)!=abs(c-j)
                for i in range(r)
                for j in range(n) if board[i][j]=='Q'):
                    board[r][c]='Q'
                    backtrack(r+1)
                    board[r][c]='.'
        backtrack(0)
        return res

        