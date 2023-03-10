def solution(n, m, x, y, r, c, k):
    dist = abs(x-r) + abs(y-c)
    if k < dist or (k & 1) ^ (dist & 1):
        return 'impossible'
    
    answer = ''
    alpha = (k - dist) >> 1

    if x <= r:
        answer += 'd' * (r-x)
        x = r

    if alpha:
        extra = alpha if alpha <= (n-x) else n-x
        answer += 'd' * extra
        x += extra
        alpha -= extra

    if c <= y:
        answer += 'l' * (y-c)
        y = c

    if alpha:
        extra = alpha if alpha <= y-1 else y-1
        answer += 'l' * extra
        y -= extra
        alpha -= extra

    if alpha:
        answer += 'rl' * alpha

    answer += 'r' * (c-y)
    answer += 'u' * (x-r)
    return answer
