class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
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
    while current :
        print(current.data,end = " ")
        current = current.next
    print()
    
def reverse_linked_list(head):
    prev = None
    current = head
    while current :
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    return prev
        
                
n = int(input())
a = list(map(int,input().split()))
head = create_linked_list(a)
reversed_head = reverse_linked_list(head)
print_linked_list(reversed_head)
