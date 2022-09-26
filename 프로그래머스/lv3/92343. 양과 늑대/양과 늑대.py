answer = 0


def solution(info: list, edges: list) -> int:
    def dfs(pn: int, sheep: int, wolf: int, an_list: set):
        global answer

        if not info[pn]:
            sheep += 1
            answer = max(answer, sheep)
        else:
            wolf += 1
        
        if sheep <= wolf:
            return
        
        for cn in an_list:
            nan_list = an_list.copy()
            nan_list.remove(cn)
            for ccn in graph[cn]:
                nan_list.add(ccn)
            dfs(cn, sheep, wolf, nan_list)
        return


    graph = [set() for _ in range(len(info))]
    for p, c in edges:
        graph[p].add(c)
    
    dfs(0, 0, 0, graph[0])
    return answer
