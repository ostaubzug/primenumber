import math


def prime(a):
    while (True):

        y = 1
        a = a+1
        sqrt = math.sqrt(a)

        while (True):
            y = y+1
            z = a % y

            if y > sqrt:
                print(a)
                break

            if z == 0:
                break


# Enter the number from where you want to start
start = int(input("Enter the number where you want to start "))
prime(start)
