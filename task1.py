#1-Programs that read a string and the number of repetitions, the string as a number
# Entered, it repeats and displays) the purpose of the program is to use
# The * operator is for repeating the string.
# s=input("Enter a string:")
# rep = int(input("Enter the repeat:"))
# print(s * rep)
#end
# -----------------------------------------------------------
#2-A program that reads two numbers and gives the complex equivalent
# a = int(input("Enter the real part :"))
# b = int(input("Enter the image part :"))
# complex1 = complex(a,b)
# print(complex1)
#end
#--------------------------------------------------------------
# 3-A program that reads the student's number and GPA and finds the highest GPA along 
# with the student's number
# id1 = -1
# max1 = -1
# max2 = -1
# id2 = -1
# n = int(input("Enter n:"))
# if n <2:
#     print("Please enter a number greater than 1")
# else:
#     for i in range(1,n+1):
#         id = int(input("Enter id:"))
#         aver = float(input("Enter average:"))
#         if aver > max1:
#             id2 = id1
#             max2 = max1
#             max1 = aver
#             id1 = id
#         else:
#             if aver > max2:
#                 max2 = aver
#                 id2 = id

#     print("Max2=",max2,'\t',"Id2=",id2)
#end
#-----------------------------------------------------------------------------
#4-A program that determines whether this number is whole or not
# while True:
#     num = int(input("Enter the number "))
#     sum=0
#     for i in range(1,num):
#         if(num % i == 0):
#             sum = sum + i
#     if(sum == num):
#         print("tom")
#     else:
#         print("not tom")
#     a = input("DO you want continu?:(y,n)")
#     if(a == "n"):
#         break
#------------------------------------------------------------------------------
#5-A program that generates n terms of the Fibonacci series.
# f1 = 1
# f2 = 1
# n = int(input("Enter the number:"))
# if n == 1:
#     print(f1)
#     exit(0) 
# elif n == 2:
#     print(f1)
#     print(f2)
# else:
#     print(f1)
#     print(f2)
#     i = 3
#     while i<=n:
#         f3 = f1 + f2
#         print(f3,"  ")
#         f1 = f2
#         f2 = f3
#         i = i + 1
#-----------------------------------------------------------------------------------
#6-Write a program that takes a string and creates a space between each character
# s = input("Enter the string:")
# for i in s:
#     print(i,end="  ")
#---------------------------------------------------------------------------------------
#7-A program that reads the user's birth year and the current year from input, determines how many years,
#months, days, hours, minutes, and seconds he has lived.

# byy = int(input("Enter brith data(year):"))
# bmm = int(input("Enter brith data(month):"))
# bdd = int(input("Enter brth data(day):"))
# cyy = int(input("Enter current data(year):"))
# cmm = int(input("Enter current data(month):"))
# cdd = int(input("Enter current data(day):"))
# if cdd < bdd:
#     cmm-=1
#     cdd += 30
# day = cdd - bdd
# if cmm < bmm:
#     cyy -= 1
#     cdd += 30
# month = cmm - bmm
# year = cyy - byy
# days = day + month * 30 + year * 36
# hh = day + 24
# mm = hh * 60
# ss = mm * 60
# print("Old is :{0}/{1}/{2}",year,month,day)
# print("Hour is(hh:mm:ss):{0}:{1}:{2}",hh,mm,ss)
#---------------------------------------------------------------------------------------------------------------
#8-Write a program that receives three numbers from the user and sorts them in ascending order
#a = int(input("Enter the number 1:"))
#b = int(input("Enter the number 2:"))
#c = int(input("Enter the number 3:"))
#
#if  a > b :
#    temp = a
#    a = b 
#    b = temp
#if a > c :
#    temp = a
#    a = c 
#    c = temp
#if b > c:
#    temp = b
#    b = c 
#    c = temp
#print("sorted is ",a,b,c)
#-------------------------------------------------------------------------------------------------------------------
#9-Write a program that performs the Fibonacci series with a recursive function
# def fibo(n):
#     if (n==1):
#         return (1)
#     if (n==2):
#         return (1)
#     return (fibo(n-2) + fibo(n-1))
# def main():
#     n = int(input("Enter n sri:"))
#     print("Result is :")
#     for i in range(1 , n+1):
#         print(fibo(i),end=" ")
# main()
#------------------------------------------------------------------------------------------------------------------
