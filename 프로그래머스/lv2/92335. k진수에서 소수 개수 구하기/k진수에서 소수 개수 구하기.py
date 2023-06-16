def is_prime(x):
    if x == 2:
        return True
    if not x&1 or x == 1:
        return False
    for i in range(3, int(pow(x, 0.5))+1, 2):
        if not x%i:
            return False
    return True


def solution(n, k):
    kn = []
    while n:
        n, r = divmod(n, k)
        kn.append(r)
    cands = [int(i) for i in ''.join(map(str, kn[::-1])).split('0') if i]
    print(cands)
    if len(cands) == 1:
        return 1 if is_prime(cands[0]) else 0
    return sum(is_prime(cand) for cand in cands)
    