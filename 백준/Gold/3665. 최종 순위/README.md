# [Gold I] 최종 순위 - 3665 

[문제 링크](https://www.acmicpc.net/problem/3665) 

### 성능 요약

메모리: 37908 KB, 시간: 360 ms

### 분류

그래프 이론(graphs), 위상 정렬(topological_sorting)

### 문제 설명

<p>There are n teams (labelled from 1 to n) who take part in a programming competition every year, and at the end they are ranked in order of merit. The rankings for last year are known. This year, the jury wants to make the event less competitive, and decides not to publish such a ranking list (since teams near the bottom might get disheartened). Instead, they will produce a complete list of pairs of teams whose relative rank order has changed from last year to this year. For example, if team 13 placed above team 6 last year, but team 6 placed above team 13 this year, the pair (6, 13) is announced. This would enable teams to track their progress against a particular opposing team, but not give them a clear sense of where they stand overall.</p>

<p>Of course, this isn’t going to stop your team from trying to determine the overall ranking list. Given last year’s rankings and a complete list of the pairs of teams whose relative rank order has changed, reconstruct as much of this year’s standings as possible. It is possible that the jury might have made an error, so if the data given is inconsistent with any possible ranking list for this year, you should also detect this.</p>

### 입력 

 <p>On the ﬁrst line a positive integer: the number of test cases, at most 100. After that per test case:</p>

<ul>
	<li>One line with an integer n (2 ≤ n ≤ 500): the number of teams.</li>
	<li>One line with n integers t<sub>i</sub> (1 ≤ t<sub>i</sub> ≤ n): the rankings for last year, from best team to worst team. t<sub>i</sub> represents the team who came in position i (1-indexed) on the ranklist. All the ti will be distinct.</li>
	<li>One line with an integer m (0 ≤ m ≤ 25000): the number of pairs whose relative rank order has changed.</li>
	<li>m lines with two integers a<sub>i</sub> and b<sub>i</sub> (1 ≤ a<sub>i</sub> < b<sub>i</sub> ≤ n) each: a pair of teams whose relative rank order has changed. Each such pair will be mentioned exactly once.</li>
</ul>

### 출력 

 <p>Per test case:</p>

<ul>
	<li>One line with n integers: the rankings for this year, from best to worst, where the i-th term (1-indexed) represents the team in position i. If this team cannot be determined with certainty, the integer should be replaced with a ‘?’ character. If the data for a particular test case is inconsistent with any possible ranking list for this year, the line must contain “IMPOSSIBLE” instead.</li>
</ul>

