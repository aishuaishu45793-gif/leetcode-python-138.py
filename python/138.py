try:
    number = int(input("Enter a non-negative integer: "))

    if number < 0:
        print("Factorial is not defined for negative integers.")
    else:
        factorial = 1

        for i in range(1, number + 1):
            factorial *= i

        print("Factorial:", factorial)

except ValueError:
    print("Invalid input! Please enter an integer.")