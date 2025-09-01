# print() function

print("Welcome to the Interactive Personal Data Collecter")

# Collect information & type casting

Name = input("Please enter your name: ")
Age = int(input("Please enter your age: "))
Height = float(input("Please enter your height in meters: "))
Email = input("Please enter your Mail I'd: ")
Fav_num = int(input("Please enter your favourite number: "))

print(Name)
print(Age)
print(Height)
print(Email)
print(Fav_num)

print("Thank you! Here is the informatiom we collected")

# Type() Function & Id() Function

print("Type of Name: ", type(Name), "Memory ID: ",id(Name))
print("Type of Age: ", type(Age), "Memory ID: ",id(Age))
print("Type of Height: ", type(Height), "Memory ID: ",id(Height))
print("Type of Fav_num: ", type(Fav_num), "Memory ID: ",id(Fav_num))


# Find Birth year based on the age


current_year = 2025
birthyear = current_year - Age


print(Age)
print("your birthyear is appoximately:  ")
print(birthyear)


print("Thank you for using personal data collecter , Good Bye!")



