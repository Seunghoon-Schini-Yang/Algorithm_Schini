# [Platinum V] 문자열 제곱 - 4354 

[문제 링크](https://www.acmicpc.net/problem/4354) 

### 성능 요약

메모리: 42604 KB, 시간: 1500 ms

### 분류

KMP(kmp), 문자열(string)

### 문제 설명

<p>Given two strings a and b we define a*b to be their concatenation. For example, if a = "abc" and b = "def" then a*b = "abcdef". If we think of concatenation as multiplication, exponentiation by a non-negative integer is defined in the normal way: a^0 = "" (the empty string) and a^(n+1) = a*(a^n).</p>

### 입력 

 <p>Each test case is a line of input representing s, a string of lower-case alphabetic characters.</p>

### 출력 

 <p>For each s you should print the largest n such that s = a^n for some string a. The length of s will be at least 1 and will not exceed 1 million characters. A line with a period follows the last test case.</p>

