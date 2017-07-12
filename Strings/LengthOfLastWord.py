class Solution:
    # @param A : string
    # @return an integer
    def lengthOfLastWord(self, A):
        # last_word_seen = ""
        last_seen_len = 0
        for i,letter in enumerate(A):
            if letter == " " and i+1 < len(A) and A[i+1] != " ":
                last_word_seen = ""
                last_seen_len = 0
            elif letter != " ":
                # last_word_seen += letter
                last_seen_len += 1
        return last_seen_len