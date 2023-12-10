#print("hello world")
#print("привет")
# name = "Yana"
# print("hello", name)
#age = 20.4
#print(age)
#text = "hello"
#print(text)
#print(text + str(age))
#print(type(age)) # int=20 float = 20.4 str =text
#print(type(text))
#a = True
#print(a)
#print(type(a))
import random

# a = 4
   # b = 5
    #print(a, id(a))
   # print(b)
    #a=b
    #print(a)
#print(b)
#a,b,c =5,"hi",9.2
#print(a)
#print(b)
#print(c)

# PI= 3.14
# print(PI)
# PI=2
# print(PI)

# print("kitten\n  july \r file.txt D:\\folder\\f")
# s1="hello"
# s2="python"
# s3=s1+","+s2 +"!\t\t"
# #print(s1,",",s2,"!")
# print(s3*3)
# print(2345678987654323456789)
# print(23.12345678987654321234567890987654321234567)
#
# number = (6+4)*(5**2+7)
# print(number)
# num -= 3
# print(num) 12
# num= 4321
# print("исходное число",num)
# a = num%10
# print(a)
# num//=10
# print(num)
# b=num%10
# print(b)
# num//=10
# c = num % 10
# print(c)
# num //= 10
# d = num % 10
# print(d)
# print(a*1000+b*100+c*10+d)
# num = 4321
# print("исходное число",num)
# res=num%10*1000
# num//=10
# res+=num%10*100
# num//=10
# res+=num%10*10
# num//=10
# res+=num%10
# print(res)
# num1 = "2"
# num2=3
# res=num1+str(num2)#23
# #re=int(num)+num2 //5
# print(res)

# print(int(3.8))
# print(round(3.8876,3))
# print(type(round(3.8987,2))  input(" Enter your name :"))
# name = 5
# power = input("enter s:")
# res = name**int(power)
#
# print("number",name,"in s",power,"ravno",res)

# print(5-3==2 or 1+3==4)
# print(5-3==2or 1+3<4)
# print(5-3>2or 1+3==4)
# print(5-3>2or 1+3<4)
#
#
# cnt=5
# if cnt<10:
#     cnt+=2
#     print(cnt)
# age = int(input("Введите возраст:"))
# if age >= 18:
#     print("allowed")
# else:
#     print("you can't enter this site")
# a = 25
# b = 56
# if a > b:
#     print("a > b")
# elif a < b:
#     print("a < b")
# else:
#     print("a == b")
#
# day = int(input("Enter the day of the week(number):"))
# if 1<=day<=5:
#     print("рабочий день-",end="")
#     if day ==2:
#         print("Tuesday")
#         if day == 3:
#             print("wednesday")
#             if day == 4:
#                print("thurstday")
#         if day ==5:
#             print("friday")
#     elif day==6 or day ==7:
#         print("Выходной день-", end-"")
#         if day == 6:
#             print("saturday")
#             if day == 7:
#                 print("sunday")
#     else:
#         print("no")

# n= int(input("Введите колличество ворон:"))
# if 0 <= n <= 9:
#     print("на ветке ",n,end=" ")
#     if n==1:
#         print("ворона")
#     elif 2 <= n <=4:
#         print("вороны")
#        else:
#         print("Ворон")
# else:
#     print("Ошибка ввода данных")

# password ="qwerty"
# match password:
#         case 'admin':
#            print("Admin")
#         case "user" :
#            print("User")
#         case'Yana':
#           print("Yana")
#         case _:
#          print("Login not found")

# day ='Monday'
# time=10
#
# match day:
#     case "Monday"|"Tuesday"|"Wednesday"|"Thurstday"|"Friday" if 9<= time<=16:
#         print("Work day")
#     case "Saturday"|"Sunday":
#         print("Weekends")
#     case _:
#         print("Not found or not work time")

#Тернарное выражение if
# a,b= 30,20
# print(a if a <b else b )
# a,b= 30,20
# print("a==b" if a ==b else "a>b" if a>b else "b>a")


