n = int(input())
s1 = list(map(int, input().split()))[::-1]
s2 = []

answer = 'Nice'
for i in range(1, n+1):
    if s2 and s2[-1] == i:
        s2.pop()
    elif s1:
        while s1 and s1[-1] != i:
            s2.append(s1.pop())
        if s1:
            s1.pop()
        else:
            answer = 'Sad'
            break
    else:
        answer = 'Sad'
        break

print(answer)