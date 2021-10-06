"""FUNCTIONS"""
import random
from math import *
# 1. We'll say that an element in an array is "alone" if there are values before and after it, and those values are
# different from it. Return a version of the given array where every instance of the given value which is alone is
# replaced by whichever value to its left or right is larger.
# Ենթադրենք տարրը "միայնակ" է, եթե նրանից առաջ կամ հետո գտնվող տարրերի արժեքը տարբերվում է իր արժեքից։ Ստեղծել ֆունկցիա,
# որը կվերցնի լիստ որպես արգումենտ և կվերադարձնի այդ լիստը ձևափոխված այնպես, որ բոլոր միայնակ տարրերը փոխարինված լինեն
# իրենցից աջ կամ ձախ գտնվող առավելագույն արժեք ունեցող տարրով ([4, 4, 1, 3, 3], այստեղ 1-ը կփոխարինվի 4-ով):
lst = [1, 1, 1, 2, 2, 2, 3, 4, 4, 4, 5, 5, 5]
def rep(arr: list):
    for i in range(len(arr)):
        if (i != 0 and i != -1) and arr[i] != arr[i-1] and arr[i+1]:
            if arr[i] < arr[i-1] < arr[i+1]:
                arr[i] = arr[i+1]
            elif arr[i] < arr[i+1] < arr[i-1]:
                arr[i] = arr[i-1]
print(rep(lst))
# 2. Write a function to create and print a list where the values are square of numbers between 1 and 30
# (both included).
# Ստեղծել ֆունկցիա, որը կստեղծի և կտպի լիստ, որի արժեքները [1, 30] միջակայքում գտնվող թվերի քառակուսիներն են։
def one_thirty(arr):
    for i in range(1, 31):
        arr.append(i ** 2)
    return arr
# 3. Write a function which will take one argument n. Return a list of size n, that will contain random numbers
# from (-100, 400).
# Ստեղծել ֆունկցիա, որը կվերցնի մեկ արգումենտ՝ n: Վերադարձնել n երկարությամբ լիստ, որը կպարունակի (-100, 400)
# միջակայքում գտնվող պատահական թվեր։
def rand(n):
    lst = []
    for i in range(n):
        i = random.randint(-100, 400)
        lst.append(i)
    return lst
# 4. Write a function, that will take a list of words as an argument and return all the words in the list that start
# with a vowel.
# Ստեղծել ֆունկցիա, որը կվերցնի լիստ որպես արգումենտ (սթրինգերի) և կվերադարձնի մեկ այլ լիստ, որը կպարունակի այդ լիստի
# բոլոր այն բառերը, որոնք սկվում են ձայնավորով։
poem = '''All that is gold does not glitter,
Not all those who wander are lost;
The old that is strong does not wither,
Deep roots are not reached by the frost.
From the ashes a fire shall be woken,
A light from the shadows shall spring;
Renewed shall be blade that was broken,
The crownless again shall be king.'''

# Ավելի հարմար է ձայնավորների սթրինգ կամ լիստ հայտարարել ու in օպերատորով ստուգել
def only_v(str_3: str):
    lst_3 = []
    lst_1 = str_3.split(" ")
    for item in range(len(lst_1)):
        if lst_1[item][0].lower() == "a" or lst_1[item][0].lower() == "e" or lst_1[item][0].lower() == "i" \
                or lst_1[item][0].lower() == "o" or lst_1[item][0].lower() == "u" or lst_1[item][0].lower() == "y":
            lst_3.append(lst_1[item])
    return lst_3

# 5. We want make a package of goal kilos of chocolate. We have small bars (1 kilo each) and big bars (5 kilos each).
# Write a function to return the number of small bars to use, assuming we always use big bars before small bars. Return
# -1 if it can't be done.
# Մենք ուզում ենք պատրաստել որոշակի x կշռով շոկոլադ։ Ունենք փոքր և մեծ շոկոլադե սալիկներ, որոնք համապատասխանաբար
# կշռում են 1 և 5 կգ։ x կգ շոկոլադը պատրաստելու համար առաջինը օգտագործելու ենք մեծ սալիկները, ապա փոքր։ Սալիկները
# կտրատել հնարավոր չէ։ Գրել ֆունկցիա, որը կվերադարձնի անհրաժեշտ փոքր սալիկների քանակը։ Եթե հնարավոր չէ տրված սալիկների
# քանակով պատրաստել անհրաժեշտ շոկոլադը՝ վերադարձնել -1։
# Ֆւնկցիայի սահմանումն ունի հետևյալ տեսքը, որտեղ small, big -> հասանելի փոքր և մեծ սալիկների քանակը, իսկ goal-ը
# վերոնշյալ x-ն է։

