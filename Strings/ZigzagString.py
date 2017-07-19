class Solution:
    # @param A : string
    # @param B : integer
    # @return a strings
    def convert(self, A, B):
        if B <= 1:
            return A
        if A == "":
            return B
        rows = []
        for i in range(B):
            rows.append([])
        direction = 1
        level = 0
        for i,letter in enumerate(A):
            rows[level].append(letter)
            level += direction
            if level == B - 1 or level == 0:
                direction *= -1
        final_word = []
        for row in rows:
            final_word += row
        return "".join(final_word)