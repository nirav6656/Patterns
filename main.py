def pattern1(n):
    for i in range(n):
        for j in range(n):
            print("*", end=" ")
        print("\n")


def pattern2(n):
    for i in range(n):
        for j in range(i):
            print("*", end=" ")
        print("\n")


def pattern3(n):
    for i in range(1, n + 1):
        for j in range(1, i):
            print(j, end=" ")
        print("\n")


def pattern4(n):
    for i in range(1, n + 1):
        for j in range(i):
            print(i, end=" ")
        print("\n")


def pattern5(n):
    for i in reversed(range(1, n + 1)):
        for j in range(i):
            print("*", end=" ")
        print("\n")


def pattern6(n):
    for i in reversed(range(1, n + 1)):
        for j in range(1, i):
            print(j, end=" ")
        print("\n")


def pattern7(n):
    for i in range(n):
        for _ in range(n - i - 1):
            print(" ", end=" ")
        for j in range((2 * i) + 1):
            print("*", end=" ")
        print(" ")


def pattern8(n):
    for i in range(n):
        for _ in range(i):
            print(" ", end=" ")
        for j in range(2 * n - 2 * i - 1):
            print("*", end=" ")
        print(" ")


def pattern9():
    pattern7(5)
    pattern8(5)


def pattern10(n):
    for i in range(n):
        for j in range(i):
            print("*", end=" ")
        print("\n")
    for i in reversed(range(n)):
        for j in range(i):
            print("*", end=" ")
        print("\n")


# Floyd's Triangle
def pattern11(n):
    for i in range(n):
        if i % 2 == 0:
            start = 1
        else:
            start = 0
        for j in range(i):
            print(start, end=" ")
            start = 1 - start
        print("\n")

def pattern17(n):
    for i in range(n):
        for _ in range(n - i - 1):
            print(" ", end=" ")
        for j in range(i + 1):
            print(chr(65 + j), end=" ")
        for j in range(i - 1, -1, -1):
            print(chr(65 + j), end=" ")
        print()


def pattern18(n):
    for i in range(n):
        for j in reversed(range(i+1)):
            print(chr(69 - j), end=" ")
        print()

def pattern19(n):
    inispace = 0
    for i in range(n):

        for _ in range(n - i):
            print("*", end=" ")
        for _ in range(inispace):
            print(" ", end=" ")
        for _ in range(n-i):
            print("*", end=" ")

        inispace += 2
        print(" ")

    inispace = 8
    for i in range(n):

        for _ in range(i+1):
            print("*", end=" ")
        for _ in range(inispace):
            print(" ", end=" ")
        for _ in range(i+1):
            print("*", end=" ")

        inispace -= 2
        print(" ")






# count digit

import math
count = int(math.log10(778945)+1)
print(count)

# reverse a number

rev_number = 0
n = 6348

while(n>0):
    last_digit = n % 10
    n = n//10
    rev_number = (rev_number*10) + last_digit

print(rev_number)