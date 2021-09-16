import random
import math
# 1. Write a program to loop through a range from 0 to 100 and print the even numbers only.
# Գրել ցիկլ, որը կտպի 0-100 զույգ թվերը։
for i in range(0, 101):
    if i % 2 == 0:
        print(i)
# 2. Write a program to loop through a range from 350 to 677 and print only numbers ending with 7.
# Գրել ցիկլ, որը կտպի 350-677 միջակայքի միայն այն թվերը, որոնք ավարտվում են 7-ով։
for i in range(350, 678):
    if i % 10 == 7:
        print(i)
# 3. Print every 6th number from 0 to 100.
# Տպել 0-100 ամեն 6-րդ թիվը։
ren = range(0, 100)
for i, j in enumerate(ren):
    if (i + 1) % 6 == 0:
        print(i)
# 4. Write a program that will output the multiplication table.
# Գրել ծրագիր, որը կտպի բազմապատկման աղյուսակը։
for i in range(1, 10):
    for j in range(1, 10):
        print("{:>2} * {} = {:>2}".format(i, j, i * j), end="\t")
    print()
# 5. Write the FizzBuzz program. Only this time, loop through a range of 0-100 and for each iteration, print Fizz,
# if the loop variable is divisible by 3, Buzz, if it's divisible by 5, and FizzBuzz if it's divisible by both.
# Գրել նախորդ դասի FizzBuzz ծրագիրը, սակայն այս անգամ ցիկլի միջոցով տպել առաջին 100 թվերի FizzBuzz արժեքները։
for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
# 6. Write a program that will loop through a range of 0-1000 and print out only prime numbers.
# Տպել 0-1000 միջակայքի պարզ թվերը։
for i in range(2, 1001):
    for j in range(2, int(i / 2)+1):
        if i % j == 0:
            break
    else:
        print(i)

# 7. Write a program that will keep a random number from 1-10 (use random package). The user must guess that number.
# They can input as many times as they want. Terminate the program with a congratulation message when the user has
# guessed the number.

# To make this more interesting, you can add lives (attempt limit) for the user, and after each guess let them know if
# their guess was larger or smaller from the actual number.

# Գրել խաղ, որը կպահի 1-100 պատահական թիվ։ Խաղացողը պետք է գուշակի այդ թիվը։ Նա կարող է այնքան անգամ գուշակել, ինչքան
# ցանկանում է։ Ավարտել ծրագիրը շնորհավորանքի նամակ տպելով, երբ խաղացողը թիվը գուշակի։

# Խաղն ավելի հետաքրքիր դարձնելու համար կարելի է սահմանափակել հնարավորությունների քանակը։ Կարելի է նաև խաղացողին
# տեղեկացնել, արդյո՞ք նրա մուտքագրած թիվը մեծ է պահված թվից, թե փոքր։
rand_num = random.randint(1, 100)
guessed = False
while not guessed:
    x = int(input())
if x == rand_num:
    print("Congratulations!!!")
elif x < rand_num:
    print("Your number is smaller")
elif x > rand_num:
    print("Your number is bigger")

# 8. Given a string, print a string where for every character in the original, there are two characters.
# Տրված է սթրինգ։ Տպեք նոր սթրինգ, որը կպարունակի օրիգինալ սթրինգի բոլոր տառերը կրկնապատկված։
str_1 = input()
result = ""
for char in str_1:
    result += char*2
    print(result)
# Օրինակ, եթե ունենք հետևյալ սթրինգը՝ Monty, պետք է ստանանք MMoonnttyy

# 9. Given 2 strings, a and b, return the number of the positions where they contain the same length 2 substring. So
# "xxcaazz" and "xxbaaz" yields 3, since the "xx", "aa", and "az" substrings appear in the same place in both strings.

# 10. Reverse a string without the use of indexation (e.g. [::-1]).
# Շրջել սթրինգը առանց գործածելու str[::-1]
str_1 = "asdsad"