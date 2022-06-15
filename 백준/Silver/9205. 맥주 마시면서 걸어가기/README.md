# [Silver I] 맥주 마시면서 걸어가기 - 9205 

[문제 링크](https://www.acmicpc.net/problem/9205) 

### 성능 요약

메모리: 32492 KB, 시간: 92 ms

### 분류

너비 우선 탐색(bfs), 그래프 이론(graphs), 그래프 탐색(graph_traversal)

### 문제 설명

<p>Once every year, Jo and his friends want to visit the local fair in Erlangen, called Bergkirchweih. This year, they want to make a Kastenlauf (box run). They start at Jo’s home, and have one box (Kasten) of beer (with twenty bottles). As they are very thirsty, they drink one bottle of beer every 50 metres. In other words, in order to walk 50 metres, they should drink a bottle right before that.</p>

<p>As the way from Jo’s home to the Bergkirchweih is pretty long, they need more beer than they have initially. Fortunately, there are stores selling beer on the way. When they visit a store, they can drop their empty bottles and buy new bottles, but their total number of full bottles will not be more than twenty (because they are too lazy to carry more than one full box). After leaving the store, they should drink a bottle before moving 50 metres.</p>

<p>You are given the coordinates of the stores, of Jo’s home and of the location of the Bergkirchweih.</p>

<p>Write a program to determine whether Jo and his friends can happily reach the Bergkirchweih, or whether they will run out of beer on the way.</p>

### 입력 

 <p>Input starts with one line containing the number of test cases t (t ≤ 50).</p>

<p>Each test case starts with one line, containing the number n of stores selling beer (with 0 ≤ n ≤ 100).</p>

<p>The next n + 2 lines cointain (in this order) the location of Jo’s home, of the stores, and of the Bergkirchweih. The location is given with two integer coordinates x and y, (both in meters, -32768 ≤ x, y ≤ 32767).</p>

<p>As Erlangen is a rectangularly laid out city, the distance between two locations is the difference of the first coordinate plus the difference of the second coordinate (also called Manhattan-Metric).</p>

### 출력 

 <p>For each test case print one line, containing either “happy” (if Jo and his friends can happily reach the Bergkirchweih), or “sad” (if they will not reach the Bergkirchweih because they run out of beer.).</p>

