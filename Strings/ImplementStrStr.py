class Solution:
    # @param haystack : string
    # @param needle : string
    # @return an integer
    def strStr(self, haystack, needle):
        if needle == "" or haystack == "" or len(needle) > len(haystack):
            return -1
        if needle == haystack:
            return 0
        needle_length = len(needle)
        for i in range(len(haystack)-needle_length):
            if haystack[i:i+needle_length] == needle:
                return i
        return -1
