class Solution(object):
    def matrixBlockSum(self, mat, K):
        """
        :type mat: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """
        cum_sum_matrix = [[0 for _ in mat[0]] for _ in mat]

        cum_sum_matrix[0][0] = mat[0][0]

        rows, columns = len(mat), len(mat[0])

        for row in range(1, rows):
            cum_sum_matrix[row][0] = cum_sum_matrix[row - 1][0] + mat[row][0]

        for column in range(1, columns):
            cum_sum_matrix[0][column] = cum_sum_matrix[0][column - 1] + mat[0][column]

        for row in range(1, rows):
            for column in range(1, columns):
                cum_sum_matrix[row][column] = mat[row][column] + cum_sum_matrix[row - 1][column] + cum_sum_matrix[row][
                    column - 1] - cum_sum_matrix[row - 1][column - 1]

        result = [[0 for _ in mat[0]] for _ in mat]

        for i in range(rows):
            for j in range(columns):
                start_row = max(i - K, 0)
                end_row = min(i + K, rows-1)
                start_col = max(j - K, 0)
                end_col = min(j + K, columns-1)
                if start_row != 0 and start_col != 0:
                    result[i][j] = cum_sum_matrix[end_row][end_col] - cum_sum_matrix[start_row-1][end_col] - \
                                   cum_sum_matrix[end_row][start_col-1] + cum_sum_matrix[start_row-1][start_col-1]
                elif start_row == 0 and start_col == 0:
                    result[i][j] = cum_sum_matrix[end_row][end_col]
                elif start_row == 0:
                    result[i][j] = cum_sum_matrix[end_row][end_col] - cum_sum_matrix[end_row][start_col - 1]
                else:
                    result[i][j] = cum_sum_matrix[end_row][end_col] - cum_sum_matrix[start_row-1][end_col]
        return result


sol = Solution()
print(sol.matrixBlockSum([[76, 4, 73], [21, 8, 56], [4, 56, 61], [70, 32, 38], [31, 94, 67]], 1))