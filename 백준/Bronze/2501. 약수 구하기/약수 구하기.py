def main():
    N, K = map(int, input().split())
    a, b = [1], [N]
    for i in range(2, int(pow(N, 0.5))+1):
        if not N % i:
            a.append(i)
            b.append(N//i)
    if a[-1] == b[-1]:
        a.pop()
    a += b[::-1]
    if len(a) < K:
        return 0
    return a[K-1]


if __name__ == '__main__':
    kth = main()
    print(kth)
