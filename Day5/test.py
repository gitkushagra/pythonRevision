import math
def is_prime(num):
    if num <= 1:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    for check in range(3, math.isqrt(num)+1, 2):
        if num % check == 0:
            return False
    return True
    
print(is_prime(29))
print(is_prime(15))
print(is_prime(2))
print(is_prime(1))
print(is_prime(37))
print(is_prime(100))
print(is_prime(97)) 


for i in range(1, 21,3):
    print(f"{i}: {is_prime(i)}")