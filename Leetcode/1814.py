class Solution:
    def countNicePairs(self, nums):
        rev_array = self.compute_rev(nums)
        diff_dict = {}

        for index in range(len(nums)):
            diff = nums[index] - rev_array[index]
            if diff not in diff_dict:
                diff_dict[diff] = []
            diff_dict[diff].append(index)

        result = 0
        for diff in diff_dict:
            result += ((len(diff_dict[diff]) * (len(diff_dict[diff]) - 1)) // 2)

        return result

    def compute_rev(self, nums):
        """
        This function computes the reverse of all the elements of array.
        """
        rev_array = []
        for num in nums:
            new_num = 0
            while num != 0:
                last_element = num % 10
                new_num = new_num * 10 + last_element
                num = num // 10
            rev_array.append(new_num)
        return rev_array

sol = Solution()
sol.countNicePairs([13,10,35,24,76])