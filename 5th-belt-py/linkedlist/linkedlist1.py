#create a linked list and print it 
class Node:
    def __init__(self, data):  
        self.data = data
        self.next = None
        
def create_linked_list(list):
    if not list:
        return None
    head = Node(list[0])
    current = head
    for data in list[1:]:
        current.next = Node(data)
        current = current.next
    return head

def print_linked_list(head):
    current = head
    while current :
        print(current.data,end=" ")
        current = current.next
    print()
        
n = int(input())
input_list = list(map(int,input().split()))
head = create_linked_list(input_list)
print_linked_list(head)
            