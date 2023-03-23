import sys
input = sys.stdin.readline
from bisect import bisect_left


def main():
    N = int(input())
    answer = []
    cords = [0] * 501
    for _ in range(N):
        s, e = map(int, input().split())
        cords[e] = s
    for cord in cords:
        if not cord:
            continue
        idx = bisect_left(answer, cord)
        if idx == len(answer):
            answer.append(cord)
        else:
            answer[idx] = cord
    print(N - len(answer))


if __name__ == '__main__':
    main()
