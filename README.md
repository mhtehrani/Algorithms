# Algorithms



Maximum Pairwise Product
========================
Find the maximum product of two distinct numbers in a sequence of non-negative integers.
Input: A sequence of non-negative integers.
Output: The maximum value that can be obtained by multiplying two different elements from the sequence.
Input format: The first line contains an integer 𝑛. The next line contains n non-negative integers a1, ..., an (separated by spaces).
Output format: The maximum pairwise product.
Constraints: 2 < 𝑛 < 2 *10^5; 0 < a1, ..., an < 2*10^5.



Fibonacci Number
================
Given an integer 𝑛, find the 𝑛th Fibonacci number 𝐹𝑛.
Input Format: The input consists of a single integer 𝑛.
Constraints: 0 ≤ 𝑛 ≤ 45.
Output Format: Output 𝐹𝑛.



Last Digit of a Large Fibonacci Number
======================================
Given an integer 𝑛, find the last digit of the 𝑛th Fibonacci number 𝐹𝑛 (that is, 𝐹𝑛 mod 10).
Input Format: The input consists of a single integer 𝑛.
Constraints: 0 ≤ 𝑛 ≤ 10^7.
Output Format: Output the last digit of 𝐹𝑛.



Greatest Common Divisor
=======================
Given two integers 𝑎 and 𝑏, find their greatest common divisor.
Input Format: The two integers 𝑎, 𝑏 are given in the same line separated by space.
Constraints: 1 ≤ 𝑎, 𝑏 ≤ 2 · 10^9.
Output Format: Output GCD(𝑎, 𝑏).



Least Common Multiple
=====================
Given two integers 𝑎 and 𝑏, find their least common multiple.
Input Format: The two integers 𝑎 and 𝑏 are given in the same line separated by space.
Constraints: 1 ≤ 𝑎, 𝑏 ≤ 10^7.
Output Format: Output the least common multiple of 𝑎 and 𝑏.




Fibonacci Number mode 𝑚
========================
Given two integers 𝑛 and 𝑚, output 𝐹𝑛 mod 𝑚 (that is, the remainder of 𝐹𝑛 when divided by 𝑚).
Input Format: The input consists of two integers 𝑛 and 𝑚 given on the same line (separated by a space).
Constraints: 1 ≤ 𝑛 ≤ 10^14, 2 ≤ 𝑚 ≤ 10^3.
Output Format: Output 𝐹𝑛 mod 𝑚.



Last Digit of the Sum of Fibonacci Numbers
==========================================
Given an integer 𝑛, find the last digit of the sum 𝐹0 + 𝐹1 + · · · + 𝐹𝑛.
Input Format: The input consists of a single integer 𝑛.
Constraints: 0 ≤ 𝑛 ≤ 10^14.
Output Format: Output the last digit of 𝐹0 + 𝐹1 + · · · + 𝐹𝑛.



Last Digit of the Sum of Fibonacci Numbers
==========================================
Given two non-negative integers 𝑚 and 𝑛, where 𝑚 ≤ 𝑛, find the last digit of the sum 𝐹𝑚 + 𝐹𝑚+1 + · · · + 𝐹𝑛.
Input Format: The input consists of two non-negative integers 𝑚 and 𝑛 separated by a space.
Constraints: 0 ≤ 𝑚 ≤ 𝑛 ≤ 10^14.
Output Format: Output the last digit of 𝐹𝑚 + 𝐹𝑚+1 + · · · + 𝐹𝑛.




Last Digit of the Sum of Squares of Fibonacci Numbers
=====================================================
Compute the last digit of 𝐹0^2 + 𝐹1^2 + · · · + 𝐹𝑛^2.
Input Format: Integer 𝑛.
Constraints: 0 ≤ 𝑛 ≤ 10^14.
Output Format: The last digit of 𝐹0^2 + 𝐹1^2 + · · · + 𝐹𝑛^2.



Money Change
============
Finding the minimum number of coins needed to change the input value (an integer) into coins with denominations 1, 5, and 10.
Input Format: The input consists of a single integer 𝑚.
Constraints: 1 ≤ 𝑚 ≤ 10^3.
Output Format: Output the minimum number of coins with denominations 1, 5, 10 that changes 𝑚.



Fractional Knapsack
===================
Input Format: The first line of the input contains the number 𝑛 of items and the capacity 𝑊 of a knapsack. The next 𝑛 lines define the values and weights of the items. The 𝑖-th line contains integers 𝑣𝑖 and 𝑤𝑖 — the value and the weight of 𝑖-th item, respectively.
Constraints: 1 ≤ 𝑛 ≤ 10^3, 0 ≤ 𝑊 ≤ 2*10^6; 0 ≤ 𝑣𝑖 ≤ 2*10^6, 0 < 𝑤𝑖 ≤ 2*10^6 for all 1 ≤ 𝑖 ≤ 𝑛. All the numbers are integers.
Output Format: Output the maximal value of fractions of items that fit into the knapsack.



