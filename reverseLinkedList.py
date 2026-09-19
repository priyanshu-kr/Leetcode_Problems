'''
206. Reverse Linked List

Given the beginning of a singly linked list head, reverse the list, and return the new beginning of the list.

Example 1:

Input: head = [0,1,2,3]
Output: [3,2,1,0]

Example 2:

Input: head = []
Output: []

Constraints:
0 <= The length of the list <= 5000.
-5000 <= Node.val <= 5000
'''

head = [0,1,2,3]

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head):
        prev = None
        current = head

        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        return prev


def create_linked_list(values):
    if not values:
        return None

    head = ListNode(values[0])
    current = head

    for value in values[1:]:
        current.next = ListNode(value)
        current = current.next

    return head


def print_linked_list(head):
    current = head

    while current:
        print(current.val, end="")

        if current.next:
            print(" → ", end="")

        current = current.next

    print()


# Create linked list
values = [0, 1, 2, 3]

head = create_linked_list(values)

print("Original list:")
print_linked_list(head)

# Reverse the linked list
solution = Solution()
head = solution.reverseList(head)

print("Reversed list:")
print_linked_list(head)