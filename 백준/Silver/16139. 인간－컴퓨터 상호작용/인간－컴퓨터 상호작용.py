import sys
input = sys.stdin.readline
print = sys.stdout.write


def sol(string: str, q: int) -> None:
    n = len(string)
    prefix_sum = [0] * (n+1)
    prefix_sum[0] = dict()

    for i in range(n):
        prefix_sum[i+1] = prefix_sum[i].copy()
        prefix_sum[i+1][string[i]] = prefix_sum[i+1].get(string[i], 0) + 1

    for _ in range(q):
        query = input().split()
        print(f'{prefix_sum[int(query[2])+1].get(query[0], 0) - prefix_sum[int(query[1])].get(query[0], 0)}\n')
    return


sol(input().rstrip(), int(input()))
