# [Gold III] 마라톤 2 - 10653 

[문제 링크](https://www.acmicpc.net/problem/10653) 

### 성능 요약

메모리: 34588 KB, 시간: 3948 ms

### 분류

다이나믹 프로그래밍

### 문제 설명

<p>Unhappy with the poor health of his cows, Farmer John enrolls them in an assortment of different physical fitness activities.  His prize cow Bessie is enrolled in a running class, where she is eventually expected to run a marathon through the downtown area of the city near Farmer John's farm!</p>

<p>The marathon course consists of N checkpoints (3 <= N <= 500) to be visited in sequence, where checkpoint 1 is the starting location and checkpoint N is the finish.  Bessie is supposed to visit all of these checkpoints one by one, but being the lazy cow she is, she decides that she will skip up to K checkpoints (K < N) in order to shorten her total journey.  She cannot skip checkpoints 1 or N, however, since that would be too noticeable.</p>

<p>Please help Bessie find the minimum distance that she has to run if she can skip up to K checkpoints.  </p>

<p>Since the course is set in a downtown area with a grid of streets, the distance between two checkpoints at locations (x1, y1) and (x2, y2) is given by |x1-x2| + |y1-y2|.</p>

### 입력 

 <p>The first line gives the values of N and K.</p>

<p>The next N lines each contain two space-separated integers, x and y, representing a checkpoint (-1000 <= x <= 1000, -1000 <= y <= 1000). The checkpoints are given in the order that they must be visited. Note that the course might cross over itself several times, with several checkpoints occurring at the same physical location.  When Bessie skips such a checkpoint, she only skips one instance of the checkpoint -- she does not skip every checkpoint occurring at the same location.</p>

### 출력 

 <p>Output the minimum distance that Bessie can run by skipping up to K checkpoints.  In the sample case shown here, skipping the checkpoints at (8, 3) and (10, -5) leads to the minimum total distance of 4.</p>

