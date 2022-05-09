# my
# dp + recursive + path_track
import sys
input = sys.stdin.readline


def sol(n: int) -> int:
    def max_ind_set_weight(c_node: int, p_node: int) -> tuple:
        is_c_w, not_c_w = weigths[c_node], 0
        is_c_path, not_c_path = [c_node], []

        for cc_node in tree[c_node]:
            if cc_node != p_node:
                is_cc_path, not_cc_path = max_ind_set_weight(cc_node, c_node)
                is_cc_w, not_cc_w = dp[cc_node]

                is_c_w += not_cc_w
                is_c_path.extend(not_cc_path)

                if is_cc_w >= not_cc_w:
                    not_c_w += is_cc_w
                    not_c_path.extend(is_cc_path)
                else:
                    not_c_w += not_cc_w
                    not_c_path.extend(not_cc_path)

        dp[c_node][:] = is_c_w, not_c_w

        return is_c_path, not_c_path

    
    dp = [[0,0] for _ in range(n+1)]
    weigths = [0] + list(map(int, input().split()))
    tree = [[] for _ in range(n+1)]
    for _ in range(n-1):
        v1,v2 = map(int, input().split())
        tree[v1].append(v2)
        tree[v2].append(v1)
    
    is_root_path, not_root_path = max_ind_set_weight(1, 0)
    
    if dp[1][0] >= dp[1][1]:
        print(dp[1][0])
        print(*sorted(is_root_path))
    else:
        print(dp[1][1])
        print(*sorted(not_root_path))
    # return (dp[1][0], sorted(is_root_path)) if dp[1][0] >= dp[1][1] else (dp[1][1], sorted(not_root_path))


sol(int(input()))
