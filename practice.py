print("Hello Mindcoders!")

# Adtya

'''
iwuebv aiweubv oiwquebv oiqwebuvoiquwebv iuqubwev 
'''

# print("Hello")
# print("How")
# print("Are")
# print("You")
# print("Adtya")

# age = 4
# print(age)
# print(type(age))

# age = "Four"
# print(age)
# print(type(age))

# name = "Aditya"
# profession = "Software developer"
# experience = 10
# print("Hello, I am", name, ". I am a ", profession, " professionally. And I have around ", experience, " years of experience with it!")

# x = 5
# print(x, type(x))
# x = "Hello World"
# print(x, type(x))
# x = 20
# print(x, type(x))
# x = 20.5
# print(x, type(x))
# x = 1j
# print(x, type(x))
# x = ["apple", "banana", "cherry", 3]
# print(x, type(x))
# x = ("apple", "banana", "cherry")
# print(x, type(x))
# x = range(6)
# print(x, type(x))
# x = {"name" : "John", "age" : 36}
# print(x, type(x))
# x = {"apple", "banana", "cherry", "apple"}
# print(x, type(x))
# x = frozenset({"apple", "banana", "cherry"})
# print(x, type(x))
# x = True		
# print(x, type(x))				
# x = b"Hello"
# print(x, type(x))
# x = bytearray(5)				
# print(x, type(x))
# x = memoryview(bytes(5))		
# print(x, type(x))
# x = None
# print(x, type(x))

#Operators

# print("10 + 2 = ", 10 + 2)
# print("10 - 2 = ", 10 - 2)
# print("10 * 2 = ", 10 * 2)
# print("10 / 2 = ", 10 / 2)
# print("10 % 2 = ", 10 % 2)
# print("9 % 5 = ", 9 % 5)
# print("10 // 3 = ", 10 // 3)
# print("2 ** 3 = ", 2 ** 3)

'''
    x       y       x & y
    0       0       0
    1       0       0
    0       1       0
    1       1       1

    x       y       x | y
    0       0       0
    1       0       1
    0       1       1
    1       1       1


0010 1010   => 5
1100 1101   => 2
----------
0000 1000   => 

'''

# print(5 & 3)
# x = 5
# print(x)
# x += 3
# print(x)
# x -= 2
# print(x)
# x *= 3
# print(x)
# x /= 2
# print(x)
# x //=3
# print(x)
# x **= 2
# print(x)
# x = 5
# x %= 3
# print(x)
# x |= 2
# print(x)
# x ^= 3
# print(x)


# a = 10
# b = 20

# print("a == b: ", a == b)
# print("a == 10: ", a == 10)

# print("a != b: ", a != b)
# print("a != 10: ", a != 10)

# print("a > b: ", a > b)
# print("a < b: ", a < b)

# print("a <= b: ", a <= b)
# print("a >= b: ", a >= b)
# print("a >= 10: ", a >= 10)

# x = 3

# print(x < 5 and x < 10)
# print(x < 5 or x < 4)
# print(not(x < 5 and x < 10))

# y = 3 #4

# print(x is y)
# print(x is not y)

# x = int(input("Enter first value for sum: "))
# y = int(input("Enter second value for sum: "))
# x = input("Enter first value for sum: ")
# y = input("Enter second value for sum: ")
# z = x + y
# z = int(x) + int(y)
# print("Sum: ",z)

# print(1 + "2")
# print("1" + 2)
# int(x + y)

# p = 5
# b = 5

# h = (((p ** 2) + (b ** 2)) ** (1/2))
# print(h)

# print("+----------+")
# print("|          |")
# print("|          |")
# print("|          |")
# print("|          |")
# print("|          |")
# print("+----------+")


# print("+" + "-" * 10 + "+")
# print(("|" + " " * 10 + "|\n") * 5, end="")
# print("+" + "-" * 10 + "+")

# print("Hello How are you?", end="\n")
# print("I am good")

# city = 'Bhopal'
#       012345   ← index positions
#      -6-5-4-3-2-1  ← negative indices (from end)
 
# print(city[0])     # B   (first character)
# print(city[-6])
# print(city[2])     # o
# print(city[-1])    # l   (last character)
# print(city[-3])    # p

# print(2 == 2)
# print(2 == 2.0)

# var = 0  # Assigning 0 to var
# print(var == 0)

# var = 1  # Assigning 1 to var
# print(var == 0)

# print(("+" + "-" * 10 + "+" + "\n")+ (("|" + ' ' * 10 + "|\n")*5) + ("+" + "-" * 10 + "+") )

# var = 11

# if var == 11:
#     print("Var is 11")
# print("Hello")

# number1 = int(input("Enter the first number: "))
# number2 = int(input("Enter the second number: "))

# # if number1 > number2:
# #     larger_number = number1
# # else:
# #     larger_number = number2

# if number1 > number2: larger_number = number1
# else: larger_number = number2

# print("The larger number is:", larger_number)


# number1 = int(input("Enter the first number: "))
# number2 = int(input("Enter the second number: "))
# number3 = int(input("Enter the third number: "))
 
# largest_number = number1
 
