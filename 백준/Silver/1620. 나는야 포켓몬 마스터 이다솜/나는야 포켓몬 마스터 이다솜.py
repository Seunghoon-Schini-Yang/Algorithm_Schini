import sys
input = sys.stdin.readlines


def sol() -> str:
    I = input()
    n,m = map(int, I[0].split())
    dogam = {key.rstrip():str(val) for val,key in enumerate(I[1:n+1], start=1)}
    rev_dogam = [''] + list(dogam.keys())
    return '\n'.join(rev_dogam[int(q)] if q.rstrip().isnumeric() else dogam[q.rstrip()] for q in I[n+1:])


print(sol())
