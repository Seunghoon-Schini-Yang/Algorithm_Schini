import sys
input = sys.stdin.readline


def main(r, c, k):
    A = [list(map(int, input().split())) for _ in range(3)]
    r -= 1; c -= 1
    cnt = 0
    while len(A) <= r or len(A[0]) <= c or A[r][c] != k:
        if r < len(A) and c < len(A[0]) and A[r][c] == k:
            return cnt
        cnt += 1
        if cnt == 101:
            return -1
        
        if len(A[0]) <= len(A):
            max_len = 0
            for i in range(len(A)):
                counter = {}
                for v in A[i]:
                    if not v:  continue
                    counter[v] = counter.get(v, 0) + 1
                row = sorted([[v, c] for v, c in counter.items()], key=lambda x: (x[1], x[0]))
                A[i] = []
                for rr in row[:50]:
                    A[i].extend(rr)
                max_len = max(max_len, len(A[i]))
            for i in range(len(A)):
                A[i].extend([0] * (max_len - len(A[i])))
        else:
            B = []
            max_len = 0
            for col in zip(*A):
                counter = {}
                for v in col:
                    if not v:  continue
                    counter[v] = counter.get(v, 0) + 1
                row = sorted([[v, c] for v, c in counter.items()], key=lambda x: (x[1], x[0]))
                B.append([])
                for rr in row[:50]:
                    B[-1].extend(rr)
                max_len = max(max_len, len(B[-1]))
            for i in range(len(A[0])):
                B[i].extend([0] * (max_len - len(B[i])))
            A = [list(row) for row in zip(*B)]

    return cnt


if __name__ == '__main__':
    cnt = main(*map(int, input().split()))
    print(cnt)
