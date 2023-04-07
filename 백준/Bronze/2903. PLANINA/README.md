# [Bronze III] PLANINA - 2903 

[문제 링크](https://www.acmicpc.net/problem/2903) 

### 성능 요약

메모리: 31256 KB, 시간: 40 ms

### 분류

Mathematics

### 문제 설명

<p>Mirko and Slavko are filming a movie adaptation of the popular SF novel "Chicks in space 13". The script requires them to present a lot of different worlds so they decided to film the entire movie in front of a green screen and add CGI backgrounds later. Mirko heard that the best way to generate artificial terrain is to use midpoint displacement algorithm.</p>

<p>To start the algorithm, Mirko selects 4 points forming a perfect square. He then performs the following steps:</p>

<ol>
	<li>On each side of the square, he adds a new point in the exact middle of the side. The height of this new point is the average height of the two points on that side.</li>
	<li>In the exact center of the square he adds a new point whose height is the average height of all 4 square vertices, plus a small random value.</li>
</ol>

<p>After those two steps are performed, he now has 4 new squares. He performs the same steps on the newly created squares again and again until he is pleased with the results. The following diagram illustrates 2 iterations of the algorithm.</p>

<table class="table table-bordered td-center">
	<tbody>
		<tr>
			<td><img alt="" src="https://upload.acmicpc.net/5e446f0f-613c-4ce0-a626-6b0c2729ed1e/-/preview/" style="width: 214px; height: 213px;"></td>
			<td><img alt="" src="https://upload.acmicpc.net/65c1bcf1-7d8a-463b-91df-d6cabcc2ceae/-/preview/" style="width: 212px; height: 213px;"></td>
			<td><img alt="" src="https://upload.acmicpc.net/27b99467-cfdf-4ce3-a0b0-2897747edcf9/-/preview/" style="width: 212px; height: 213px;"></td>
		</tr>
		<tr>
			<td>Start - 4 points</td>
			<td>1 iteration - 9 points</td>
			<td>2 iterations - 25 points</td>
		</tr>
	</tbody>
</table>

<p>Mirko noticed that some of the points belong to more than one square. In order to decrease memory consumption, he stores calculates and stores such points only once. He now wonders how many points in total will he need to store in memory after N iterations.</p>

### 입력 

 <p>The first and only line of input contains one integer N (1 ≤ N ≤ 15), number of iterations</p>

### 출력 

 <p>The first and only line of output should contain one number, the number of points stored after N iterations.</p>

