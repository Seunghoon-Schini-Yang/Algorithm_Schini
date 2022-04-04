import sys
from collections import deque

def sol(n: int, k: int) -> int:
    visited = set()
    q = deque([n])
    cnt = flag = 0
    larger_min = sys.maxsize

    while q:
        larger_min -= 1
        for _ in range(len(q)):
            from_q = q.popleft()
            if from_q > k:
                if larger_min > from_q:
                    larger_min = from_q
                m_o = larger_min-1
                if m_o not in visited:
                    visited.add(m_o)
                    q.append(m_o)
            elif from_q == k:
                flag = 1
                break
            else:
                for x in from_q-1, from_q+1, from_q*2:
                    if x not in visited:
                        q.append(x)
                        visited.add(x)
        
        if flag:
            break
        cnt += 1

    return cnt


print(sol(*map(int, input().split())))
