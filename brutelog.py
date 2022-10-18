# bruteforce discrete log algorithm
x = 27
g = 5
p = 43

res = 0
while True:
    if (g**res) % p == x:
        break
    res+=1
    
print(res)

