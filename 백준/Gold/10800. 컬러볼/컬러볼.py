import sys
input = sys.stdin.readline


if __name__ == '__main__':
    N = int(input())
    stack = []
    size_by_color = [0] * 200_001
    prev = total = 0
    balls = [(*map(int, input().split()), i) for i in range(N)]
    balls.sort(key=lambda x: x[1])
    answer = [0] * N
    
    for color, size, i in balls:
        if size == prev:
            answer[i] = total - size_by_color[color]
            stack.append((color, size))
            continue
        
        for cc, ss in stack:
            total += ss
            size_by_color[cc] += ss
        
        stack = [(color, size)]
        answer[i] = total - size_by_color[color]
        prev = size
        
    print('\n'.join(map(str, answer)))
