class Solution:
    # @param A : list of integers
    # @return a list of integers
    def plusOne(self, A):
        remainder = 0
        A.reverse()
        for i,digit in enumerate(A):
            if i == 0:
                new_digit = digit + 1
            else:
                new_digit = digit
            new_digit += remainder
            remainder = 0
            remainder = new_digit / 10
            new_digit = new_digit % 10
            A[i] = new_digit 
        A.reverse()
        if remainder != 0:
            A = [1] + A
        while True:
            if A[0] == 0:
                A = A[1:]
            else:
                break
        return A
