# [Gold I] 소가 길을 건너간 이유 4 - 14464 

[문제 링크](https://www.acmicpc.net/problem/14464) 

### 성능 요약

메모리: 40572 KB, 시간: 116 ms

### 분류

자료 구조, 그리디 알고리즘, 우선순위 큐

### 문제 설명

<p>Farmer John's cows are trying to learn to cross the road effectively. Remembering the old "why did the chicken cross the road?" joke, they figure the chickens must be experts on crossing the road, and go off in search of chickens to help them.</p>

<p>As it turns out, chickens are very busy creatures and have limited time to help the cows. There are C chickens on the farm (1 ≤ C ≤ 20,000), conveniently numbered 1…C, and each chicken i is only willing to help a cow at precisely time T<sub>i</sub>. The cows, never in a hurry, have more flexibility in their schedules. There are N cows on the farm (1 ≤ N ≤ 20,000), conveniently numbered 1…N, where cow j is able to cross the road between time A<sub>j</sub> and time B<sub>j</sub>. Figuring the "buddy system" is the best way to proceed, each cow j would ideally like to find a chicken i to help her cross the road; in order for their schedules to be compatible, i and j must satisfy A<sub>j </sub>≤ T<sub>i</sub> ≤ B<sub>j</sub>.</p>

<p>If each cow can be paired with at most one chicken and each chicken with at most one cow, please help compute the maximum number of cow-chicken pairs that can be constructed.</p>

### 입력 

 <p>The first line of input contains C and N. The next C lines contain T<sub>1</sub>…T<sub>C</sub>, and the next N lines contain A<sub>j</sub> and B<sub>j</sub> (A<sub>j </sub>≤ B<sub>j</sub>) for j=1…N. The A's, B's, and T's are all non-negative integers (not necessarily distinct) of size at most 1,000,000,000.</p>

### 출력 

 <p>Please compute the maximum possible number of cow-chicken pairs.</p>

<p> </p>

