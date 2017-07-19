class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return an integer
    def diffPossible(self, A, B):
        if len(A) <= 1:
            return 0
        seen = {}
        for i in A:
            if i-B in seen:
                return 1
            if i+B in seen:
                return 1
            seen[i] = True
        return 0