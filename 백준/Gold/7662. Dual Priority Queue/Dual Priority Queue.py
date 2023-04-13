import sys
input = sys.stdin.readline
from heapq import heappop, heappush
from collections import defaultdict


def main(n: int) -> str:
    cnts = defaultdict(int)
    maxq = []
    minq = []

    for _ in range(n):
        cmd, val = input().split()
        val = int(val)
        if cmd == 'I':
            heappush(maxq, -val)
            heappush(minq, val)
            cnts[val] += 1
        elif val == 1:
            while maxq:
                val = -heappop(maxq)
                if cnts[val]:
                    cnts[val] -= 1
                    break
        else:
            while minq:
                val = heappop(minq)
                if cnts[val]:
                    cnts[val] -= 1
                    break
    
    answer = ''
    chk = False
    while maxq:
        val = -heappop(maxq)
        if cnts[val]:
            chk = True
            break
    if not chk:
        return 'EMPTY'
    answer += f'{val} '
    chk = False
    while minq:
        val = heappop(minq)
        if cnts[val]:
            chk = True
            break
    if not chk:
        return 'EMPTY'
    answer += f'{val}'
    return answer


if __name__ == '__main__':
    print('\n'.join(main(int(input())) for _ in range(int(input()))))
