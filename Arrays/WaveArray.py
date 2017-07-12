class Solution:
    # @param A : list of integers
    # @return a list of integers
    def wave(self, A):
        A.sort()
        wave = []
        i = 0
        lengthA = len(A)
        while i <= lengthA-1:
            if i + 1 <= lengthA-1:
                wave.append(A[i+1])
                wave.append(A[i])
            else:
                wave.append(A[i])
            i += 2
        return wave
            
