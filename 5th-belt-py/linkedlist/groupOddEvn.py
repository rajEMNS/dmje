# given a linked list write a code to group all the number at odd indicex together 
# and display it first and then group number at even idices together and then display it 

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

def odd_even_reorder(head):
    if not head or not head.next:
        return None
    odd_head = head
    even_head = head.next
    odd = odd_head
    even = even_head
    
    while even and even.next:
        odd.next = even.next
        odd = odd.next
        even.next = odd.next
        even = even.next
    odd.next = even_head
    
    return odd_head

n = int(input()) 
values = list(map(int, input().split()))  
head = create_linked_list(values)  
reordered_head = odd_even_reorder(head)  
print_linked_list(reordered_head) 
