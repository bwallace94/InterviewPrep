# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def deleteDuplicates(self, A):
        node = A
        if A == None:
            return 
        while node.next != None:
            if node.next.val == node.val:
                check_node = node.next
                while check_node.val == node.val:
                    if check_node.next == None:
                        check_node = None
                        break
                    if check_node.next.val == node.val:
                        check_node = check_node.next
                    else:
                        break
                if check_node == None:
                    node.next = None
                    break
                node.next = check_node.next
            node = node.next
            if node == None:
                break
        return A
