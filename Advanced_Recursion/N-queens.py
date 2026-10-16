class Solution:
    def solveNQueens(self, n):
        result = []
        board = [["."] * n for _ in range(n)]

        columns = set()
        diagonals1 = set()  # row - col
        diagonals2 = set()  # row + col

        def backtrack(row):
            if row == n:
                result.append(["".join(r) for r in board])
                return

            for col in range(n):
                if (
                    col in columns
                    or (row - col) in diagonals1
                    or (row + col) in diagonals2
                ):
                    continue

                # Place queen
                board[row][col] = "Q"
                columns.add(col)
                diagonals1.add(row - col)
                diagonals2.add(row + col)

                # Move to the next row
                backtrack(row + 1)

                # Backtrack: remove queen
                board[row][col] = "."
                columns.remove(col)
                diagonals1.remove(row - col)
                diagonals2.remove(row + col)

        backtrack(0)
        return result