# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
#
# if __name__ == '__main__':
#     print_hi('PyCharm')

    # See PyCharm help at https://www.jetbrains.com/help/pycharm/

# records = []
# for _ in range(3):
#         name = input("Enter Name: \n")
#         age = int(input("Enter Age: \n"))
#         records.insert(age, name)
#         print("name = {}, age = {}".format(name, age))
# insert() is used to add elements into
# specific indices, so use as age here is
# actually a specification of an index

# names = ["ayo", "ade", "ada"]
# for var in enumerate(names):
#         print(var)

# for index, name in enumerate(names):
#         print("name = {}, index = {}".format(name,index))

# name = "BBS"
# pseudonym = "Wolvie"
# crush = "Rita Dominic"
#
# fact = "if he likes {1}, his name must be {2}, though he calls himself the {0}"
# print(fact.format(pseudonym, crush, name))

# name = 'John Marwood Cleese'
# first, middle, last = name.split()
# transformed = last+', '+first+' '+middle
# print(transformed)

# lit = [1, 2, 3]
# st = 'wait'
# lit += [st]
# print(lit)

# ip_add = '127.0.0.1'
# print(ip_add.split('7'))

# import datetime
# time = datetime.datetime.today()
# print(f"{time:%B %D, %Y}")
# print(f"{time:%b %d %y}")

# var = ord('A')        #chr(65)
# print(f'{var}')

# fruits = ['apple', 'pineapple', 'coconut', 'apple']
# print(list(reversed(fruits)))

# fruits = ['apple', 'pineapple', 'coconut', 'apple']
# print(fruits.pop())

# fruits = ['apple', 'pineapple', 'coconut', 'apple']
# fruits.remove("apple")
# print(fruits)

# fruits = "the fruit coconut i like"
# print(fruits.find('coco'))

# print(" ".join(["banana", "strawberry"]))

# class example:
#     eyes = "blue"
#     age = 22
#
#     @classmate          //@abstractmethod
#     def sample(self, married, divorced):
#             self.married = married
#             self.divorced = divorced
#             return "na so dem do dem chop our "+self.married+" and "+self.divorced
#
# class child_example(example):
#     pass
#
# ex_object = child_example()
# print(ex_object.age)
# print(ex_object.sample("5Alive", "HobNobs"))

# fob = open('c:/karaiyemapakadarada.txt', 'w')
# fob.write("She Has Us Locked-Down")
# fob.close()
# fob = open('c:/karaiyemapakadarada.txt', 'a')
# fob.writelines(["\nShe No Dey Agree", "\nNo Dey Slow Down"])
# fob = open('c:/karaiyemapakadarada.txt', 'rt')
# for x in fob:
# print(x)
# fob.close()

# with open('/path/to/some/file/you/want/to/read') as file_1, \
#         open('/path/to/some/file/being/written', 'w') as file_2:
#     file_2.write(file_1.read())

# import os
# if os.path.exists('c:/karaiyemapakadarada.txt'):
#     os.remove('c:/karaiyemapakadarada.txt')
#     print("Done, With A Big Smile")

# import random
# names = ["ayo", "ade", "ada"]
# random.shuffle(names)
# print(names)

# import random
# print(random.randrange(0, 9))
# print(random.randint(0, 9))

# name = "BBS"
# if type(name) is str:
#     print(isinstance(name, str))

# senior_man = ['John', 'Marwood', 'Cleese']
# print(range(len(senior_man)))

# senior_man = ['John', 'Marwood', 'Cleese']
# [print(x) for x in senior_man]


# def myfunc(n):
#   return len(n)
#
# x = map(myfunc, ('apple', 'banana', 'cherry'))
#
# print(list(x))

# num = 2020
# res = list(map(int, str(num)))
# print(res)

# pseudonym = list('Wolvie')
# pseudonym.sort(key=str.lower)
# pseudonym.sort(reverse=True)
# print(pseudonym)

# favouriteNumbers = [64, 7, 34]
#
# def closerTo50(n):
#     return abs(n-50)
#
# favouriteNumbers.sort(key=closerTo50)
# print(favouriteNumbers)

# favouriteNumbers = [64, 7, 34]
# favouriteColours = ["Yellow", "White", "Navy-Blue", "Grey"]
# for x in favouriteNumbers:
#     favouriteColours.append(x)
#     print(favouriteColours)

