from math import ceil, sqrt 
from sympy.ntheory.primetest import is_square
from tabulate import tabulate
def FermatPrime(Num):
    a = ceil(sqrt(Num))
    table = []
    while True:
        b = pow(a,2) - Num
        table.append([f"{a}^2({pow(a,2)}) - {Num} = {b}"])
        if is_square(b):
            break
        a += 1
    return a, int(sqrt(b)), table

User = int(input("Insert the number that need to be tested: "))
a , b , table= FermatPrime(User)
print(f"√{User} = |{sqrt(User)}| = {ceil(sqrt(User))}")
print(tabulate(table, headers=['a^2 - n = b'],tablefmt="outline"))
print(f"a = {a} , b = {b}")
print(f"Factors: p = {a}+{b} = {a+b} , the q = {a}-{b} = {a-b}")
if a+b == 1 or a-b ==1:
    print(f"The number {User} is a prime number")    
else:
    print(f"Since we found the factors, that means the number {User} isn't a prime")
