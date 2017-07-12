class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maxSubArray(self, A):
        highest_sum = max(A)
        current_sum = 0
        for i in range(len(A)):
            current_sum += A[i]
            highest_sum = max(highest_sum,current_sum)
            current_sum = max(current_sum,0)
        return highest_sum
                
                
        
