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

def reverse_list(head):
    prev = None
    current = head
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    return prev

def add_two_lists(head1, head2):
    head1 = reverse_list(head1)
    head2 = reverse_list(head2)
    
    carry = 0
    result_head = None
    result_tail = None

    while head1 or head2 or carry:
        val1 = head1.data if head1 else 0
        val2 = head2.data if head2 else 0

        total = val1 + val2 + carry

        carry = total // 10  
        new_node = Node(total % 10)

        if result_head is None:
            result_head = new_node
            result_tail = result_head
        else:
            result_tail.next = new_node
            result_tail = result_tail.next

        if head1:
            head1 = head1.next
        if head2:
            head2 = head2.next

    return reverse_list(result_head)

n1 = int(input())  
list1 = list(map(int, input().split()))  
n2 = int(input())  
list2 = list(map(int, input().split()))  
head1 = create_linked_list(list1)
head2 = create_linked_list(list2)
result_head = add_two_lists(head1, head2)
print_linked_list(result_head)
