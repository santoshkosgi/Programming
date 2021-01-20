class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        start_index = 0
        prev_num = nums[0]
        for _ in range(len(nums)):
            next_index = (start_index + k) % (len(nums))
            next_num = nums[next_index]
            nums[next_index] = prev_num
            start_index = next_index
            prev_num = next_num
        return nums
sol = Solution()
sol.rotate([-1,-100,3,99], 2)