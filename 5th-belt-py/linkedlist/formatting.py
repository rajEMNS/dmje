# output : 1 -> 2 -> 3 -> 4 -> 5 -> Nullptr
def print_linked_list(head):
    current = head
    while current:
        print(current.data, end=" -> ")
        current = current.next
    print("nullptr")



#output: print a space when there is no elements in linked list 
def print_linked_list(head):
    if not head:  # If the linked list is empty
        print(" ", end="")  # Print a space
        return
    current = head
    while current:
        print(current.data, end=" -> ")
        current = current.next
    print("None")


#when there is no elements print no elements
def print_linked_list(head):
    if not head:  # If the linked list is empty
        print("No elements", end="")  # Print "No elements"
        return
    current = head
    while current:
        print(current.data, end=" -> ")
        current = current.next
    print("None")
