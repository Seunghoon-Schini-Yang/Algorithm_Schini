# [Gold III] 가스관 - 2931 

[문제 링크](https://www.acmicpc.net/problem/2931) 

### 성능 요약

메모리: 31256 KB, 시간: 40 ms

### 분류

구현, 시뮬레이션

### 문제 설명

<p>To help design the new gas pipeline which will be used to deliver Russian gas to Croatia, Zagreb and Moscow are using the computer game Pipe Mania. In the game, Europe is divided into R rows and C columns. Each cell can be empty or contain one of the seven basic pipeline building blocks:</p>

<table class="table table-bordered td-center">
	<tbody>
		<tr>
			<td><img alt="" src="https://upload.acmicpc.net/3a92cfe2-8d8f-4059-b4e1-1d23b2e7df12/-/crop/73x118/29,0/-/preview/" style="width: 37px; height: 59px;"></td>
			<td><img alt="" src="https://upload.acmicpc.net/3a92cfe2-8d8f-4059-b4e1-1d23b2e7df12/-/crop/127x118/168,0/-/preview/" style="width: 64px; height: 59px;"></td>
			<td><img alt="" src="https://upload.acmicpc.net/3a92cfe2-8d8f-4059-b4e1-1d23b2e7df12/-/crop/116x118/339,0/-/preview/" style="width: 58px; height: 59px;"></td>
			<td><img alt="" src="https://upload.acmicpc.net/3a92cfe2-8d8f-4059-b4e1-1d23b2e7df12/-/crop/91x118/519,0/-/preview/" style="width: 46px; height: 59px;"></td>
			<td><img alt="" src="https://upload.acmicpc.net/3a92cfe2-8d8f-4059-b4e1-1d23b2e7df12/-/crop/90x118/685,0/-/preview/" style="width: 45px; height: 59px;"></td>
			<td><img alt="" src="https://upload.acmicpc.net/3a92cfe2-8d8f-4059-b4e1-1d23b2e7df12/-/crop/89x118/853,0/-/preview/" style="width: 45px; height: 59px;"></td>
			<td><img alt="" src="https://upload.acmicpc.net/3a92cfe2-8d8f-4059-b4e1-1d23b2e7df12/-/crop/90x118/1018,0/-/preview/" style="width: 45px; height: 59px;"></td>
		</tr>
		<tr>
			<td>Block '<code>|</code>'</td>
			<td>Block '<code>-</code>'</td>
			<td>Block '<code>+</code>'</td>
			<td>Block '<code>1</code>'</td>
			<td>Block '<code>2</code>'</td>
			<td>Block '<code>3</code>'</td>
			<td>Block '<code>4</code>'</td>
		</tr>
	</tbody>
</table>

<p>Gas flows from Moscow to Zagreb. Gas can flow in either direction through the building blocks. Block '<code>+</code>' is special in that gas must flow in two directions (one vertical, one horizontal), as in the following example:</p>

<p style="text-align: center;"><img alt="" src="https://upload.acmicpc.net/66956a75-fdf1-4706-923d-cb2794fc0ab9/-/preview/" style="width: 253px; height: 158px;"></p>

<p>Work on the new pipeline had already started when it was found that malicious hackers got hold of the plan and erased exactly one building block from the plan i.e. replaced it with an empty cell. </p>

<p>Write a program that determines where the block was erased from and what type it was. </p>

### 입력 

 <p>The first line contains two integers R and C, the dimensions of Europe (1 ≤ R, C ≤ 25). </p>

<p>The following R lines contain the plan, each consisting of exactly C characters. The characters are: </p>

<ul>
	<li>Period ('<code>.</code>'), representing an empty cell; </li>
	<li>The characters '<code>|</code>' (ASCII 124), '<code>-</code>', '<code>+</code>', '<code>1</code>', '<code>2</code>', '<code>3</code>', '<code>4</code>', representing the building block types; </li>
	<li>The letters '<code>M</code>' and '<code>Z</code>', representing Moscow and Zagreb. Each of these will appear exactly once in the plan. </li>
</ul>

<p>The flow of gas will be uniquely determined in the input; exactly one building block will be adjacent to each of Moscow and Zagreb. Additionally, the plan will not have redundant blocks i.e. all blocks in the plan must be used after the missing block is added. </p>

<p>The input will be such that a solution will exist and it will be unique. </p>

### 출력 

 <p>Output the row and column of the erased block, and the type of the block (one of the seven characters as in the input). </p>

