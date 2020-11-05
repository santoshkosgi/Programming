"""
This code has methods to compute suffix array, LCP array and some applications of both.
"""

class SuffixArray(object):
    def __init__(self, text):
        self.text = text
        self.suffixarray = []
        self.lps = []

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
        rank1 = []
        rank2 = []

        for index in sorted_suffixes_index:
            rank1.append(ord(suffix_array_dict[index][0]) - ord('a'))

        sorted_suffixes_index = [x for _, x in sorted(zip(rank1, sorted_suffixes_index), key=lambda pair: pair[0])]
        rank1.sort()
        first_element = True
        for index, rank in enumerate(rank1):
            if first_element is True:
                first_element = False
                rank2 = []
                start_index = index
                prev_rank = rank
                string = suffix_array_dict[sorted_suffixes_index[index]]
                if len(string) > 1:
                    rank2.append(ord(string[1])- ord('a'))
                else:
                    rank2.append(-1)
                end_index = start_index
            else:
                if rank == prev_rank:
                    end_index = index
                    string = suffix_array_dict[sorted_suffixes_index[index]]
                    if len(string) > 1:
                        rank2.append(ord(string[1])- ord('a'))
                    else:
                        rank2.append(-1)
                else:
                    sorted_suffixes_index[start_index:end_index+1] = [x for _, x in sorted(zip(
                        rank2[start_index:end_index+1], sorted_suffixes_index[start_index:end_index+1]), key=lambda pair: pair[0])]

                    rank2[start_index:end_index+1] = sorted(rank2[start_index:end_index+1])
                    start_index = index
                    prev_rank = rank
                    end_index = index
                    string = suffix_array_dict[sorted_suffixes_index[index]]
                    if len(string) > 1:
                        rank2.append(ord(string[1]) - ord('a'))
                    else:
                        rank2.append(-1)
        sorted_suffixes_index[start_index:end_index + 1] = [x for _, x in sorted(zip(
            rank2[start_index:end_index + 1], sorted_suffixes_index[start_index:end_index + 1]),
            key=lambda pair: pair[0])]
        rank2[start_index:end_index+1] = sorted(rank2[start_index:end_index+1])
        for i in sorted_suffixes_index:
            print(suffix_array_dict[i])
        print(rank1, rank2)

    @staticmethod
    def compute_newrank(rank1, rank2):
        """
        This method computes new rank, starting with zero. If elements at two consecutive indices of rank1 and rank2
        are same, they get same rank. Else, one more than the previous one. All this is in the context of suffix arrays
        @param rank1:
        @param rank2:
        @return:
        """
        starting = True
        prev_rank1_element = None
        prev_rank2_element = None
        new_rank = []
        rank = 0
        for index in range(len(rank1)):
            if starting is True:
                prev_rank1_element = rank1[index]
                prev_rank2_element = rank2[index]
                new_rank.append(rank)
            else:
                if rank1[index] != prev_rank1_element or rank2[index] != prev_rank2_element:
                    rank += 1
                    prev_rank1_element = rank1[index]
                    prev_rank2_element = rank2[index]
                new_rank.append(rank)
        return new_rank



    # @staticmethod
    # def quicksort(actual_array, ref_array):
    #     """
    #     This function does quick sort of actual array based on ref array
    #     @param actual_array: Actual array that needs to be sorted
    #     @param ref_array: Ranks of each element in actual array
    #     @return: sorted actual and ref_array
    #     """


if __name__ == '__main__':
    suffix_array = SuffixArray(text="ssipqississippi")
    suffix_array.compute_suffix_array_optimal()