Car Fueling
===========
the minimum number of refills needed to travel to another city that is located 𝑑 miles away. Your car can travel at most 𝑚 miles on a full tank and you start with a full tank. Along your way, there are gas stations at distances stop1, stop2, . . . , stop𝑛 from your home city.
Input Format: The first line contains an integer 𝑑. The second line contains an integer 𝑚. The third line specifies an integer 𝑛. Finally, the last line contains integers stop1, stop2, . . . , stop𝑛.
Output Format: The minimum number of refills needed. If it is not possible to reach the destination, output −1.
Constraints: 1 ≤ 𝑑 ≤ 10^5. 1 ≤ 𝑚 ≤ 400. 1 ≤ 𝑛 ≤ 300. 0 < stop1 < stop2 < · · · < stop𝑛 < 𝑑.



Maximum Number of Prizes
========================
The goal is to represent a given positive integer 𝑛 as a sum of as many pairwise distinct positive integers as possible. That is, to find the maximum 𝑘 such that 𝑛 can be written as 𝑎1 + 𝑎2 + · · · + 𝑎𝑘 where 𝑎1, . . . , 𝑎𝑘 are positive integers and 𝑎𝑖 ̸= 𝑎𝑗 for all 1 ≤ 𝑖 < 𝑗 ≤ 𝑘.
Input Format: The input consists of a single integer 𝑛.
Constraints: 1 ≤ 𝑛 ≤ 10^9.
Output Format: In the first line, output the maximum number 𝑘 such that 𝑛 can be represented as a sum of 𝑘 pairwise distinct positive integers. In the second line, output 𝑘 pairwise distinct positive integers that sum up to 𝑛.



Largest Number
==============
Composing the largest number out of the given single-digit numbers.
Input Format: The first line of the input contains integers 𝑎1, 𝑎2, . . . , 𝑎𝑛.
Constraints: 1 ≤ 𝑛 ≤ 100; 1 ≤ 𝑎𝑖 ≤ 10^3 for all 1 ≤ 𝑖 ≤ 𝑛.
Output Format: Output the largest number that can be composed out of 𝑎1, 𝑎2, . . . , 𝑎𝑛.



Binary Search
=============
The goal is to implement the binary search algorithm.
Input Format: The first line of the input contains an integer 𝑛 and a sequence 𝑎0 < 𝑎1 < . . . < 𝑎𝑛−1 of 𝑛 pairwise distinct positive integers in increasing order. The next line contains an integer 𝑘 and 𝑘 positive integers 𝑏0, 𝑏1, . . . , 𝑏𝑘−1.
Constraints: 1 ≤ 𝑘 ≤ 10^5; 1 ≤ 𝑛 ≤ 3*10^4; 1 ≤ 𝑎𝑖 ≤ 109 for all 0 ≤ 𝑖 < 𝑛; 1 ≤ 𝑏𝑗 ≤ 10^9 for all 0 ≤ 𝑗 < 𝑘;
Output Format: For all 𝑖 from 0 to 𝑘 − 1, output an index 0 ≤ 𝑗 ≤ 𝑛 − 1 such that 𝑎𝑗 = 𝑏𝑖 or −1 if there is no such index.



Majority Element
================
The goal is to check whether an input sequence contains a majority element, that is, repeated more than fifty percent.
Input Format: The first line contains an integer 𝑛, the next one contains a sequence of 𝑛 non-negative integers 𝑎0, 𝑎1, . . . , 𝑎𝑛−1.
Constraints: 1 ≤ 𝑛 ≤ 10^5; 0 ≤ 𝑎𝑖 ≤ 10^9 for all 0 ≤ 𝑖 < 𝑛.
Output Format: Output 1 if the sequence contains an element that appears strictly more than 𝑛/2 times, and 0 otherwise.



3-Way Quick Sort Algorithm
==========================
The goal is to replace a 2-way partition with a 3-way partition in quick sort algorithm. That is, the new partition procedure should partition the array into three parts: < 𝑥 part, = 𝑥 part, and > 𝑥 part.
Input Format: The first line of the input contains an integer 𝑛. The next line contains a sequence of 𝑛 integers 𝑎0, 𝑎1, . . . , 𝑎𝑛−1.
Constraints: 1 ≤ 𝑛 ≤ 10^5; 1 ≤ 𝑎𝑖 ≤ 10^9 for all 0 ≤ 𝑖 < 𝑛.
Output Format: Output this sequence sorted in non-decreasing order.



