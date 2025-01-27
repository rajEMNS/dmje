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
    for data in lst[1:]:
        new_node = Node(data)
        current.next = new_node
        new_node.prev = current
        current = new_node
    return head

def print_linked_list(head):
    current = head
    while current:
        print(current.data,end = " ")
        current = current.next
    print()

n = int(input())
input_list = list(map(int,input().split()))
head = create_doubly_linked_list(input_list)
print_linked_list(head)
