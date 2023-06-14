def point_addition(P1, P2, p, a):
    (x1, y1), (x2, y2) = P1, P2
    if P1 == P2:
        lam = (3 * x1 * x1 + a) * pow(2 * y1, p - 2, p)
        print(f"Вычисление лямбда (λ) для сложения точек:")
        print(f"λ = (3 * {x1}^2 + {a}) * (2 * {y1})^({p} - 2) mod {p}")
        print(f"   = {lam}")
    else:
        lam = (y2 - y1) * pow(x2 - x1, p - 2, p)
        print(f"Вычисление лямбда (λ) для сложения точек:")
        print(f"λ = ({y2} - {y1}) * ({x2} - {x1})^({p} - 2) mod {p}")
        print(f"   = {lam}")

    x3 = (lam**2 - x1 - x2) % p
    print(f"Вычисление x-координаты результирующей точки:")
    print(f"x3 = λ^2 - {x1} - {x2} mod {p}")
    print(f"   = {x3}")

    y3 = (lam*(x1 - x3) - y1) % p
    print(f"Вычисление y-координаты результирующей точки:")
    print(f"y3 = λ * ({x1} - {x3}) - {y1} mod {p}")
    print(f"   = {y3}")

    return (x3, y3)


def point_multiplication(P, n, p, a):
    Q = P
    R = None
    i = 1
    while n > 0:
        if n & 1:
            if R is None:
                R = Q
                print(f"Установка R = Q = {Q}")
            else:
                R = point_addition(Q, R, p, a)
                print(f"Вычисление сложения точек Q и R:")
                print(f"R = Q + R = {Q} + {R} = R = {R}")

        if n - 1 != 0:
            Q = point_addition(Q, Q, p, a)
            print(f"Вычисление удвоения точки Q:")
            print(f"Q = 2Q = {Q}")

        n >>= 1
        i += 1

        if n == 0:
            break

    print("Умножение точек завершено.")
    print(f"Результирующая точка R = {R}")
    return R

def modular_inverse(n, p):
    return pow(n, p - 2, p)

p = int(input("Введите модуль p: "))
a = int(input("Введите коэффициент a уравнения эллиптической кривой: "))
b = int(input("Введите коэффициент b уравнения эллиптической кривой: "))
Gx = int(input("Введите x-координату базовой точки G: "))
Gy = int(input("Введите y-координату базовой точки G: "))
G = (Gx, Gy)
n = int(input("Введите порядок базовой точки G: "))
d = int(input("Введите секретный ключ d: "))
k = int(input("Введите случайное число k: "))
z = int(input("Введите хэш сообщения z: "))
print("------------------------")
print(f"Открытый ключ Q = dG = {d}*{G}")
Q = point_multiplication(G, d, p, a)
print(f"Q = {Q}")
print("------------------------")
print(f"Точка R = kG = {k}*{G}")
R = point_multiplication(G, k, p, a)
print(f"R = {R}")
print("------------------------")
r = R[0] % n
if r == 0:
    print('r = 0, выберите другое k')
else:
    print(f"Компонента подписи r = x-координата R mod n = {R[0]} mod {n} = {r}")
    s = (modular_inverse(k, n) * (z + r * d)) % n
    if s == 0:
        print('s = 0, выберите другое k')
    else:
        print(f"Компонента подписи s = (1/k) * (z + r*d) mod n = (1/{k}) * ({z} + {r}*{d}) mod {n} = {s}")
        print('Подпись:', (r, s))
