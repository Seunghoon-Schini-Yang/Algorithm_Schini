from bisect import bisect_left


if __name__ == '__main__':
    N = int(input())
    stack = []
    for a in map(int, input().split()):
        idx = bisect_left(stack, a)
        if idx == len(stack):
            stack.append(a)
        else:
            stack[idx] = a
    print(len(stack))
