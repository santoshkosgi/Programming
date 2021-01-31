class Solution:
    def maxJumps(self, arr, d: int) -> int:

        result = [None for _ in arr]

        index = len(arr) - 1
        while index >=0:
            self.get_max_jumps_at_a_index(arr, d, index, result)
            index -= 1
        final = max(result)
        if final > 0:
            return final + 1
        return final

    def get_max_jumps_at_a_index(self, arr, d, index, result):
        if result[index] is not None:
            return result[index]
        # Finding the number of jumps on the right side
        right_side_jumps = 0
        for i in range(index + 1, index + d + 1):
            if i >= len(arr):
                break
            if arr[i] > arr[index]:
                break
            jumps = self.get_max_jumps_at_a_index(arr, d, i, result) + 1
            right_side_jumps = max(jumps, right_side_jumps)

        left_side_jumps = 0
        i = index - 1
        while i >= index - d:
            if i < 0:
                break
            if arr[i] > arr[index]:
                break
            jumps = self.get_max_jumps_at_a_index(arr, d, i, result) + 1
            left_side_jumps = max(left_side_jumps, jumps)
            i -= 1
        result[index] = max(left_side_jumps, right_side_jumps)
        return max(left_side_jumps, right_side_jumps)


sol = Solution()
print(sol.maxJumps([6,4,14,6,8,13,9,7,10,6,12], 2))
