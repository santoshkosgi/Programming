class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        req_sum = sum(nums)
        if req_sum % 2 != 0:
            return False
        req_sum = int(req_sum / 2)
        return self.split(req_sum, nums[0], None, [], [], nums[1:]) or self.split(req_sum, None, nums[0], [], [],
                                                                                  nums[1:])

    def split(self, req_sum, num1, num2, arr1, arr2, nums):
        # Checking if we have added all the numbers, we have to see if partitioned arrays have equal sum.
        import copy
        arr1 = copy.deepcopy(arr1)
        arr2 = copy.deepcopy(arr2)
        if num1 is not None:
            arr1.append(num1)
        if num2 is not None:
            arr2.append(num2)
        if sum(arr1) > req_sum or sum(arr2) > req_sum:
            return False
        if len(nums) == 0:
            if sum(arr1) == sum(arr2):
                return True
            return False

        num = nums[0]
        return self.split(req_sum, num, None, arr1, arr2, nums[1:]) or self.split(req_sum, None, num, arr1, arr2,
                                                                                  nums[1:])
sol = Solution()
print(sol.canPartition([1,5,11,5]))