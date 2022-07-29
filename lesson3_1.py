def count_b():
    b = 1
    c = 0
    while b < 11:
        c = a * b
        print(f"{a} * {b} = {c}")
        b += 1

a = 1
while a < 10:
    count_b()
    print()
    a += 1