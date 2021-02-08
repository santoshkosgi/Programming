class Solution:
    def mctFromLeafValues(self, arr) -> int:
        """
        Checked some hints and finally came up DP solution.
        dp[i,j] = min(dp[i,k]+dp[k+1,j]+max(arr[i,k+1])*max(arr[i+1, j+1]))
        This is of O(n^3) complexity. As we have to compute n8n matrix and each of which
        takes O(n) time.
        """
        dp = [[0 for _ in arr] for _ in arr]

        for end_index in range(len(arr)):
            for start_index in range(len(arr)):
                if start_index + end_index >= len(arr):
                    break
                if end_index == 0:
                    dp[start_index][start_index + end_index] = arr[start_index]
                else:
                    min_value = None
                    for k in range(start_index, start_index + end_index):
                        temp_value = dp[start_index][k] + dp[k + 1][start_index + end_index] + max(arr[start_index: k + 1]) * max(
                            arr[k + 1: start_index + end_index + 1])
                        if min_value is None:
                            min_value = temp_value

                        min_value = min(min_value, temp_value)

                    dp[start_index][start_index + end_index] = min_value
        return dp[0][-1] - sum(arr)


sol = Solution()
sol.mctFromLeafValues([6,2,4])