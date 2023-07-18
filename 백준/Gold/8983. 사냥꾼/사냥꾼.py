import sys
input = sys.stdin.readline


class Hunter():
    def __init__(self):
        M, N, L = map(int, input().split())
        shots = sorted(map(int, input().split()))
        preys = sorted(tuple(map(int, input().split())) for _ in range(N))
        shots_step = [(shots[i] + shots[i-1])>>1 for i in range(1, M)] + [sys.maxsize]
        self.cnt = self._count_hunt(M, N, L, shots, preys, shots_step)
    
    
    def _count_hunt(self, M, N, L, shots, preys, shots_step):
        cnt = pi = 0
        for si in range(M):
            while pi < N and preys[pi][0] <= shots_step[si]:
                if abs(shots[si] - preys[pi][0]) + preys[pi][1] <= L:
                    cnt += 1
                pi += 1
            if pi == N:
                return cnt
        

if __name__ == '__main__':
    hunter = Hunter()
    print(hunter.cnt)
