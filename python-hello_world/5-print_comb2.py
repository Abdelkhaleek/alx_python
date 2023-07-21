def print_numbers():
    numbers = ", ".join("{:02d}".format(i) for i in range(100))
    print(numbers)

print_numbers()

