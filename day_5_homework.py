"""DATA STRUCTURES"""
import random
# 1. Write a program to multiply all the items in a list.
# Գրել ծրագիր, որը կբազմապատկի լիստի բոլոր թվերը։
lst_1 = [1, 2, 3, 4, 5, 6, 7, 8]
counter_1 = 1
for i in range(len(lst_1)):
    counter_1 *= lst_1[i]
print(counter_1)
# 2. Write a program to count the number of strings where the string length is 2 or more and the first and last
# character are same from a given list of strings.
# Գրել ծրագիր, որը կհաշվի լիստում եղած 2 կամ ավել երկարություն ունեցող լիստերի քանակը, որոնց առաջին և վերջին տառերը
# նույնն են։
lst_9 = ["lol", "pop", "rock", "pep", "else"]
counter_2 = 0
for i in range(len(lst_9)):
    if len(lst_9) >= 2 and lst_9[i][0] == lst_9[i][-1]:
        counter_2 += 1
print(counter_2)
# 3. Write a program that will remove duplicates from a list. DO NOT use set() method directly on the list.
# Գրել ծրագիր, որը կջնջի դուպլիկատները լիստից։ ՉՕԳՏԱԳՈՐԾԵԼ set() մեթոդը։
lst_4 = [1, 2, 3, 1, 2, 3, 4, 5, 2, 3, 1, 3, 4, 2, 1]
lst_5 = []
for i in range(len(lst_4)):
    if lst_4[i] not in lst_5:
        lst_5.append(lst_4[i])
print(lst_5)
# 4. Create a list from 5 user inputs.
# Ստեղծել լիստ 5 ներմուծված թվերից
lst_2 = []
for i in range(9):
    lst_2[i] = int(input())
print(lst_2)

# 5. Write a program to print the given list after removing the 2nd, 4th and 5th elements.
# Գրել ծրագիր, որը կջնջի տրված լիստի 2-րդ, 4-րդ և 5-րդ էլեմենտները։
lst = ['Rock', 'Pop', 'Metal', 'Hip-Hop', 'Rap']
del(lst[1], lst[3-1], lst[4-2])
print(lst)
# 6. Given a list of ints, print True if the array contains a 2 next to a 2 somewhere.
# Գրել ծրագիր, որը կտպի True, եթե տրված լիստում ինչ-որ տեղ 2 թվին 2 է հաջորդում։
lst_6 = [1, 3, 4, 2, 2, 3, 6, 7, 8]
for i in range(1, len(lst_6)):
    if lst_6[i] == lst_6[i-1] and lst_6[i] == 2:
        print("True")
        break
# 7. Given a list of ints, print True if every element is a 1 or a 4, and False otherwise.
# Գրել ծրագիր, որը կտպի True, եթե լիստի բոլոր էլեմենտները 1 կամ 4 են։ Հակառակ դեպքում տպել False:
lst_3 = [1, 4, 1, 3, 1, 4, 1, 4]
flag = True
for i in range(len(lst_3)):
    if lst_3[i] != 1 and lst_3[i] != 4:
        flag = False
        break
print(flag)

# 8. Ask for user input and add that input as a key into the dictionary. If the key exists, warn the user about it and
# do nothing. Assign some arbitrary value to it.
# Պահանջել ներմուծել բանալի և ավելացնել այդ բանալին dictionary-ի։ Եթե այն արդեն գոյություն ունի, տպել, որ բանալին արդեն
# կա և ոչինչ չանել։ Որպես արժեք տեղադրել պատահական օբյեկտ
dict_1 = {"key1": "value1", "key2": "value2", "key3": "value3"}
key_input = input("Enter the key: ")
if key_input in dict_1.keys():
    print("Already in dict_1")
else:
    dict_1.update({key_input: random.randint(0, 100)})

# 9. Loop through the values of a dictionary and add them to a new list.
# Ցիկլի միջոցով ավելացնել dictionary—ի արժեքները նոր լիստի մեջ։
dict_2 = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3', 'key4': 'value4'}
lst_10 = []
for i in dict_2.values():
    lst_10.append(i)
print(lst_10)
# 10. Write a script to print a dictionary where the keys are numbers between 1 and 15 (both included)
# and the values are square of keys.
# Գրել ծրագիր, որը կստեղծի և կտպի dictionary, որի բանալիները [1,15] թվերն են, իսկ արժեքները դրանց քառակուսիները։
dict_3 = {}
for i in range(1, 16):
    dict_3[i] = i*i
print(dict_3)
