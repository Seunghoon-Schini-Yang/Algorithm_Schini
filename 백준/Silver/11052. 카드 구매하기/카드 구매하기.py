def main():
    N = int(input())
    ps = list(map(int, input().split()))
    for i in range(1, N):
        ps[i] = max(ps[i], max(ps[j] + ps[i-j-1] for j in range((i+1)>>1)))
    return ps[-1]


if __name__ == '__main__':
    answer = main()
    print(answer)
    