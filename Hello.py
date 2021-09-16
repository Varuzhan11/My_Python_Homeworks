k = 1
while True:
    lst_2 = [[j**2 for j in range(k, k+3)]]
    k += 3
    if k == 10:
        break
    print(lst_2)
