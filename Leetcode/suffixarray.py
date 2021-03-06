"""
This code has methods to compute suffix array, LCP array and some applications of both.
"""

"""
TODO: Try using radixsort instead of quicksort
LPS Array
Some Applications of Suffix Arrays
"""

class SuffixArray(object):
    def __init__(self, text):
        self.text = text
        self.suffixarray = []
        self.lps = []
        self.suffix_array_dict = {}

    def compute_suffix_array_naive(self):
        """
        This function given a string a string computes a suffix array using bruteforce way
        @param text: String.
        @return: Array of sorted suffixes
        """
        for start_pos in range(len(self.text)):
            self.suffixarray.append(self.text[start_pos:])

        self.suffixarray.sort()
        return self.suffixarray

    def compute_suffix_array_optimal(self):
        """
        The idea here is first create the suffixes, sort them by first two charecters, then sort them by first four
        characters using suffixes starting at 3 position of the suffix. After this, the suffixes are sorted
        based on first four charecters. Repeat this process untill the max length of string is covered.
        @return: sorted suffixes and also its starting position.
        """

        suffix_array_dict = {}
        sorted_suffixes_index = []
        for start_pos in range(len(self.text)):
            suffix_array_dict[start_pos] = self.text[start_pos:]
            # Initially assuming some sorted order
            sorted_suffixes_index.append(start_pos)
        rank1 = {}

        for index in sorted_suffixes_index:
            rank1[index] = ord(suffix_array_dict[index][0]) - ord('a')

        # sorted_suffixes_index = [x for _, x in sorted(zip(rank1, sorted_suffixes_index), key=lambda pair: pair[0])]
        # rank1.sort()
        first_element = True

        next_suffix_start_index = 1

        while next_suffix_start_index < len(self.text):
            rank2 = {}
            for index in sorted_suffixes_index:
                if index + next_suffix_start_index > len(self.text) - 1:
                    rank2[index] = -1
                    continue
                rank2[index] = rank1[index+next_suffix_start_index]
            sorted_suffixes_index = self.sort_suffix_array(sorted_suffixes_index, rank1, rank2)
            rank1 = self.compute_newrank(sorted_suffixes_index, rank1, rank2)
            next_suffix_start_index *= 2

        for i in sorted_suffixes_index:
            print(suffix_array_dict[i])
        self.suffix_array_dict = suffix_array_dict
        self.suffixarray = sorted_suffixes_index

    def sort_suffix_array(self, sorted_suffixes_index, rank1, rank2):
        """
        This function sorts numbers present in sorted_suffixes_index based on the values of rank1 and then rank2
        @param sorted_suffixes_index: Suffix array which stores start indices of array
        @param rank1: first rank of each suffix starting at a index
        @param rank2: second rank of each suffix starting at a index
        @return: sorted_suffixes_index
        """
        # sorted_suffixes_index.sort(key=rank1.get)

        self.quicksort(sorted_suffixes_index, 0, len(sorted_suffixes_index)-1, rank1)

        # Now we have to iterate through the sorted suffix array and sort the subset of suffix array based on rank2
        start_index = 0
        end_index = 0
        first_element = True
        prev_rank = rank1[sorted_suffixes_index[0]]
        for index, suffix_start_index in enumerate(sorted_suffixes_index):
            if first_element is True:
                first_element = False
                continue
            curr_rank = rank1[suffix_start_index]
            if curr_rank != prev_rank:
                self.quicksort(sorted_suffixes_index, start_index, end_index, rank2)
                # sorted_suffixes_index_subset = sorted_suffixes_index[start_index:end_index+1]
                # sorted_suffixes_index_subset.sort(key=rank2.get)
                # sorted_suffixes_index[start_index:end_index + 1] = sorted_suffixes_index_subset
                start_index = end_index + 1
                end_index = start_index
                prev_rank = rank1[sorted_suffixes_index[start_index]]
            else:
                end_index += 1
        self.quicksort(sorted_suffixes_index, start_index, end_index, rank2)
        # sorted_suffixes_index_subset = sorted_suffixes_index[start_index:end_index + 1]
        # sorted_suffixes_index_subset.sort(key=rank2.get)
        # sorted_suffixes_index[start_index:end_index + 1] = sorted_suffixes_index_subset

        return sorted_suffixes_index

    def quicksort(self, sorted_suffixes_index, start_index, end_index, rank):
        """
        This is inplace quicksort
        @param sorted_suffixes_index: Array that needs to be sorted
        @param rank: Based on this rank
        @return: sorted array which is sorted inplace
        """
        low = start_index
        high = end_index - 1
        pivot = rank[sorted_suffixes_index[end_index]]
        if not (low <= high):
            return
        while low <= high:
            while rank[sorted_suffixes_index[low]] <= pivot and low < end_index:
                low += 1
            while rank[sorted_suffixes_index[high]] > pivot and high > start_index:
                high -= 1
            if low < high:
                sorted_suffixes_index[low], sorted_suffixes_index[high] = sorted_suffixes_index[high], \
                                                                          sorted_suffixes_index[low]
            else:
                break

        sorted_suffixes_index[low], sorted_suffixes_index[end_index] = sorted_suffixes_index[end_index], \
                                                                       sorted_suffixes_index[low]
        self.quicksort(sorted_suffixes_index, start_index, low - 1, rank)
        self.quicksort(sorted_suffixes_index, low + 1, end_index, rank)

    @staticmethod
    def compute_newrank(sorted_suffixes_index, rank1, rank2):
        """
        This method computes new rank, starting with zero. If elements at two consecutive indices of rank1 and rank2
        are same, they get same rank. Else, one more than the previous one. All this is in the context of suffix arrays
        @param rank1:
        @param rank2:
        @return:
        """
        new_rank = {}
        rank = 0
        first_entry = True
        for suffix_index in sorted_suffixes_index:
            if first_entry is True:
                first_entry = False
                new_rank[suffix_index] = rank
                prev_rank1 = rank1[suffix_index]
                prev_rank2 = rank2[suffix_index]
                continue
            curr_rank1 = rank1[suffix_index]
            curr_rank2 = rank2[suffix_index]
            if prev_rank1 != curr_rank1 or prev_rank2 != curr_rank2:
                rank += 1
                new_rank[suffix_index] = rank
                prev_rank1, prev_rank2 = curr_rank1, curr_rank2
            else:
                new_rank[suffix_index] = rank

        return new_rank

    def compute_lps_array(self):
        """
        LPS array is defined as longest prefix between a suffix and its predecessor in the suffix array.
        So, for the first element in the suffix array there will not be a lps.
        This function computes lcp array of the suffix array. Uses computed suffix array and suffix array dict.
        Using Kansai Algorithm
        @return: lcp array.
        """
        rank_dict = {start_pos: index for index, start_pos in enumerate(self.suffixarray)}
        # Minimum length of the prefix which we know already.
        min_prefix_match = 0
        self.lps = [None for _ in self.suffixarray]
        for start_pos in range(len(self.text)):
            curr_string = self.suffix_array_dict[start_pos]
            pos_in_suffix_array = rank_dict[start_pos]
            if pos_in_suffix_array == 0:
                self.lps[pos_in_suffix_array] = None
                continue
            # Get the string which is before this curr_string in the suffix array.
            prev_string_start_position = self.suffixarray[pos_in_suffix_array - 1]
            prev_string = self.suffix_array_dict[prev_string_start_position]

            # Minimum lenght to check for longest prefix
            min_length_to_check = min(len(curr_string), len(prev_string))
            num_prefix_char_match = 0
            for h in range(min_prefix_match, min_length_to_check):
                if curr_string[h] == prev_string[h]:
                    num_prefix_char_match += 1
                else:
                    break
            self.lps[pos_in_suffix_array] = min_prefix_match + num_prefix_char_match
            min_prefix_match += num_prefix_char_match
            if min_prefix_match >= 1:
                min_prefix_match -= 1
        print(self.lps)


if __name__ == '__main__':
    # ssipqississippi
    suffix_array = SuffixArray(text="ababaa")
    suffix_array.compute_suffix_array_optimal()
    suffix_array.compute_lps_array()