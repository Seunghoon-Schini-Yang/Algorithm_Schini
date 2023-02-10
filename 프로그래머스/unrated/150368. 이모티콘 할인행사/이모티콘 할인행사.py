def solution(users, emoticons):
    answer = [0, 0]
    users.sort(key=lambda x: x[0])
    memo = [0] * len(users)
    backtrack(0, users, emoticons, memo, answer)
    return answer


def backtrack(e_i, users, emojis, memo, answer):
    if e_i == len(emojis):
        cand = [0, 0]
        for (_, ulimit), upay in zip(users, memo):
            if upay >= ulimit:
                cand[0] += 1
            else:
                cand[1] += upay
        if cand[0] > answer[0]:
            answer[:] = cand
        elif cand[0] == answer[0] and cand[1] > answer[1]:
            answer[1] = cand[1]
    
    else:
        for dcr in range(10, 50, 10):  # discount rate
            for u_i in range(len(users)):
                if dcr >= users[u_i][0]:
                    memo[u_i] += emojis[e_i]//100 * (100-dcr)
                else:
                    break

            backtrack(e_i+1, users, emojis, memo, answer)

            for u_i in range(len(users)):
                if dcr >= users[u_i][0]:
                    memo[u_i] -= emojis[e_i]//100 * (100-dcr)
                else:
                    break
