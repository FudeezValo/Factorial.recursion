# Program that calculates the factorial of a number.
# It uses a function and demo the use of recursion:
#
def factorial(n):
    "calculating the factorial of a number"
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def main():
    num = int(input("Enter a number: "))
    print("The factorial of", num, "is", factorial(num))

if __name__ == "__main__":
    main()