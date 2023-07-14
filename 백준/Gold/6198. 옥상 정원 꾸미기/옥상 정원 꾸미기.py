import sys
input = sys.stdin.readline


class Cows():
    def __init__(self):
        self._stack(int(input())-1)
        
    
    def _stack(self, N):
        stack = [int(input())]
        cnt = idx = 0
        for _ in range(N):
            cur = int(input())
            idx += 1
            while stack and stack[-1] <= cur:
                idx -= 1
                stack.pop()
            cnt += idx
            stack.append(cur)
        self.answer = cnt

        
if __name__ == '__main__':
    cow_hairs = Cows()
    print(cow_hairs.answer)
