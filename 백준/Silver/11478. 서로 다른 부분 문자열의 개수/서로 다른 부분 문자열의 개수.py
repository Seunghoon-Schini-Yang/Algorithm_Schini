# naracar12 님 코드 참고
def sol(s: str) -> int:
    s_len = len(s)
    return sum(len({s[i:i+gap] for i in range(s_len+1-gap)}) for gap in range(1, s_len+1))


print(sol(input()))
