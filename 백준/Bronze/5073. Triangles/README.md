# [Bronze III] Triangles - 5073 

[문제 링크](https://www.acmicpc.net/problem/5073) 

### 성능 요약

메모리: 31256 KB, 시간: 40 ms

### 분류

Mathematics, Implementation, Geometry

### 문제 설명

<p>We know that triangles have 3 sides. Triangles may be classified according to the lengths of those sides, as shown in this table:</p>

<ul>
	<li>Equilateral: All three sides are of equal length.</li>
	<li>Isosceles: Two sides are of equal length, the other side is different.</li>
	<li>Scalene: All three sides have different lengths.</li>
</ul>

<p>There is one other possibility. It is possible to give three lengths of sides which would not form a valid traingle. For example 6, 3, 2. If the sum of the lengths of the two shortest sides is not greater than the length of the longest side, then the sides do not represent a triangle – the data is invalid.</p>

<p>In this problem you will be given values for the three lengths of the sides of a triangle and asked to classify it. </p>

### 입력 

 <p>Input consists of a number of lines, each line containing three positive integers, not more than 1,000, separated by single spaces. The last line of input will be 0 0 0 – do not process this line.</p>

### 출력 

 <p>For each line of input, produce one line of output containing a single word (Equilateral, Isosceles, Scalene or Invalid) which is the classification of the lengths shown in the input.</p>

