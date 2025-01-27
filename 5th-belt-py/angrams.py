#check if given strings are angrams or not 
s1,s2 = map(str,input().split())
count1 = {}
for char in s1:
    if char in count1:
        count1[char] += 1 
    else:
        count1[char]= 1 

count2 = {}
for char in s2:
    if char in count2:
        count2[char] += 1 
    else:
        count2[char] = 1 

if count1==count2:
    print("Anagrams")
else:
    print("Not Anagrams")



