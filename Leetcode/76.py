class Solution:
    def minWindow(self, s: str, t: str) -> str:
        from collections import Counter
        result = ""
        t_dict = Counter(t)
        found = False
        for start_index in range(len(s)):
            if s[start_index] in t_dict:
                found = True
                break
        if found is False:
            return result

        end_index = start_index
        s_dict = {}

        while end_index < len(s):
            if s[end_index] not in s_dict:
                s_dict[s[end_index]] = 0
            s_dict[s[end_index]] += 1

            # Checking if the window is not found yet.
            if self.is_window_found(s_dict, t_dict) is False:
                end_index += 1
            else:
                if result == "" or len(result) > (end_index - start_index + 1):
                    result = s[start_index: end_index + 1]

                s_dict[s[start_index]] -= 1
                if s_dict[s[start_index]] == 0:
                    s_dict.pop(s[start_index])
                start_index += 1

                for index in range(start_index, end_index + 1):
                    if s[index] not in t_dict or s_dict[s[index]] > t_dict[s[index]]:
                        s_dict[s[index]] -= 1
                        if s_dict[s[index]] == 0:
                            s_dict.pop(s[index])
                    else:
                        start_index = index
                        break
                if self.is_window_found(s_dict, t_dict) is True:
                    result = s[start_index: end_index + 1]

                end_index += 1

        return result

    def is_window_found(self, s_dict, t_dict):
        for char in t_dict:
            if char not in s_dict:
                return False
            if t_dict[char] > s_dict[char]:
                return False
        return True


sol = Solution()
sol.minWindow("bba", "ab")