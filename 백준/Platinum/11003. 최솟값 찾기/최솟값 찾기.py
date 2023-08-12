# pen2402 님 코드 참고
import sys
input = sys.stdin.readline
from collections import deque


class Arr():
    def __init__(self):
        self.N, self.L = map(int, input().split())
        self.arr = tuple(map(int, input().split()))
        self.dq = deque()
        self.mins = [self._get_min(i) for i in range(self.N)]
    
    
    def _get_min(self, i):
        while self.dq and self.arr[i] < self.dq[-1]:
            self.dq.pop()
        self.dq.append(self.arr[i])
        if self.L <= i and self.arr[i-self.L] == self.dq[0]:
            self.dq.popleft()
        return self.dq[0]


if __name__ == '__main__':
    arr = Arr()
    print(*arr.mins)
