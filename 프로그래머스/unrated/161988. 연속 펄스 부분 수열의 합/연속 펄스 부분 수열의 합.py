def solution(sequence):
    sequence = [sequence[i] if i&1 else -sequence[i] for i in range(len(sequence))]
    miny = maxy = max_acc = min_acc = 0
    for i in sequence:
        max_acc += i
        maxy = max(maxy, max_acc)
        if max_acc < 0:
            max_acc = 0
        min_acc += i
        miny = min(miny, min_acc)
        if min_acc > 0:
            min_acc = 0
    return max(maxy, -miny)