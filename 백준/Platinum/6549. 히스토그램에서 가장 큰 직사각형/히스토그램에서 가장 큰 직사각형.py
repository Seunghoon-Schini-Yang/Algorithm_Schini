import sys
input = sys.stdin.readline

def solution() -> None:
    while True:
        if (line := input())[0] == '0':
            return

        n, *nums = map(int, line.split())
        nums.append(0)
        stack = [(0, 0)]
        maxy = 0

        for i, h in enumerate(nums, start=1):
            while stack and h <= stack[-1][1]:
                if (c_h := stack.pop()[1]) == h:
                    break
                maxy = max((i - 1 - stack[-1][0]) * c_h, maxy)
            stack.append((i, h))
        
        print(maxy)
        

solution()
