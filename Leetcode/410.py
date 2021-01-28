class Solution:
    def splitArray(self, nums, m):
        """
        The idea is to iterate through the range of possible solutions
        and see if we can split the array into m splits for a given solution.
        The minimum value of solution occurs when number of splits is equal to number
        of elements in the array which is equal to maximum number of the array.
        While the maximum value of the result can be found when number of splits is equal
        to one and the solution is sum(nums)
        """

        # Occurs when number of splits is equal to length of nums
        min_value = max(nums)
        # Occurs when number of splits is equal to 1.
        max_value = sum(nums)
        final_solution = None

        while min_value <= max_value:
            mid = int((min_value + max_value) / 2)
            num_of_splits,  solution= self.number_of_splits_possible_for_a_sum(nums, mid)
            if num_of_splits == m:
                if final_solution is None:
                    final_solution = solution
                final_solution = min(final_solution, solution)
                max_value = mid - 1
            elif num_of_splits > m:
                min_value = mid + 1
            else:
                max_value = mid - 1

        return min_value

    def number_of_splits_possible_for_a_sum(self, nums, req_sum):
        no_of_splits = 0
        temp_sum = 0
        max_sum = 0
        for num in nums:
            if temp_sum + num <= req_sum:
                temp_sum += num
            else:
                no_of_splits += 1
                max_sum = max(temp_sum, max_sum)
                temp_sum = num
        max_sum = max(temp_sum, max_sum)
        no_of_splits += 1
        return no_of_splits, max_sum

sol = Solution()
print(sol.splitArray([2,3,1,1,1,1,1], 5))
