class Solution:
    def smallestRange(self, nums):
        # Stroing all the first elements in a list in the following form
        # number, index in the list and index of the list.
        elements_list = [(l[0], 0, index) for index, l in enumerate(nums)]
        result = None
        while True:
            elements_list.sort(key=lambda x: x[0])
            curr_range = [elements_list[0][0], elements_list[-1][0]]
            if result is None or ((curr_range[1] - curr_range[0]) < (result[1] - result[0])):
                result = curr_range
            number, index, list_index = elements_list.pop(0)
            if index == len(nums[list_index]) - 1:
                return result

            elements_list.append((nums[list_index][index + 1], index + 1, list_index))


sol = Solution()
sol.smallestRange([[4,10,15,24,26],[0,9,12,20],[5,18,22,30]])