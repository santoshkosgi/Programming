class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        from collections import Counter
        p = s1
        s = s2
        p_counter = Counter(p)
        s_counter = Counter(s[0:len(p)])
        if p_counter == s_counter:
            return True
        for index in range(len(p), len(s)):
            s_counter[s[index-len(p)]] -= 1
            if s_counter[s[index-len(p)]] == 0:
                s_counter.pop(s[index-len(p)])
            if s[index] not in s_counter:
                s_counter[s[index]] = 0
            s_counter[s[index]] += 1
            if s_counter == p_counter:
                return True
        return False

sol = Solution()
sol.checkInclusion()