# if number2 > largest_number:
#     largest_number = number2
 
# if number3 > largest_number:
#     largest_number = number3
# largest_number = max(number1, number2, number3)
# lowest_number = min(number1, number2, number3)

 
# print("The largest number is:", largest_number)
# print("The lowest number is:", lowest_number)

# while True:
#     print("I'm stuck inside a loop.")

# largest_number = -999999999

# number = int(input("Enter a number or type -1 to stop: "))
 
# while number != -1:
#     if number > largest_number:
#         largest_number = number
#     number = int(input("Enter a number or type -1 to stop: "))
 
# print("The largest number is:", largest_number)

'''
input -> num
num -> check => even and odd
check -> even_count, odd_count
num = 0 -> exit
'''

# num = int(input("Please enter a number:"))
# even_count = 0
# odd_count = 0
# while num != 0:
#     if num % 2 == 0:
#         even_count += 1 # even_count = even_count + 1
#     else:
#         odd_count += 1
    
#     num = int(input("Please enter a number:"))

# print("Even:", even_count)
# print("Odd:", odd_count)

# print(bool(5))
# print(bool(1))
# print(bool(-1))
# print(bool(0))

# print(bool("a"))
# print(bool("b"))
# print(bool(" "))
# print(bool(""))

# print(bool())
# print(bool(None))
# print(bool(NULL))
# print(bool(Null))

# counter = 5
# while counter != 0:
#     print("Inside the loop.", counter)
#     counter -= 1
# print("Outside the loop.", counter)

# counter = 5
# while counter:
#     print("Inside the loop.", counter)
#     counter -= 1
# print("Outside the loop.", counter)	


# print(range(100))

# for counter in range(10):
#     print("Counter :", counter)

# for counter in range(2, 8):
#     print("Counter: ", counter)

# print("The break instruction:")
# for counter in range(1, 6):
#     if counter == 3:
#         continue
#     print("Inside the loop.", counter)
# print("Outside the loop.")

# largest_number = -99999999
# counter = 0
# while True:
#     number = int(input("Enter a number or type -1 to end the program: "))
#     if number == -1:
#         break
#     counter += 1
#     if number > largest_number:
#         largest_number = number

# if counter != 0:
#     print("The largest number is", largest_number)
# else:
#     print("You haven't entered any number.")

# largest_number = -99999999
# counter = 0
# number = int(input("Enter a number or type -1 to end program: "))
# while number != -1:
#     # if number == -1:
#     #     continue
#     counter += 1
#     if number > largest_number:
#         largest_number = number
#     number = int(input("Enter a number or type -1 to end the program: "))

# if counter:
#     print("The largest number is", largest_number)
# else:
#     print("You haven't entered any number.")

# counter = 1
# while counter < 5:
#     print(counter)
#     counter += 1
# else:
#     print("else:", counter)

# for counter in range(5):
#     print(counter)
# else:
#     print("else:", counter)

# counter = 111
# for counter in range(2, 1):
#     print(counter)
# else:
#     print("else:", counter)

# blocks = int(input("Enter number of blocks:"))
# counter = 0
# while(blocks - counter > 0):
#     counter += 1
#     blocks = blocks - counter
    

# print(f'Hieght of the Pyramid: {counter}')

# print("Hello How are you",counter, "wefjb", blocks)

'''
blocks      13  12  10  7   3
counter     1   2   3   4   5
'''
# git add *
# git commit -m "Explain the commit here"
# git push

# Lists
# numbers = []        # Declaration
# numbers = [10, 5, 7, 2, 1]  # Declaration & Initialisation

# print(numbers)
# print(type(numbers))

# print(numbers[0])#Reading an element
# print(numbers[1])
# print(numbers[2])
# print(numbers[3])
# print(numbers[4])
# #print(numbers[5])

# numbers[0] = 100    # Writing an element
# print(numbers)

# numbers = [10, 5, 7, 2, 1]
# print("Original list contents:", numbers)  # Printing original list contents. 
# numbers[0] = 111
# print("New list contents: ", numbers)  # Current list contents.

# print("Original list contents:", numbers)  # Printing original list contents.
# numbers[1] = numbers[4]  # Copying value of the fifth element to the second.
# print("New list contents:", numbers)  # Printing current list contents.

# print(numbers)
# print(len(numbers))

# del numbers[1]

# print(numbers)
# print(len(numbers))

# numbers = [111, 7, 2, 1, " "]
# print(numbers[-1])

# print(numbers[-2])

# print(numbers[-4])
# # print(numbers[-5])

# print(numbers[4])

# print(numbers[len(numbers) * -1])

# list = [5,4,3,2,1]
# print(list)
# print(f'Length of List:{len(list)}')
# list.append(6)
# print(list)
# print(f'Length of List:{len(list)}')

# # print("Hello How are you?"+list)
# print(f'efiuh uwhefiuhwef {list}')

# numbers = [111, 7, 2, 1]
# print(len(numbers))
# print(numbers)

# numbers.append(4)

# print(len(numbers))
# print(numbers)

# numbers.insert(0, 222)
# print(len(numbers))
# print(numbers)

