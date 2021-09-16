"""IF, ELIF, ELSE"""
import random
# 1. Enter your name, then find the sum of the ASCII values of the letters in your name. If that number is larger than
# 500, print "I've got a great name!", and "I've got a fancy name!" otherwise.
m = input("Enter your name : ")
count = 0
for i in m:
    count += ord(i)
if count > 500:
    print("I\'ve got a great name!")
else:
    print("I\'ve got a fancy name!")
# 2. Ask the user for a movie title. If the title starts with a capital letter, print "Great title!", otherwise print
# "Titles start with capital letters...". If the input is not a string, print "Why are you doing this to me?".
title = input()
if title.isalpha() == True:
    print("Why are you doing this to me?")
if title[0] == title[0].capitalize():
    print("Great title")
else:
    print("Titles start with capital letters...")
# Type is always string

# 3. Ask the user to input his/her age. If the user is older than 18, than tell them they're eligible to vote. If they
# are younger than 18, tell them how many years do they have to wait.
x = int(input("Enter your age:"))
if x >= 18:
    print("You are eligible to vote")
else:
    print("You have to wait "+str(18-x)+" years")
# 4. Write a program that will tell us whether a given year is a leap year or not.
k = int(input())
if k % 4 == 0:
    print("This is a leap year")
# 5. Using 'random' module, generate a random number between -1000 and 1000. If the number is positive, print positive.
# If it's negative, print negative along with the absolute value of the number.
rand_num = random.randint(-1000, 1001)
if rand_num >= 0:
    print(rand_num)
elif rand_num < 0:
    print(rand_num, -rand_num)