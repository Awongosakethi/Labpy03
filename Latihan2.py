a = int()
b = 0
while a >= 0:
    a = int(input("Masukan Bilangan: "))
    if a > b:
        b = a
    if a == 0:
        break
print("Bilangan terbesar adalah", b)