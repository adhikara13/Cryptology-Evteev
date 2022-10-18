from tabulate import tabulate
# Shanks algo
print("Log g^x = n mod p")
p = int(input("p = "))
x = int(input("x = "))
g = int(input("g = "))
print(f"Log{g}^{x} mod = n mod {p} or {x} = {g}^n(mod^{p})")
k = int(input("Enter k = "))

res = []
sec = []
for i in range(1, k-1):
    res.append([f"{g}^{i} mod {p} =",g**i % p])
for i in range(-k, -50,-1):
    sec.append([f"{x}*({g})^{i} mod {p} =",((x * pow(g, i, p)) % p)])

print(tabulate(res, headers=["baby step", "result"],tablefmt="outline"))
print(tabulate(sec, headers=["giant step", "result"], tablefmt="outline",stralign="right"))


