from collections import defaultdict


def solution(genres, plays):
    acc = defaultdict(int)
    top = defaultdict(list)
    for i, (genre, play) in enumerate(zip(genres, plays)):
        acc[genre] += play
        if not top[genre]:
            top[genre].append((play, i))
        elif len(top[genre]) == 1:
            if top[genre][0][0] < play:
                top[genre].insert(0, (play, i))
            else:
                top[genre].append((play, i))
        else:
            if play <= top[genre][1][0]:
                continue
            top[genre].pop()
            if top[genre][0][0] < play:
                top[genre].insert(0, (play, i))
            else:
                top[genre].append((play, i))

    answer = []
    for genre, _ in sorted(acc.items(), key=lambda x: -x[1]):
        for _, i in top[genre]:
            answer.append(i)
    return answer
