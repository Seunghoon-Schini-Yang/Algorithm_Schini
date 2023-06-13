maxy = 0
answer = ([], 0)


def solution(n, info):
    def dfs(res, sc, idx):
        global maxy, answer
        if not res:
            if maxy < sc-peach:
                maxy = sc-peach
                answer = (stack[:], res)
            elif maxy == sc-peach and peach < sc:
                if answer[1] == res:
                    if answer[0][-1] < stack[-1]:
                        answer = (stack[:], res)
                elif answer[1] < res:
                    answer = (stack[:], res) 
            return
        for i in range(idx, 11):
            if res < info[i]:
                if maxy < sc-peach:
                    maxy = sc-peach
                    answer = (stack[:], res)
                elif maxy == sc-peach and peach < sc:
                    if answer[1] == res:
                        if answer[0][-1] < stack[-1]:
                            answer = (stack[:], res)
                    elif answer[1] < res:
                        answer = (stack[:], res) 
                continue
            stack.append(i)
            dfs(res-info[i], sc+scores[i], i+1)
            stack.pop()
        return

    
    peach = sum(10-i if info[i] else 0 for i in range(11))
    scores = [(10-i)*2 if info[i] else 10-i for i in range(11)]
    info = [info[i]+1 for i in range(11)]
    stack = []
    dfs(n, 0, 0)
    
    if not answer[0]:
        return [-1]
    result = [0] * 11
    for i in answer[0]:
        result[i] = info[i]
    result[-1] = n - sum(result)
    return result
