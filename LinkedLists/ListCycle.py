# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the first node in the cycle in the linked list
    def detectCycle(self, A):
        if A == None or A.next == None:
            return 
        slow = A
        fast = A
        first = True
        while fast.next != None and fast.next.next != None:
            if slow == fast and not first:
                loop = 1
                slow = slow.next
                while slow != fast:
                    loop += 1
                    slow = slow.next
                slow = A
                fast = A
                for i in range(loop):
                    fast = fast.next
                while slow != fast:
                    slow = slow.next
                    fast = fast.next
                return slow
            else:
                slow = slow.next
                fast = fast.next.next
            first = False
        return
