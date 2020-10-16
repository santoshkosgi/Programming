"""
This script has functions to find Longest Palindromic substring using various approaches.
"""

class Node(object):
    def __init__(self, key):
        """
        Represents each node of the tree. It contains a key and children which is a dictionary.
        @param key: key of the node
        """
        self.key = key
        self.children = {}
        # This dictionary stores for each text the position at which this charecter occured
        self.text_occurence = {}


class SuffixTree(object):
    def __init__(self, texts):
        # An array containing list of texts
        self.texts = texts
        self.suffix_tree = Node("main")

    def get_list_of_suffixes(self, text):
        suffixes_list = []
        start_index_of_suffix = len(text) - 1
        while start_index_of_suffix >= 0:
            suffixes_list.append((start_index_of_suffix, text[start_index_of_suffix:]))
            start_index_of_suffix -= 1
        return suffixes_list

    def build_suffix_tree(self):
        for text_index, text in enumerate(self.texts):
            suffixes_list = self.get_list_of_suffixes(text)
            for start_index, suffix in suffixes_list:
                root = self.suffix_tree
                for char in suffix:
                    # Checking if suffix tree creation is not started yet
                    if char in root.children:
                        root = root.children[char]
                        if text_index not in root.text_occurence:
                            root.text_occurence[text_index] = []
                        root.text_occurence[text_index].append(start_index)
                    else:
                        root.children[char] = Node(key=char)
                        root = root.children[char]
                        if text_index not in root.text_occurence:
                            root.text_occurence[text_index] = []
                        root.text_occurence[text_index].append(start_index)
                    start_index += 1
        return self.suffix_tree

    def get_lps(self):
        """
        This function finds the longest palindromic substring given suffix tree constructed on text and its reverse.
        Approach is to find substring which is present in both of them and also some constraint on positions in
        actual and reversed to check if its pallindrome.
        Assumes that length of self.texts is two.
        @return: returns the substring and position at which it occurs.
        """
        stack = list()
        stack.append(self.suffix_tree)
        processed_string = []
        longest_substring = ""
        while len(stack) > 0:
            node = stack.pop()
            if node == "remove":
                processed_string.pop()
                continue
            if node.key != "main":
                processed_string.append(node.key)
                stack.append("remove")
            # Checking of the node has been seen more than once.
            if len(node.text_occurence) == 2 and len(processed_string) > len(longest_substring):
                occurences_in_first_string = node.text_occurence[0]
                occurences_in_second_string = node.text_occurence[1]
                for end_pos in occurences_in_first_string:
                    start_pos = end_pos - len(processed_string) + 1
                    req_pos = len(self.texts[0]) - 1 - start_pos
                    if req_pos in occurences_in_second_string:
                        longest_substring = "".join(processed_string)
                        break
            if node.key != "main" and len(node.text_occurence) < 2:
                continue
            for child in node.children:
                stack.append(node.children[child])
        return longest_substring

if __name__ == '__main__':
    text = "abcdabbafe"
    texts = [text]
    texts.append(text[::-1])
    suffix_tree = SuffixTree(texts=texts)
    suffix_tree.build_suffix_tree()
    print(suffix_tree.get_lps())
