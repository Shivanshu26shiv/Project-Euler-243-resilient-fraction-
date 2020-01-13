# Project-Euler-243-resilient-fraction
Brief description is present at https://projecteuler.net/problem=243 . 
Given rep is my 2 cents on this problem involving both computational and mathematical logic.

<p><q>
As per description, "A positive fraction whose numerator is less than its denominator is called a proper fraction.
For any denominator, d, there will be d−1 proper fractions; for example, with d = 12:
1/12 , 2/12 , 3/12 , 4/12 , 5/12 , 6/12 , 7/12 , 8/12 , 9/12 , 10/12 , 11/12 .

We shall call a fraction that cannot be cancelled down a resilient fraction.
Furthermore we shall define the resilience of a denominator, R(d), to be the ratio of its proper fractions that are resilient; for example, R(12) = 4/11 .
In fact, d = 12 is the smallest denominator having a resilience R(d) < 4/10 .

Find the smallest denominator d, having a resilience R(d) < 15499/94744 ."
</q></p>

Using code <b>list_resilient.py</b> you can list minimum resilience. 
After playing around with numbers and relevant functions, I observed that pattern in the rate at which minimum resilient integer were increasing.
Min resilience in observed in this series: 4, 6, 12, 18, 24, 30, 60... which was https://oeis.org/A060735 (numbers k at which k / (phi(k) + 1) increases)

Ignoring 4, 6 from the start, if we subtract as:

R  = 12, 18, 24, 30, 60...
R1 =     12, 18, 24, 30, 60...
R-R1 =    6, 6, 6, 6, 30, 30, 30, 30, 30, 30, 210, ...

Verbosing,

R-R1 = 4 times 6, 6 times 30, 10 times 210, 12 times 2310 and so on.

After comparing above and more than 100 resilience values, I observed that given pattern, 
4, 6, 10, 12, 16, 18, 22, 28, 30, 36... matches exactly with https://oeis.org/A006093 which is 	a(n) = prime(n) - 1.

So far that's it. My goal is to predict next resilience values based on previous input.
Will update post new findings.
