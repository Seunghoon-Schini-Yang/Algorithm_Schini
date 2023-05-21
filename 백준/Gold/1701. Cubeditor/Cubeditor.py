import sys
input = sys.stdin.readline


def find_matching(x, y):
    maxy = memo = 0
    for i, j in zip(x, y):
        if i == j:
            memo += 1
        else:
            maxy = max(maxy, memo)
            memo = 0
    return max(maxy, memo)


if __name__ == '__main__':
    given = input().rstrip()
    print(max(find_matching(given[i:], given[:-i]) for i in range(1, len(given)-1)))
