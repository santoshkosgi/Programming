class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums_dict = {}

        for index, num in enumerate(nums):
            if num in nums_dict and 2 * num == target:
                return [index, nums_dict[num]]
            nums_dict[num] = index

        for index, num in enumerate(nums):
            if 2 * num == target:
                continue
            if target - num in nums_dict:
                return [index, nums_dict[target - num]]


sol = Solution()
sol.twoSum([3,2,4], 6)