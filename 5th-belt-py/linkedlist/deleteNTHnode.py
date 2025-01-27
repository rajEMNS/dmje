class Node:
    def __init__(self, data):  
        self.data = data
        self.next = None

# Function to create a linked list from a given array
def create_linked_list(arr):
    if not arr:
        return None
    head = Node(arr[0])
    current = head
    for data in arr[1:]:
        current.next = Node(data)
        current = current.next
    return head

# Function to print the linked list
def print_linked_list(head):
    current = head
    while current:
        print(current.data, end=" ")
        current = current.next
    print()

# Function to calculate the length of the linked list
def length(head):
    curr = head
    l = 0
    while curr:
        curr = curr.next
        l += 1
    return l

def remove_node(head, n):
    l = length(head)
    temp = head
    if l == n:
        return head.next
    for i in range(l - n - 1):
        temp = temp.next
    temp.next = temp.next.next
    return head

n = int(input())  
input_list = list(map(int, input().split())) 
pos = int(input()) 
head = create_linked_list(input_list)
head = remove_node(head, pos)
print_linked_list(head)
