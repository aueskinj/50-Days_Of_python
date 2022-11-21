from math import sqrt

def divide_or_square(n):
    if (n%5 == 0):
        print(sqrt(n))
    else:
        print(n%5)




divide_or_square(10)
