import math
# file = open("November_21.txt", 'a')
# file.write("seh")
# file.close()
# file = open("November_21.txt", 'r')
#
# print(file.readlines())
# file.close()

# file = open("November_21.txt", 'r')
# print(file.read())
#
# file = open("November_21.txt", 'a')
# file.write("new line\n")
#
# file = open("November_21.txt", 'w')
# file.write("deleted everything\n")
# file.write("new line\n")
# file.write("new line\n")
# file.write("new line\n")
# file.write("new line\n")
#
# print(file.readlines)

# try:
#     f = open('samplefile.txt', 'r')
# except IOError:
#     print('What happened to my file')
#     f = open('samplefile.txt', 'x')
# except ArithmeticError:
#     print("Don't even try to divide by zero")
# else:
#     print("success")
#
# try:
#     print(4/0)
# except ZeroDivisionError:
#     print("oops tried to divide by zero")

try:
    f = open('file1', 'r')
except IOError:
    print("There wasn't a file")
    f = open('file1', 'x')

try:
    math.sqrt(-1)
except ValueError:
    print("That is imaginary just like your friends")

try:
    'friends' + 14
except TypeError:
    print("You cant add 14 to the amount of friends you have")

index5list = [1, 2, 3]
try:
    print(index5list[5])
except IndexError:
    print("That's not possible")
    index5list.extend((4, 5, 6))
