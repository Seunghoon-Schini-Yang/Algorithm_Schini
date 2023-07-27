# [Platinum V] 거의 최단 경로 - 5719 

[문제 링크](https://www.acmicpc.net/problem/5719) 

### 성능 요약

메모리: 34348 KB, 시간: 240 ms

### 분류

데이크스트라, 그래프 이론, 그래프 탐색

### 문제 설명

<p>Finding the shortest path that goes from a starting point to a destination point given a set of points and route lengths connecting them is an already well known problem, and it’s even part of our daily lives, as shortest path programs are widely available nowadays.</p>

<p>Most people usually like very much these applications as they make their lives easier. Well, maybe not that much easier.</p>

<p>Now that almost everyone can have access to GPS navigation devices able to calculate shortest paths, most routes that form the shortest path are getting slower because of heavy traﬃc. As most people try to follow the same path, it’s not worth it anymore to follow these directions.</p>

<p>With this in his mind, your boss asks you to develop a new application that only he will have access to, thus saving him time whenever he has a meeting or any urgent event. He asks you that the program must answer not the shortest path, but the almost shortest path. He deﬁnes the almost shortest path as the shortest path that goes from a starting point to a destination point such that no route between two consecutive points belongs to any shortest path from the starting point to the destination.</p>

<p>For example, suppose the ﬁgure below represents the map given, with circles representing location points, and lines representing direct, one-way routes with lengths indicated. The starting point is marked as S and the destination point is marked as D. The bold lines belong to a shortest path (in this case there are two shortest paths, each with total length 4). Thus, the almost shortest path would be the one indicated by dashed lines (total length 5), as no route between two consecutive points belongs to any shortest path. Notice that there could exist more than one possible answer, for instance if the route with length 3 had length 1. There could exist no possible answer as well.</p>

<p><img alt="" src="https://www.acmicpc.net/upload/images/almost.png" style="height:174px; width:265px"></p>

### 입력 

 <p>The input contains several test cases. The ﬁrst line of a test case contains two integers N (2 ≤ N ≤ 500) and M (1 ≤ M ≤ 10<sup>4</sup>), separated by a single space, indicating respectively the number of points in the map and the number of existing one-way routes connecting two points directly. Each point is identiﬁed by an integer between 0 and N − 1. The second line contains two integers S and D, separated by a single space, indicating respectively the starting and the destination points (S ≠ D; 0 ≤ S, D < N). Each one of the following M lines contains three integers U, V and P (U ≠ V ; 0 ≤ U, V < N; 1 ≤ P ≤ 10<sup>3</sup>), separated by single spaces, indicating the existence of a one-way route from U to V with distance P. There is at most one route from a given point U to a given point V , but notice that the existence of a route from U to V does not imply there is a route from V to U, and, if such road exists, it can have a diﬀerent length. The end of input is indicated by a line containing only two zeros separated by a single space.</p>

### 출력 

 <p>For each test case in the input, your program must print a single line, containing -1 if it is not possible to match the requirements, or an integer representing the length of the almost shortest path found.</p>

