#https://kalvium.community/livebooks/psup_v1_sc002/PSUP_Data_structures/psup_practical_min_stack  (link for trying this code)
class MaxStack:
    def __init__(self):
        self.stack = []
        self.max_stack = []

    def push(self, val):
        self.stack.append(val)
        if not self.max_stack:
            self.max_stack.append(val)
        else:
            self.max_stack.append(max(val, self.max_stack[-1]))

    def pop(self):
        if self.stack:
            popped_value = self.stack.pop()
            self.max_stack.pop()  
            return popped_value  
        return None 

    def getMax(self):
        if self.max_stack:
            return self.max_stack[-1]
        return None
    
n = int(input())
stack = MaxStack()
output = [] 

for _ in range(n):
    query = list(map(int, input().split()))
    if query[0] == 1:  
        stack.push(query[1])
    elif query[0] == 2:  
        popped_value = stack.pop()
        if popped_value is not None:
            output.append(popped_value) 
    elif query[0] == 3: 
        output.append(stack.getMax())  

print(" ".join(map(str, output)))