# a = int(input("Enter number"))
# b=0
# print("not found "if b==0 else a/b)
# try :
#     n = int(input("enter"))
#     print(n*2)
# except :
#      # print("tyiyuiuyi")
#
# print("dfghjklkjhgfg")

#Циклы
# i= 2
# while i<=20:
#     print("i=",i)
#     i+=2

# i = 1
# while i <= 20:
#     if i % 2 == 0:
#         print(i)
#         i += 1

# a = int(input("begin"))
# b = int(input("end"))
# res = 0
# while a <= b:
#     if a % 2 !=0:
#        res += a
#     a += 1
#     print(res)

# nums = [i for i in range(30) if i % 2 == 0]
# print(nums)
#Списки (list)
# nums = [8, 3, 9, 4, 5, "one"]
# print(nums)
# # print(type(nums))
# #
# # print(nums[0])
# # print(nums[2])
# # print(nums[-1])
# # print(nums[-2])
# #
# # nums[1] = 256
# # print(nums)
# # nums[3] +=100
# # print(nums)
# print(len(nums))
# for i in range(len(nums)):
#     print(nums[i] ** 2)
#
#
# s = []
# print(s)
#
# b = list()
# print(b)
#
# a = list("hello")
# print(a)
#
# p = list("hello" , "kid")
# print(p)

# print(range(6))
# n = list(range(6))
# print(n)
#
# print(list(range(3,10)))
# print(list(range(2,10+1,2)))

# a = [ 8 for i in range(5)]
# print(a)
#
# b = [ i for i in range(5)]
# print(b)

# n = 54
# b = [i ** 2 for i in range(1, n + 1)]
# print(b)
#
# a = [ 1, 2, 3]
# b = [4,5]
# c = a + b
# print(c)
# d = b * 3
# print(d)

# a = [0] * int(input("number"))
# print(a)
# for i in range(len(a)):
#     a[i] = input("->")
# print(a)

# a = [input() for i in range(int(input()))]
# print(a)

# a = [int(input("->")) for i in range(int(input("n=")))]
# print(a)
# s = 0
# for i in range(len(a)):
#     if a[i] <  0:
#         print(a[i])
#         s += a[i]
# print(s)

# a = list(range(10, 100, 10))
# print(a)
#
# for i in range(len(a)):
#     print(a[i] + 2, end=" ")
# print()
#
# for i in a:
#     print(i +2 ,end=" ")
# a = list(range(21, 41))
# print(a)
# s = k  = 0
# for i in range(len(a)):
#     if a[i] % 2 == 0:
#         k += 1
#     else:
#         s += a[i]
# print(s)
# print(k)

#

# a = [ int(input('->')) for _ in range(int(input('n='))) ]
# print(a)
# for i in range(1, len(a)):
#     if a[i] > a[i - 1]:
#         print(a[i], end=" ")

#Срез
#список[start;stop;step]
# a = [7, 8, 2, 1, 4, 5,  7]
# print(a)
# # a[0],a[1] = a[1],a[0]
# # print(a)
# print(a[1:4])#срез
# print(a[1:])
# print(a[:3])

#a = list(range(1,8))
# print(a)
# print(a[::-1])
# print(a[0:7:2])
# print(a[::2])
# print(a[-1:])
# print(a[3:4])
# print(a[3:1:-1])
# print(a[2:5])
# #
# s = [5, 9, 6, 7, 3, 4]
# print(s)
# s[1:3] = [0, 0, 0, 0]
# print(s)
# s[1:2] = [20]
# print(s)
# s[4:] = []
# print(s)
# del s[1]
# print(s)

# Методы списков
# s = [5, 9, 6, 7, 3, 4]
# print(s)
# s.append(99)#Добавить значение в  конец списока
# print(s)
# s.extend([1, 2, 3]) #Добавляет список [] элементов  или слово 'word' конец списка
# print(s)
# s.insert(0, 100) # Добавляется элемент (вторым параметром(100)), в заданный индекс(первый параметр(1))
# print(s)
# s.insert(-1,100)
# print(s)

