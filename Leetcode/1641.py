class Solution:
    def countVowelStrings(self, n: int) -> int:
        """
        Idea is to start computing number of sorted vowel strings for a given length using
        sorted vowel strings for length -1.
        lets say we want to compute sorted vowel strings for length 4. So number of
        strings start with "a" is equal to total number of strings of length-1. for "e" is equal
        to total number of strings of length - 1 - "string start with "a""
        Similarly for the rest.
        """
        vowels = ["a", "e", "i", "o", "u"]

        counts_dict = {key: 1 for key in vowels}
        total_strings = sum(counts_dict.values())

        for i in range(2, n + 1):
            temp_dict = {}
            cum_count = 0
            for index, vowel in enumerate(vowels):
                if index == 0:
                    temp_dict[vowel] = total_strings
                    cum_count += counts_dict[vowel]
                else:
                    temp_dict[vowel] = total_strings - cum_count
                    cum_count += counts_dict[vowel]
            counts_dict = temp_dict
            total_strings = sum(counts_dict.values())

        return sum(counts_dict.values())


sol = Solution()
sol.countVowelStrings(3)