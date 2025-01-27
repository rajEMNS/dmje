class Node:
    def __init__(self, data):  
        self.data = data
        self.next = None

def create_linked_list(lst):
    if not lst:
        return None
    head = Node(lst[0])
    current = head
    for data in lst[1:]:
        current.next = Node(data)
        current = current.next
    return head

def print_linked_list(head):
    current = head
    while current:
        print(current.data, end=" ")
        current = current.next
    print()

def delete_occurrences(head, x):
    while head and head.data == x:
        head = head.next
    current = head
    while current and current.next:
        if current.next.data == x:
            current.next = current.next.next
        else:
            current = current.next
    return head

n, x = map(int, input().split())  
values = list(map(int, input().split()))  
head = create_linked_list(values)  
head = delete_occurrences(head, x) 
print_linked_list(head)

