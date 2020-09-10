"""
The problem here is to find if there exists a subset of an array equal to the given sum
"""


class Solution(object):
    def subsetsum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        result = False
        if len(nums) == 0:
            return False
        if len(nums) == 1:
            if nums[0] == k:
                return True
        for index, num in enumerate(nums):
            processed_array = nums[0:index] + nums[index+1:]
            result = result or self.subsetsum(processed_array, k - num) or self.subsetsum(processed_array, k)
        return result

    def subsetsum_dp(self, nums, k):
        result = [[False for _ in range(k+1)] for _ in range(len(nums)+1)]
        result[0][0] = True
        rows, columns = len(result), len(result[0])
        for i in range(1, rows):
            for j in range(columns):
                if nums[i-1] > k:
                    result[i][j] = result[i-1][j]
                else:
                    result[i][j] = result[i-1][j] or result[i-1][k - nums[i-1]]
        return result[-1][-1]


sol = Solution()
print(sol.subsetsum_dp([1, 2, 3, 4, 5, 6], 9))