class Solution:
    # @param A : string
    # @return an integer
    def isPalindrome(self, A):
        alphanumeric = "abcdefghijklmnopqrstuvwxyz1234567890"
        A.replace(" ","")
        A = A.lower()
        new_A = ""
        for i,letter in enumerate(A):
            if letter in alphanumeric:
                new_A += letter
        A = new_A
        if A == "":
            return 1
        start_index = 0
        end_index = len(A) - 1
        while True:
            if A[start_index] != A[end_index]:
                return 0
            if start_index == end_index:
                break
            elif start_index > end_index:
                break
            start_index += 1
            end_index -= 1
        return 1
            
