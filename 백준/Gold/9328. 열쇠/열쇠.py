import sys
input = sys.stdin.readline


class John():
    def __init__(self, keys):
        self.keys = set(map(ord, keys))
        self.docs = 0


class Building():
    def __init__(self, h, w):
        self.h, self.w = h, w
        self.board = [input().rstrip() for _ in range(h)]
        self.visited = [[False] * w for _ in range(h)]


    def _adjs(self, r, c):
        if r > 0:  yield r-1, c
        if c > 0:  yield r, c-1
        if r < self.h-1:  yield r+1, c
        if c < self.w-1:  yield r, c+1


def main():
    for _ in range(int(input())):
        building = Building(*map(int, input().split()))
        john = John(input().rstrip())

        edges = [(r, 0) for r in range(building.h)] +\
            [(r, building.w-1) for r in range(building.h)] +\
            [(0, c) for c in range(1, building.w-1)] +\
            [(building.h-1, c) for c in range(1, building.w-1)]

        locked = []
        for r, c in edges:
            if building.visited[r][c] or building.board[r][c] == '*':
                continue
            building.visited[r][c] = True
            if 65 <= ord(building.board[r][c]) <= 90 and ord(building.board[r][c])+32 not in john.keys:
                locked.append((r, c))
                continue
            if building.board[r][c] == '$':
                john.docs += 1            
            elif 97 <= ord(building.board[r][c]) <= 122:
                john.keys.add(ord(building.board[r][c]))
                
            stack = [(r, c)]
            while stack:
                for r, c in building._adjs(*stack.pop()):
                    if building.visited[r][c] or building.board[r][c] == '*':
                        continue
                    building.visited[r][c] = True
                    if building.board[r][c] == '$':
                        john.docs += 1
                        stack.append((r, c))
                    elif building.board[r][c] == '.':
                        stack.append((r, c))
                    elif 97 <= ord(building.board[r][c]) <= 122:
                        john.keys.add(ord(building.board[r][c]))
                        stack.append((r, c))
                    elif ord(building.board[r][c])+32 in john.keys:
                        stack.append((r, c))
                    else:
                        locked.append((r, c))
        
        while locked:
            tmp = []
            unlocked = False
            for r, c in locked:
                if ord(building.board[r][c])+32 in john.keys:
                    unlocked = True
                    stack = [(r, c)]
                    while stack:
                        for r, c in building._adjs(*stack.pop()):
                            if building.visited[r][c] or building.board[r][c] == '*':
                                continue
                            building.visited[r][c] = True
                            if building.board[r][c] == '$':
                                john.docs += 1
                                stack.append((r, c))
                            elif building.board[r][c] == '.':
                                stack.append((r, c))
                            elif 97 <= ord(building.board[r][c]) <= 122:
                                john.keys.add(ord(building.board[r][c]))
                                stack.append((r, c))
                            elif ord(building.board[r][c])+32 in john.keys:
                                stack.append((r, c))
                            else:
                                tmp.append((r, c))
                else:
                    tmp.append((r, c))
            if not unlocked:
                break
            locked = tmp

        print(john.docs)


if __name__ == '__main__':
    main()
