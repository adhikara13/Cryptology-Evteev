from sympy import mod_inverse

# Запросить у пользователя ввод
P = int(input("Введите модуль P: "))
alpha = int(input("Введите образующее α: "))
a = int(input("Введите секретный ключ a: "))
X = int(input("Введите сообщение X: "))
r = int(input("Введите случайное число r: "))

# Вычислить открытый ключ
b = pow(alpha, a, P)
print(f"b = α^a mod P = {alpha}^{a} mod {P} = {b}")

# Вычислить подпись
y1 = pow(alpha, r, P)
print(f"y1 = α^r mod P = {alpha}^{r} mod {P} = {y1}")

k = mod_inverse(r, P-1)
print(f"k - обратный элемент к r по модулю (P-1) = {r} mod {P-1} = {k}")

y2 = ((X - a*y1) * k) % (P - 1)
print(f"y2 = ((X - a*y1) * k) mod (P - 1) = (({X} - {a}*{y1}) * {k}) mod {P - 1} = {y2}")

# Проверить подпись
check = (pow(b, y1, P) * pow(y1, y2, P)) % P
expected = pow(alpha, X, P)

if check == expected:
    print("Подпись верна.")
    print(f"(b^y1 * y1^y2) mod P = α^X mod P => ({b}^{y1} * {y1}^{y2}) mod {P} = {alpha}^{X} mod {P} => {check} = {expected}")
else:
    print("Подпись неверна.")
    print(f"(b^y1 * y1^y2) mod P != α^X mod P => ({b}^{y1} * {y1}^{y2}) mod {P} != {alpha}^{X} mod {P} => {check} != {expected}")

print("y1 = ", y1)
print("y2 = ", y2)
