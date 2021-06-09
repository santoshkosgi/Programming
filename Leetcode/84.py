class Solution:
    def largestRectangleArea(self, height):
        """
        The idea is to find the area of the consecutive rectangles where each of the
        recatange is the smallest one. Now, to find the left and right boundaries for
        each histogram such that particular histogram is smallest, firstly we ll maintain a
        stack of increasing histograms, so the left boundary is the first left element
        in the stack and right boundary can be found when an element that is less than found            in the array
        """
        stack = [-1]
        max_height = 0
        for index in range(len(height)):
            if len(stack) == 1:
                stack.append(index)
                max_height = max(height[index], max_height)
                continue
            if height[stack[-1]] <= height[index]:
                stack.append(index)
            else:
                while len(stack) > 1 and height[index] < height[stack[-1]]:
                    temp_index = stack.pop()
                    width = index - stack[-1] - 1
                    height_ = height[temp_index]
                    area = width * height_
                    max_height = max(area, max_height)
                stack.append(index)
        last_index = len(height)
        if len(stack) != 1:
            while len(stack) > 1:
                temp_index = stack.pop()
                width = last_index - stack[-1] - 1
                height_ = height[temp_index]
                area = width * height_
                max_height = max(area, max_height)
        return max_height


sol = Solution()
print(sol.largestRectangleArea([2,1,5,6, 0, 2,3]))