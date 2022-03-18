def solution(n: int) -> int:
    q = list(range(1, n + 1))
    k = 0

    while (l := len(q)) > 1:
        if k == 0:
            q = q[1::2]
        else:
            q = q[::2]

        if l % 2 == 1:
            k = (k + 1) % 2
    
    return q[0]


print(solution(int(input())))
