# [Silver III] 칸토어 집합 - 4779 

[문제 링크](https://www.acmicpc.net/problem/4779) 

### 성능 요약

메모리: 33892 KB, 시간: 56 ms

### 분류

분할 정복, 재귀

### 문제 설명

<p>The Cantor set was discovered by Georg Cantor. It is one of the simpler fractals. It is the result of an infinite process, so for this program, printing an approximation of the whole set is enough.</p>

<p>The following steps describe one way of obtaining the desired output for a given order Cantor set:</p>

<ol>
	<li>Start with a string of dashes, with length 3<sup>order</sup></li>
	<li>Replace the middle third of the line of dashes with spaces. You are left with two lines of dashes at each end of the original string.</li>
	<li>Replace the middle third of each line of dashes with spaces. Repeat until the lines consist of a single dash.</li>
</ol>

<p>For example, if the order of approximation is 3, start with a string of 27 dashes:</p>

<pre>---------------------------</pre>

<p>Remove the middle third of the string:</p>

<pre>---------         ---------</pre>

<p>and remove the middle third of each piece:</p>

<pre>---   ---         ---   ---</pre>

<p>and again:</p>

<pre>- -   - -         - -   - -</pre>

<p>The process stops here, when the groups of dashes are all of length 1. You should not print the intermediate steps in your program. Only the ﬁnal result, given by the last line above, should be displayed.</p>

### 입력 

 <p>Each line of input will be a single number between 0 and 12, inclusive, indicating the order of the approximation. The input stops when end-of-ﬁle is reached.</p>

### 출력 

 <p>You must output the approximation of the Cantor set, followed by a newline. There is no whitespace before or after your Cantor set approximation. The only characters that should appear on your line are ‘-’ and ‘ ’. Each set is followed by a newline, but there should be no extra newlines in your output.</p>