#
# s = []
# n = int(input("number:"))
# for num in range(n):
#     x = int(input("Enter number"))
#     s.insert(0,x)
# print(s)

# a = [5, 6, 7, 8, 8, 9]
# b = [ 8, 2, 7, 4, 5, 6]
# c = []
#
# for element in a:
#      if element in b and element not in c:
#          c.append(element)
#
# print(c)

# a = [1, 2, 3, 77, 77]
# b = [11, 22, 33, 99, 0000, 777]
# c = []
# if len(b) > len(a):
#     for i in range(len(a)):
#                 c.append(a[i])
#                 c.append(b[i])
#     for i in range(len(a),len(b)):
#        c.append(b[i])
# print(c)

# a.copy (опирование элементов массива)
#a.append (добавить элемент )
# a = [5, 6, 4, 2, 7]
# print(a)
# a.reverse()
# print(a)
#
# a.sort(reverse=True)
# print(a)

# b = ["felix", "teyona", "Cristofer", "ban"]
# b.sort(key=len)
# print(b)
# a = [5, 6, 4, 2, 7]
# sort = sorted(a)
# print(sort)
# print(a)

# Генерация случайных данныъ

# import random
# print(random.random())
# print(random.randint(3, 9)) # от 3 до 9 вклячительно
# print(random.randrange(3, 9, 2))  # от 3 до 9 не вклячительно
#
# print(random.uniform(10.5, 25.5))
# print(round(random.uniform(10.5, 25.5) ,2))
#
# city_list = ['Moscow','Paris','Munchen','Sochi']
# # print(random.choice(city_list))
# # print(random.choices(city_list, k=3))
# random.shuffle(city_list)
# print(city_list)
# lst = [ '5', '4', '3', '2', '1']
# print(len(lst))
# print(sum((lst)))
# print(min(lst))
# print(max(lst))
#
# mas = [random.randint(0, 20) for i in range(10)]
# print(mas)
# m = max(mas)
# print(m)
# mas.insert(0, m)
# print(mas)
# lst = []
# print(bool(lst))
# if not lst:
#           print("not found")
# else:
# #           print("Have some elements")
# import random
# n1 = int(input("Введите размер первого списка"))
# n2 = int(input("Введите размер второго списка"))
# a = [random.randint(0, 10) for i in range(n1)]
# b = [random.randint(0, 10) for i in range(n2)]
# print(a)
# print(b)
# c = a + b
# print(c)


# d = []
# for element in a:
#     if element not in b and element not in d:
#         d.append(element)
# for element in b:
#        if element not in d:
#            d.append(element)
# print('Елементы списка без повторений ',d)

# c = []
# for i in a:
#     if i in b and i not in c :
#         c.append(i)
# print('элементы общие в двух списках',c)
# c = [min(a), min(b), max(a), max(b)]
# print(c)

# m = [
#     [1, 2, 3, 4],
#     [5, 6, 7, 8],
#     [9, 10, 11, 12]
# ]
# m = ["Hello","world"]

# print(m)
# print(len(m))
# print(m[1][2])#получение доступа к 7
# for row in range(len(m)):
#     # print(m[row])
#     for col in range(len(m[row])):
#         print(m[row][col], end="\t")
#     print()
# for row in m:
#     for x in row:
#         print(x,end="\t")
#     print()
# import random
# w,h = 4, 3
# matrix = [[random.randint(-20, 10) for x in range(w)] for y in range(h)]
# # matrix = []
# for y in range(h):
#     new_row = []
#     for x in range(w):
#         new_row.append(0)
#     matrix.append((new_row))
# print(matrix)
# m = 0
# for row in matrix:
#      for x in row:
#         print(x,end="\t")
#         if x < 0:
#             m += 1
#
#
#      print()
# print(m)


# for x, y in [[1, 6], [3, 6], [5, 2], [ 7, 4]]:
#     print(x, "+", y ,"=",x+y)

