import sys
input = sys.stdin.readline


def cal_score() -> int:
    score = i = 0
    for inning in innings:
        out_cnt = one = two = three = 0
        while out_cnt != 3:
            hit = inning[lineup[i%9]]
            if not hit:
                out_cnt += 1
            elif hit == 1:
                score += three
                three, two, one = two, one, 1
            elif hit == 2:
                score += two+three
                three, two, one = one, 1, 0
            elif hit == 3:
                score += one+two+three
                three, two, one = 1, 0, 0
            else:
                score += one+two+three+1
                three = two = one = 0
            i += 1
    return score


def backtrack(player: int) -> None:
    global max_score
    if player == 9:
        max_score = max(cal_score(), max_score)
        return

    for i in range(9):
        if lineup[i] != 9:
            continue
        
        lineup[i] = player
        backtrack(player+1)
        lineup[i] = 9
    return


if __name__ == '__main__':
    max_score = 0
    lineup = [9]*9
    lineup[3] = 0
    innings = [list(map(int, input().split())) for _ in range(int(input()))]

    backtrack(1)
    print(max_score)