Number of Inversions
====================
An inversion of a sequence 𝑎0, 𝑎1, . . . , 𝑎𝑛−1 is a pair of indices 0 ≤ 𝑖 < 𝑗 < 𝑛 such that 𝑎𝑖 > 𝑎𝑗 . For example, a sorted (in non-descending order) sequence contains no inversions at all, while in a sequence sorted in descending order any two elements constitute an inversion (for a total of 𝑛(𝑛 − 1)/2 inversions).
The goal is to count the number of inversions of a given sequence.
Input Format: The first line contains an integer 𝑛, the next one contains a sequence of integers 𝑎0, 𝑎1, . . . , 𝑎𝑛−1.
Constraints: 1 ≤ 𝑛 ≤ 10^5, 1 ≤ 𝑎𝑖 ≤ 10^9 for all 0 ≤ 𝑖 < 𝑛.
Output Format: Output the number of inversions in the sequence.



Points and Segments
===================
Given a set of points on a line and a set of segments on a line, the goal is to compute, for each point, the number of segments that contain this point.
Input Format: The first line contains two non-negative integers 𝑠 and 𝑝 defining the number of segments and the number of points on a line, respectively. The next 𝑠 lines contain two integers 𝑎𝑖, 𝑏𝑖 defining the 𝑖-th segment [𝑎𝑖, 𝑏𝑖]. The next line contains 𝑝 integers defining points 𝑥1, 𝑥2, . . . , 𝑥𝑝.
Constraints: 1 ≤ 𝑠, 𝑝 ≤ 50000; −10^8 ≤ 𝑎𝑖 ≤ 𝑏𝑖 ≤ 10^8 for all 0 ≤ 𝑖 < 𝑠; −10^8 ≤ 𝑥𝑗 ≤ 10^8 for all 0 ≤ 𝑗 < 𝑝.
Output Format: Output 𝑝 non-negative integers 𝑘0, 𝑘1, . . . , 𝑘𝑝−1 where 𝑘𝑖 is the number of segments which contain 𝑥𝑖. More formally, 𝑘𝑖 = |{𝑗 : 𝑎𝑗 ≤ 𝑥𝑖 ≤ 𝑏𝑗}|.



Closet Points
=============
Given 𝑛 points on a plane, find the smallest distance between a pair of two (different) points.
Input Format: The first line contains the number 𝑛 of points. Each of the following 𝑛 lines defines a point (𝑥𝑖, 𝑦𝑖).
Constraints: 2 ≤ 𝑛 ≤ 10^5; −10^9 ≤ 𝑥𝑖, 𝑦𝑖 ≤ 10^9 are integers.
Output Format: Output the minimum distance.



Money Change (Dynamic Programming)
==================================
The goal is to apply dynamic programming for solving the Money Change Problem for denominations 1, 3, and 4.
Input Format: Integer money.
Output Format: The minimum number of coins with denominations 1, 3, 4 that changes money.
Constraints: 1 ≤ money ≤ 10^3.



Primitive Calculator (Dynamic Programming)
==========================================
Given an integer 𝑛, compute the minimum number of operations needed to obtain the number 𝑛 starting from the number 1 by performing the following three operations with the current number 𝑥: multiply 𝑥 by 2, multiply 𝑥 by 3, or add 1 to 𝑥.
Input Format: The input consists of a single integer 1 ≤ 𝑛 ≤ 10^6.
Output Format: In the first line, output the minimum number 𝑘 of operations needed to get 𝑛 from 1. In the second line output a sequence of intermediate numbers. That is, the second line would contain positive integers 𝑎0, 𝑎2, . . . , 𝑎𝑘−1 such that 𝑎0 = 1, 𝑎𝑘−1 = 𝑛 and for all 0 ≤ 𝑖 < 𝑘 − 1, 𝑎𝑖+1 is equal to either 𝑎𝑖 + 1, 2𝑎𝑖, or 3𝑎𝑖.



Edit Distance (Dynamic Programming)
===================================
The edit distance between two strings is the minimum number of operations (insertions, deletions, and substitutions of symbols) to transform one string into another. It is a measure of similarity of two strings. The goal is to implement the algorithm for computing the edit distance between two strings.
Input Format: Each of the two lines of the input contains a string consisting of lower case latin letters.
Constraints: The length of both strings is at least 1 and at most 100.
Output Format: Output the edit distance between the given two strings.