# my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# for count in range(len(my_list)):
# 	print(my_list[count])

my_list = []
# for count in range(1, 11):
#     my_list.append(count)
# print(my_list)

# for count in range(1, 11):
#     my_list.insert(count-1, count)
# print(my_list)

# count = 1
# while count<=10:
#     my_list.append(count)
#     count += 1
# print(my_list)

# my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]  # Creating an empty list.
# for count in range(10):
#     my_list[count] += 1
# print(my_list)

# my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# # Print the sum of all elements from the list
# sum = 0
# # for index in range(len(my_list)):
# #     sum += my_list[index]

# for element in my_list:
#     sum += element

# print("Sum:", sum)

# a = 10
# b = 20
# print("a:", a)
# print("b:", b)
# #
# a, b = b, a
# print("a:", a)
# print("b:", b)

# my_list = [10, 1, 8, 3, 5]
# print(my_list)
# my_list[0], my_list[4] = my_list[4], my_list[0]
# my_list[1], my_list[3] = my_list[3], my_list[1]
# print(my_list)

'''
index = 0 => my_list[index] => 8
index +1 => my_list[index + 1] => 10

compare my_list[index] > my_list[index + 1]
    swap

index += 1

my_list[index] => 10
my_list[index + 1] => 6



my_list[index]
'''
# my_list = [8, 10, 6, 9, 2, 4, 5, 1, 3, 7]
# my_list = [1, 2, 3, 4, 5]
# swapped = 0
# print(my_list)
# count = 0
# for index1 in range(len(my_list) - 1):
#     for index in range(len(my_list) - 1 - index1):
#         count += 1
#         if( my_list[index] > my_list[index + 1] ):
#             my_list[index], my_list[index + 1] = my_list[index + 1], my_list[index]
#             swapped = 1
#     if swapped == 0:
#         break

# print(my_list)
# print("My program has run for :", count, "times")

'''
4   => 5th element sorted
3   => 4th element sorted
2   => 3rd element sorted
1   => 2nd element sorted
'''

# my_list = [8, 10, 6, 2, 4]  # list to sort
# my_list = [1, 2, 3, 4, 5]
# swapped = True  # It's a little fake, we need it to enter the while loop.
# count = 0
# while swapped:
#     swapped = False  # no swaps so far
#     for i in range(len(my_list) - 1):
#         count += 1
#         if my_list[i] > my_list[i + 1]:
#             swapped = True  # a swap occurred!
#             my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]
# print(my_list)
# print("Loops are running for :", count, "Times")

'''
[8, 6, 2, 4, 10] => 10 > 4 => swapping
swapped     True    False   True    True
i(0-4)      0   1   2   3
'''

# my_list = [8, 10, 6, 2, 4]
# my_list.sort()
# print(my_list)


lst = [5, 3, 1, 2, 4]
# print(lst)
# lst.reverse()
# print(lst)  # outputs: [4, 2, 1, 3, 5]

'''
length = x
[a, b, c, d, e, f, g]
[g, f, e, d, c, b, a]

0 - -1
1 - -2
-1 * (index +1)

[ a, b, c, d, e, f, g, h, i, j]
loop => 5
a = j
0 = -1 => (-1 * (index + 1))
index = (-1 * (index + 1))

index = len(lst) - (index + 1)
'''

# print(len(lst)//2)

# print(lst)
# for index in range(len(lst)//2):
#     # print(lst[index])
#     # lst[index], lst[(-1 * (index +1))] = lst[(-1 * (index +1))], lst[index]
#     lst[index], lst[len(lst) - (index + 1)] = lst[len(lst) - (index + 1)], lst[index]
# print(lst)

# lst = ["D", "F", "a", "Z"]
# lst.sort()
 
# print(lst)

# print("A" > "a")

# a = 3
# b = 1
# c = 2
# lst = [a, c, b]
# lst.sort()
# print(lst)

# a = "A"
# b = "B"
# c = "C"
# d = " "
# lst = [a, b, c, d]
# lst.reverse()
# print(lst)

# list_1 = [1]
# list_2 = list_1 # refrence copy
# list_1[0] = 2
# print(list_2)   #

# a = 1
# b = a
# a = 2
# print(a)
# print(b)

# list_1 = [1, 2, 3, 4]
# list_2 = list_1[0:2]
# list_1[0] = 2
# print("list_2:", list_2)
# print("list_1:", list_1)


# my_list = [10, 8, 6, 4, 2]
# new_list = my_list[1:3]
# print(new_list)

# new_list = my_list[1:-1]
# print(new_list)

# new_list = my_list[-1:1]
# print(new_list)

# print(ord("A"))

# my_list = [10, 8, 6, 4, 2]
# del my_list
# print(my_list)


# my_list = [0, 3, 12, 8, 2]
# print(5 in my_list)
# print(5 not in my_list)
# print(12 in my_list)

# lst = [3, 11, 5, 1, 9, 7, 15, 17, 13]
# for i in range(len(lst)):
#     if lst[i]>lst[i+1]:
#         break
# print("largest no.",lst[i])

