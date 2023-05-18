import sys
input = sys.stdin.readline


def get_post(ps, pe, os, oe):
    if ps > pe:  return []
    if ps == pe:  return [pre[ps]]
    idx = ino[pre[ps]]
    return get_post(ps+1, ps+idx-os, os, idx-1) + get_post(ps+1+idx-os, pe, idx+1, oe) + [pre[ps]]


if __name__ == '__main__':
    for _ in range(int(input())):
        n = int(input())
        pre = input().split()
        ino = {v: i for i, v in enumerate(input().split())}
        print(' '.join(get_post(0, n-1, 0, n-1)))
