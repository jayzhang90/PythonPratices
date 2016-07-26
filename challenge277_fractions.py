'''

A fraction exists of a numerator (top part) and a denominator (bottom part) as you probably all know.
Simplifying (or reducing) fractions means to make the fraction as simple as possible. Meaning that the denominator is a
close to 1 as possible. This can be done by dividing the numerator and denominator by their greatest common divisor.


'''

def gcd(a, b):
    while b:
        a, b = b, a%b
    return a

def f(x, y):
    gcd_x_y = gcd(x, y)
    return x // gcd_x_y, y // gcd_x_y