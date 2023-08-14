# [Gold I] 풍선 - 4716 

[문제 링크](https://www.acmicpc.net/problem/4716) 

### 성능 요약

메모리: 31256 KB, 시간: 84 ms

### 분류

그리디 알고리즘, 정렬

### 문제 설명

<p>As you know, balloons are handed out during this contest to teams as they solve problems. However, in the past this has sometimes presented challenging logistical problems.</p>

<p>One contest hosting site maintained two rooms, A and B, each containing a supply of balloons. There were N teams attending the contest, each sitting in different locations, some being closer to room A, and others to room B. Given the number of balloons needed by each team and each teams distance from room A and room B, what is the minimum total possible distance that must be traveled by all balloons as they are delivered to their respective teams, assuming they are allocated in an optimal fashion from rooms A and B? For the purposes of this problem, assume that the contest staff were cheap and only bought one color of balloon.</p>

### 입력 

 <p>There will be several test cases in the data ﬁle. Each test case will begin with a line with three integers:</p>

<pre>N A B</pre>

<p>where N is the number of teams (1 ≤ N ≤ 1,000), and A and B are the number of balloons in rooms A and B, respectively (0 ≤ A, B ≤ 10,000).</p>

<p>On each of the next N lines there will be three integers, representing information for each team:</p>

<pre>K D<sub>A</sub> D<sub>B</sub></pre>

<p>where K is the total number of balloons that this team will need, D<sub>A</sub> is the distance of this team from room A, and D<sub>B</sub> is this teams distance from room B (0 ≤ D<sub>A</sub>, D<sub>B</sub> ≤ 1 000). You may assume that there are enough balloons - that is, Σ<sub>i</sub> K<sub>i</sub> ≤ A+B. The data ﬁle will end with a line with three 0s.</p>

### 출력 

 <p>For each test case, output a single integer, representing the minimum total distance that must be traveled to deliver all of the balloons. Count only the outbound trip, from A or B to the team. Dont count the distance that a runner must travel to return to room A or room B. Print each integer on its own line with no spaces. Do not print any blank lines between answers.</p>

