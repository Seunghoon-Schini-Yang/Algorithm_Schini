# https://velog.io/@ashooozzz/Python-%ED%8C%8C%EC%9D%B4%EC%8D%AC-KMP-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-%EA%B5%AC%ED%98%84BOJ-1786.-%EC%B0%BE%EA%B8%B0 참고
import sys
input = sys.stdin.readline


if __name__ == '__main__':
    t = input().rstrip()
    p = input().rstrip()

    lt, lp = len(t), len(p)
    lps = [0] * lp
    length = 0
    i = 1
    while i < len(p):
        if p[length] == p[i]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length == 0:
                lps[i] = 0
                i += 1
            else:
                length = lps[length - 1]
    
    i, j = 0, 0
    idxs = []
    while i < lt:
        if t[i] == p[j]:
            i += 1
            j += 1
            if j == lp:
                idxs.append(i-lp+1)
                j = lps[j-1]
        else:
            if j != 0:
                j = lps[j-1]
            else:
                i += 1

    print(len(idxs))
    print(*idxs)
