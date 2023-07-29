import sys
input = sys.stdin.readline


if __name__ == '__main__':
    n = int(input())
    cnt = 0
    for _ in range(n):
        char = input().rstrip()
        if char == 'ENTER':
            memo = set()
        elif char not in memo:
            cnt += 1
            memo.add(char)
    print(cnt)