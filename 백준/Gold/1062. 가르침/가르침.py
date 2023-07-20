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
            words = [self._word_to_idx(input().rstrip()) for _ in range(N)]
            self.answer = self._teach_words(words, K)

        
    def _word_to_idx(self, word):
        return set(self.atoi[c] for c in word if not self.memo[self.atoi[c]])
    

    def _teach_words(self, words, K):
        answer = 0
        for seq in comb((i for i in range(26) if not self.memo[i]), K-5):
            for i in seq:
                self.memo[i] = True
            answer = max(answer, sum(all(self.memo[i] for i in word) for word in words))
            for i in seq:
                self.memo[i] = False
        return answer


if __name__ == '__main__':
    teacher = Teach(*map(int, input().split()))
    print(teacher.answer)
