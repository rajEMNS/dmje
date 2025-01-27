class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

# Function to create a doubly linked list from an array
def create_doubly_linked_list(arr):
    if not arr:
        return None
    head = Node(arr[0])
    curr = head
    for data in arr[1:]:
        new_node = Node(data)
        curr.next = new_node
        new_node.prev = curr
        curr = new_node
    return head

# Function to print a doubly linked list
def print_doubly_linked_list(head):
    curr = head
    while curr:
        print(curr.data, end=" ")
        curr = curr.next
    print()

# Function to reverse a doubly linked list
def reverse_doubly_linked_list(head):
    if not head:
        return None

    current = head
    while current:
        current.prev, current.next = current.next, current.prev
        head = current
        current = current.prev

    return head

n = int(input()) 
input_list = list(map(int, input().split()))  
head = create_doubly_linked_list(input_list)
head = reverse_doubly_linked_list(head)
print_doubly_linked_list(head)
