import sys
input = sys.stdin.readline


class Waitings():
    def __init__(self, N):
        pairs = 0
        stack = []
        for _ in range(N):
            x = int(input())
            while stack and stack[-1][0] < x:
                _, acc = stack.pop()
                pairs += acc
            if stack and stack[-1][0] == x:
                pairs += stack[-1][1]
                stack[-1][1] += 1
                if len(stack) > 1:
                    pairs += 1
            else:
                if stack:
                    pairs += 1
                stack.append([x, 1])
        self.answer = pairs
        
        
if __name__ == '__main__':
    wating_line = Waitings(int(input()))
    print(wating_line.answer)
