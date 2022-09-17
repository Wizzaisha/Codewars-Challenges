import math

def is_square(n):
    if n < 0:
        return False
    else:
        if math.sqrt(n)%1 == 0:
            return True
        else:
            return False

n1 = -1
n2 = 0
n3 = 3
n4 = 4
n5 = 25
n6 = 26


print(is_square(n1))
print(is_square(n2))
print(is_square(n3))
print(is_square(n4))
print(is_square(n5))
print(is_square(n6))