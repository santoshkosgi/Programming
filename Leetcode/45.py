class Solution:
    def jump(self, nums) -> int:
        """
        30/1/2021
        This is same formulation as Jump Game V, which I solved just now.
        Will code this later
        """
        min_jumps = [0 for _ in nums]
        index = len(nums) - 2
        while index >= 0:
            if len(nums) - 1 - index <= nums[index]:
                min_jumps[index] = 1
            else:
                min_jump = None
                for i in range(index, index+nums[index]+1):
                    if i == index:
                        continue
                    if min_jump is None:
                        min_jump = min_jumps[i] + 1
                    else:
                        min_jump = min(min_jump, min_jumps[i] + 1)
                min_jumps[index] = min_jump
            index -= 1
        return min_jumps[0]

sol = Solution()
sol.jump([2,3,0,1,4])