# my_list = [17, 3, 11, 5, 1, 9, 7, 15, 13]
# largest = my_list[0]
# # for index in range(1, len(my_list)):
# #     if largest < my_list[index]:
# #         largest = my_list[index]

# for element in my_list:
#     if largest < element:
#         largest = element

# print(largest)

# my_list = [17, 3, 11, 1, 9, 7, 15, 13, 25]
# # Search for 5 and print its index
# found = -1
# for index in range(len(my_list)):
#     if my_list[index] == 5:
#         found = index
#         break

# if found < 0:
#     print("5 not found in the list")
# else:
#     print("5 is found at ", found)

# print("HEllo")
# print("HEllo")
# print("HEllo")
# print("HEllo")

# age = 10
# Age = 20

# myFriendsName = "LuvKush"       # Camel case
# my_friends_name = "LuvKush"     # Snake case

# myFriendsName()
# my_friends_name()

# MyFriendsName
# My_Friends_Name

# age = 4
# print(age)
# print("Hello")

# x = 5
# print(x)
# print(type(x))
# x = "Hello World"						
# print(x)
# print(type(x))
# x = 20.5	
# print(x)
# print(type(x))						
# x = 1j		
# print(x)
# print(type(x))						
# x = ["apple", "banana", "cherry"]	
# print(x)
# print(type(x))
# x = ("apple", "banana", "cherry")	
# print(x)
# print(type(x))
# x = range(6)
# print(x)
# print(type(x))						
# x = {"name" : "John", "age" : 36}	
# print(x)
# print(type(x))
# x = {"apple", "banana", "cherry"}	
# print(x)
# print(type(x))
# x = frozenset({"apple", "banana", "cherry"})	
# print(x)
# print(type(x))
# x = True								
# print(x)
# print(type(x))
# x = b"Hello"							
# print(x)
# print(type(x))
# x = bytearray(5)						
# print(x)
# print(type(x))
# x = memoryview(bytes(5))				
# print(x)
# print(type(x))
# x = None								
# print(x)
# print(type(x))

# student_name = "Khushi"
# age = 10
# marks = 4

# print("Student:", student_name, "Age:", age, "Marks:", marks)

# print(f'Student: {student_name}, Age: {age}, Marks:{marks}')

# x = y = z = 0
# print(x)
# print(y)
# print(z)
# a, b, c = 10, 20, 30
# print(a)
# print(b)
# print(c)

# print(10 // 4)
# print(9 % 4)
# print(2 ** 3)

# monthly_salary = float(input('Monthly salary (Rs.): '))
# annual_salary  = monthly_salary * 12
# daily_salary   = monthly_salary / 30
# tax = annual_salary * 0.10  # 10% tax
# print(f'Annual: Rs.{annual_salary:,.0f}')
# print(f'Daily:  Rs.{daily_salary:,.2f}')
# print(f'Tax:    Rs.{tax:,.2f}')
# print(f'Net:    Rs.{annual_salary - tax:,.0f}')

# a = 10

# # a += 1      #a = a + 1
# # print(a)
# # a %= 3
# # print(a)

# b = 20

# print(a == b)
# print(a != b)
# print(a == 10)
# print(a < b)
# print(a > b)
# print(a <= b)
# print(a >= b)

# print(2 << 1)
# print()
# c = 2
# c <<= 2 # c = c << 2

# && => and => multiplication

'''
a   b   a and b
T   F   F
F   T   F
T   T   T
F   F   F

a   b   a or b
T   F   T
F   T   T
T   T   T
F   F   F
'''

a = 20
b = 30

# print(a < b and a == 20)
# print(a > b and a == 20)

# print(a < b or a == 20)
# print(a > b or a == 20)

# print(not(a < b and a == 20))
# print(not(a > b and a == 20))

# print(a is b)
# print(a is not b)

# x = 10      #["Maruti", "BMW"]
# y = 10      #["Maruti", "BMW"]
# z = x

# print(x is y)
# print(x is z)
# print(y is z)

# print(x is not y)
# print(x is not z)
# print(y is not z)

# x = ["Maruti", "BMW"]

# maruti = "Maruti"

# print("Maruti" in x)
# print(maruti in x)
# print("Maruti1" in x)
# print("Maruti" not in x)

'''
0 1 2 3 4 5 6 7 8 9
=> 10
0 1 => 2
0 1 2 3 4 5 6 7 => 8 Octal
0 1 2 3 4 5 6 7 8 9 A B C D E F => 16
--------
1 => 0000 0001 => 8-bit
2 => 0000 0010
3 => 0000 0011

a = 10
a & 2 => 10 & 2
10 => 0000 1010
2 =>  0000 0010
    x
     ----------
     0000 0010

'''
# print(10 & 2)
# print(10 ^ 2)

# number1 = input("Enter a number:")
# print(number1)
# print(type(number1))
# # print(number1 + 10)

# number1 = int(number1)
# print(number1)
# print(type(number1))
# print(number1 + 10)

# print("Hello" + ", how are you?")

# x = int(input("Enter first value for sum: "))
# y = int(input("Enter second value for sum: "))
# z = x + y
# print("Sum: ",z)

