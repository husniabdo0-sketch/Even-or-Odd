while True:
    try:
        number = int(input("Enter a whole number: "))
        break
    except ValueError:
        print("Please enter a whole number, such as -3, 0, or 8.")

if number % 2 == 0:
    print(f"{number} is even.")
else:
    print(f"{number} is odd.")