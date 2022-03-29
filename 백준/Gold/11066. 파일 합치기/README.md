# [Gold III] 파일 합치기 - 11066 

[문제 링크](https://www.acmicpc.net/problem/11066) 

### 성능 요약

메모리: 38880 KB, 시간: 948 ms

### 분류

다이나믹 프로그래밍(dp)

### 문제 설명

<p>A novelist Mr. Kim usually writes a book by chapters, where each chapter is saved in a different file. After finishing all chapters, he merges the files into one file in the order of the chapters for a new novel. He can only merge two files containing continuing chapters into a new intermediate file and keep merging the original files or intermediate files until he gets one final file. Assuming the cost (e.g., time) it takes for him to merge two files is exactly the same as the size sum of the two files, calculate the minimum cost to complete the final one file.</p>

<p>For example, let C1, C2, C3 and C4 be continuing chapter files of size 40, 30, 30 and 50 respectively. We could first merge C2 and C3 to get an intermediate file X1, where it requires 60 units of cost. Merging C1 and X1 to get X2 requires 100 units. X2 and C4 could be merged, requiring 150 units, to obtain the desired file containing all chapters in sequence. Therefore the total units of cost is 60+100+150=310. Alternatively, we could first merge C1 and C2 getting Y1, then merge C3 and C4 getting Y2 and finally merge Y1 and Y2 getting the desired file. This sequence of mergings requires 70+80+150=300 units of cost. </p>

<p>Given sizes of chapter files, write a program to calculate the minimum cost for merging the files into one.</p>

### 입력 

 <p>Your program is to read from standard input. The input consists of T test cases. The number of test cases T is given in the first line of the input. Each test case consists of two lines. The first line contains a positive integer K (3 ≤ K ≤ 500), denoting the number of chapters. The second line contains K positive integers which are sizes of chapters from 1 to K. You may assume that sizes of chapters do not exceed 10,000.</p>

### 출력 

 <p>Your program is to write to standard output. Print exactly one line for each test case. For each test case, print the minimum cost for merging all chapters given.</p>

