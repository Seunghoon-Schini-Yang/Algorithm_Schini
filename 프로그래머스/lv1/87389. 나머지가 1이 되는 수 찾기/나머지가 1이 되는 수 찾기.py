def solution(n):
    if n&1:
        return 2
    
    n -= 1
    for i in range(3, int(pow(n, 0.5))+1, 2):
        if not n % i:
            return i
    return n
    
    
    
    
    
    return answer
