def put(word, trie):
    for char in word:
        trie['cnt'] = trie.get('cnt', 0) + 1
        trie[char] = trie.get(char, {})
        trie = trie[char]


def count(word, trie):
    for char in word:
        if char == '?':
            return trie.get('cnt', 0)
        trie = trie.get(char, False)
        if not trie:
            return 0


def solution(words, queries):
    front, back = [{} for _ in range(10001)], [{} for _ in range(10001)]
    for word in words:
        l = len(word)
        put(word[::-1], back[l])
        put(word, front[l])
    for i, word in enumerate(queries):
        l = len(word)
        queries[i] = count(word[::-1], back[l]) if word[0] == '?' else count(word, front[l])
    return queries
