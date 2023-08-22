import sys
input = sys.stdin.readline


def gcd(p, q):
    while q:
        p, q = q, p%q
    return p
    
def lcm(p, q):
    return (p // gcd(p, q)) * q

def get_gcded(p, q):
    x = gcd(p, q)
    return p//x, q//x

def get_lcmed(p, q):
    x = lcm(p, q)
    return x//p, x//q

def multi(x, v, qnt, grp):
    for xx in grp[x]:
        qnt[xx] *= v

def combine(a, b, grp):
    tmp = grp[a] + grp[b]
    for x in tmp:
        grp[x] = tmp


class Portions():
    def __init__(self, N):
        qnt = [1] * N
        grp = [[i] for i in range(N)]
        for _ in range(N-1):
            a, b, p, q = map(int, input().split())
            p, q = get_gcded(p, q)
            ma, mb = get_lcmed(qnt[a], qnt[b])
            ma, mb = get_gcded(ma*p, mb*q)
            multi(a, ma, qnt, grp)
            multi(b, mb, qnt, grp)
            combine(a, b, grp)
        self.qunatites = qnt


if __name__ == '__main__':
    portions = Portions(int(input()))
    print(*portions.qunatites)
