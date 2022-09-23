from collections import defaultdict


def solution(str1: str, str2: str) -> int:
    def get_fisrt_alpha_idx(string: str) -> int:
        for i in range(len(string)):
            if string[i].isalpha():
                break

        if i == len(string)-1:
            return -1
        return i

    
    def get_two_char_dict(str_dict: defaultdict, string: str, i: int, j: int) -> None:
        if i == -1:
            return
        
        while j < len(string):
            if not string[j].isalpha():
                while j < len(string) and not string[j].isalpha():
                    j += 1
                i = j; j += 1
            else:
                str_dict[string[i:i+2].lower()] += 1
                i = j; j += 1


    str1_dict = defaultdict(int); str2_dict = defaultdict(int)

    i = get_fisrt_alpha_idx(str1)
    get_two_char_dict(str1_dict, str1, i, i+1)
    
    i = get_fisrt_alpha_idx(str2)
    get_two_char_dict(str2_dict, str2, i, i+1)
    
    if not str1_dict and not str2_dict:
        answer = 1
    elif not str1_dict or not str2_dict:
        answer = 0
    else:
        intersect = union = 0
        for word, cnt in str1_dict.items():
            if word in str2_dict:
                intersect += min(cnt, str2_dict[word])
                union += max(cnt, str2_dict[word])
            else:
                union += cnt
        union += sum(cnt for word, cnt in str2_dict.items() if word not in str1_dict)
        answer = intersect / union

    return int(answer * 65536)
