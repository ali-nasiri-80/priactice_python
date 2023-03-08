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
# -----------------------------------------------------------------------------------

