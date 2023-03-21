import sys
input = sys.stdin.readline


def main():
    N, M = map(int, input().split())
    baskets = [0] * (N+1)
    for _ in range(M):
        s, e, v = map(int, input().split())
        baskets[s:e+1] = [v] * (e+1-s)
    print(*baskets[1:])
    
    
if __name__ == '__main__':
    main()