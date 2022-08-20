def solution(key, lock):
    def rotate():
        rotated = [[0]*n for _ in range(m)]
        for r in range(m):
            for c in range(m):
                rotated[r][c] = key[~c][r]
        return rotated
    
    
    def is_compatible(r, c):
        for rr in range(m):
            for cc in range(m):
                new_lock[r+rr][c+cc] += key[rr][cc]
        
        if [new_lock[r][m-1:m-1+n] for r in range(m-1, m-1+n)] == dstn:
            return True
    
        for rr in range(m):
            for cc in range(m):
                new_lock[r+rr][c+cc] -= key[rr][cc]
            
        return False
    
    
    n, m = len(lock), len(key)
    new_lock = [[0]*(n+2*m-2) for _ in range(m-1)]
    for i in range(n):
        new_lock.append([0]*(m-1) + lock[i] + [0]*(m-1))
    new_lock.extend([[0]*(n+2*m-2) for _ in range(m-1)])
    
    dstn = [[1]*n for _ in range(n)]
    for _ in range(4):
        key = rotate()
        for r in range(n+m-1):
            for c in range(n+m-1):
                if is_compatible(r, c):
                    return True
    
    return False