# digitalNomads = ("village", "chief", "elder", "natives", "cohorts")
# (semicolon, sam, chibuzor, *theFuture ) = digitalNomads
# print(theFuture)

# mySet = {"apple", "banana", "cherry"}
# myList = ["kiwi", "orange"]
# mySet.update(myList)
# print(mySet)

# mySet1 = {"apple", "banana", "cherry"}
# mySet2 = ["kiwi", "orange", "banana"]
# mySet1.symmetric_difference(mySet2)   # keep elements NOT common to both
# mySet1.symmetric_difference_update(mySet2)    # create new set of the elements NOT common to both
# mySet1.intersection(mySet2)   # create new set of the elements common to both
# mySet1.intersection_update(mySet2)    # keep elements common to both

# id(mySet1)

# num = 6
# print(0 <= num <= 5)                       //False
# speak_up = not(num < 5 and num < 10)      //True

# import numpy as np
# def createlist (a, b):
#     return np.arange(a, b+1, 1)
# print(createlist(5, 10))

# def insertionSort(arr):
#     for i in range(1, len(arr)):
#         key = arr[i]
#         j = i - 1
#         while j >= 0 and key < arr[j]:
#             arr[j + 1] = arr[j]
#             j -= 1
#             arr[j + 1] = key
#
# arr = [12, 11, 13, 5, 6]
# insertionSort(arr)
# print("Sorted array is:")
# for i in range(len(arr)):
#     print("%d" %arr[i])

# def centeredZero(limit, diff):
#     list = [-limit]
#     while list[-1] < limit:
#         list.append(list[-1] + diff)
#     list[-1] = limit
#     return list
#
# print(centeredZero(3, 0.5))

# lst = [1095, 746, 94, 126, 35, 50, 24]
# for i in range(len(lst)):
#     minimum = i
#     for j in range(i+1, len(lst)):
#         if lst[minimum] > lst[j]:
#             minimum = j
#     lst[i], lst[minimum] = lst[minimum], lst[i]
#
# for i in range(len(lst)):
#     print(lst[i])

# import re
# regex = '^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$'
# def check(email):
#     if (re.search(regex, email)):
#         print("Valid Email")
#     else:
#         print("Invalid Email")

# takeItBack = 6
# print("The reversed numbers are : ", end=" ")
# for num in reversed(range(takeItBack + 1)):
#     print(num, end=" ")

# class NotEvenNumberException(BaseException):
#     def __init__(self, message="Number Is Not Even"):
#         super(NotEvenNumberException,self).__init__(message)

# import array
# arr = array.array('i', [1, 2, 3, 4, 5, 6])
# for i in range(0, 6):
#     print(arr[i], end=" ")
#     print("\r")
#arr.index(2) | arr.reverse() | arr.remove(1)
#arr.pop(2) | arr.insert(2, 5) | arr.append(4)

# def remove_sorted_duplicates(arr):
#     nextNonDuplicate = 0
#     i = 0
#
#     while i < len(arr):
#         if arr[nextNonDuplicate - 1] != arr[i]:
#             arr[nextNonDuplicate] = arr[i]
#             nextNonDuplicate += 1
#         i += 1
#     return nextNonDuplicate
#
#
# theList = [1, 1, 3, 3, 7, 7, 4, 4, 9, 9, 0, 0, 2, 2]
# print(remove_sorted_duplicates(theList))

# float = 2.154327
# format_float = "{:.2f}".format(float)
# print(format_float)

# my_float = 2.13456
# limit_float = round(my_float, 2)
# print(limit_float)

# def character_range(char1, char2):
#     for char in range(ord(char1), ord(char2) + 1):
#         yield (char)
#
#
# for letter in character_range('a', 'z'):
#     print(chr(letter), end=', ')

# from typing import List
# target = 9
#
# def two_sum(self, nums: List[int], target: int) -> List[int]:
#     return list(filter(lambda x: target - nums[x] in nums, list(range(len(nums)))))

# def arrow(n):
#     for i in range(n):
#         if i == n-1:
#             print((2 * n) * "*", end="")
#             print((i + 1) * "*")
#         else:
#             print((2 * n) * " ", end="")
#             print((i + 1) * "*")
#     for j in range(n-1, 0, -1):
#         print((2 * n) * " ", end="")
#         print(j * "*")
#
#
# arrow(5)


# my_set = set(('a', 'b', 'c'))
# my_set.remove('a')
