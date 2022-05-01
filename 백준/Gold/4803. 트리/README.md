# [Gold IV] 트리 - 4803 

[문제 링크](https://www.acmicpc.net/problem/4803) 

### 성능 요약

메모리: 30840 KB, 시간: 312 ms

### 분류

자료 구조(data_structures), 깊이 우선 탐색(dfs), 분리 집합(disjoint_set), 그래프 이론(graphs), 그래프 탐색(graph_traversal), 트리(trees)

### 문제 설명

<p>A graph consists of a set of vertices and edges between pairs of vertices. Two vertices are connected if there is a path (subset of edges) leading from one vertex to another, and a connected component is a maximal subset of vertices that are all connected to each other. A graph consists of one or more connected components.</p>

<p>A tree is a connected component without cycles, but it can also be characterized in other ways. For example, a tree consisting of n vertices has exactly n-1 edges. Also, there is a unique path connecting any pair of vertices in a tree.</p>

<p>Given a graph, report the number of connected components that are also trees.</p>

### 입력 

 <p>The input consists of a number of cases. Each case starts with two non-negative integers n and m, satisfying n ≤ 500 and m ≤ n(n-1)/2. This is followed by m lines, each containing two integers specifying the two distinct vertices connected by an edge. No edge will be speciﬁed twice (or given again in a different order). The vertices are labelled 1 to n. The end of input is indicated by a line containing n = m = 0.</p>

### 출력 

 <p>For each case, print one of the following lines depending on how many different connected components are trees (T > 1 below):</p>

<ul>
	<li>Case x: A forest of T trees.</li>
	<li>Case x: There is one tree.</li>
	<li>Case x: No trees.</li>
</ul>

<p>x is the case number (starting from 1).</p>

