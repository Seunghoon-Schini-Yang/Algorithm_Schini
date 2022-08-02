# [Platinum III] 아이돌 - 3648 

[문제 링크](https://www.acmicpc.net/problem/3648) 

### 성능 요약

메모리: 37016 KB, 시간: 352 ms

### 분류

2-sat(2_sat), 그래프 이론(graphs), 강한 연결 요소(scc)

### 문제 설명

<p>Karl is competing in the preliminary round of a talent show called North-Western European Idol (NWEI), and wants to advance to the next round: World Idol. In the talent show, each contestant gets 10 minutes to impress the judges. After all the contestants have performed, each of the judges will cast two distinct votes. A vote can be either in favour of a contestant (meaning this contestant should advance) or against a contestant (meaning this contestant should not advance). The number of contestants that advance to the next round is not known in advance; if there are only very bad contestants, then it is possible that nobody will advance, or if everybody is amazing, then everybody may advance.</p>

<p>Karl is afraid that the judges will not appreciate his programming talents, and hence wants to use his other talent to advance to the next round: hacking. Having gained access to the jury system, Karl is capable of overriding the regular process of counting votes, and instead selecting exactly which contestants advance to the next round. The only problem is, he has to be careful not to arouse suspicion.</p>

<p>Each judge expects that at least one of his (or her) own two votes corresponds to the outcome of the contest. If the outcome contradicts both votes, the judge becomes alarmed. As an example, assume judge Harry casts a vote in favour of Pete and a vote against Sally. If Sally advances and Pete does not, judge Harry will be alarmed and may discover Karl’s tampering with the system.</p>

<p>Since Karl’s programming talents are limited (otherwise he would not have needed his hacking talents), he needs you to make a program that ﬁnds out if there is a set of contestants, which includes himself, that he can select to advance to the next round by hacking the jury system, such that it does not alarm any of the judges.</p>

### 입력 

 <p>For each test case, the input is as follows:</p>

<ul>
	<li>One line containing two positive integers: the number of contestants n (2 ≤ n < 1000) and the number of judges m (1 ≤ m < 2000).</li>
	<li>m lines containing the votes of each judge. Each of these line contains two integers: the numbers a (1 ≤ |a| ≤ n), and b (1 ≤ |b| ≤ n), the two votes of this judge (|a| ≠ |b|). A vote x < 0 means that the vote is against advancement of contestant |x|. A vote x > 0 means that the vote is in favour of contestant |x|.</li>
</ul>

<p>Contestants are numbered 1 ... n.</p>

<p>Karl is contestant 1.</p>

### 출력 

 <p>For each test case, print one line of output containing the word ‘yes’ if there is a set of contestants that advances to the next round that includes Karl, and does not alarm any of the judges. If there is no such set of contestants, the line should contain ‘no’.</p>

