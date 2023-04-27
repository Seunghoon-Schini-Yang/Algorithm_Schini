if __name__ == '__main__':
    N = int(input())
    fac = 1
    for i in range(2, N+1):
        fac *= i
    _type, *arr = map(int, input().split())
    cands = [i for i in range(1, N+1)]
    
    if _type == 1:
        k = arr[0] - 1
        seq = []
        for i in range(N, 0, -1):
            fac //= i
            div, k = divmod(k, fac)
            seq.append(cands.pop(div))
        print(*seq)
    else:
        k = 0
        for arr_i, i in enumerate(range(N, 0, -1)):
            fac //= i
            x = arr[arr_i]
            for j in range(len(cands)):
                if cands[j] == x:
                    break
            cands.pop(j)
            k += fac * j
        print(k + 1)
