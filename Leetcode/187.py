class Solution:
    def findRepeatedDnaSequences(self, s: str):
        dict_freq = set([])
        result = []
        for start_index in range(len(s)):
            req_str = s[start_index: start_index+10]
            if len(req_str) != 10:
                break
            if req_str not in dict_freq:
                dict_freq.add(req_str)
            else:
                result.append(req_str)
        return result

sol = Solution()
sol.findRepeatedDnaSequences("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT")