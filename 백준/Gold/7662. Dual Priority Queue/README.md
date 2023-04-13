# [Gold IV] Dual Priority Queue - 7662 

[문제 링크](https://www.acmicpc.net/problem/7662) 

### 성능 요약

메모리: 178656 KB, 시간: 4128 ms

### 분류

Data Structures, Set / Map By Trees, Priority Queue

### 문제 설명

<p>A dual priority queue is a data structure in which we can insert and delete data like a typical queue. Its difference from a typical queue is that when an item is to be deleted from the queue either an item with highest priority or with lowest priority in it is deleted according to the operation for deletion. There are two operations for the dual priority queue, one for inserting an item into it, the other for deleting an item from it. Deletion operation itself has two parameters: one for deleting an item with highest priority from it, and the other for deleting an item with lowest priority. </p>

<p>Suppose there is a dual priority queue Q which stores integers only. The value of each integer in Q is considered the priority of itself. </p>

<p>Given a list of operations, write a program that processes the operations for Q and shows the minimum and maximum numbers in Q after finishing the operations. </p>

### 입력 

 <p>Your program is to read from standard input. The input consists of T test cases. The number of test cases T is given in the first line of the input. Each test case starts with a line containing an integer k (k ≤ 1,000,000), the number of operations for Q. In the next k lines, each line contains either ‘D’ or ‘I’ followed by an integer n. Operation ‘I n’ means inserting integer n into Q. Note that the same integers can be inserted into Q. Operation ‘D 1’ means deleting the maximum number from Q. While Operation ‘D -1’ is used to delete the minimum number from Q. If there are two or more maxima (minima) in Q when the operation is ‘D 1’(‘D -1’), only one of them is deleted. </p>

<p>If Q is empty when the operation is ‘D’ you can ignore it. Each input to be inserted into Q is a 32-bit integer. </p>

### 출력 

 <p>Your program is to write to standard output. For each test case, print the maximum and the minimum numbers among those which remain in Q. The two numbers should be printed in a line separated by a blank. If Q is empty at the end, print ‘EMPTY’. </p>