# name = input('Enter your name: ')          # Returns str
# age  = int(input('Enter your age: '))      # Convert to int
# gpa  = float(input('Enter your GPA: '))    # Convert to float
# print(name)
# print(type(name))
# print(age)
# print(type(age))
# print(gpa)
# print(type(gpa))

# leg_a = float(input("Input first leg length: "))
# leg_b = float(input("Input second leg length: "))
# hypo = ((leg_a**2) + (leg_b**2)) ** .5
# print("Hypotenuse length is", hypo)

# print("+--------+")
# print("|        |")
# print("|        |")
# print("|        |")
# print("|        |")
# print("+--------+")

# str = "-" * 10
# print(str)

# print("123", end="--")
# print("789", end="--")
# print("456")


# print("+" + 10 * "-" + "+")
# print(("|" + " " * 10 + "|\n") * 5, end="")
# print("+" + 10 * "-" + "+")

# city = 'Bhopal'
# #       012345   		← index positions
# #      -6-5-4-3-2-1  	← negative indices (from end)
 
# print(city[0])     # B   (first character)
# print(city[2])     # o
# print(city[-1])    # l   (last character)
# print(city[-3])    # p

# Slicing: string[start:stop:step]
# name = 'Priya Sharma'
# print(name[0:5])   # Priya  (index 0 to 4)
# print(name[6:])    # Sharma (from index 6 to end)
# print(name[:5])    # Priya  (from start to index 4)
# print(name[::2])   # Pay hr  (every 2nd character)
# print(name[::-1])  # amrahS ayirP  (reversed!)
 
# # Length of string
# print(len(city))   # 6
# print(len(name))   # 12

# text = '  Hello python World!  '
 
# # Case
# print(text.upper())           # '  HELLO PYTHON WORLD!  '
# print(text.lower())           # '  hello python world!  '
# print(text.title())           # '  Hello Python World!  '
# print(text.capitalize())      # '  hello python world!  ' → first only
 
# # Strip whitespace
# print(text.strip())           # 'Hello Python World!'
 
# # Search
# print('python' in text)       # True
# print(text.find('python'))    # 8  (index where found, -1 if not found)
# print(text.count('l'))        # 3

# str = "hello how are YOU?"
# print(str.capitalize())
# text = '  Hello python World!  '
# # Replace
# print(text.replace('Python', 'AI'))  # '  Hello AI World!  '
 
# # Split and Join
# csv = 'Rahul,22,Bhopal,Engineer'
# print(csv.split('a'))
# parts = csv.split(',')        # ['Rahul', '22', 'Bhopal', 'Engineer']
# print("parts: ",parts)
# print(parts[0])               # Rahul
# rejoined = ' | '.join(parts)  # 'Rahul | 22 | Bhopal | Engineer'
# print("rejoined: ", rejoined)

# # Check content
# print('hello123'.isalnum())   # True — all letters/digits
# print('hello123*'.isalnum())   # True — all letters/digits
# print('12345'.isdigit())      # True — all digits
# print('Python'.isalpha())     # True — all letters
# print('  '.isspace())         # True — all spaces

# # Start/end check
# email = 'student@gmail.com'
# # a@b.c
# print(email.endswith('.com'))  # True
# print(email.startswith('stu')) # True

# name, marks, rank = 'Anita', 92.567, 3
# print(name, marks, rank)

# # Basic
# print(f'Hello, {name}!')
 
# # Format numbers
# print(f'Marks: {marks:.2f}')       # 92.57 (2 decimal places)
# print(f'Marks: {marks:.0f}')       # 93    (rounded)
# print(f'Count: {1000000:,}')       # 1,000,000 (comma separator)
 
# # Padding and alignment
# print(f'{name:<15}|{marks:>8.2f}|Rank:{rank}')  # left/right align
# # Anita          |   92.57|Rank:3
# name = "Adtya Gupta"
# print(f'{name:<15}|{marks:>8.2f}|Rank:{rank}')  # left/right align
 
# # Expressions inside {}
# price, gst = 500, 0.18
# print(f'Price:Rs.{price} | GST:Rs.{price*gst:.2f} | Total:Rs.{price*(1+gst):.2f}')

# print(2 == 2.)
# var = 10
# print(var = 10)

#Comparision operators
'''
==
<
>
<=
>=

'''

# Read two numbers
# number1 = int(input("Enter the first number: "))
# number2 = int(input("Enter the second number: "))
 
# # Choose the larger number
# if number1 > number2: larger_number = number1
# else: larger_number = number2
 
# # Print the result
# print("The larger number is:", larger_number)



# Read three numbers
# number1 = int(input("Enter the first number: "))
# number2 = int(input("Enter the second number: "))
# number3 = int(input("Enter the third number: "))
 
# # We temporarily assume that the first number is the largest one. We will verify this soon.
# # largest_number = number1
 
# # We check if the second number is larger than the current largest_number and update the largest_number if needed.
# # if number2 > largest_number:
# #     largest_number = number2
 
# # # We check if the third number is larger than the current largest_number and update the largest_number if needed.
# # if number3 > largest_number:
# #     largest_number = number3

# largest_number = max(number1, number2, number3)
# lowest_number = min(number1, number2, number3)


