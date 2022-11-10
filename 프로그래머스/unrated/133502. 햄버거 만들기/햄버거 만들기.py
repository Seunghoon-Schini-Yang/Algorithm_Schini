def solution(ingredient):
    cnt = 0
    stack = ingredient[:3]
    query = [1, 2, 3, 1]

    for i in range(3, len(ingredient)):
        stack.append(ingredient[i])
        if ingredient[i] == 1 and stack[-4:] == query:
            cnt += 1
            del stack[-4:]

    return cnt