# w,h = 4, 3
# matrix = [[input("->") for x in range(w)] for y in range(h)]
# for row in matrix:
#       for x in row:
#         print(x,end="\t")
# print()

# import math
# nul1 = math.sqrt(144)#корень числа
# nul2 = math.ceil(3.1)#округлить в большую стороны
# nul3 = math.floor(3.8)#округлить в меньшую стороны
# print(nul1)
# print(nul2)
# print(nul3)
# print(math.pi)
#
# import math as m
# from math import *
#
# nul1 = sqrt(144)
# nul2 = ceil(5.8
#             )
# print(nul1)
# print(nul2)

import time
# sec = time.time()
# print(sec)
# local_time = time.ctime(sec)
# print(local_time)
#
# res = time.localtime()
# print(res)
# print(time.strftime(" today December %B %d %Y"))
#
# start = time.time()
# time.sleep(2)
# finish = time.time()
# res = finish - start
# print(res)

# Function
# def hello(name):#аргументы
#     print("hello",name)
# hello()#параметры
# hello("Igor")
# hello("Gleb")

# def getSum(a, b):
#     print(a + b)
#
# x = 2
# y = 5
# getSum(x, y )

# def getSum(a, b):
#     return  a + b
#
# x = 2
# y = 5
# res = getSum(x, y)
# print(res)

# def maximum(one, two):
#     if one > two:
#         return one
#     else:
#         return two
#
# print(maximum(9, 16))

# def zeb(a, b):
#     if a > b:
#         return a - b
#     else:
#         return a + b
# print(zeb(int(input()), int(input())))

# def cube(a):
#     return a ** 3
#
# for i in range(1, 11):
#     print(i)
#
# def change(lst):
#
#     symbol = lst.pop(0)
#     # print(str(lst))
#     print(lst)
#     return symbol
#
# print(change([1, 2, 3]))
# print(change([9, 12, 33, 54, 105]))
# print(change(['c', 'k', 'o', 'i']))
#
#
#
# def get_sum (a, b, c =0,d =1):
#     return a+b+c+d
#
#
# print(get_sum(1,2,3,4))
# print(get_sum(1,2,3))
# print(get_sum(1, 5))
# print(get_sum(1,4,d=2))
# n1 = 1
# n2 = 5
# n4 = 2
# print(get_sum(n1,n2,d=n4))

# def set_param(c=20, s ="-"):
#         print(s*c)
#
#
# set_param()
# set_param(7)
# set_param(s="#")

# def digit_sum(n,even = True):# Cумма четных чисел
#     s = 0
#     while n > 0:
#         current = n % 10
#         if  even and current % 2 == 0:
#             s += current
#         if not even and current % 2:
#             s += current
#         n //= 10
#     return s
#
#
# print("Cумма четных чисел")
# print(digit_sum(9874023))
# print(digit_sum(38271))
# print(digit_sum(123456789))
# print("Cумма нечетных чисел")
# print(digit_sum(9874023, even=False))
# print(digit_sum(38271 , even=False))
# print(digit_sum(123456789,even=False))


# t = (10,111,[1,2,3],[4,5,6],["hi","you"])#кортеж
# print(t,id(t))
# t[4][0]="new"
# print(t,id(t))

# t =( 1,2,3)
# x,y,z = t
# print(x,y,z)

# tp = (1, 2, 3,4,5,6)
# print(tp)
# lst = list(tp)
# print(lst)
# ptl = tuple(lst)
# del ptl
# print(ptl)

# countries = (
#     ("Germany", 80.2 ,(("Berlin", 3.326),("Gambutg",1.718))),
#     ("France",66,(("Paris",2.2),("Marsel",1.6)))
# )
# print(countries , end="\n\n")
#
#
#
# for country in countries:
#     country_name,country_population,cities = country
#     print("\nСтрана",country_name,"\nНаселение:",country_population,)
#     for city in cities:
#         city_name,city_population = city
#         print("\tГород:",city_name,"\tНаселение",city_population)




