# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : head node of linked list
    # @param B : head node of linked list
    # @return the head node in the linked list
    def addTwoNumbers(self, A, B):
        if B == None:
            return A
        if A == None:
            return B
        total = A.val+B.val
        remainder = total/10
        digit = total % 10
        head = ListNode(digit)
        current_node = head
        A = A.next
        B = B.next
        while True:
            if A == None and B == None:
                if remainder == 1:
                    current_node.next = ListNode(1)
                return head
            elif A == None:
                total = B.val + remainder
                B = B.next
            elif B == None:
                total = A.val + remainder
                A = A.next
            else:
                total = A.val + B.val + remainder
                A = A.next
                B = B.next
            remainder = total/10
            digit = total % 10
            current_node.next = ListNode(digit)
            current_node = current_node.next
        
                
