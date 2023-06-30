import sys
input = sys.stdin.readline


def is_consistent(n):
    memo = {}
    nums = [input().rstrip() for _ in range(n)]
    for num in nums:
        res = False
        cur = memo
        for d in num:
            if '-1' in cur:
                return 'NO'
            if d not in cur:
                res = True
                cur[d] = {}
            cur = cur[d]
        if not res:
            return 'NO'
        cur['-1'] = {}
    return 'YES'


if __name__ == '__main__':
    print('\n'.join(is_consistent(int(input())) for _ in range(int(input()))))
