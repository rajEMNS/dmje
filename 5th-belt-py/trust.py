def findJudge(n, trust):
    first = [i[0] for i in trust]

    case1 = (n * (n + 1)) // 2 - sum(set(first))

    if case1 == 0:
        return -1
    else:
        for j in range(1, n + 1):
            if j == case1:
                continue
            elif [j, case1] not in trust:
                return -1
        return case1

first_input = input()  

n = int(input()) 

trust_input = input().split() 

trust = []
for i in range(0, len(trust_input), 2):
    trust.append([int(trust_input[i]), int(trust_input[i + 1])])

judge = findJudge(n, trust)
print(judge)