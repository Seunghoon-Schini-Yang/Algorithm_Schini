# [Platinum I] 직사각형 - 7626 

[문제 링크](https://www.acmicpc.net/problem/7626) 

### 성능 요약

메모리: 318508 KB, 시간: 4624 ms

### 분류

값 / 좌표 압축(coordinate_compression), 자료 구조(data_structures), 세그먼트 트리(segtree), 스위핑(sweeping)

### 문제 설명

<p>There are N axis-parallel rectangles in the plane. Calculate the total area they cover.</p>

<p> </p>

### 입력 

 <p>The ﬁrst line contains a positive integer N (1 ≤ N ≤ 200, 000). N lines then follow, each with four space-separated values “x<sub>1</sub> x<sub>2</sub> y<sub>1</sub> y<sub>2</sub>” denoting the rectangle [x<sub>1</sub>, x<sub>2</sub>]×[y<sub>1</sub>, y<sub>2</sub>]. Each of the values x<sub>1</sub>, x<sub>2</sub>, y<sub>1</sub>, y<sub>2</sub> are integers between 0 and 10<sup>9</sup>, inclusive, and for a given rectangle x<sub>1</sub> < x<sub>2</sub> and y<sub>1</sub> < y<sub>2</sub> always.</p>

### 출력 

 <p>Output the total area covered by the given N rectangles. Any region covered by multiple rectangles should only be counted once.</p>

