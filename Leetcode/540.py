class Solution:
    def singleNonDuplicate(self, nums) -> int:
        """
        The idea is to find the number which has different number on both the sides.
        Find the start index of the number if its repeating and based on whether its
        odd or even we can decide whether the solution is present in left or right
        if its even, the solution is present in the right part of mid, else left part
        """

        start = 0
        end = len(nums) - 1

        while start < end:
            # Taking the floor of the mid.
            mid = int((start + end) / 2)
            found = False
            if mid + 1 <= end:
                # mid is the start index of a repeating number.
                if nums[mid] == nums[mid + 1]:
                    found = True
                    if mid % 2 != 0:
                        end = mid - 1
                    else:
                        start = mid + 2

            if mid - 1 >= start and found is False:
                # mid - 1 is the start index of a repeating number.
                if nums[mid] == nums[mid - 1]:
                    found = True
                    if (mid - 1) % 2 != 0:
                        end = mid - 2
                    else:
                        start = mid + 1
            if found is False:
                return nums[mid]
        return nums[start]

sol = Solution()
print(sol.singleNonDuplicate([1,1,2,3,3,4,4,8,8]))