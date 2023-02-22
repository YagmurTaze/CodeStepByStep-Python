"""
1) z is odd : z % 2 != 0
2) z is not greater than y's square root : z <= math.sqrt(y)
3) y is positive : y > 0
4) Either x or y is even, and the other is odd : x % 2 != y % 2
5) y is a multiple of z : y % z == 0
6) z is not zero : z != 0
7) y is greater in magnitude than z : math.abs(y) > math.abs(z)
8) x and z are of opposite signs : x * z < 0
9) y is a nonnegative one-digit number : y == y % 10
10)z is nonnegative : z >= 0
11)x is even : x % 2 == 0
12)x is closer in value to y than z is : math.abs(x - y) < math.abs(z - y)
"""
