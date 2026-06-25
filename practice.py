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
my_list = [8, 10, 6, 2, 4]
print(my_list)
for index1 in range(len(my_list) - 1):
    for index in range(len(my_list) - 1):
        if( my_list[index] > my_list[index + 1] ):
            my_list[index], my_list[index + 1] = my_list[index + 1], my_list[index]

print(my_list)