def make_chocolate(small, big, goal):
    five_count = goal//5
    if 5 * five_count > big * 5 + small or 5 * big + small < goal or 5 * five_count + small < goal:
        return -1
    elif 5 * big + small >= goal and big > five_count:
        return goal - 5 * five_count
    return goal - 5 * big
print(make_chocolate(4, 4, 13))



# 6. Given three ints, a b c, return True if one of b or c is "close" (differing from a by at most 1), while the other
# is "far", differing from both other values by 2 or more. Return False otherwise.
# Գրել ֆունկցիա, որը կվերցնի երեք ամբողջ թիվ որպես արգումենտ։ Վերադարձնել True, եթե b-ն կամ c-ն իրենց բացարձակ արժեքովm
# տարբերվում են a-ից առավելագույնը 1-ով, երբ միաժամանակ մյուս երկուսը տարբերվում են իրարից 2-ով։ Հակառակ դեպքում
# վերադարձնել False
def mod(a, b ,c):
    if abs(abs(a)-abs(b)) == 1 and abs(abs(a)-abs(c)) >= 2:
        return True
    elif abs(abs(a)-abs(c)) == 1 and abs(abs(a)-abs(b)) >= 2:
        return True
    else:
        return False

# 7. Write a function that gets a numerical list as an argument. Find the sum of the elements. If a certain element is
# 13 stop the count and return whatever was the sum before that.
# Ստեղծել ֆունկցիա, որը կգումարի տրված լիստի բոլոր թվերը և կվերադարձնի այն։ Եթե տարրերից մեկը 13 է, դադարեցնել հաշվարկը
# և վերադարձնել մինչև այդ պահը հաշված գումարը։

example_list = [4, 1, 2253, 32, 13, 64, 1, 90]
def thi(arr):
    count = 0
    for i in range(len(arr)):
        if arr[i] != 13:
            count += arr[i]
        else:
            break
    return count
# 8. Write down the following functions in a lambda form
# Գրել հետևյալ ֆունկցիաների լամբդա տարբերակները

def square(x):
    return x ** 2
m = lambda x: x**2

def circle_area(r, pi=3.14):
    return pi * r ** 2
n = lambda x, pi=3.14 : pi * x ** 2

def sum_to_power(x, y, p):
    return (x + y) ** p
k = lambda x, y, p: (x + y) ** p

# 9. Create a list from 1-100. Using the filter function, return a new list containing only the numbers ending with 7.
# Ստեղծել 1-100 թվերը պարունակող լիստ։ Օգտագործելով ֆիլտր ֆունկցիան, վերադարձնել նոր լիստ, որը կպարունակի օրիգինալի
# միայն այն թվերը, որոնք վերջանում են 7-ով
lst_2 = []
def sev(arr: list):
    for i in range(1, 100):
        arr.append(i)
    arr = list(filter(lambda x: x % 10 == 7, arr))
    return arr
print(sev(lst_2))
# 10. Create a function that will take a string as an argument. Return a new string which is the original string with
# each letter doubled. For example 'cat' will become 'ccaatt'
# Ստեղծել ֆունկցիա, որը կվերցնի սթրինգ։ Վերադարձնել սթրինգ, որը կլինի օրիգինալ սթրինգը, սակայն ամեն տառ կլինի
# կրկնապատկված։ Օրինակ cat—ը կվերադարձնի 'ccaatt'
str_1 = "cat"
str_1 = list(map(lambda x: x * 2, str_1))
str_2 = ""
for i in range(len(str_1)):
    str_2 += str_1[i]
print(str_2)
