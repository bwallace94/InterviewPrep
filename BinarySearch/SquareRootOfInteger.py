class Solution:
    # @param A : integer
    # @return an integer
    def sqrt(self, A):
        minimum = 0
        maximum = A
        if A == 1:
            return 1
        while maximum - minimum > 1:
            middle = (maximum+minimum)/2
            if middle * middle > A:
                maximum = middle
            elif middle * middle < A:
                minimum = middle
            else:
                return middle
        return minimum
