class Solution:
    # @param A : tuple of integers
    # @return an integer
    def repeatedNumber(self, A):
        dict_nums = {}
        for num in A:
            if num in dict_nums:
                return num
            dict_nums[num] = 1
        return -1
            
