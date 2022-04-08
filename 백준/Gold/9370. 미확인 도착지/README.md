# [Gold II] 미확인 도착지 - 9370 

[문제 링크](https://www.acmicpc.net/problem/9370) 

### 성능 요약

메모리: 44196 KB, 시간: 352 ms

### 분류

다익스트라(dijkstra), 그래프 이론(graphs)

### 문제 설명

<p>You are agent B100. A pair of prominently dressed circus artists is traveling over the roads of the city and your mission is to ﬁnd out where they are headed. All we know is that they started at point s and that they are heading for one of several possible destinations. They are in quite a hurry, though, so we are sure they will not take a detour to their destination.</p>

<p>Alas, prominently dressed as they may be, the duo is nowhere to be seen. Fortunately, you have an exceptional sense of smell. More speciﬁcally: your nose will never let you down. You can actually smell they have traveled along the road between intersections g and h.</p>

<p>Where is the elusive duo headed? Or are we still not sure?</p>

<p><img alt="" src="https://www.acmicpc.net/upload/images/destination.png" style="height:230px; width:236px"></p>

<p>A visual representation of the second sample. The duo is travelling from the gray circle to one of the two black circles, and you smelled them on the dashed line, so they could be heading to 6.</p>

### 입력 

 <p>On the ﬁrst line one positive number: the number of test cases, at most 100. After that per test case:</p>

<ul>
	<li>One line with three space-seperated integers n, m and t (2 ≤ n ≤ 2 000, 1 ≤ m ≤ 50 000 and 1 ≤ t ≤ 100): the number of intersections in the city, the number of individual roads between those intersections, and the number of possible destinations respectively.</li>
	<li>One line with three space-seperated integers s, g and h (1 ≤ s, g, h ≤ n): the intersection the duo started from and the two intersections between which the duo has traveled, with g ≠ h.</li>
	<li>m lines with three space-separated integers a, b and d (1 ≤ a < b ≤ n and 1 ≤ d ≤ 1 000), indicating that there is a bidirectional road between intersections a and b of length d.</li>
	<li>t lines with one integer x (1 ≤ x ≤ n): the possible destinations. All possible destinations are distinct and they are all different from s.</li>
</ul>

<p>There is at most one road between a pair of intersections. One of the m lines describes the road between g and h. This road is guaranteed to be on a shortest path to at least one of the possible destinations.</p>

### 출력 

 <p>Per test case:</p>

<ul>
	<li>One line with one or more space-separated integers, indicating the destinations that the duo can still be headed for, in increasing order.</li>
</ul>

