from bisect import bisect_right


if __name__ == '__main__':
    N, K = map(int, input().split())
    thres = N-K
    arr = map(lambda x: -int(x), input().rstrip())
    stack = []
    
    for i, cur in zip(range(N, 0, -1), arr):
        idx = bisect_right(stack, cur)
        if idx < (cut := thres-i):
            idx = cut
        if idx == len(stack):
            stack.append(cur)
        else:
            stack[idx] = cur
            del stack[idx+1:]
        
    print(''.join(map(lambda x: str(-x), stack))[:thres])
