# [Gold I] 용이 산다 - 3430 

[문제 링크](https://www.acmicpc.net/problem/3430) 

### 성능 요약

메모리: 332368 KB, 시간: 4464 ms

### 분류

자료 구조, 그리디 알고리즘, 우선순위 큐, 트리를 사용한 집합과 맵

### 문제 설명

<p>The capital of Ardenia is surrounded by several lakes, and each of them is initially full of water. Currently, heavy rainfalls are expected over the land. Such a rain falls to one of the lakes: if the lake is dry and empty, then it will be filled with water; if the lake is already full, then it will overflow, which will result in a natural disaster. Fortunately, the citizens have a dragon at their disposal (and they will not hesitate to use it). The dragon may drink the whole water from a lake in one sitting. Also, the mages of Ardenia already predicted the weather conditions for the next couple of years. The only question is: from which lake and when should the dragon drink to prevent a catastrophe?</p>

<p>The input contains several test cases. The first line of the input contains a positive integer Z ≤ 40, denoting the number of test cases. Then Z test cases follow, each conforming to the format described in section Input. For each test case, your program has to write an output conforming to the format described in section Output.</p>

### 입력 

 <p>The first line of the input instance contains two space-separated positive integers n ≤ 10<sup>6</sup> and m ≤ 10<sup>6</sup>, where n is the number of lakes. (There are at most 10 input instances for which n ≥ 10<sup>5</sup> or m ≥ 10<sup>5</sup>.) The second line contains the weather forecast for the next m days: m space-separated integers t<sub>1</sub>, t<sub>2</sub>, ... , t<sub>m</sub> (t<sub>i</sub> ∈ [0, n]). If t<sub>i</sub> ∈ [1, n], it means a heavy rainfall over lake t<sub>i</sub> at day i. If t<sub>i</sub> = 0, there is no rain at day i, and the dragon has the time to drink the water from one lake of your choice. Note that the dragon does not drink on a rainy day.</p>

### 출력 

 <p>In the first line your program should output word YES if it is possible to prevent a catastrophic overflow and NO otherwise. In the former case, you should output the second line containing ℓ integers from the range [0, n], where ℓ is the number of zeros in the weather forecast description, i.e., the number of non-rainy days. Each of these integers denotes the number of the lake from which the dragon should drink; zero means the dragon should not drink from any lake (this might be necessary, as even the dragon cannot drink from an empty lake).</p>

