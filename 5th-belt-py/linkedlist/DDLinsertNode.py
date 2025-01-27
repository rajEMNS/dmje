class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

def create_doubly_linked_list(lst):
    if not lst:
        return None
    head = Node(lst[0])
    current = head
    for value in lst[1:]:
        new_node = Node(value)
        current.next = new_node
        new_node.prev = current
        current = new_node
    return head

def insert_at_position(head, k, val):
    new_node = Node(val)
    if k == 0:
        new_node.next = head
        if head:
            head.prev = new_node
        return new_node

    current = head
    for _ in range(k - 1):
        if current.next is None: 
            break
        current = current.next
    new_node.next = current.next
    if current.next:
        current.next.prev = new_node
    new_node.prev = current
    current.next = new_node

    return head

def print_linked_list(head):
    current = head
    while current:
        print(current.data, end=" ")
        current = current.next
    print()

n, k, val = map(int, input().split())
arr = list(map(int, input().split()))
head = create_doubly_linked_list(arr)
head = insert_at_position(head, k, val)
print_linked_list(head)
