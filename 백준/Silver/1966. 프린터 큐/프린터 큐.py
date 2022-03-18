import sys
input = sys.stdin.readline
from collections import deque, defaultdict

def solution(t: int) -> None:
    for _ in range(t):
        print(case_cost(input(), input()))


def case_cost(info: str, queue: str) -> int:
    n, my_i = map(int, info.split())
    q = list(enumerate(map(int, queue.split())))
    q = list(filter(lambda x: x[1] >= q[my_i][1], q))
    deq = deque(q)
    ans = 0

    d = defaultdict(int)

    for i, p in q:
        d[p] += 1
    
    e_l_ps = sorted(d.keys(), reverse=True)
    for p in e_l_ps[:-1]:
        while d[p]:
            if (temp := deq.popleft())[1] == p:
                d[p] -= 1
                ans += 1
            else:
                deq.append(temp)

    while True:
        if deq.popleft()[0] == my_i:
            break
        ans += 1

    return ans + 1


solution(int(input()))
