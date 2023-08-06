def put(idx, word, trie):
    l = len(word)
    cur = trie
    for i, char in enumerate(word):
        if char == '?':
            cur[0] = cur.get(0, {})
            cur = cur[0]
            cur[l-i] = cur.get(l-i, [])
            cur[l-i].append(idx)
            break
        cur[char] = cur.get(char, {})
        cur = cur[char]


def count(word, trie, table):
    l = len(word)
    cur = trie
    for i, char in enumerate(word):
        if cur.get(0, False):
            if l-i in cur[0]:
                for idx in cur[0][l-i]:
                    table[idx] += 1
        cur = cur.get(char, False)
        if not cur:
            break

    
def solution(words, queries):
    front, back = {}, {}
    only_marks = []
    for i, q in enumerate(queries):
        if q[0] == '?':
            put(i, q[::-1], back)
        else:
            put(i, q, front)
        if q[0] == q[-1] == '?':
            only_marks.append(i)
    queries = [0] * len(queries)
    for word in words:
        count(word, front, queries)
        count(word[::-1], back, queries)
    for i in only_marks:
        queries[i] >>= 1
    return queries
