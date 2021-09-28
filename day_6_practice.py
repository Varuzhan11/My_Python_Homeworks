"""FUNCTIONS"""

# 1. Write your version of max()/min() function (without using them inside your function). It will take a list as an
# argument and return max()/min() value of the list. You may write one function with a keyword argument, that will let
# the user switch between max()/min() or write two separate functions for each.
def max_min(lst, k):
    num_1 = 0
    if k == "max":
        for i in range(1, len(lst)):
            if lst[i] > lst[i-1]:
                num_1 = lst[i]
    elif k == "min":
        for i in range(1, len(lst)):
            if lst[i] < lst[i-1]:
                num_1 = lst[i]
    else:
        return "Wrong k"
    return num_1


# 2. Write a function that will take a string as an argument. The function shall return number of upper-case and
# lower-case characters as a tuple.
def func(n):
    count_1 = 0
    count_2 = 0
    for i in n:
        if n.isalpha() == True and n[i] == n.upper()[i]:
            count_1 += 1
        elif n.isalpha() == True and n[i] == n.lower()[i]:
            count_2 += 1
        else:
            print("This is a wrong string")
    tup = (count_1, count_2)
    return tup

# 3. Write the Fibonacci exercise in a function this time. The function accepts 1 numerical argument - n, and returns
# the n-th element from Fibonacci's sequence.
def fib(n):
    lst_1 = [0, 1]
    x = 0
    for i in range(1, 1000):
        x = lst_1[i] + lst_1[i-1]
        lst_1.append(x)
    return lst_1[n-1]
# 4. Write a function which will take a string as an argument, return True if the string is a palindrome and False
# otherwise.
def pol(n):
    str_1 = ""
    str_2 = ""
    for i in range(0, len(n)//2):
        str_1 += n[i]
    for i in range(len(n)//2, len(n)):
        str_2 += n[i]
    if str_1 == str_2[::-1]:
        return True
    else:
        return False
# 5. Write a function which will take a list as an argument. If the list is monotonically descending, print that the
# list is 'descending'. Print increasing if it's monotonically 'increasing'. If it isn't monotonic, print 'neither'.




# 6. Write a function that will calculate the factorial of n.
def fact(n):
    x = 1
    if n == 0 or n == 1:
        return 1
    else:
        for i in range(1, n+1):
            x *= i
        return x

# 7. Write a function that will take 4 arguments. First two are tuples and represent 2D coordinates of two circles.
# The others are the radii of our circles. The function must tell us whether one of the circles is inside the other, or
# do circles intersect, or are they far apart.

# 8. Write a function that sorts a list in ascending. Additionally, the function may take a keyword argument that will
# reverse the sort.
def sort(lst, k):
    x = 0
    if k == "dec":
        for i in range(1, len(lst)):
            for j in range(0, i):
                if lst[j] < lst[i]:
                    a = lst[i]
                    b = lst[j]
                    lst[i] = b
                    lst[j] = a

    elif k == "inc":
        for i in range(1, len(lst)):
            for j in range(0, i):
                if lst[j] > lst[i]:
                    a = lst[i]
                    b = lst[j]
                    lst[i] = b
                    lst[j] = a

    return lst
# 9. Create 3 numerical lists. Using the map function, return a new list, which is the element-wise sum of the 3 lists.