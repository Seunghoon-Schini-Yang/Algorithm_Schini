# [Gold I] 인터넷 설치 - 1800 

[문제 링크](https://www.acmicpc.net/problem/1800) 

### 성능 요약

메모리: 35888 KB, 시간: 96 ms

### 분류

이분 탐색, 데이크스트라, 그래프 이론, 매개 변수 탐색

### 문제 설명

<p>Farmer John wants to set up a telephone line at his farm. Unfortunately, the phone company is uncooperative, so he needs to pay for some of the cables required to connect his farm to the phone system.</p>

<p>There are N (1 <= N <= 1,000) forlorn telephone poles conveniently numbered 1..N that are scattered around Farmer John's property; no cables connect any them.  A total of P (1 <= P <= 10,000) pairs of poles can be connected by a cable; the rest are too far apart.</p>

<p>The i-th cable can connect the two distinct poles A_i and B_i, with length L_i (1 <= L_i <= 1,000,000) units if used. The input data set never names any {A_i,B_i} pair more than once. Pole 1 is already connected to the phone system, and pole N is at the farm. Poles 1 and N need to be connected by a path of cables; the rest of the poles might be used or might not be used.</p>

<p>As it turns out, the phone company is willing to provide Farmer John with K (0 <= K < N) lengths of cable for free. Beyond that he will have to pay a price equal to the length of the longest remaining cable he requires (each pair of poles is connected with a separate cable), or 0 if he does not need any additional cables.</p>

<p>Determine the minimum amount that Farmer John must pay.</p>

### 입력 

 <p>* Line 1: Three space-separated integers: N, P, and K</p>

<p>* Lines 2..P+1: Line i+1 contains the three space-separated integers: A_i, B_i, and L_i</p>

### 출력 

 <p>* Line 1: A single integer, the minimum amount Farmer John can pay. If it is impossible to connect the farm to the phone company, print -1.</p>

