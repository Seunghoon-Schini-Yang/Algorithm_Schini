def solution(a):
    cnt = [0]*len(a)
    last = [-1, a[0]]
    loc = [0, 0]
    
    for i in a[1:]:
        tmp_last = last[1]; tmp_loc = loc[1]
        if loc[1]:
            if i == last[1]:
                loc[1] = 0
            elif i == last[0]:
                if loc[0]:
                    loc[1] = 1
                    cnt[i] += 1
                else:
                    loc[1] = 0
            else:
                loc[1] = 1
                cnt[i] += 1
        else:
            if i == last[1]:
                loc[1] = 0
            else:
                loc[1] = 1
                cnt[i] += 1; cnt[last[1]] += 1
                
        last[1] = i
        last[0], loc[0] = tmp_last, tmp_loc
                
    return max(cnt)*2