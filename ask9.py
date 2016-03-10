import random
z = 0
# L is the variable which count how many "L" managed to enter in the table
L = 0
# creat table called "A"
A = [0 for i in range(10)]

while True:
    #find random a number from zero to eight
    #until 8 because "L" have 2 width so it doesn't overcome the table "A"
    newL = random.randint(0, 8)
    z = max(A[newL], A[newL + 1])
    if z + 3 > 20 or z + 1 > 20:
        break
    else:
        A[newL] = z + 3
        A[newL + 1] = z + 1
        L = L + 1
print L
