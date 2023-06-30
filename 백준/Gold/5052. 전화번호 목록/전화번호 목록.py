import sys
input = sys.stdin.readline


def is_consistent(n):
    nums = sorted(input().rstrip() for _ in range(n))
    memo = {}
    for num in nums:
        cur = memo
        for d in num:
            if '-1' in cur:
                return 'NO'
            cur[d] = cur.get(d, {})
            cur = cur[d]
        cur['-1'] = {}
    return 'YES'


if __name__ == '__main__':
    print('\n'.join(is_consistent(int(input())) for _ in range(int(input()))))
