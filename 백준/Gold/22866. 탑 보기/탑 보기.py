import sys
input = sys.stdin.readline

        
def main():
    N = int(input())
    heights = [0] + list(map(int, input().split()))
    cnt = [0] * (N+1)
    nearest = [0] * (N+1)
    
    stack = [N]
    for i in range(N-1, 0, -1):
        while stack and heights[i] >= heights[stack[-1]]:
            stack.pop()
        cnt[i] += len(stack)
        if stack:
            nearest[i] = stack[-1]
        stack.append(i)
    
    stack = [1]
    for i in range(2, N+1):
        while stack and heights[i] >= heights[stack[-1]]:
            stack.pop()
        cnt[i] += len(stack)
        if stack and (not nearest[i] or nearest[i] - i >= i - stack[-1]):
            nearest[i] = stack[-1]
        stack.append(i)

    for i in range(1, N+1):
        if cnt[i]:
            print(cnt[i], nearest[i])
        else:
            print(cnt[i])


if __name__ == '__main__':
    main()
