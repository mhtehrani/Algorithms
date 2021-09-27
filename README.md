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













