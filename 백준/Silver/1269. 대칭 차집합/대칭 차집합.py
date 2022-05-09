import sys
input = sys.stdin.readline


def sol() -> int:
    a_org = set(input().split())
    a = a_org.copy()
    b = set(input().split())
    for x in a_org:
        if x in b:
            a.remove(x)
            b.remove(x)

    return len(a) + len(b)

    
input()
print(sol())
