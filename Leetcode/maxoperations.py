class Solution(object):
    def minOperations(self, nums, x):
        """
        :type nums: List[int]
        :type x: int
        :rtype: int
        """
        s = sum(nums) - x
        if s == 0:
            return len(nums)
        subarray_sum = {}
        subarray_sum[0] = None
        sum_till_now = 0
        result = -1
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
        if result == -1:
            return -1
        return len(nums) - result

sol = Solution()