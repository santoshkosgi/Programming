class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        nums = str(num)

        stack = []

        for num in nums:
            if k == 0:
                stack.append(num)
                continue
            if len(stack) == 0:
                stack.append(num)
            elif num >= stack[-1]:
                stack.append(num)
            else:
                while len(stack) > 0 and (num < stack[-1]) and k > 0:
                    k -= 1
                    stack.pop()
                stack.append(num)

        if k != 0:
            while k != 0 and len(stack) > 0:
                stack.pop()
                k -= 1
        if len(stack) == 0:
            return str(0)
        if stack[0] != "0":
            result = ("".join(stack))
        else:
            start = 0
            while stack[start] == "0" and start < len(stack) - 1:
                start += 1
            result = "".join(stack[start:])
        return result

sol = Solution()
print(sol.removeKdigits("10200", 1))
