import sys
input = sys.stdin.readline
from string import ascii_lowercase
from itertools import combinations as comb


class Teach():
    def __init__(self, N, K):
        self.answer = 0
        if K == 26:
            self.answer = N
        elif 5 <= K:
            self.atoi = {c: i for i, c in enumerate(ascii_lowercase)}
            self.memo = [False] * 26
            for c in 'acint':
                self.memo[self.atoi[c]] = True
            words = [self._word_to_idx(input().rstrip()[4:-4]) for _ in range(N)]
            self.answer = self._teach_words(words, K)

        
    def _word_to_idx(self, word):
        mask = 0
        for i in set(self.atoi[c] for c in word if not self.memo[self.atoi[c]]):
            mask |= 1<<i
        return mask
    

    def _teach_words(self, words, K):
        answer = 0
        for seq in comb((1<<i for i in range(26) if not self.memo[i]), K-5):
            mask = sum(seq)
            answer = max(answer, sum(mask&word == word for word in words))
        return answer


if __name__ == '__main__':
    teacher = Teach(*map(int, input().split()))
    print(teacher.answer)
