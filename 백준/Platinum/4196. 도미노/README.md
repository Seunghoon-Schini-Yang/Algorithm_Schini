# [Platinum IV] 도미노 - 4196 

[문제 링크](https://www.acmicpc.net/problem/4196) 

### 성능 요약

메모리: 162780 KB, 시간: 1344 ms

### 분류

그래프 이론(graphs), 강한 연결 요소(scc)

### 문제 설명

<p>Dominos are lots of fun. Children like to stand the tiles on their side in long lines. When one domino falls, it knocks down the next one, which knocks down the one after that, all the way down the line. However, sometimes a domino fails to knock the next one down. In that case, we have to knock it down by hand to get the dominos falling again.</p>

<p>Your task is to determine, given the layout of some domino tiles, the minimum number of dominos that must be knocked down by hand in order for all of the dominos to fall.</p>

### 입력 

 <p>The first line of input contains one integer specifying the number of test cases to follow. Each test case begins with a line containing two integers, each no larger than 100 000. The first integer n is the number of domino tiles and the second integer m is the number of lines to follow in the test case. The domino tiles are numbered from 1 to n. Each of the following lines contains two integers x and y indicating that if domino number x falls, it will cause domino number y to fall as well.</p>

### 출력 

 <p>For each test case, output a line containing one integer, the minimum number of dominos that must be knocked over by hand in order for all the dominos to fall.</p>