Longest Common Subsequence of Two Sequences (Dynamic Programming)
=================================================================
Given two sequences 𝐴 = (𝑎1, 𝑎2, . . . , 𝑎𝑛) and 𝐵 = (𝑏1, 𝑏2, . . . , 𝑏𝑚), finding the length of their longest common subsequence, i.e., the largest non-negative integer 𝑝 such that there exist indices 1 ≤ 𝑖1 < 𝑖2 < · · · < 𝑖𝑝 ≤ 𝑛 and 1 ≤ 𝑗1 < 𝑗2 < · · · < 𝑗𝑝 ≤ 𝑚, such that 𝑎𝑖1 = 𝑏𝑗1 , . . . , 𝑎𝑖𝑝 = 𝑏𝑗𝑝.
Input Format: First line: 𝑛. Second line: 𝑎1, 𝑎2, . . . , 𝑎𝑛. Third line: 𝑚. Fourth line: 𝑏1, 𝑏2, . . . , 𝑏𝑚.
Constraints: 1 ≤ 𝑛,𝑚 ≤ 100; −10^9 < 𝑎𝑖, 𝑏𝑖 < 10^9.
Output Format: Output 𝑝.



Longest Common Subsequence of Three Sequences (Dynamic Programming)
===================================================================
Given three sequences 𝐴 = (𝑎1, 𝑎2, . . . , 𝑎𝑛), 𝐵 = (𝑏1, 𝑏2, . . . , 𝑏𝑚), and 𝐶 = (𝑐1, 𝑐2, . . . , 𝑐𝑙), finding the length of their longest common subsequence, i.e., the largest non-negative integer 𝑝 such that there exist indices 1 ≤ 𝑖1 < 𝑖2 < · · · < 𝑖𝑝 ≤ 𝑛, 1 ≤ 𝑗1 < 𝑗2 < · · · < 𝑗𝑝 ≤ 𝑚, 1 ≤ 𝑘1 < 𝑘2 < · · · < 𝑘𝑝 ≤ 𝑙 such that 𝑎𝑖1 = 𝑏𝑗1 = 𝑐𝑘1 , . . . , 𝑎𝑖𝑝 = 𝑏𝑗𝑝 = 𝑐𝑘𝑝
Input Format: First line: 𝑛. Second line: 𝑎1, 𝑎2, . . . , 𝑎𝑛. Third line: 𝑚. Fourth line: 𝑏1, 𝑏2, . . . , 𝑏𝑚. Fifth line: 𝑙. Sixth line: 𝑐1, 𝑐2, . . . , 𝑐𝑙.
Constraints: 1 ≤ 𝑛, 𝑚, 𝑙 ≤ 100; −10^9 < 𝑎𝑖, 𝑏𝑖, 𝑐𝑖 < 10^9.
Output Format: Output 𝑝.



Knapsack without Repetitions (Dynamic Programming)
==================================================
Given 𝑛 items, find the maximum weight of items fits into a bag of capacity 𝑊.
Input Format: The first line of the input contains the capacity 𝑊 of a knapsack and the number 𝑛 of items of similar value. The next line contains 𝑛 integers 𝑤0,𝑤1, . . . ,𝑤𝑛−1 defining the weights of the items.
Constraints: 1 ≤ 𝑊 ≤ 10^4; 1 ≤ 𝑛 ≤ 300; 0 ≤ 𝑤0, . . . ,𝑤𝑛−1 ≤ 10^5.
Output Format: Output the maximum weight of gold that fits into a knapsack of capacity 𝑊.


Partitioning (Dynamic Programming)
==================================
The goal is to evenly split all the items with different values into three subsets with equal sums.
Problem Description
Input Format: The first line contains an integer 𝑛. The second line contains integers 𝑣1, 𝑣2, . . . , 𝑣𝑛 separated by spaces.
Constraints: 1 ≤ 𝑛 ≤ 20, 1 ≤ 𝑣𝑖 ≤ 30 for all 𝑖.
Output Format: Output 1, if it possible to partition 𝑣1, 𝑣2, . . . , 𝑣𝑛 into three subsets with equal sums, and 0 otherwise.



Maximum Value of an Arithmetic Expression (Dynamic Programming)
===============================================================
Finding the maximum value of an arithmetic expression by specifying the order of applying its arithmetic operations using additional parentheses.
Input Format: The only line of the input contains a string 𝑠 of length 2𝑛 + 1 for some 𝑛, with symbols 𝑠0, 𝑠1, . . . , 𝑠2𝑛. Each symbol at an even position of 𝑠 is a digit (that is, an integer from 0 to 9) while each symbol at an odd position is one of three operations from {+,-,*}.
Constraints: 0 ≤ 𝑛 ≤ 1000.
Output Format: Output the maximum possible value of the given arithmetic expression among different orders of applying arithmetic operations.
