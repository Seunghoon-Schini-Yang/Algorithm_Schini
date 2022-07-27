# [Platinum IV] 축구 전술 - 3977 

[문제 링크](https://www.acmicpc.net/problem/3977) 

### 성능 요약

메모리: 67468 KB, 시간: 1828 ms

### 분류

그래프 이론(graphs), 강한 연결 요소(scc)

### 문제 설명

<p>World Soccer Championship is coming soon and coach Yogi wants to prepare his team as well as possible. So he made up a strategy field plan for every player of the team. One plan describes a number of possible locations for the player on the field. Moreover, if Yogi wants the player to be able to move from one location A to another location B then the plan specifies the ordered pair (A, B). He is sure that his team will win if the players run over the field from one location to another using only moves of the plan.</p>

<p><img alt="" src="https://www.acmicpc.net/upload/images2/field(1).png" style="float:right; height:124px; width:188px">Yogi tells every player to follow his plan and to start from a location that reaches every other location on the plan (by possibly multiple moves). However, it is quite difficult for some soccer players, simple minded as they are, to find a suitable starting location. Can you help every player to figure out the set of possible start locations?</p>

### 입력 

 <p>The first line gives the number of field plans. The input contains at most eleven field plans (what else?). Every plan starts with a line of two integers N and M, with 1 ≤ N ≤ 100 000 and 1 ≤ M ≤ 100 000, giving the number of locations and the number of moves. In the following M lines a plan specifies moves (A, B) by two white space separated integers 0 ≤ A, B < N. The plans are separated by a blank line.</p>

### 출력 

 <p>For every plan print out all possible starting locations, sorted increasingly and one per line. If there are no possible locations to start, print “Confused”. Print a blank line after each plan output.</p>

