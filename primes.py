import sys
from sympy import *

num =int(sys.argv[1])
prime = 2

for i in range(num):
    print(prime)
    prime = prime + 1
    while(not (isprime(prime))):
        prime = prime + 1
