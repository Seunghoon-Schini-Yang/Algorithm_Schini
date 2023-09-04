import sys
input = sys.stdin.readline


class Repair():
    def __init__(self, N):
        arr = [(i, *map(int, input().split())) for i in range(1, N+1)]
        arr.sort(key=lambda x: (-x[2]/x[1], x[0]))
        self.odr = [seq[0] for seq in arr]


if __name__ == '__main__':
    repairs = Repair(int(input()))
    print(*repairs.odr)
