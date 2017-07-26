class Solution:
    # @param A : string
    # @param B : tuple of strings
    # @return a list of integers
    def findSubstring(self, A, B):
        if A == "":
            return []
        if len(B) == 0:
            return []
        word_len = len(B[0])
        total_len = len(B) * word_len
        i = 0
        result = []
        required_words = {}
        for word in B:
            required_words[word] = required_words.get(word,0) + 1
        while i + total_len <= len(A):
            substring = A[i:i+total_len]
            words = {}
            for j in range(len(B)):
                word = A[i+j*word_len:i+j*word_len+word_len]
                words[word] = words.get(word,0) + 1
            # print words
            # print required_words
            if words == required_words:
                result.append(i)
                # print "HERE"
            # print
            i += 1
        return result