# # Print the result
# print("The largest number is:", largest_number)
# print("The lowest number is:", lowest_number)

'''
30  largest
20  
10  

'''

# while True:
#     print("I'm stuck inside a loop.")

# Store the current largest number here.
# largest_number = -999999999
 
# number = int(input("Enter a number or type -1 to stop: "))
 
# while number != -1:   
#     if number > largest_number:
#         largest_number = number
#     number = int(input("Enter a number or type -1 to stop: "))
 
# print("The largest number is:", largest_number)

# counter = 0
# while counter < 100:
#     print(counter)
#     counter += 1

# counter = 0
# for counter in range(100):
#     print(counter)

# '''
# counter     0   1   2... 99     100
# output      0   1   2... 99
# '''

# exit = 1

# while exit != 0:
#     exit = int(input("Enter number:"))
#     print(exit)

# for counter in range(10):
#     print("The value of counter is currently", counter)
#                   start, end, step
# for counter in range(2, 8):
#     print("The value of counter is currently: ", counter)

# for counter in range(2, 8, 3):
#     print("The value of counter is currently: ", counter)

# power = 1
# for expo in range(16):
#     print("2 to the power of", expo, "is", power)
#     power *= 2
#     if expo == 7:
#         break

# power = 1
# for expo in range(16):
#     if expo == 7:
#         continue
#     print("2 to the power of", expo, "is", power)
#     power *= 2
    

# print("---------Now I am out---------")

# print("The break instruction:")
# for counter in range(1, 6):
#     if counter == 3:
#         break
#     print("Inside the loop.", counter)
# print("Outside the loop.")

# print("\nThe continue instruction:")
# for counter in range(1, 6):
#     if counter == 3:
#         continue
#     print("Inside the loop.", counter)
# print("Outside the loop.")

# largest_number = -99999999
# counter = 0

# while True:
#     number = int(input("Enter a number or type -1 to end the program: "))
#     if number == -1:
#         break
#     counter += 1
#     if number > largest_number:
#         largest_number = number

# if counter != 0:
#     print("The largest number is", largest_number)
# else:
#     print("You haven't entered any number.")

# i = 1
# j = not not i
# print(i)
# print(j)

'''
Truthy:     1, 2, 3, -1, -20, "a", "Hello", [1, 2], {1:1}, " "
Falsy:      0, "", [], {}, (), None, NULL

numbers[0] = address in numbers + (size of element * index)
             0x0000 + (2 * 0) => 0x0000
             0x0000 + 2 => 0x0002

'''

# numbers = [10, 5, 7, 2, 1]
# print(numbers)
# print(type(numbers))

# print(numbers[0])
# print(numbers[1])
# print(numbers[2])
# print(numbers[3])

# numbers[3] = 20
# print(numbers)

# numbers[2] = numbers[0]
# print(numbers)

# numbers[2], numbers[1] = numbers[1], numbers[2]
# print(numbers)
# numbers = [10, 5, 7, 2, 1]
# print(len(numbers))
# del numbers[4]
# print(len(numbers))
# print(numbers)

# print(len(numbers))

# lengthOfList = len(numbers)
# print(lengthOfList)

# print(numbers[-1])
# print(numbers[-2])
# print(numbers[-4])

# a = 10
# print("Variable a:", a)
# print("Address of Variable a in integer:", id(a))
# print("Address of Variable a in hex:", hex(id(a)))

# print(hex(id(numbers)))
# print(hex(id(numbers[0])))
# print(hex(id(numbers[1])))
# print(hex(id(numbers[2])))

# list = [5,4,3,2,1]
# print(len(list))
# print(list)

# list.append(6)
# print(len(list))
# print(list)

# list.insert(0, 222)
# print(len(list))
# print(list)

# list = [11, 21, 31, 41, 51, 61, 71, 81, 91, 101]
# '''
# list[0]
# list[1]
# list[2]
# list[3]
# list[4]
# '''

# for index in range(len(list)):
#     # print(i)
#     print(list[index])

# index = 0
# while index < len(list):
#     print(list[index])
#     index += 1


# list = []
'''
0 -> 1
1 -> 2
2 -> 3
.....
9 -> 10
'''
# list.append(1)
# list.append(2)
# list.append(3)
# list.append(4)
# list.append(5)    

# for iterator in range(1, 11):
    # print("---------")
    # print(iterator)
    # print("---------")
    # list.append(iterator+1)
    # list.append(iterator)

# print(list)

# my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

# for index in range(len(my_list)):
#     my_list[index] += 1

# print(my_list)

# sum = 0
# for index in range(len(my_list)):
#     sum = sum + my_list[index]

# print(sum)
# index = 0
# for abc in my_list:
#     print("my_list[",index,  "] => ",abc)
#     index += 1

# a = 10
# b = 20

# print("a: ", a)
# print("b: ", b)

# print("---------")

# b = a
# a = b

# temp = b
# b = a
# a = temp

# a, b = b, a

# print("a: ", a)
# print("b: ", b)

# my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

# print(my_list)
# # swap - 2nd and 5th values

