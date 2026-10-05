'''
141. Linked List Cycle

Given head, the head of a linked list, determine if the linked list has a cycle in it.
There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.
Return true if there is a cycle in the linked list. Otherwise, return false.

 
Example 1:
Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).

Example 2:
Input: head = [1,2], pos = 0
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 0th node.

Example 3:
Input: head = [1], pos = -1
Output: false
Explanation: There is no cycle in the linked list.
 

Constraints:
The number of the nodes in the list is in the range [0, 104].
-10^5 <= Node.val <= 10^5
pos is -1 or a valid index in the linked-list.
'''

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def create_linked_list(values, pos):
    if not values:
        return None

    # Create all nodes
    nodes = []

    for value in values:
        nodes.append(ListNode(value))

    # Connect nodes
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]

    # Create cycle if pos is valid
    if pos != -1:
        nodes[-1].next = nodes[pos]

    return nodes[0]

####################################################################

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head

        while fast and fast.next: 
            '''
            Why both?
            fast → makes sure fast itself exists.
            fast.next → makes sure fast can make its second jump as it moves two nodes at a time
            '''
            slow = slow.next
            fast = fast.next.next

            if fast == slow:
                return True

        return False

####################################################################

# Create linked list with or without cycle.. 
values = [3,2,0,-4]
pos = 1          # pos = -1 for no cycle
head = create_linked_list(values, pos)

sol = Solution()
print(sol.hasCycle(head))