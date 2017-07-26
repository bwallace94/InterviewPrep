class Solution:
    # @param A : list of list of integers
    # @param B : integer
    # @return an integer
    def searchMatrix(self, A, B):
        start = 0
        end = len(A)-1
        m = 0
        if len(A) == 0:
            return 0
        if (A[0] != [] and B < A[0][0]) or (A[-1] != [] and B > A[-1][-1]):
            return 0
        while abs(end-start) > 1:
            middle = (end+start)/2
            # print start
            # print end
            # print middle
            # print 
            if A[middle][0] <= B <= A[middle][-1]:
                start = middle
                break
            elif A[middle][0] > B:
                end = middle
            elif A[middle][-1] < B:
                start = middle
        if start != end:
            if A[end][0] <= B <= A[end][-1]:
                start = end
        integers = A[start]
        if integers == []:
            return -1
        start = 0
        end = len(integers)
        while abs(end-start) > 1:
            middle = (start+end)/2
            if integers[middle] == B:
                return 1
            elif integers[middle] > B:
                end = middle
            else:
                start = middle
        if integers[start] == B:
            return 1
        return 0