import sys
input = sys.stdin.readline


def main():
    N = int(input())
    arr = list(map(int, input().split()))

    counter = {}
    stack = list()
    for n in arr:
        counter[n] = counter.get(n, 0) + 1
    for i in range(N):
        while stack and counter[arr[stack[-1]]] < counter[arr[i]]:
            arr[stack.pop()] = arr[i]
        stack.append(i)
    for n in stack:
        arr[n] = -1
    
    print(*arr)
    return 


if __name__ == '__main__':
    main()
