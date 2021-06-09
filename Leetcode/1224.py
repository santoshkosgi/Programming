class Solution:
    def maxEqualFreq(self, nums) -> int:
        """
        Idea is to maintain freq dict and for each prefix and check if the frequencies
        fall into two buckets and check if removing one element from the bucket where there
        is only one number satisfies the required condition or not. While all of this
        keep track of the length of the longest prefix satisfied the condition.
        """

        result = 1
        freq_dict = {nums[0]: 1}
        for index in range(1, len(nums)):
            if nums[index] not in freq_dict:
                freq_dict[nums[index]] = 0
            freq_dict[nums[index]] += 1
            if self.check_condition(freq_dict) is True:
                result = index + 1
        return result

    def check_condition(self, freq_dict):
        from collections import Counter
        values = list(freq_dict.values())
        values_dict = Counter(values)

        if len(values_dict) != 2:
            return False

        if 1 in values_dict and values_dict[1] == 1:
            return True

        values_sort = list(values_dict.keys())
        values_sort.sort()
        if values_dict[values_sort[1]] == 1 and values_sort[1] - 1 == values_sort[0]:
            return True
        return False


sol = Solution()
sol.maxEqualFreq([10,2,8,9,3,8,1,5,2,3,7,6])