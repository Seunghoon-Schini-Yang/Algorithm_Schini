# [Gold III] 레이저 통신 - 6087 

[문제 링크](https://www.acmicpc.net/problem/6087) 

### 성능 요약

메모리: 31256 KB, 시간: 52 ms

### 분류

너비 우선 탐색, 데이크스트라, 그래프 이론, 그래프 탐색

### 문제 설명

<p>The cows have a new laser-based system so they can have casual conversations while out in the pasture which is modeled as a W x H grid of points (1 <= W <= 100; 1 <= H <= 100).</p>

<p>The system requires a sort of line-of-sight connectivity in order to sustain communication. The pasture, of course, has rocks and trees that disrupt the communication but the cows have purchased diagonal mirrors ('/' and '\' below) that deflect the laser beam through a 90 degree turn. Below is a map that illustrates the problem.</p>

<p>H is 8 and W is 7 for this map. The two communicating cows are notated as 'C's; rocks and other blocking elements are notated as '*'s:</p>

<pre>7 . . . . . . .         7 . . . . . . .
6 . . . . . . C         6 . . . . . /-C
5 . . . . . . *         5 . . . . . | *
4 * * * * * . *         4 * * * * * | *
3 . . . . * . .         3 . . . . * | .
2 . . . . * . .         2 . . . . * | .
1 . C . . * . .         1 . C . . * | .
0 . . . . . . .         0 . \-------/ .
  0 1 2 3 4 5 6           0 1 2 3 4 5 6
</pre>

<p>Determine the minimum number of mirrors M that must be installed to maintain laser communication between the two cows, a feat which is always possible in the given test data.</p>

### 입력 

 <ul>
	<li>Line 1: Two space separated integers: W and H</li>
	<li>Lines 2..H+1: The entire pasture.</li>
</ul>

### 출력 

 <ul>
	<li>Line 1: A single integer: M</li>
</ul>

