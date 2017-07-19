class Solution:
    # @param A : integer
    # @return a list of list of integers
    def generate(self, A):
        if A == 0:
            return []
        triangle = [[1]]
        if A == 1:
            return triangle
        triangle.append([1,1])
        for i in range(A-2):
            new_row = [1]
            last_row = triangle[-1]
            for j in range(len(last_row)-1):
                new_row.append(last_row[j]+last_row[j+1])
            new_row.append(1)
            triangle.append(new_row)
        return triangle