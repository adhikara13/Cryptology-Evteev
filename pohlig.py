# Helper for pohlig hellman
from tabulate import tabulate
import math
def inv(a, m) :
     
    m0 = m
    x0 = 0
    x1 = 1
 
    if (m == 1) :
        return 0
 
    # Apply extended Euclid Algorithm
    while (a > 1) :
        # q is quotient
        q = a // m
 
        t = m
 
        # m is remainder now, process
        # same as euclid's algo
        m = a % m
        a = t
 
        t = x0
 
        x0 = x1 - q * x0
 
        x1 = t
     
    # Make x1 positive
    if (x1 < 0) :
        x1 = x1 + m0
 
    return x1
def Chinese(num, rem) :
     
    # Compute product of all numbers
    prod = 1
    for i in range(0, len(num)) :
        prod = prod * num[i]
    print(f"Products of all result = a1 * a2 = {prod}") 
    # Initialize result
    result = 0
    # Apply above formula
    print("x = ", end = '')
    for i in range(0,len(num)):
        pp = prod // num[i]
        result = result + rem[i] * inv(pp, num[i]) * pp
        print(f"({rem[i]} * {pp} * {inv(pp, num[i])})", end = '+')
     
    print(f"mod {prod}")
    return result % prod
def printPFsInPairs(n):
    for i in range(1, int(pow(n, 1 / 2))+1):
        if n % i == 0:
            test.append([str(i) +"*"+str(int(n / i))])
            if i != 1 and int(n/i) != 1 and math.gcd(i , int(n/i)) == 1:
                return i, int(n/i)

def inver_pow(left, equal, p):
    res = 0
    while True:
        if pow(left,res,p) == equal:
            break
        res+=1
    return res

print("Log g^x = n mod p\nx = g^n mod p")
p = int(input("Input the p: "))
x = int(input("Input the x: "))
g = int(input("Input the g: "))

phi = p - 1
print(f"phi({p}) = {phi}")
test = []

a, b = printPFsInPairs(phi)
print(tabulate(test, headers=[f'Factors of {phi}'], stralign='center', tablefmt='outline'))
# For a
a0 = inver_pow(pow(g,b,p), pow(x,b,p), p)
print(f'''Пусть\nn = a0 + {a}a1
({g}^(a0+{a}a1))^{b} = {x}^{b} mod {p}
{g}^({b}a0+{a*b}a1) = {x}^{b} mod {p}
({g}^{b})^a0 * ({g}^a1)^{a*b} = {pow(x,b,p)} mod {p}
Due to congruency we can get rid of ({g}^a1)^{a*b}
({g}^{b})^a0 = {pow(x,b,p)} mod {p}
{pow(g,b,p)}^a0 = {pow(x,b,p)} mod {p}
a0 = {a0}
x = {a0} mod {a}''')
# For b
b0 = inver_pow(pow(g,a,p), pow(x,a,p), p)
print(f'''\nПусть\nn = a0 + {b}a1
({g}^(a0+{b}a1))^{a} = {x}^{a} mod {p}
{g}^({a}a0+{a*b}a1) = {x}^{a} mod {p}
({g}^{a})^a0 * ({g}^a1)^{a*b} = {pow(x,a,p)} mod {p}
Due to congruency we can get rid of ({g}^a1)^{a*b}
({g}^{a})^a0 = {pow(x,a,p)} mod {p}
{pow(g,a,p)}^a0 = {pow(x,a,p)} mod {p}
a0 = {b0}
x = {b0} mod {b}''')

print("\nChinese remainder theorem")
print(f'''x = {a0} mod {a}
x = {b0} mod {b}''')
num = [a, b]
rem = [a0, b0]
print(f"a1 = {a}, a2 = {b} - rem1 = {a0}, rem2 = {b0}")
print(f"The n or x (answer) is = {Chinese(num , rem)}")


