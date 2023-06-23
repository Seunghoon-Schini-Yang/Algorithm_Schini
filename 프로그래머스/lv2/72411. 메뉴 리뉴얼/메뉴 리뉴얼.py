from itertools import combinations


def solution(orders, course):
    orders = [''.join(sorted(order)) for order in orders]
    answer = []
    for c in course:
        counter = {}
        for order in orders:
            for seq in combinations(order, c):
                counter[seq] = counter.get(seq, 0) + 1
        maxy = max(counter.values()) if counter else 0
        if maxy < 2:
            continue
        for seq in counter:
            if counter[seq] == maxy:
                answer.append(''.join(seq))
    return sorted(answer)