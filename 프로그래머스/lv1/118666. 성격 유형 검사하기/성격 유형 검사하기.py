def solution(survey, choices):
    pty = ["R", "T", "C", "F", "J", "M", "A", "N"]
    score_acc = {char: 0 for char in pty}
    for case, score in zip(survey, map(lambda x: x-4, choices)):
        if score >= 0:
            score_acc[case[1]] += score
        else:
            score_acc[case[0]] -= score

    return ''.join(pty[i] if score_acc[pty[i]] >= score_acc[pty[i+1]] else pty[i+1] for i in range(0, 8, 2))
    