# kmp
import sys
input = sys.stdin.readline
print = sys.stdout.write


def sol() -> None:
    while True:
        s = input().rstrip()
        if s == '.':
            return
        s_len = len(s)
        
        quot,rem = divmod(s_len, s_len - lps(s, s_len))
        print(f'{1 if rem else quot}\n')


def lps(s: str, s_len: int) -> int:
    s_len = len(s)
    lps = [0] * s_len

    j = 0; i = 1
    while i < s_len:
        if s[j] == s[i]:
            i += 1; j += 1
        else:
            if not j:
                i += 1
            else:
                lps[i-1] = j
                j = lps[j-1]
    
    return j


sol()
