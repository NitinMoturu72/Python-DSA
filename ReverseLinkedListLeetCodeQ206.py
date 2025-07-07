# Reverse Linked List
 
# Given the beginning of a singly linked list head, reverse the list, and return the new beginning of the list.

# Example 1:

# Input: head = [0,1,2,3]

# Output: [3,2,1,0]
# Example 2:

# Input: head = []

# Output: []
# Constraints:

# 0 <= The length of the list <= 1000.
# -1000 <= Node.val <= 1000


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
            
        return prev

# Iterative Solution:
# We use three pointers: prev, curr, and nxt.
# Prev is set to None, curr is set to head, and nxt is used to store the next node.
# In each iteration, we reverse the link by setting curr.next to prev, then move prev and curr one step forward.
# The process continues until curr becomes None, at which point prev will be the new head of the reversed list.
# Time complexity is O(n) where n is the number of nodes in the list,
# Space complexity is O(1) since we are using a constant amount of extra space.