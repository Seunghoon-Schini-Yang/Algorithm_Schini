def solution(babbling):
    words = ['aya', 'ye', 'woo', 'ma']
    idx = {'a': 0, 'y': 1, 'w': 2, 'm': 3}
    cnt = 0

    for bab in babbling:
        token = w_idx = -1
        c_idx = 0
        is_cnt = True

        for char in bab:
            if w_idx == -1:
                w_idx = idx.get(char, -1)
                if w_idx == -1:
                    is_cnt = False
                    break
                c_idx += 1

            else:
                if char == words[w_idx][c_idx]:
                    c_idx += 1

                    if c_idx == 2:
                        if w_idx in (1, 3):
                            if w_idx == token:
                                is_cnt = False
                                break
                            token = w_idx
                            w_idx = -1
                            c_idx = 0

                    else:
                        if w_idx == token:
                            is_cnt = False
                            break
                        token = w_idx
                        w_idx = -1
                        c_idx = 0
        
        if c_idx in (1, 2):
            is_cnt = False

        if is_cnt:
            cnt += 1

    return cnt
