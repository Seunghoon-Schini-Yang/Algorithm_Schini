# trie
import sys
input = sys.stdin.readline
print = sys.stdout.write


def sol() -> None:
    while True:
        try:
            n = int(input())
        except:
            break
        avg = str(testcase(n))
        if avg[-2] == '.':
            avg += '0'
        print(f'{avg}\n')


def testcase(n: int) -> float:
    words = [input().rstrip() for _ in range(n)]
    trie = dict()
    for word in words:
        trie_insert(word, trie)
    return round(sum(trie_check(word, trie) for word in words) / n, 2)


def trie_insert(word: str, trie: dict) -> None:
    for char in word:
        trie.update({char: trie.get(char, dict())})
        trie = trie[char]
    trie[0] = 0


def trie_check(word: str, trie: dict) -> int:
    cnt = 1
    trie = trie[word[0]]
    for char in word[1:]:
        if trie.get(0, 1) == 0 or len(trie) > 1:
            cnt += 1
        trie = trie[char]
    return cnt


sol()
