class Solution:
    def merge(self, nums1, m: int, nums2, n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1_index = 0
        nums2_index = 0

        for index in range(m, len(nums1)):
            nums1[index] = None

        while nums2_index < n:
            if nums1[nums1_index] is None:
                nums1[nums1_index] = nums2[nums2_index]
                nums1_index += 1
                nums2_index += 1
                continue

            if nums1[nums1_index] <= nums2[nums2_index]:
                nums1_index += 1
            else:
                # Move all the elements by one position towards the right and copy number from nums2
                temp_index = len(nums1) - 1
                while temp_index > nums1_index:
                    nums1[temp_index] = nums1[temp_index - 1]
                    temp_index -= 1
                nums1[nums1_index] = nums2[nums2_index]
                nums1_index += 1
                nums2_index += 1

        return nums1

sol = Solution()
sol.merge([1,2,3,0,0,0], 3, [2,5,6], 3)