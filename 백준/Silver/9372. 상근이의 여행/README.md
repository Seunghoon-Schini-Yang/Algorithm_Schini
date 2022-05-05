# [Silver III] 상근이의 여행 - 9372 

[문제 링크](https://www.acmicpc.net/problem/9372) 

### 성능 요약

메모리: 30840 KB, 시간: 84 ms

### 분류

그래프 이론(graphs), 트리(trees)

### 문제 설명

<p>Due to budget cuts, even spies have to use commercial airlines nowadays to travel between cities in the world. Although this mode of travel can be very convenient for a spy, it also raises a problem: the spy has to trust the pilot to make sure he is not in danger during the ﬂight. And even worse, sometimes there is no direct ﬂight between  some pairs of cities, so that the spy has to take multiple ﬂights to get to the desired location, and thus has to trust multiple pilots!</p>

<p>To limit the trust issues you are asked for help. Given the ﬂight schedule, ﬁgure out the smallest set of pilots that need to be trusted, such that the spy can safely travel between all cities.</p>

### 입력 

 <p>On the ﬁrst line one positive number: the number of test cases, at most 100. After that per test case:</p>

<ul>
	<li>one line with two space-separated integers n (2 ≤ n ≤ 1 000) and m (1 ≤ m ≤ 10 000): the number of cities and the number of pilots, respectively.</li>
	<li>m lines with two space-separated integers a and b (1 ≤ a, b ≤ n; a ≠ b): a pilot ﬂying his plane back and forth between city a and b.</li>
</ul>

<p>It is possible to go from any city to any other city using one or more ﬂights. In other words: the graph is connected.</p>

### 출력 

 <p>Per test case:</p>

<ul>
	<li>one line with and integer: the minimum number of pilots that need to be trusted such that it is possible to travel between each pair of cities.</li>
</ul>

