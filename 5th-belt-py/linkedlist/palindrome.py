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
        
                
def compare_list(head1,head2):
    while head1 and head2:
        if head1.data != head2.data:
            return False
        head1 = head1.next
        head2 = head2.next
    return head1 is None and head2 is None
    
n = int(input())
input_list = list(map(int,input().split()))
head1 = create_linked_list(input_list)
head2 = reverse_linked_list(create_linked_list(input_list))
if compare_list(head1, head2):
    print("Yes")
else:
    print("No")
