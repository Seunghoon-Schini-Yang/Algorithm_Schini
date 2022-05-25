# [Platinum III] 디지털 비디오 디스크(DVDs) - 9345 

[문제 링크](https://www.acmicpc.net/problem/9345) 

### 성능 요약

메모리: 169600 KB, 시간: 1440 ms

### 분류

자료 구조(data_structures), 세그먼트 트리(segtree)

### 문제 설명

<p>DVD Rental shops are disappearing because of online video streaming. However, a very popular series has just been released and the shops are hoping that this series will boost their popularity. This series consists of n DVDs (numbered from 0 to N-1). </p>

<p>You own a rental shop and have a specific shelf for this series. There are N slots in this shelf (numbered from 0 to N-1 as well). When you first get this series, you place the DVD number i into the slot number i, obviously. A customer who is a fan of this series will want to rent a sequence of DVDs numbered l to r. Knowing that you have a shelf for this series, the customer will just pick up all DVDs from slot l to r, without checking the actual index of the DVDs.</p>

<p>However, there is one crazy customer who comes into your shop just to swap two DVDs in the slots, i.e., this customer takes a DVD from the slot a and exchanges it with the DVD in the slot b. This causes lots of problems for normal customers since normal customer do not check the index of the DVDs. For no reason, this crazy customer comes to your shop quite often and you don't have enough time to chase him away.</p>

<p>Your task is to write a program that monitors the activities in this shop and indicates whether a renting customer actually get the DVDs she wants, i.e., the customer actually get the DVDs numbered l to r. Be noted that the DVDs may be in any order, we just want to know if the customer get the DVDs numbered l to r. For example, let us assume that a customer comes to get DVDs from slot 2 to 4 and the slot 2, 3 and 4 have DVDs numbered 4, 2, and 3, respectively, we will say that the customer get what she wants.</p>

<p>For simplicity, we will assume that when a customer rents the DVDs, she will immediately watch all of it and place it back into the same slot they are taken. In other words, renting DVDs has no effect on the position of the DVDs at all. </p>

### 입력 

 <p>First line of input is a number of test cases T ≤ 20. </p>

<p>The first line of each test case contains two integer N and K (1 ≤ N ≤ 100 000, 1 ≤ K ≤ 50 000) which gives the number of DVDs and the number of activities that happens in the shops, respectively. </p>

<p>Following K lines describes the activities in the shop in the order that they happen. Each line contains three integers q, a and b (q is either 0 or 1 and 0 ≤ a ≤ b < N) </p>

<p>When q is 0, the activity is that a crazy customer comes in to swap DVDs in the slot number a and b. </p>

<p>When q is 1, a renting activity happens. A normal customer who needs DVD numbered a to b comes in and get DVDs from slot a to b. As noted earlier, this customer immediately uses the DVDs and returns it to the same slot (there is no change to the DVDs for this activity). </p>

### 출력 

 <p>For each renting activity, display a line with a word “YES” when the customer gets what she wants, i.e., when slot a to b have DVDs numbered a to b, and display a word “NO” in any other case.</p>

