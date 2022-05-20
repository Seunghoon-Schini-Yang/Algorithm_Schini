# [Platinum IV] 시계 사진들 - 10266 

[문제 링크](https://www.acmicpc.net/problem/10266) 

### 성능 요약

메모리: 57192 KB, 시간: 416 ms

### 분류

KMP(kmp), 문자열(string)

### 문제 설명

<p>You have two pictures of an unusual kind of clock. The clock has n hands, each having the same length and no kind of marking whatsoever. Also, the numbers on the clock are so faded that you can’t even tell anymore what direction is up in the picture. So the only thing that you see on the pictures, are n shades of the n hands, and nothing else.</p>

<p>You’d like to know if both images might have been taken at exactly the same time of the day, possibly with the camera rotated at different angles.</p>

<p>Given the description of the two images, determine whether it is possible that these two pictures could be showing the same clock displaying the same time.</p>

### 입력 

 <p>The first line contains a single integer n (2 ≤ n ≤ 200 000), the number of hands on the clock.</p>

<p>Each of the next two lines contains n integers ai (0 ≤ a<sub>i</sub> < 360 000), representing the angles of the hands of the clock on one of the images, in thousandths of a degree. The first line represents the position of the hands on the first image, whereas the second line corresponds to the second image. The number a<sub>i</sub> denotes the angle between the recorded position of some hand and the upward direction in the image, measured clockwise. Angles of the same clock are distinct and are not given in any specific order.</p>

### 출력 

 <p>Output one line containing one word: possible if the clocks could be showing the same time, impossible otherwise.</p>

