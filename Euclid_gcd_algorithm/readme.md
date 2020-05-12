#Euclidian GCD Algorithm
- returns the greatest common divisor of two numbers.

Ex- gcd(1701, 3768)
first will pick the greater of two
`3768 = 1701.quotient + remainder` --> `3768 = 1701.2 + 366`
Replace 3768 with 1701 and 1701 with remainder
`1701 = 366.quotient + remainder`
Till we reach to the remainder as 0, the remainder before that is our gcd.

###Follow up:

3768 = 1701.2 + 366
1701 = 366.4 + 237
366 = 237.1 + 129
237 = 129.1 + 108
129 = 108.1 + 21
108 = 21.5 + 3
21 = 3.7 + 0

### gcd(1701, 3768) --> 3
