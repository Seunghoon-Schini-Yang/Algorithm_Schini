import sys
input = sys.stdin.readline
from collections import deque, Counter


if __name__ == '__main__':
    N, d, k, c = map(int, input().split())
    _types = 0
    belt = [int(input()) for _ in range(N)]
    counter = Counter(belt[:k])
    dq = deque(belt[:k])
    
    for i in range(k, N+k):
        cur_types = len(counter)
        if c not in counter:  cur_types += 1
        _types = max(_types, cur_types)
        
        _out = dq.popleft()
        counter[_out] -= 1
        if not counter[_out]:
            counter.pop(_out)
        _in = belt[i%N]
        counter[_in] = counter.get(_in, 0) + 1
        dq.append(_in)
        
    print(_types)
