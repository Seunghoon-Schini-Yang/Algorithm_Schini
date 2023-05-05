# [Gold III] 트리 복구 - 6597 

[문제 링크](https://www.acmicpc.net/problem/6597) 

### 성능 요약

메모리: 31256 KB, 시간: 44 ms

### 분류

분할 정복, 그래프 이론, 그래프 탐색, 재귀, 트리

### 문제 설명

<p>Little Valentine liked playing with binary trees very much. Her favorite game was constructing randomly looking binary trees with capital letters in the nodes. </p>

<p>This is an example of one of her creations:</p>

<pre>                                               D
                                              / \
                                             /   \
                                            B     E
                                           / \     \
                                          /   \     \
                                         A     C     G
                                                    /
                                                   /
                                                  F</pre>

<p>To record her trees for future generations, she wrote down two strings for each tree: a preorder traversal (root, left subtree, right subtree) and an inorder traversal (left subtree, root, right subtree). For the tree drawn above the preorder traversal is DBACEGF and the inorder traversal is ABCDEFG. </p>

<p>She thought that such a pair of strings would give enough information to reconstruct the tree later (but she never tried it).</p>

<p>Now, years later, looking again at the strings, she realized that reconstructing the trees was indeed possible, but only because she never had used the same letter twice in the same tree. </p>

<p>However, doing the reconstruction by hand, soon turned out to be tedious. </p>

<p>So now she asks you to write a program that does the job for her!</p>

### 입력 

 <p>The input file will contain one or more test cases. </p>

<p>Each test case consists of one line containing two strings preord and inord, representing the preorder traversal and inorder traversal of a binary tree. Both strings consist of unique capital letters. (Thus they are not longer than 26 characters.)</p>

<p>Input is terminated by end of file.</p>

### 출력 

 <p>For each test case, recover Valentine's binary tree and print one line containing the tree's postorder traversal (left subtree, right subtree, root)</p>

<p> </p>

