# a = True
# b = False

# print(a and b)
# print(a or b)
# # print(a not b)

# factorial of a number using recursive function
def fact(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * fact(n-1)
num = int(input("Enter a number: "))

print("Factorial of given number is = ", fact(num))


# fibonacci series of a number using recursive function
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
num = int(input("Enter a positive number: "))

print("Fibonacci series of given number: ", fibonacci(num))
    