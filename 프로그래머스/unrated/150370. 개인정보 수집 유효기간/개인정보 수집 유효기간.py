def solution(today, terms, privacies):
    Y, M, D = map(int, today.split('.'))

    terms = [info.split() for info in terms]
    terms = {key:int(val) for key, val in terms}

    answer = list()
    for i in range(len(privacies)):
        y, m, d = map(int, privacies[i][:-2].split('.'))
        m_add = terms[privacies[i][-1]]

        m += m_add - 1
        y += m // 12
        m %= 12; m += 1

        if Y > y:
            answer.append(i+1)
            continue
        elif Y < y:
            continue

        if M > m:
            answer.append(i+1)
            continue
        elif M < m:
            continue

        if D >= d:
            answer.append(i+1)
            continue

    return answer
