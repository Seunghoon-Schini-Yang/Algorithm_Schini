import sys
input = sys.stdin.readline


if __name__ == '__main__':
    input()
    mod = 1_000_000_007
    memo = [0]*4
    for char in input().rstrip():
        if char == 'W':
            memo[0] += 1
        elif char == 'H':
            memo[1] += memo[0]
        elif char == 'E':
            memo[3] += sum(memo[2:])
            memo[3] %= mod
            memo[2] += memo[1]
            memo[2] %= mod
    print(memo[3])
