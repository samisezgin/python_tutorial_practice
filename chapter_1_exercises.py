# 1
for i in range(4):
    for j in range(19):
        print("*", end="")
    print()

# 2
print()
for i in range(4):
    if i % 3 == 0:
        print("*" * 19)
    else:
        print("*", end="");
        print(" " * 17, end="");
        print("*", end="\n")

# 3
print()
for i in range(4):
    print("*" * (i + 1))

# 4
print()
result = (512 - 282) / (47 * 48 + 5)
print(result)

# 5
print()
number = int(input("Enter a number: "))
print("The square of %d is %d" % (number, number ** 2))

# 6
print()
number = int(input("Enter a number: "))
print(number, 2 * number, 3 * number, 4 * number, 5 * number, sep="---")

# 7
print()
kg = int(input("Enter your weight: "))
print("Your weight is %d kg converted to %d pounds" % (kg, kg * 2.2))

# 8
print()
num1, num2, num3 = int(input("Enter 1/3 number: ")), int(input("Enter 2/3 number: ")), int(input("Enter 3/3 number: "))
total = num1 + num2 + num3
average = total / 3
print("total: %d \naverage: %d" % (total, average))

# 9
print()
price = int(input("Enter the meal of the price: "))
tip = int(input("Enter the tip percent: "))
total = price + price * tip / 100
print("Tip: %d\nTotal bill: %d" % (tip, total))
