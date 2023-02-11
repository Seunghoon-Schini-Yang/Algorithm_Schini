from itertools import accumulate
from collections import defaultdict


def solution(info, query):
    scores = defaultdict(lambda: [0 for _ in range(100_001)])
    mapping = {
        0: ('cpp', 'java', 'python'),
        1: ('backend', 'frontend'),
        2: ('junior', 'senior'),
        3: ('chicken', 'pizza')
    }

    for nfo in info:
        key, score = nfo.rsplit(" ", 1)
        scores[key][int(score)] += 1

    for _, score_list in scores.items():
        score_list[:] = list(accumulate(score_list))
    
    answer = [0] * len(query)

    for q_i, quer in enumerate(query):
        cands = [""]
        *cracked, score = quer.split(" ")
        for i in range(4):
            tmp = []
            for cand in cands:
                if cracked[i<<1] == "-":
                    for cat in mapping[i]:
                        tmp.append(cand + ' ' + cat)
                else:
                    tmp.append(cand + ' ' + cracked[i<<1])
            cands = tmp

        score = int(score)
        for cand in cands:
            answer[q_i] += scores[cand.lstrip()][-1] - scores[cand.lstrip()][score-1]

    return answer
