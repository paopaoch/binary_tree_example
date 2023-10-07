# linked list

# list: array of item
# linked list: each node will point to 1 more node and only one node will point to that node.

# 3 -> 4 -> 5 -> null
# ^ Head

class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
    

def reverse(head):
    prev = None
    while head:
        temp_head = head.next
        head.next = prev
        prev = head
        head = temp_head
    return prev

if __name__ == "__main__":
    last_node = Node(5)
    middle_node = Node(4, last_node)
    head = Node(3, middle_node)