class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left = 0
        right = len(height) - 1
        max_area = 0
        while left < right:
            max_area = max(max_area, (right - left) * min(height[left], height[right]))
            if height[left] < height[right]:
                for i in range(left + 1, right + 1):
                    if i == right:
                        left = i
                    if height[i] > height[left]:
                        left = i
                        break

            else:
                i = right - 1
                while i >= left:
                    if i == left:
                        right = i
                    if height[i] > height[right]:
                        right = i
                        break
                    i -= 1
        return max_area

sol = Solution()
print(sol.maxArea([1,8,6,2,5,4,8,3,7]))