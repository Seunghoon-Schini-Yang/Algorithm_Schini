from bisect import bisect_right


if __name__ == '__main__':
    N, K = map(int, input().split())
    thres = N-K
    arr = map(lambda x: -int(x), input().rstrip())
    stack = []
    
    for i in range(N, 0, -1):
        cur = next(arr)
        cut = max(thres-i, 0)
        idx = bisect_right(stack, cur)
        idx = cut if idx < cut else idx
        if idx == len(stack):
            stack.append(cur)
        else:
            stack[idx] = cur
            del stack[idx+1:]
        
    print(''.join(map(lambda x: str(-x), stack))[:thres])
