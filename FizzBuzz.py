# FizzBuzz Problem SOLVED

# Give an input of 2 Integers

# If can be divided by 3, print (Fizz)
# If can be divided by 5, print (Buzz)
# If can be divided by 7, print (Guzz)
# If can be divided by 3 and 5, print (FizzBuzz)
# If can be divided by 3, 5 and 7, print (FizzBuzzGuzz)
# Else, print number

x = int(input("Enter A Number: "))
y = int(input("Enter Another Number: "))


def fizzbuzz(x, y):
    for num in range(x, y):

        string = ""

        if (num % 3 == 0) and (num % 5 == 0) and (num % 7 == 0):
            print(string + "FizzBuzzGuzz")
        elif (num % 3 == 0) and (num % 5 == 0):
            print(string + "FizzBuzz")
        elif num % 3 == 0:
            print(string + "Fizz")
        elif num % 5 == 0:
            print(string + "Buzz")
        elif num % 7 == 0:
            print(string + "Guzz")
        else:
            print(num)


fizzbuzz(x, y)
