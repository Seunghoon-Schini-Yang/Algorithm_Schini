import sys
input = sys.stdin.readline


def sol() -> int:
    a_org = set(input().split())
    a = a_org.copy()
    b = set(input().split())
    a_rm = a.remove; b_rm = b.remove
    for x in a_org:
        if x in b:
            a_rm(x); b_rm(x)

    return len(a) + len(b)

    
input()
print(sol())
