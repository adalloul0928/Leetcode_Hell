class Solution:
    def gameOfLife(self, board) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        neighbors = [(-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]

        rows = len(input)
        cols = len(input[0])

        for row in range(rows):
            for col in range(cols):
                total = 0

                for neighbor in neighbors:
                    r = row + neighbor[0]
                    c = col + neighbor[1]

                    if (r < rows and r >= 0) and (c < cols and c >= 0) and (board[r][c] == 1):
                        total += 1

                if total

input = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]