class Solution:
    def binarysearch(self, nums, target):
        start = 0
        end = len(nums) - 1

        while start <= end:
            mid = int((start+end)/2)
            if target < nums[mid]:
                end = mid - 1
            elif target > nums[mid]:
                start = mid + 1
            else:
                return mid
        return -1

    def number_lessthan_target(self, nums, target):
        """
        This function returns the number that is just less than the target of the number is not found.
        If target is less than the starting element it should return -1.
        @param nums:
        @param target:
        @return:
        """
        start = 0
        end = len(nums) - 1
        while start <= end:
            mid = int((start + end)/2)
            if target < nums[mid]:
                end = mid - 1
            elif target > nums[mid]:
                start = mid + 1
            else:
                return mid
        return start - 1

    def number_greaterthan_target(self, nums, target):
        """
        This function returns the number that is just less than the target of the number is not found.
        If target is less than the starting element it should return -1.
        @param nums:
        @param target:
        @return:
        """
        start = 0
        end = len(nums) - 1
        while start <= end:
            mid = int((start + end)/2)
            if target < nums[mid]:
                end = mid - 1
            elif target > nums[mid]:
                start = mid + 1
            else:
                return mid
        return start

    def find_left_most_entry(self, nums, target):
        """
        Here, the array can have duplicate elements and we would like to find the left most occurence of the target
        @param nums:
        @param target:
        @return:
        """
        start = 0
        end = len(nums) - 1
        while start < end:
            mid = int((start + end)/2)
            if target < nums[mid]:
                end = mid - 1
            elif target > nums[mid]:
                start = mid + 1
            else:
                end = mid
        return start

    def find_right_most_entry(self, nums, target):
        """
        Here, the array can have duplicate elements and we would like to find the left most occurence of the target
        @param nums:
        @param target:
        @return:
        """
        import math
        start = 0
        end = len(nums) - 1
        while start < end:
            mid = math.ceil((start + end) / 2)
            if target < nums[mid]:
                end = mid - 1
            elif target > nums[mid]:
                start = mid + 1
            else:
                 start = mid
        return start


sol = Solution()
print(sol.find_right_most_entry([1,2, 2, 2, 3, 3, 4, 5], 3))