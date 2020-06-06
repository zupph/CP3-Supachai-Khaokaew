number = int(input("Please enter number : "))
star = 1
for i in range(number):
    print(" " * (number - i) + "*" * star)
    star = star + 2