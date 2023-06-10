import sys
input = sys.stdin.readline


if __name__ == '__main__':
    N = int(input())
    stack = [(0, 100_000_001)]
    rs = [0] * N
    for i, h in enumerate(map(int, input().split())):
        while stack[-1][1] < h:
            stack.pop()
        rs[i] = stack[-1][0]
        stack.append((i+1, h))
    print(*rs)
