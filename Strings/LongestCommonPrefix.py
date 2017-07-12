class Solution:
    # @param A : list of strings
    # @return a strings
    def longestCommonPrefix(self, A):
        shortest_string = ""
        shortest_string_length = float("inf")
        for word in A:
            if len(word) < shortest_string_length:
                shortest_string = word
                shortest_string_length = len(word)
        prefix_dict = {}
        for word in A:
            for i,letter in enumerate(word):
                if i == shortest_string_length:
                    break
                prefix_dict[word[0:i+1]] = prefix_dict.get(word[0:i+1],0) + 1
        longest_prefix = ""
        longest_prefix_length = 0
        for prefix in prefix_dict:
            if prefix_dict[prefix] == len(A) and len(prefix) > longest_prefix_length:
                longest_prefix = prefix
                longest_prefix_length = len(prefix)
        return longest_prefix
        
                
            
