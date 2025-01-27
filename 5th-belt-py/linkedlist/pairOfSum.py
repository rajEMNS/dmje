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
    
def pair_sum(head,x):
    visited = set()
    current = head
    while current :
        complement = x - current.data
        if complement in visited:
            print(complement,current.data)
            return
        visited.add(current.data)
        current = current.next
    print(-1)
    
n,x = map(int,input().split())
input = list(map(int,input().split()))
head = create_linked_list(input)
pair_sum(head,x)
        
    