def lemonade_change(bills):
    five = 0
    ten = 0
    for bill in bills:
        if bill == 5:
            five += 1
        elif bill == 10:
            if five == 0:
                return ("False")
            else:
                five -=1
                ten += 1
        elif bill == 20:
            if ten > 0 and five > 0:
                five += 1
                ten += 1
            elif five >= 3:
                five -= 3
            else:
                return("False")
    return("True")
    
n = int(input())
bills = list(map(int,input().split()))
print(lemonade_change(bills))