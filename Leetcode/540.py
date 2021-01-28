class Solution:
    def singleNonDuplicate(self, nums) -> int:
        low = 0
        high = len(nums) - 1

        while low <= high:
            mid = int((low + high) / 2)
            # Have to find if the solution exists in left subarray or right one
            if mid % 2 == 0:
                if nums[mid] == nums[mid - 1]:
                    high = mid
                else:
                    low = mid
            else:
                if nums[mid] == nums[mid - 1]:
                    low = mid
                else:
                    high = mid
        return low


sol = Solution()
sol.singleNonDuplicate([1,1,2,3,3,4,4,8,8])