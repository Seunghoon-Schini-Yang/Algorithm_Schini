# [Silver III] 링 - 3036 

[문제 링크](https://www.acmicpc.net/problem/3036) 

### 성능 요약

메모리: 30840 KB, 시간: 72 ms

### 분류

유클리드 호제법(euclidean), 수학(math), 정수론(number_theory)

### 문제 설명

<p>After an exhausting morning, Mirko fell asleep. His brother Stanko, however, just awoke and, like his brother, is all about excitement. Stanko found N rings of varying radiuses in the garage. He arranged them on the floor so that each ring (except the first and last) touches the ones before and after it. </p>

<p><img alt="" src="https://www.acmicpc.net/upload/images/ring.png" style="height:150px; width:318px"></p>

<p>He started turning the first ring and noticed that the other rings turned as well; some faster, some slower! </p>

<p>Thrilled with his discovery, he decided to count how many times the other rings turn while the first ring turns once. He gave up after noticing that this number is not always an integer and not knowing what to do. </p>

<p>Write a program that determines how many times each ring turns while the first turns once. </p>

### 입력 

 <p>The first line of input contains an integer N (3 ≤ N ≤ 100), the number of rings. </p>

<p>The next line contains N integers between 1 and 1000, the radiuses of Stanko's rings, in the order they are laid out on the floor.</p>

### 출력 

 <p>The output must contain N-1 lines. For every ring other than the first, in the order they are given in the input, output a fraction A/B, meaning that the respective ring turns A/B times while the first ring turns once. </p>

<p>The fractions must be in reduced form (the numerator and denominator must not have a common divisor larger than 1).</p>

