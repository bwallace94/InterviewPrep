class Solution:
    # @param A : string
    # @return an integer
    def lengthOfLongestSubstring(self, A):
        d = {}
        longest = 1
        if A == "":
            return 0
        if len(A) == 1:
            return 1
        start = 0
        while start < len(A):
            end = start
            letters = set()
            letters.add(A[start])
            while end+1 < len(A) and A[end+1] not in letters:
                letters.add(A[end+1])
                end += 1
            longest = max(longest,end-start+1)
            if end == len(A) - 1:
                break
            double = A[end+1]
            # print double
            find_double = start
            # print start
            while True:
                if A[find_double] == double:
                    break
                else:
                    find_double += 1
            start = find_double + 1
            # print start
            
        
        return longest