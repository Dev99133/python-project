print("welcome to the pattern Generator and Number analyzer")
print("This program allows you to generate various patterns and analyze numbers.")


while(True):
    print("Select and option:")
    print("1.genrate a pattern")
    print("2.analyze a range of numbers")
    print("3. Exit")
    user_choice = int(input("Enter your choice :"))

    if user_choice == 3:
        break

    if user_choice == 2:
        starting_range = int(input("Enter the start number of range:"))
        ending_range = int(input("Enter the end number of the range:"))
        sum = 0
        for num in range(starting_range, ending_range):
            sum = sum+num 
            if num % 2:
                print(f"Number {num} is odd")
            else:
                print(f"Number {num} is even")

        else:
            print(f"sum of all number from{starting_range} to {ending_range} is: {sum}")


    if user_choice == 1:
        n = int(input("enter the number of rows for the pattern:"))
        for row in range(0,n):
            for i in range(1, row+1):
                print("*" * i)

                print()