# my_list[1], my_list[4] = my_list[4], my_list[1]
# print(my_list)
# list
# lst
# list = [8, 10, 6, 2, 4]
#[1, 3, 2, 4, 5]

# print(list)
# count = 0
# swapped = False
# for index in range(len(list) - 1):      # 4
#     for index_inner in range(len(list) - 1 - index):    #4
#         if list[index_inner] > list[index_inner + 1]:
#             list[index_inner], list[index_inner + 1] = list[index_inner + 1], list[index_inner]
#             swapped = True
#         count += 1
#     if not swapped:
#         break

# list.sort()
# # list = sorted(list)
# # list.sorted()
# print(list)
# list.reverse()
# print(list)

# lst = ["D", "F", "A", "Z"]
# lst.sort()
 
# print(lst)


# print(count)

'''
10 > 4
Dry Run
[8, 10, 6, 2, 4] - 4 => [8, 6, 2, 4, 10]
[8, 6, 2, 4, 10] - 3 =>
[]               - 2
                 - 1 =>
Current list        [8, 6, 2, 4, 10]

index(0-3)       0  
index_inner(0-3) 0  1   2   3
'''
# list = [8, 10, 6, 2, 4]
# list.sort()
# # list = sorted(list)
# print(list)
# list.reverse()
# print(list)

# lst = ["D", "F", "A", "Z"]
# lst.sort()
 
# print(lst)


# my_list = [0, 3, 12, 8, 2]
# print(5 in my_list)
# print(5 not in my_list)
# print(12 in my_list)

# row = []
# for i in range(8):
#     row.append("WHITE_PAWN")

# row = ["WHITE_PAWN" for i in range(8)]

# print(row)

#List comprehension

# squares = [x ** 2 for x in range(10)]

# print(squares)

# twos = [2 ** i for i in range(8)]

# print(twos)

# #[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
# odds = [x for x in squares if x % 2 != 0 ]

# print(odds)

# board = []
# for i in range(8):
#     row = ["EMPTY" for i in range(8)]
#     board.append(row)

# print(board)

# board[0][0] = "ROOK"
# board[0][7] = "ROOK"
# board[7][0] = "ROOK"
# board[7][7] = "ROOK"

# board[0][1] = "KNIGHT"
# board[0][6] = "KNIGHT"
# board[7][1] = "KNIGHT"
# board[7][6] = "KNIGHT"


# for index in range(len(board)):
#     print(board[index])

'''
index(7)       0    1

'''

'''
[['ROOK', 'KNIGHT', 'EMPTY', 'EMPTY', 'EMPTY', 'EMPTY', 'KNIGHT', 'ROOK']   0
['EMPTY', 'EMPTY', 'EMPTY', 'EMPTY', 'EMPTY', 'EMPTY', 'EMPTY', 'EMPTY']    1
['EMPTY', 'EMPTY', 'EMPTY', 'EMPTY', 'EMPTY', 'EMPTY', 'EMPTY', 'EMPTY']    2
['EMPTY', 'EMPTY', 'EMPTY', 'EMPTY', 'EMPTY', 'EMPTY', 'EMPTY', 'EMPTY']
['EMPTY', 'EMPTY', 'EMPTY', 'EMPTY', 'EMPTY', 'EMPTY', 'EMPTY', 'EMPTY']
['EMPTY', 'EMPTY', 'EMPTY', 'EMPTY', 'EMPTY', 'EMPTY', 'EMPTY', 'EMPTY']
['EMPTY', 'EMPTY', 'EMPTY', 'EMPTY', 'EMPTY', 'EMPTY', 'EMPTY', 'EMPTY']
['ROOK', 'KNIGHT', 'EMPTY', 'EMPTY', 'EMPTY', 'EMPTY', 'KNIGHT', 'ROOK']]

 Rooks
    0,0, | 0,7 | 7,0 | 7,7
'''

'''
Cafe Management
z
Dev - Devlopment / Dev Environment      dev.cafemanagement.com
Testing - Stage Environment             stage.cafemanagement.com
Client Testing - UAT environment        uat.cafemanagement.com
Users - Production Evironment           cafemanagement.com

Dev     - Development branch
        - feature/v1.0/khushi
        - bugfix/v1.1/khushi
|
stage   - stage branch
|
uat     - uat branch
|
Prod    - main branch

'''
# print("Checking branch changes!")
# print("Again checking changes!")

# temps = [[0.0 for h in range(24)] for d in range(31)]
# # print(temps)

# random = [20, 34, 44, 12, 34, 20, 34, 44, 12, 34, 20, 34, 44, 12, 34, 20, 34, 44, 12, 34, 20, 34, 44, 12, 34, 20, 34, 44, 12, 34, 45]
# print(len(random))

# for index in range(len(temps)):
#     temps[index][11] = random[index]

# for index in range(len(temps)):
#     print(temps[index])

# # calculate the average temperature of the month. 

# sum = 0
# for index in range(len(temps)):
#     sum += temps[index][11]

# print(sum/31)

# highest = 0
# for index in range(len(temps)):
#     for inner_index in range(len(temps[index])):
#         if highest < temps[index][inner_index]:
#             highest = temps[index][inner_index]

# print(highest)

