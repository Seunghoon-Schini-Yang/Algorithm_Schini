import sys
input = sys.stdin.readline


def main():
    n, m = map(int, input().split())
    memo = {int(input()): 0}
    names = [int(input()) for _ in range(n-1)]
    for name in names:
        tmp = {name: min(sqr + ((m - loc) ** 2) for loc, sqr in memo.items())}
        for loc, sqr in memo.items():
            new_loc = loc + 1 + name
            if new_loc > m:
                continue
            tmp[new_loc] = min(tmp.get(new_loc, sqr), sqr)
        memo = tmp
    print(min(memo.values()))

        
if __name__ == '__main__':
    main()
