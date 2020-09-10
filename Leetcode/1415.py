class Solution(object):
    def getHappyString(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        import math
        total_number_of_strings = 3 * math.pow(2, n - 1)
        if k > total_number_of_strings:
            return ""
        req_str = []
        if k <= total_number_of_strings / 3:
            req_str.append("a")
        elif k <= 2 * (total_number_of_strings / 3):
            req_str.append("b")
            k = k - (total_number_of_strings / 3)
        else:
            req_str.append("c")
            k = k - (2 * (total_number_of_strings / 3))

        total_number_of_strings = math.pow(2, n - 1)

        for next_char_number in range(1, n):
            alphabet_set = ["a", "b", "c"]
            if k <= total_number_of_strings / 2:
                req_index = 0
            else:
                req_index = 1
                k = k - (total_number_of_strings / 2)
            total_number_of_strings /= 2
            alphabet_set.remove(req_str[next_char_number - 1])
            req_str.append(alphabet_set[req_index])
        return "".join(req_str)

sol = Solution()
print(sol.getHappyString(3,9))