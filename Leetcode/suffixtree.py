"""
This file has python implementation of suffix tress datastructure for a given string.
This is not a compressed suffix tree.
"""


class Node(object):
    def __init__(self, key):
        """
        Represents each node of the tree. It contains a key and children which is a dictionary.
        @param key: key of the node
        """
        self.key = key
        self.children = {}
        self.appeared_more_than_once = False


class SuffixTree(object):
    def __init__(self, text):
        self.text = text
        self.suffix_tree = Node("main")

    def get_list_of_suffixes(self):
        suffixes_list = []
        start_index_of_suffix = len(self.text) - 1
        while start_index_of_suffix >= 0:
            suffixes_list.append(self.text[start_index_of_suffix:])
            start_index_of_suffix -= 1
        return suffixes_list

    def build_suffix_tree(self):
        suffixes_list = self.get_list_of_suffixes()
        for suffix in suffixes_list:
            root = self.suffix_tree
            for char in suffix:
                # Checking if suffix tree creation is not started yet
                if char in root.children:
                    root = root.children[char]
                    root.appeared_more_than_once = True
                else:
                    root.children[char] = Node(key=char)
                    root = root.children[char]
        return self.suffix_tree

    def get_longest_repeated_substring(self):
        """
        Approach is to do depth first search to find a node with appreared_more_than_once_flag is set to True.
        While doing depth first search we also keep track of the path we followed so that we can return strings.
        We will use a stack to perform DFS
        @return:
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
            if node.appeared_more_than_once is True and len(processed_string) > len(longest_substring):
                longest_substring = "".join(processed_string)
            if node.key != "main" and node.appeared_more_than_once is False:
                continue
            for child in node.children:
                stack.append(node.children[child])
        return longest_substring

    def get_longest_pallindromic_substring(self):
        """
        Approach is to find the longest common substring between a string and its reversed string.
        Catch is to find a common substring which is also a pallindrome. This can be done by putting some
        constraints on the starting position of the string.
        @return:
        """
    
if __name__ == '__main__':
    suffixtree = SuffixTree(text="abcpqrabpqpq")
    suffixtree.build_suffix_tree()
    print(suffixtree.get_longest_repeated_substring())