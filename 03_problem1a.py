a = 1
b = 3

if a == b // 2:
    b = a

if b == (2 * a + 1) % 2:
    a = 2 * b

a = a + b
b = a % 3