import string


def solution(name):
    char_idx_dict = {char:min(26-idx, idx) for idx, char in enumerate(string.ascii_uppercase)}
    cnt = sum(char_idx_dict[char] for char in name)
    n = len(name)
    required = [i for i in range(1, n) if name[i] != 'A']
    if not required:
        pass
    elif len(required) == 1:
        cnt += min(required[0], n-required[0])
    else:
        cnt += min(
            min(min(required[i-1]*2 + n-required[i], (n-required[i])*2 + required[i-1]) for i in range(1, len(required))),
            required[-1],
            n-required[0]
        )
    return cnt
