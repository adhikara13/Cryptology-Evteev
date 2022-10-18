# bruteforce discrete log algorithm
print("Log g^x = n mod p")
x = int(input("x = "))
g = int(input("g = "))
p = int(input("p = "))


res = 0
while True:
    if (g**res) % p == x:
        break
    res+=1
    
print(f"n = {res}")

