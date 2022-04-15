n = int(input())

def solution(n: int) -> int:
    if n == 1:
        return 0
    
    dp = {0: 0, 1: 0}
    dp_queue = {n}
    stack = [n]

    while stack:
        operand = stack.pop()
        dp_queue.add(operand)
        a, b = operand // 3, operand // 2
        if a > 1:
            dp_queue.add(a)
            stack.append(a)
        if b > 1:
            dp_queue.add(b)
            stack.append(b)

    for i in sorted(dp_queue):
        dp[i] = 1 + min(dp[i // 2] + i % 2, dp[i // 3] + i % 3)

    return dp[n]

print(solution(n))