numbers = []

‏n = int(input("How many numbers? "))

‏for i in range(n):
‏    x = int(input("Enter number: "))
‏    numbers.append(x)

‏number = int(input("Which number do you want to find? "))

‏for x in numbers:
‏    if x == number:
‏        print("Found")