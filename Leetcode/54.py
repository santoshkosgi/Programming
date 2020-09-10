class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """

        rows, columns = len(matrix), len(matrix[0]) if matrix else 0
        start_row = 0
        start_column = 0
        end_row = rows - 1
        end_column = columns - 1

        result = []

        while start_row <= end_row and start_column <= end_column:
            result.extend(self.get_spiral_of_matrix(matrix, start_row, start_column, end_column, end_row))
            start_row += 1
            end_row -= 1
            start_column += 1
            end_column -= 1

        return result

    def get_spiral_of_matrix(self, matrix, start_row, start_column, end_column, end_row):
        """
        This function accepts a matrix and pther required fields and finds the spiral
        ordering of the matrix.
        """
        spiral_order = []

        for column in range(start_column, end_column + 1):
            spiral_order.append(matrix[start_row][column])

        for row in range(start_row + 1, end_row + 1):
            spiral_order.append(matrix[row][end_column])

        if end_row != start_row:
            for column in reversed(range(start_column, end_column)):
                spiral_order.append(matrix[end_row][column])

        if start_column != end_column:
            for row in reversed(range(start_row + 1, end_row)):
                spiral_order.append(matrix[row][start_column])

        return spiral_order

sol = Solution()
print(sol.spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]]))