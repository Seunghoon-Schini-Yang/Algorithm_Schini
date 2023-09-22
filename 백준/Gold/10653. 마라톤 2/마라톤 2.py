import sys
input = sys.stdin.readline


class Marathon():
    def __init__(self, N, K):
        self.points = [tuple(map(int, input().split())) for _ in range(N)]
        table = [[sys.maxsize] * (K+1) for _ in range(N)]
        table[0][0] = 0
        for cur in range(1, N):
            for k in range(min(cur, K+1)):
                table[cur][k] = min(table[cur-kk-1][k-kk] + self._get_dist(cur-kk-1, cur) for kk in range(k+1))
        self.miny = min(table[-1])


    def _get_dist(self, i, j):
        return abs(self.points[i][0] - self.points[j][0]) + abs(self.points[i][1] - self.points[j][1])


if __name__ == '__main__':
    course = Marathon(*map(int, input().split()))
    print(course.miny)
