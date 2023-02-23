def solution(q1: list, q2: list) -> int:
    def get_count(i: int, j: int) -> int:
        if i >= h_n:
            i -= h_n; j -= h_n
        return i+j-h_n if j >= h_n else i+j+h_n
        
        
    q = q1 + q2
    n = len(q); h_n = n >> 1
    elem_sum = sum(q)

    if elem_sum & 1:
        return -1
    elem_sum >>= 1
    
    # two pointer
    i = 0; j = 1
    cur_sum = q[0]
    cnt = 900000
    while True:
        if cur_sum < elem_sum:
            if j == n:
                break
            cur_sum += q[j]
            j += 1
        elif cur_sum > elem_sum:
            if i == j:
                break          
            cur_sum -= q[i]
            i += 1
        else:
            # count
            cnt = min(cnt, get_count(i, j))
            if j == n:
                break
            cur_sum -= q[i]; cur_sum += q[j]
            i += 1; j += 1
    
    return -1 if cnt == 900000 else cnt
