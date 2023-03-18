def main():
    cands = input().rstrip()
    pwd = input().rstrip()
    div = 900_528
    sqr = 1
    cnt = 0

    x = len(cands)
    n = len(pwd)

    cands = {char: i for i, char in enumerate(cands, start=1)}
    for i in range(n):
        sqr %= div
        cnt += cands[pwd[~i]] * sqr
        cnt %= div
        sqr *= x
    
    print(cnt)


if __name__ == '__main__':
    main()
