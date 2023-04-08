# [Bronze III] Quick Change - 2720 

[문제 링크](https://www.acmicpc.net/problem/2720) 

### 성능 요약

메모리: 31256 KB, 시간: 64 ms

### 분류

Mathematics, Greedy, Arithmetic

### 문제 설명

<p>J.P. Flathead’s Grocery Store hires cheap labor to man the checkout stations. The people he hires (usually high school kids) often make mistakes making change for the customers. Flathead, who’s a bit of a tightwad, figures he loses more money from these mistakes than he makes; that is, the employees tend to give more change to the customers than they should get. </p>

<p>Flathead wants you to write a program that calculates the number of quarters (<span>$</span>0.25), dimes (<span>$</span>0.10), nickels (<span>$</span>0.05) and pennies (<span>$</span>0.01) that the customer should get back. Flathead always wants to give the customer’s change in coins if the amount due back is <span>$</span>5.00 or under. He also wants to give the customers back the smallest total number of coins. For example, if the change due back is <span>$</span>1.24, the customer should receive 4 quarters, 2 dimes, 0 nickels, and 4 pennies. </p>

### 입력 

 <p>The first line of input contains an integer N which is the number of datasets that follow. Each dataset consists of a single line containing a single integer which is the change due in cents, C, (1 ≤ C ≤ 500).</p>

### 출력 

 <p>For each dataset, print out the dataset number, a space, and the string: </p>

<pre>Q QUARTER(S), D DIME(S), n NICKEL(S), P PENNY(S) </pre>

<p>Where Q is he number of quarters, D is the number of dimes, n is the number of nickels and P is the number of pennies. </p>

