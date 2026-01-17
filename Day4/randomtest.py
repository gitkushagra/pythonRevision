import random
import secrets
a = random.seed(3)
b = random.getstate()
c = random.randbytes(2)
d = secrets.token_bytes(2)
e = random.random() #prints between 0.0 and 1.0 (including 0.0 but not including 1.0)
f = random.uniform(1, 10) #prints between 1 and 10 (including both)
g = random.randint(1, 10) #prints between 1 and 10 (including both)
h = random.choice(['apple', 'banana', 'cherry']) #prints a random choice from the list
for i in range(10):
    print(i)