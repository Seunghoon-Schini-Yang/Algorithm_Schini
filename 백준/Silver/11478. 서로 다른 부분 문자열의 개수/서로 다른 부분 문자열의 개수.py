def sol(s: str) -> int:
    substr = set()
    s_len = len(s)
    for gap in range(1, s_len+1):
        for i in range(s_len+1-gap):
            substr.add(s[i:i+gap])

    return len(substr)


print(sol(input()))
