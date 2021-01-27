def collatz(number):
    try:
        if number % 2 == 0:
            print(number // 2)
        elif number % 2 == 1 :
            print(3 * number +1)
    except ValueError:
        print("Please enter Integer value. ")
number = int(input("Enter Number: "))

collatz(number)
