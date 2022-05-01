# eric9709 님 코드 참고
# recursive + binary search
import sys
input = sys.stdin.readlines
sys.setrecursionlimit(pow(10,9))

def sol(lines: str) -> list:
    def get_post(s: int, e: int) -> None:
        if s > e:
            return
        
        root = preodr[s]
        if s == e:
            postodr.append(root)
            return

        if root < preodr[s+1] or root > preodr[e]:
            get_post(s+1, e)
            postodr.append(root)
            return

        s += 1
        c_s = s; c_e = e
        while c_s+1 < c_e:
            m = (c_s+c_e)//2
            if preodr[m] > root:
                c_e = m
            else:
                c_s = m
            
        get_post(s, c_s)
        get_post(c_e, e)
        postodr.append(root)


    postodr = []
    preodr = list(map(int, lines))
    get_post(0, len(preodr)-1)
    return postodr


print(*sol(input()))
