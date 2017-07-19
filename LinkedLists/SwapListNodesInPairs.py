# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def swapPairs(self, A):
        if A == None:
            return A
        if A.next == None:
            return A
        first = A
        second = A.next
        previous = None
        new_head = A.next
        while first!=None and second!=None:
            first.next = second.next
            second.next = first
            if previous != None:
                previous.next = second
            previous = first
            first = first.next
            if first != None:
                second = first.next
        return new_head
