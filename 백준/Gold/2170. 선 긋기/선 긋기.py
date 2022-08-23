import sys
input = sys.stdin.readline


if __name__ == '__main__':
    lines = [tuple(map(int, input().split())) for _ in range(int(input()))]
    lines.sort()

    start, end = lines[0]
    dist = end - start
    for x, y in lines[1:]:
        if x >= end:
            start = x; end = y
            dist += end - start
        elif y >= end:
            dist += y - end
            end = y
    print(dist)
