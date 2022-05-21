import sys
input = sys.stdin.readline
print = sys.stdout.write


def sol(n: int) -> str:
    trie = dict()
    for _ in range(n):
        trie_insert(trie, input().split())
    print_dfs(trie, 0)


def trie_insert(trie: dict, feeds: list) -> None:
    for feed in feeds[1:]:
        c_trie = trie.get(feed, dict())
        if not c_trie:
            trie[feed] = c_trie
        trie = c_trie


def print_dfs(trie: dict, depth: int) -> None:
    for feed in sorted(trie):
        print(f'{"--"*depth}{feed}\n')
        print_dfs(trie[feed], depth+1)


sol(int(input()))
