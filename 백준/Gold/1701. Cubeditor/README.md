# [Gold III] Cubeditor - 1701 

[문제 링크](https://www.acmicpc.net/problem/1701) 

### 성능 요약

메모리: 31256 KB, 시간: 2208 ms

### 분류

KMP, 문자열

### 문제 설명

<p><img alt="" src="https://www.acmicpc.net/upload/images/editor(1).png" style="float:right; height:195px; width:304px">Mr. Kim is a professional programmer. Recently he wants to design a new editor which has as many functions as possible. Most editors support a simple search function that finds one occurrence (or all occurrences successively) of a query pattern string in the text. </p>

<p>He observed that the search function in commercial editors does nothing if no query pattern is given. His idea of a new search function regards each substring of the given text as a query pattern string itself and his new function finds another occurrence in the text. The problem is that there can be occurrences of many substrings in the text. So, Mr. Kim decides that the new function finds only occurrences of the longest substring in the text in order to remedy the problem. A formal definition of the search function is as follows: </p>

<p>Given a text string S, find the longest substring in text string S such that the substring appears at least twice. The two occurrences are allowed to overlap. </p>

### 입력 

 <p>Your program is to read from standard input. A text string S is given in one line. The length of S is less than or equal to 5,000 and the alphabet ∑ is the set of lowercase English characters. </p>

### 출력 

 <p>Your program is to write to standard output. Print the length of the longest substring in text string S such that the substring appears at least twice. </p>

