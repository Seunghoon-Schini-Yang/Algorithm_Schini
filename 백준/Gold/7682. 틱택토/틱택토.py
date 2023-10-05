import sys
input = sys.stdin.readline


class TicTacToe():
    def __init__(self, state):
        self.state = state


def main():
    bingos = [(0, 1, 2), (3, 4, 5), (6, 7, 8),\
              (0, 3, 6), (1, 4, 7), (2, 5, 8),\
              (0, 4, 8), (2, 4, 6)]
    while True:
        game = TicTacToe(input().rstrip())
        is_valid = True
        if game.state == 'end':
            break
        xs = [False] * 9
        os = [False] * 9
        for i in range(9):
            if game.state[i] == 'X':
                xs[i] = True
            elif game.state[i] == 'O':
                os[i] = True
        x, o = sum(xs), sum(os)
        if o > x or x > o+1 or x < 3:
            is_valid = False
        else:
            x_bingo = sum(all(xs[n] for n in bingo) for bingo in bingos)
            o_bingo = sum(all(os[n] for n in bingo) for bingo in bingos)
            if x_bingo and o_bingo:
                is_valid = False
            elif not x_bingo and not o_bingo and (x != 5 or o != 4):
                is_valid = False
            elif o_bingo and x > o or x_bingo and x == o:
                is_valid = False
        print('valid' if is_valid else 'invalid')

        
if __name__ == '__main__':
    main()
