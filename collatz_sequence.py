def main():
    start_number = int(input("Enter a non-zero positive integer (>=1) to compute its Collatz sequence:\n"))

    while start_number < 1:
        start_number = int(input("Enter a non-zero positive integer (>=1) to compute its Collatz sequence:\n"))

    lista = [start_number]

    number = start_number
    while number > 1:
        if number % 2 == 0:
            number /= 2
            lista.append(int(number))
        elif number % 2 == 1:
            number = number * 3 + 1
            lista.append(int(number))

    print(f"The Collatz sequence for {start_number} is:")

    count = 0
    for each in lista:
        count += 1
        if count == 5:
            print(each)
            count = 0
        else:
            print(each, end=' ')

    print(f"\nThe length of the Collatz sequence for {start_number} is: {len(lista)}")


main()
