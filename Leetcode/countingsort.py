"""
This algorithms works when we have to a set of numbers given in some range.
We hash them and find the oocurences of each number and using min and max of the range, we will find the sorted order
"""

class CountingSort(object):
    def __init__(self, start, end, numbers):
        """

        @param start: Minimum of the numbers
        @param end: Maximum of the numbers
        @param numbers: Array of numbers
        """
        self.start = start
        self.end = end
        self.numbers = numbers

    def do_counting_sort(self):
        """
        This function performs the counting sort.
        @return: Sorted Array
        """
        result = [0 for _ in range(self.start, self.end+1)]
        # Finding frequencies of each number in the array
        for num in self.numbers:
            index = num - self.start
            result[index] += 1

        # Calculating cumulative sum of the frequencies of the numbers in the result array.
        for i in range(1, len(result)):
            result[i] = result[i-1] + result[i]

        result_numbers = [0 for _ in self.numbers]

        for index, last_index in enumerate(result):
            # Checking for the first number
            if index == 0:
                # Checking if there were non zero number of self.start numbers
                if last_index != 0:
                    for i in range(last_index):
                        result_numbers[i] = self.start
                continue
            # Checking if there are non-zero occurences of a number
            if result[index] != result[index - 1]:
                for i in range(result[index - 1], last_index):
                    result_numbers[i] = self.start + index
        return result_numbers


if __name__ == '__main__':
    count_sort = CountingSort(start=5, end=20, numbers=[7,7,9, 10, 13, 14, 15, 15, 5, 6, 7, 8, 9, 10, 20, 18])
    print(count_sort.do_counting_sort())



