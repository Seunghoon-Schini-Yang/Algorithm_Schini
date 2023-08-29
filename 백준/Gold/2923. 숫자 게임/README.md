# [Gold I] 숫자 게임 - 2923 

[문제 링크](https://www.acmicpc.net/problem/2923) 

### 성능 요약

메모리: 39260 KB, 시간: 4916 ms

### 분류

그리디 알고리즘, 두 포인터

### 문제 설명

<p>Mirko and Slavko are playing a new game. Again. Slavko starts each round by giving Mirko two numbers A and B, both smaller than 100. Mirko then has to slove the following task for Slavko: how to pair all given A numbers with all given B numbes so that the maximal sum of such pairs is as small as possible.</p>

<p>In other words, if during previous rounds Slavko gave numbers a<sub>1</sub>, a<sub>2</sub>, a<sub>3</sub> .... a<sub>n</sub> and b<sub>1</sub>, b<sub>2</sub>, b<sub>3</sub> ... b<sub>n</sub>, determine n pairings (a<sub>i</sub>, b<sub>j</sub>) such that each number in A sequence is used in exactley one pairing, and each number in B sequenct is used in exactely one pairing and the maximum of all sums a<sub>i</sub> + b<sub>j</sub> is minimal.</p>

### 입력 

 <p>The first line of input contains a single integer N (1 ≤ N ≤ 100000), number of rounds.</p>

<p>Next N lines contain two integers A and B (1 ≤ A, B < 100), numbers given by Slavko in that round.</p>

### 출력 

 <p>Output consists of N lines, one for each round. Each line should contain the smallest maximal sum for that round.</p>

