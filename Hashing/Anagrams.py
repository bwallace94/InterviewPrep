class Solution:
    # @param A : tuple of strings
    # @return a list of list of integers
    def anagrams(self, A):
        all_words_dict = {}
        for i,word in enumerate(A):
            word_list = list(word)
            word_list.sort()
            sorted_word = "".join(word_list)
            all_words_dict[sorted_word] = all_words_dict.get(sorted_word,[])
            all_words_dict[sorted_word].append(i+1)
        anagrams = []
        for l in all_words_dict.values():
            anagrams.append(l)
        return anagrams
                
            
