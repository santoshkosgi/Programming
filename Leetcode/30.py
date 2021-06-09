class Solution:
    def findSubstring(self, s, words) :
        words_dict = {}
        for word in words:
            if word not in words_dict:
                words_dict[word] = 0
            words_dict[word] += 1

        word_len = len(words[0])
        req_len = len(words[0]) * len(words)

        start_index = 0
        result = []
        while start_index <= len(s) - req_len:
            s_dict = {}
            for i in range(len(words)):
                curr_word = s[start_index + (i*word_len): start_index + ((i+1)*word_len)]
                if curr_word not in s_dict:
                    s_dict[curr_word] = 0
                s_dict[curr_word] += 1
            if s_dict == words_dict:
                result.append(start_index)
            start_index += 1
        return result


sol = Solution()
print(sol.findSubstring("lingmindraboofooowingdingbarrwingmonkeypoundcake", ["fooo","barr","wing","ding","wing"]))