"""
https://www.geeksforgeeks.org/longest-sub-array-sum-k/
Idea is to compute sum of the elements till each of the index and see if there was a prev index sum
such that its sum == sum_till_now - req_sum
"""
class Solution(object):
    def maxSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        # stores for a given sum how many the minimum index at which this sum was found.
        subarray_sum = {}
        subarray_sum[0] = None
        sum_till_now = 0
        result = 0
        for index, num in enumerate(nums):
            sum_till_now += num
            if sum_till_now - s in subarray_sum:
                # Checking if sum till a particular index is equal to s
                start_index = subarray_sum[sum_till_now - s]
                if start_index is None:
                    result = max(result, index + 1)
                else:
                    result = max(result, (index - start_index ))
            if sum_till_now not in subarray_sum:
                subarray_sum[sum_till_now] = index
        return result

sol = Solution()
print(sol.maxSubArrayLen(15, [10, 5, 2, 7, 1, 9]))