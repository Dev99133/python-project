# 4. Functional Treat 


print("Welcome  to the Data Analyzer anf Trasformer program")

while True:
    print("=== Main Menu ===")
    print("1. Input Data")
    print("2. Display Data Summary")
    print("3. Calculate Factorial")
    print("4. Filter Data by threshold")
    print("5. Sort Data")
    print("6. Display Dataset Statistics")
    print("7. Exit Program")

    choice = int(input("Please Enter Your Choice: "))

    if choice == 1:
        data = [int(x) for x in input("Enter number seperated by space: ").split()]
        print("Data added")
    
    elif choice == 2:
        if data:
            print("Total: ",len(data))
            print("Sum: ",sum(data))
            print("Min: ",min(data))
            print("Max: ",max(data))
        else:
            print('No data available')
    
    elif choice == 3:
        num = int(input("Enter a number to calculates its factorial: "))
        def factorial(x):
            return 1 if x <= 1 else x * factorial(x-1)
        print("Factorial: ", factorial(num))

    elif choice == 4:
        if data:
            a = int(input("Enter a threshold value to filter: "))
            print("Filtered data: ", [x for x in data if x>a])
        else:
            print("No Data Available")

    elif choice == 5:
        if data:
            order = input(" Ascending (1)  or Descending (2): ")
            data.sort(reverse=(order == "2"))
            print("Sorted Data: ", data)
        else:
            print("No Data Available")
        
    elif choice == 6:
        if data:
            print("Min: ",min(data), "Max: ",max(data), "Avg: ", sum(data)/len(data))
        else:
            print("No Data Available")
    elif choice == 7:
        print("Program Ended. Thank you")
        break
    else:
        print("Invlaid Choice! Try again.")
