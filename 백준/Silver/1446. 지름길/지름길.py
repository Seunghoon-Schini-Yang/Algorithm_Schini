import sys
input = sys.stdin.readline


def main():
    N, D = map(int, input().split())
    memo = [i for i in range(D+1)]
    roads = []
    for _ in range(N):
        s, e, dist = map(int, input().split())
        if e-s <= dist or D < e:
            continue
        roads.append((s, e, dist))
    roads.sort()
    
    for s, e, dist in roads:
        val = memo[s] + dist
        for i in range(e, D+1):
            if memo[i] <= val:
                break
            memo[i] = val
            val += 1
    print(memo[D])


if __name__ == '__main__':
    main()
