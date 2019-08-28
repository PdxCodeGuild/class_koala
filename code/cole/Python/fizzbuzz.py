#fizzbuzz.py
i = 1

while i <= 100:
    a = ""
    if i % 3 == 0:
        a += "fizz"
    if i % 5 == 0:
        a += "buzz"
    if i % 5 == 0 or i % 3 == 0:
        print(a)
    else:
        print(i)
    i += 1
