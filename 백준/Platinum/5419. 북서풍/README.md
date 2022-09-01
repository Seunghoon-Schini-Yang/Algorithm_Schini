# [Platinum IV] 북서풍 - 5419 

[문제 링크](https://www.acmicpc.net/problem/5419) 

### 성능 요약

메모리: 218216 KB, 시간: 3128 ms

### 분류

값 / 좌표 압축(coordinate_compression), 자료 구조(data_structures), 세그먼트 트리(segtree), 스위핑(sweeping)

### 문제 설명

<p>A strong North-Western wind is blowing. When sailing this means that you can sail to the East, to the South or to any direction between East and South. It is impossible to go either North- or Westwards.</p>

<p>In the ocean there are a large number of small islands. These islands are described by coordinate pairs (x, y) on a grid. The positive y-direction is Northwards and the positive x-direction is Eastwards. We’d like to sail from one island to another. For how many pairs of islands is this possible? (Note: a pair consists of two diﬀerent islands.)</p>

### 입력 

 <p>The ﬁrst line of the input ﬁle contains a single number: the number of test cases to follow. Each test case has the following format:</p>

<ul>
	<li>One line with one number n with 1 ≤ n ≤ 75000: the number of islands.</li>
	<li>n lines with two numbers x<sub>i</sub> and y<sub>i</sub> with −10<sup>9</sup> ≤ x<sub>i</sub>, y<sub>i</sub> ≤ 10<sup>9</sup>: the coordinates of the islands. No two islands are located at the same coordinates.</li>
</ul>

### 출력 

 <p>For every test case in the input ﬁle, the output should contain a single number, on a single line: the number of pairs of islands for which you can sail from one to the other.</p>

