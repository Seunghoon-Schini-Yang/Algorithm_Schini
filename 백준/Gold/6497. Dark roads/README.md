# [Gold IV] Dark roads - 6497 

[문제 링크](https://www.acmicpc.net/problem/6497) 

### 성능 요약

메모리: 58980 KB, 시간: 1032 ms

### 분류

Graph Theory, Minimum Spanning Tree

### 문제 설명

<p>
Economic times these days are tough, even in Byteland. To reduce the
operating costs, the government of Byteland has decided to optimize the
road lighting. Till now every road was illuminated all night long,
which costs 1 Bytelandian Dollar per meter and day. To save money,
they decided to no longer illuminate every road, but to switch off the
road lighting of some streets. To make sure that the inhabitants of
Byteland still feel safe, they want to optimize the lighting in such
a way, that after darkening some streets at night, there will still be
at least one illuminated path from every junction in Byteland to every
other junction.
</p>
<p>
What is the maximum daily amount of money the government of Byteland
can save, without making their inhabitants feel unsafe?
</p>

### 입력 

 <p>
The input file contains several test cases. Each test case starts with
two numbers <i>m</i> and <i>n</i>, the number of junctions
in Byteland and the number of roads in Byteland, respectively.
Input is terminated by <i>m=n=0</i>. Otherwise, <i>1 ≤ m
≤ 200000</i> and <i>m-1 ≤ n ≤ 200000</i>. Then follow
<i>n</i> integer triples <i>x, y, z</i> specifying that
there will be a bidirectional road between <i>x</i> and <i>y</i>
with length <i>z</i> meters (<i>0 ≤ x, y < m</i> and
<i>x ≠ y</i>). The graph specified by each test case is connected.
The total length of all roads in each test case is less than 2<sup>31</sup>.
</p>

### 출력 

 <p>
For each test case print one line containing the maximum daily amount
the government can save.
</p>

