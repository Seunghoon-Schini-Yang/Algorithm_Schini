import sys
input = sys.stdin.readline


class Goldbach():
    def __init__(self, T):
        Ns = [int(input()) for _ in range(T)]
        maxy = max(Ns)
        cands = [i for i in range(3, maxy, 2)]
        primes = [2]
        limit = int(pow(maxy, 0.5))
        while cands[0] <= limit:
            primes.append(cands[0])
            cands = [cand for cand in cands if cand % cands[0]]
        primes += cands
        prime_set = set(primes)
        for i in range(T):
            limit = Ns[i]>>1
            cnt = j = 0
            while primes[j] <= limit:
                if Ns[i] - primes[j] in prime_set:
                    cnt += 1
                j += 1
            Ns[i] = cnt
        self.answer = Ns
            
    
if __name__ == '__main__':
    bach = Goldbach(int(input()))
    print('\n'.join(map(str, bach.answer)))
