def solution(n: int) -> int:
    left, m_i = 0, n - 1
    q = list(range(1, n + 1))

    while left < m_i:
        if left % 2 == 1:
            q.append(q[left])
            m_i += 1
        left += 1

    return q[m_i]


print(solution(int(input())))
