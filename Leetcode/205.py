class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        from collections import Counter
        s_dict = Counter(s)
        t_dict = Counter(t)

        # Now the idea is to process each list, such that we replace consecutive
        # similar charecters by local frequency and global frequency.
        start_index = 0
        end_index = 0
        s_list = []
        while end_index < len(s):
            if s[start_index] == s[end_index]:
                end_index += 1
            else:
                local_freq = end_index - start_index

                s_list.append(str(local_freq) + "_" + str(s_dict[s[start_index]]))
                start_index = end_index
        local_freq = end_index - start_index
        s_list.append(str(local_freq) + "_" + str(s_dict[s[start_index]]))
        start_index = 0
        end_index = 0
        t_list = []
        while end_index < len(t):
            if t[start_index] == t[end_index]:
                end_index += 1
            else:
                local_freq = end_index - start_index
                t_list.append(str(local_freq) + "_" + str(t_dict[t[start_index]]))
                start_index = end_index
        local_freq = end_index - start_index
        t_list.append(str(local_freq) + "_" + str(t_dict[t[start_index]]))
        if t_list == s_list:
            return True
        return False

sol = Solution()
sol.isIsomorphic(s="egg", t="add")