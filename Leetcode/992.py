class Solution:
    def subarraysWithKDistinct(self, nums, k):
        start = 0
        end = 0
        freq_dict = {}
        result = []
        for index, num in enumerate(nums):
            if index == 0:
                freq_dict[num] = 1
            else:
                if num not in freq_dict:
                    freq_dict[num] = 0
                freq_dict[num] += 1
                end = index

            i = start
            while len(freq_dict) > k:
                freq_dict[nums[i]] -= 1
                if freq_dict[nums[i]] == 0:
                    freq_dict.pop(nums[i])
                i += 1
            start = i
            if len(freq_dict) == k:
                result.append(nums[start: end + 1])
        return result

sol = Solution()
sol.subarraysWithKDistinct([1,2,1,2,3], 2)
