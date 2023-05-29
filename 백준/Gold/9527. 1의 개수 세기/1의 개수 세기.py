def get_cases(n):
    ds = list(map(int, bin(n)[2:]))[::-1]
    cases = acc = sum(ds)
    acc -= 1
    for i in range(len(ds)):
        if not ds[i]:
            continue
        cases += int(i*pow(2, i-1)) + acc*pow(2, i)
        acc -= 1
    return cases


if __name__ == '__main__':
    A, B = map(int, input().split())
    print(get_cases(B) - get_cases(A-1))
