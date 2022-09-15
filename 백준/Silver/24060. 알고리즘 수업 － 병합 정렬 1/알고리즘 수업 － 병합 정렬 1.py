def is_k(i: int) -> None:
    global odr

    odr += 1
    if odr == K:
        print(s_arr[i])
        exit()
    return


def merge_sort(l: int, r: int) -> None:
    if l == r:
        return
    
    m = (l+r)//2 + 1
    merge_sort(l, m-1); merge_sort(m, r)

    i = li = l; ri = m
    while li < m and ri < r+1:
        if arr[li] < arr[ri]:
            s_arr[i] = arr[li]
            li += 1
        else:
            s_arr[i] = arr[ri]
            ri += 1
        
        is_k(i)
        i += 1


    while li < m:
        s_arr[i] = arr[li]
        is_k(i)
        i += 1; li += 1
    while ri < r+1:
        s_arr[i] = arr[ri]
        is_k(i)
        i += 1; ri += 1

    arr[l:r+1] = s_arr[l:r+1]
    return


if __name__ == '__main__':
    N, K = map(int, input().split())
    arr = list(map(int, input().split()))
    s_arr = [0]*N
    odr = 0
    merge_sort(0, N-1)
    print(-1)
