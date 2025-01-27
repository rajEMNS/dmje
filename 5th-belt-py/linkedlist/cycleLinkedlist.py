class Node:
    def _init_(self, data):
        self.data = data
        self.next = None

def isCycle(head, n, p):
    if not head:
        return False
    if p != -1:
        temp = head
        loop_node = None
        for i in range(n):
            if i == p - 1:
                loop_node = temp
            if temp.next:
                temp = temp.next
        temp.next = loop_node
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False

def create_linked_list(list):
    if not list:
        return None
    head = Node(list[0])
    current = head
    for data in list[1:]:
        current.next = Node(data)
        current = current.next
    return head

n = int(input())
arr = list(map(int, input().split()))
p = int(input())

head = create_linked_list(arr)
result = isCycle(head, n, p)
print(result)