# rooms = [[[False for r in range(20)] for f in range(15)] for t in range(3)]

# for building_index in range(len(rooms)):
#     print("Building ", building_index+1)
#     for floor_index in range(len(rooms[building_index])): 
#         print("Floor:", floor_index+1)
#         print(rooms[building_index][floor_index])

# in the second building, on the tenth floor, room 14:

# rooms[1][9][13] = True

# and release the second room on the fifth floor located in the first building:

# rooms[0][4][1] = False

# Check if there are any vacancies on the 15th floor of the third building

'''
buildings:      1       [2]
floors:         1       [14]
rooms:          20
'''
# rooms[2][14][0] = True
# rooms[2][14][1] = True
# rooms[2][14][2] = True
# rooms[2][14][3] = True
# rooms[2][14][4] = True
# rooms[2][14][5] = True

# temp = -1
# for room_index in range(len(rooms[2][14])):
#     if rooms[2][14][room_index] == False:
#         temp = room_index
#         break
#     # print(rooms[2][14][room_index])

# if temp == -1:
#     print("No Rooms available!")
# else:
#     print(f'{temp+1}th Room is available!')

# def message():
#     print("Enter a value: ")
#     a = int(input())
#     print(a)

# message()
# message()
# message()

# def message():
#     print("Enter a value: ")
 
# print("We start here.")
# message()
# print("We end here.")


# print("Enter a value: ")
# a = int(input())
# print(a)

# print("Enter a value: ")
# b = int(input())
# print(b)

# print("Enter a value: ")
# c = int(input())
# print(c)

# print("We start here.")

# print("We end here.") 
# def message():
#     print("Enter a value: ")
# message()

# message = 1
# print(message)
# message()

# def message():
#     print("Enter a value: ")
#     return
#     a = int(input())
    
# a = message()

# print(message())

# message()

# def hi(num):        #parameter
#     print("hi")
# hi(5)               #argument

# def hello(n): # defining a function
#     print("Hello,", n) # body of the function

# name = input("Enter your name: ")
# hello(name) # calling the function

# def message(number):
#     print("Enter a number:", number)

# message(1)

# def message(num):
#     print("number:", number)
#     print("num:", num)
 
# number = 1234
# message(1)
# print(number) 

# def message(what, number):
#     print("Enter", what, "number", number)
 
# message("telephone", 11)
# message("price", 5)
# message("number", "number")

# def print_grade(name, marks):
#     grade = ""
#     if marks < 50:
#         grade = "D"
#     elif marks < 60:
#         grade = "C"
#     elif marks < 75:
#         grade = "B"
#     elif marks < 90:
#         grade = "A"
#     elif marks >= 90:
#         grade = "A+"
#     print(f'Hello {name}, your Grade from {marks} is {grade}!')

# print_grade("Kaushal", 0)
# print_grade("Dipesh", 80)
# print_grade("Harshit", 70)
# print_grade("Luvkush", 60)
# print_grade("Shivani", 95)
# print_grade("Kushi", 55)
# print_grade(55, "Kiran")

# def introduction(first_name, last_name = "NA"):
#     print("Hello, my name is", first_name, last_name)
# # Keyword Argument Passing
# introduction(first_name = "James", last_name = "Bond")
# introduction(last_name = "Bond", first_name = "James")
# introduction("Bond", "James")
# introduction("Adtya")
# introduction("Adtya", "Gupta")

# def introduction(first_name, last_name):
#     print("Hello, my name is", first_name, last_name)
 
# introduction(surname="Skywalker", first_name="Luke")

# def adding(a, b, c):
#     print(a, "+", b, "+", c, "=", a + b + c)
# # a + b + c
# adding(1, 2, 3)
# adding(c = 1, a = 2, b = 3)	
# adding(3, c = 1, b = 2)	
# adding(a = 1, 3, b = 2)	#Error
# adding(3, a = 1, b = 2)	#Error

# def happy_new_year(wishes = True):
#     print("Three...")
#     print("Two...")
#     print("One...")
#     if not wishes:
#         return
#     print("Happy New Year!")

# happy_new_year()
# happy_new_year(False)

# def boring_function():
#     return 123
 
# x = boring_function()
 
# print("The boring_function has returned its result. It's:", x)

# print(None + 2)

# value = None
# if value is None:
#     print("Sorry, you don't carry any value")

# value = input("Enter None:")
# if value == "":
#     value = None
# print(value)
# print(type(value))


# def strange_function(n):
#     if(n % 2 == 0):
#         return True

# print(strange_function(2))
# print(strange_function(1))

# def list_sum(lst):
#     s = 0
#     for elem in lst:
#         s += elem

#     print("In function, s = ", s)
    
#     return s

# print(list_sum([5, 4, 3]))


# def list_sum(lst):
#     s = 0
 
#     for elem in lst:
#         s += elem
 
#     return s
# print(list_sum(5))

def strange_list_fun(n):
    strange_list = []
    
    for i in range(0, n):
        strange_list.insert(0, i)
    
    return strange_list
'''
i   0   1   2
[]  [4  3  2  1  0]
'''

print(strange_list_fun(5))
# 