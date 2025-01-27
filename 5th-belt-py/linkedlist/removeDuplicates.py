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
    while current :
        print(current.data, end = " ")
        current = current.next
    print()
    
def remove_duplicates(head):
    if not head and head.next:
        return None
    current = head
    while current :
        runner = current
        while runner.next:
            if runner.next.data == current.data:
                runner.next = runner.next.next
            else:
                runner = runner.next
        current = current.next
    return head

    
n = int(input())
input_list = list(map(int,input().split()))
head = create_linked_list(input_list)
remove = remove_duplicates(head)
print_linked_list(remove)
    
    
    
    
    
    
    
    
    
    
    
    
    
    