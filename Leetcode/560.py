class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # This dictionary stores sum from index i till j including both of them
        subarray_sum = {}
        subarray_sum[0] = 1
        sum_till_now = 0
        result = 0
        for num in nums:
            sum_till_now += num
            if (sum_till_now - k) in subarray_sum:
                result += subarray_sum[sum_till_now - k]
            subarray_sum[sum_till_now] = subarray_sum.get(sum_till_now, 0) + 1
        return result

sol = Solution()
sol.subarraySum([1,2,1,2,1], 2)