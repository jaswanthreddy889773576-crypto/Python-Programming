
n = int(input("Enter a positive number: "))

if n <= 0:
    print("Please enter a positive number.")
else:
    print("\nNumbers from 1 to", n, ":")
    for i in range(1, n + 1):
        print(i, end=" ")

    print("\n\nNumbers from", n, "to 1:")
    i = n
    while i >= 1:
        print(i, end=" ")
        i -= 1

    print("\n\nMultiplication table of", n, ":")
    for i in range(1, 11):
        print(n, "x", i, "=", n * i)

