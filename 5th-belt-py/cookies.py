#code passes only 14/15 test cases
def find_children(g,s):
    content_children = 0
    used_cookies = [False] * len(s)
    for greed in g:
        for i in range (len(s)):
            if not used_cookies[i]  and s[i] >= greed:
                content_children += 1
                used_cookies[i] = True
                break
    return content_children
            
n = int(input())
g = list(map(int,input().split()))
m = int(input())
s = list(map(int,input().split()))
print(find_children(g,s))
    