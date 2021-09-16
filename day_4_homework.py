"""LOOPS"""

# 1. Create a 3x3 matrix that will contain the squares of the numbers from 1-9 using a nested loop.
# Օգտագործելով ցիկլեր, ստեղծել 3x3 մատրից, որը կպարունակի 1-9 թվերի քառակուսիները։
lst_1 = []
x = 1
for i in range(0, 3):
    lst_1.append([])
    for j in range(0, 3):
        lst_1[i].append(x*x)
        x += 1
        print(lst_1[i][j], end=" ")
    print("\n")


# 2. Create a 3x3 matrix that will contain the squares of the numbers from 1-9 using a list comprehension.
# Օգտագործելով comprehension, ստեղծել 3x3 մատրից, որը կպարունակի 1-9 թվերի քառակուսիները։
# ինձ մոտ չստացվեց այսպես գրել։

# 4. Count the number of 'b's in the given string. DO NOT use the count() method.
# Հաշվել տրված սթրինգում 'b'-երի քանակը։ Չօգտագործել count() մեթոդը։
nonsense = 'Blinking blindly, brainy Bob brings beautiful beer bottles beneath blue butterflies billowing brilliantly.'
counter = 0
x = len(nonsense)
for i in range(x):
    if nonsense[i] == 'b':
        counter += 1
# 5. Write a program that will print the factorial of n.
# Գրել ծրագիր, որը կտպի n թվի ֆակտորիալը։
fact = 1
n = int(input())
if n == 0:
    fact = 1
else:
    for i in range(1, n+1):
        fact *= i
print(fact)