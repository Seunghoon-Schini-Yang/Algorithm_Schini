# [Silver V] 최소공배수 - 13241 

[문제 링크](https://www.acmicpc.net/problem/13241) 

### 성능 요약

메모리: 31256 KB, 시간: 44 ms

### 분류

유클리드 호제법, 수학, 정수론

### 문제 설명

<p>The integer A is multiple of B if we can multiply B by some integer number bigger than 0 we get A. </p>

<p>Examples:</p>

<ul>
	<li>10 is multiple of 5 because 5*2 is 10</li>
	<li>10 is multiple of 10 because 10*1 is 10</li>
	<li>6 is multiple of 1 because 1*6 is 6</li>
	<li>20 is multiple of 1, 2, 4, 5, 10 and 20.</li>
</ul>

<p>We call the lowest common multiple of A and B to the the smallest positive integer C that is a multiple of both A and B.</p>

<p>Some examples:</p>

<ul>
	<li>The lowest common multiple of 2 and 5 is 10 because 10 is multiple of 2 and 5 and there is no other common multiple that is smaller.</li>
	<li>The lowest common multiple of 10 and 20 is 20.</li>
	<li>The lowest common multiple of 5 and 3 is 15.</li>
</ul>

<p>Your task is to write a program that computes the lowest common multiple of 2 numbers.</p>

### 입력 

 <p>A single line containing 2 integers A and B separated by one space.</p>

<p>In 50% of the test cases, the number A and B will be less than 1000 (10<sup>3</sup>). In the other 50% of the test cases, the numbers A and B may be bigger than 1000 but smaller than 100000000 (10<sup>8</sup>). </p>

<p>Note: For the larger test cases you’ll need to declare your variables as 64 bits integers. Use long long int in C/C++ and long in Java.</p>

### 출력 

 <p>Print a single line containing an integer, the lowest common multiple of A and B.</p>

