'''
21. Merge Two Sorted Lists

You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.


Example 1:
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

Example 2:
Input: list1 = [], list2 = []
Output: []

Example 3:
Input: list1 = [], list2 = [0]
Output: [0]
 

Constraints:

The number of nodes in both lists is in the range [0, 50].
-100 <= Node.val <= 100
Both list1 and list2 are sorted in non-decreasing order.
'''

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1, list2):

        dummy = node = ListNode()

        while list1 and list2:

            if list1.val < list2.val:
                node.next = list1
                list1 = list1.next

            else:
                node.next = list2
                list2 = list2.next

            node = node.next

        node.next = list1 or list2

        return dummy.next


# Helper function: create a linked list from a Python list
def create_linked_list(values):
    dummy = ListNode()
    current = dummy

    for value in values:
        current.next = ListNode(value)
        current = current.next

    return dummy.next


# Helper function: print a linked list
def print_linked_list(head):
    values = []

    while head:
        values.append(head.val)
        head = head.next

    print(values)


# Input
list1 = [1, 2, 4]
list2 = [1, 3, 4]

# Convert Python lists → Linked Lists
head1 = create_linked_list(list1)
head2 = create_linked_list(list2)

# Merge
solution = Solution()
merged_head = solution.mergeTwoLists(head1, head2)

# Output
print("Merged list:")
print_linked_list(merged_head)