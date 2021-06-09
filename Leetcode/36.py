class Solution:
    def isValidSudoku(self, board):
        """
        Idea is make set of each row, column and box and see if there are no
        repetations
        """
        rows = []

        columns = {}

        for column in range(9):
            columns[column] = []

        for row in range(len(board)):
            rows = []
            if (row) % 3 == 0 or row == 0:
                box = {}
                box[0] = []
                box[1] = []
                box[2] = []
            for column in range(9):
                curr_num = board[row][column]
                if board[row][column] == '.':
                    continue
                if board[row][column] in rows or board[row][column] in columns[column]:
                    return False
                rows.append(curr_num)
                columns[column].append(curr_num)

                # Checking for boxes
                # As we are processing row wise, after processing of every three rows,
                # Boxes should be reinitialised. Based on the column, we have to decide
                # which box the element should go and check for duplicates.
                box_num = int(column / 3)
                if curr_num in box[box_num]:
                    print("here")
                    return False
                box[box_num].append(curr_num)

        return True
sol = Solution()
print(sol.isValidSudoku([["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]))