import sys
input = sys.stdin.readline


class Highway():
    def __init__(self, N, K):
        self.N, self.K = N, K
        self.sensors = sorted(map(int, input().split()))


def main():
    highway = Highway(int(input()), int(input()))
    intervals = [highway.sensors[i] - highway.sensors[i-1] for i in range(1, highway.N)]
    intervals.sort(reverse=True)
    print(sum(intervals[highway.K-1:]))


if __name__ == '__main__':
    main()
