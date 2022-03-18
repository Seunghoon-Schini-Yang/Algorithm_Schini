# [Silver III] 프린터 큐 - 1966 

[문제 링크](https://www.acmicpc.net/problem/1966) 

### 성능 요약

메모리: 32396 KB, 시간: 88 ms

### 분류

자료 구조(data_structures), 구현(implementation), 큐(queue), 시뮬레이션(simulation)

### 문제 설명

<p>The only printer in the computer science students’ union is experiencing an extremely heavy workload. Sometimes there are a hundred jobs in the printer queue and you may have to wait for hours to get a single page of output.</p>

<p>Because some jobs are more important than others, the Hacker General has invented and implemented a simple priority system for the print job queue. Now, each job is assigned a priority between 1 and 9 (with 9 being the highest priority, and 1 being the lowest), and the printer operates as follows.</p>

<p>The first job J in queue is taken from the queue.<br>
If there is some job in the queue with a higher priority than job J, then move J to the end of the queue without printing it.<br>
Otherwise, print job J (and do not put it back in the queue).</p>

<p>In this way, all those important muffin recipes that the Hacker General is printing get printed very quickly. Of course, those annoying term papers that others are printing may have to wait for quite some time to get printed, but that’s life.</p>

<p>Your problem with the new policy is that it has become quite tricky to determine when your print job will actually be completed. You decide to write a program to ﬁgure this out. The program will be given the current queue (as a list of priorities) as well as the position of your job in the queue, and must then calculate how long it will take until your job is printed, assuming that no additional jobs will be added to the queue. To simplify matters, we assume that printing a job always takes exactly one minute, and that adding and removing jobs from the queue is instantaneous.</p>

### 입력 

 <p>One line with a positive integer: the number of test cases (at most 100). Then for each test case:</p>

<ul>
	<li>One line with two integers n and m, where n is the number of jobs in the queue (1 ≤ n ≤ 100) and m is the position of your job (0 ≤ m ≤ n−1). The ﬁrst position in the queue is number 0, the second is number 1, and so on.</li>
	<li>One line withn integers in the range 1 to 9, giving the priorities of the jobs in the queue. The first integer gives the priority of the ﬁrst job, the second integer the priority of the second job, and so on.</li>
</ul>

### 출력 

 <p>For each test case, print one line with a single integer; the number of minutes until your job is completely printed, assuming that no additional print jobs will arrive.</p>

