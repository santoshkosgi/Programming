"""
This file has methods to do KMP pattern finding algorithm.
"""

def compute_lps_array(pattern):
    """
    This function accepts a pattern and computes longest common prefix suffix length for each position in the
    pattern
    @param pattern: Pattern String
    @return: List which has lps for each position of the pattern.
    """
    lps = [0 for _ in pattern]
    j = 0
    i = 1
    while i < len(pattern):
        if pattern[i] == pattern[j]:
            lps[i] = j + 1
            j += 1
            i += 1
        elif j != 0:
            j = lps[j-1]
        else:
            lps[i] = 0
            i += 1
    return lps

def kmp_pattern_search(text, pattern):
    """
    @param text:
    @param pattern:
    @return: occurences of pattern in the text.
    """
    lps_array = compute_lps_array(pattern)
    text_index = 0
    pattern_index = 0
    result = []
    while text_index < len(text):
        if text[text_index] == pattern[pattern_index]:
            # Found a match
            if pattern_index == len(pattern) - 1:
                result.append(text_index - len(pattern) + 1)
                text_index += 1
                pattern_index = lps_array[-1]
            else:
                text_index += 1
                pattern_index += 1
        else:
            if pattern_index == 0:
                text_index += 1
            else:
                pattern_index = lps_array[pattern_index - 1]
    return result



print(kmp_pattern_search(text="ABABDABACDABABCABAB", pattern="ABABCABAB"))
