from math import ceil


def solution(r1, r2):
    answer = 0
    sqr2 = 2**0.5
    m = int(r1/sqr2)+1
    e = int(r2/sqr2)+1
    for i in range(1, m):
        answer += int(((r2**2)-(i**2))**0.5) - ceil(((r1**2)-(i**2))**0.5) + 1
    for i in range(m, e):
        answer += int(((r2**2)-(i**2))**0.5) - i
    answer *= 8
    answer += (e-m)*4 + (r2-r1+1)*4
    return answer