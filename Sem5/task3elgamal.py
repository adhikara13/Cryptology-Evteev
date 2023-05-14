def point_addition(P1, P2, p, a):
    (x1, y1), (x2, y2) = P1, P2
    if P1 == P2:
        lam = (3 * x1 * x1 + a) * pow(2 * y1, p - 2, p)
    else:
        lam = (y2 - y1) * pow(x2 - x1, p - 2, p)
    x3 = (lam**2 - x1 - x2) % p
    y3 = (lam*(x1 - x3) - y1) % p
    return (x3, y3)

def point_multiplication(P, n, p, a):
    Q = P
    R = None
    while n > 0:
        if n & 1:
            if R is None:
                R = Q
            else:
                R = point_addition(Q, R, p, a)
        Q = point_addition(Q, Q, p, a)
        n >>= 1
    return R

def modular_inverse(n, p):
    return pow(n, p - 2, p)

p = int(input("Введите число p: "))
a = int(input("Введите число a: "))
b = int(input("Введите число b: "))
G = tuple(map(int, input("Введите точку G (формат: x,y): ").split(',')))
n = int(input("Введите число n: "))
Q = tuple(map(int, input("Введите открытый ключ Q (формат: x,y): ").split(',')))
z = int(input("Введите хэш-свертку сообщения z: "))
r, s = map(int, input("Введите подпись (формат: r,s): ").split(','))

if not (1 <= r <= n - 1) or not (1 <= s <= n - 1):
    print("Подпись недействительна.")
else:
    w = modular_inverse(s, n)
    print(f"w = s^(-1) mod n = {s}^(-1) mod {n} = {w}")
    
    u1 = (z * w) % n
    print(f"u1 = z*w mod n = {z}*{w} mod {n} = {u1}")
    
    u2 = (r * w) % n
    print(f"u2 = r*w mod n = {r}*{w} mod {n} = {u2}")
    
    P1 = point_multiplication(G, u1, p, a)
    print(f"P1 = u1*G = {u1}*{G} = {P1}")
    
    P2 = point_multiplication(Q, u2, p, a)
    print(f"P2 = u2*Q = {u2}*{Q} = {P2}")
    
    P = point_addition(P1, P2, p, a)
    print(f"P = P1 + P2 = {P1} + {P2} = {P}")
    
    if r % n == P[0] % n:
        print("r % n == P[0] % n")
        print(f"{r} % {n} == {P[0]} % {n}")
        print("Подпись действительна.")
    else:
        print("Подпись недействительна.")
