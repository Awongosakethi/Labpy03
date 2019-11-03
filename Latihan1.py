num = int(input("Masukan nilai N: "))
jumlah = num+1
start = 1
stop = jumlah
step = 1
for i in range(start, stop, step):
    from random import random
    a = random()
    print("Data ke:",i,"=>",(a))