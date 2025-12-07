# Moduler & Packager

from datetime import datetime
import time, math, random, string, uuid,importlib

# =====================================================
# ========== DATETIME AND TIME OPERATIONS =============
# =====================================================

def datetime_operations():
    while True:
        print("\n=== Datetime and Time Operations ===")
        print("1. Display Current Date and Time")
        print("2. Calculate Difference Between Two Dates")
        print("3. Format Date into Custom Format")
        print("4. Stopwatch")
        print("5. Countdown Timer")
        print("6. Back to Main Menu")

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input! Please enter a number.")
            continue

        if choice == 1:
            print("Current Date and Time:", datetime.now())

        elif choice == 2:
            try:
                d1 = input("Enter Date 1 (YYYY-MM-DD): ")
                d2 = input("Enter Date 2 (YYYY-MM-DD): ")
                date1 = datetime.strptime(d1, "%Y-%m-%d")
                date2 = datetime.strptime(d2, "%Y-%m-%d")
                diff = abs((date2 - date1).days)
                print(f"Difference: {diff} days")
            except ValueError:
                print("Invalid date format!")

        elif choice == 3:
            try:
                date = input("Enter Date (YYYY-MM-DD): ")
                n_date = datetime.strptime(date, "%Y-%m-%d")
                print("Formatted Date:", n_date.strftime("%d-%m-%Y"))
            except ValueError:
                print("Invalid format!")

        elif choice == 4:
            input("Press Enter to start the stopwatch...")
            start = time.time()
            input("Press Enter to stop the stopwatch...")
            elapsed = round(time.time() - start, 2)
            print(f"Elapsed Time: {elapsed} seconds")

        elif choice == 5:
            try:
                seconds = int(input("Enter countdown time in seconds: "))
                while seconds:
                    mins, secs = divmod(seconds, 60)
                    timer = f"{mins:02d}:{secs:02d}"
                    print(timer, end="\r")
                    time.sleep(1)
                    seconds -= 1
                print("Time’s up! ")
            except ValueError:
                print("Invalid input! Enter a number.")

        elif choice == 6:
            break
        else:
            print("Invalid choice!")


# =====================================================
# ========== MATHEMATICAL OPERATIONS ==================
# =====================================================

def math_operations():
    while True:
        print("\n=== Mathematical Operations ===")
        print("1. Calculate Factorial")
        print("2. Solve Compound Interest")
        print("3. Trigonometric Calculations")
        print("4. Area of Geometric Shapes")
        print("5. Back to Main Menu")

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input! Please enter a number.")
            continue

        if choice == 1:
            try:
                n = int(input("Enter a number: "))
                print(f"Factorial of {n} is {math.factorial(n)}")
            except ValueError:
                print("Please enter a valid integer.")

        elif choice == 2:
            try:
                principal = float(input("Principal amount: "))
                rate = float(input("Rate of interest (%): "))
                time_yrs = float(input("Time (in years): "))
                amount = principal * (1 + rate / 100) ** time_yrs
                interest = amount - principal
                print(f"Compound Interest: {interest:.2f}")
                print(f"Total Amount: {amount:.2f}")
            except ValueError:
                print("Enter valid numeric values!")

        elif choice == 3:
            try:
                degree = float(input("Enter angle in degrees: "))
                rad = math.radians(degree)
                print(f"sin({degree}) = {math.sin(rad):.4f}")
                print(f"cos({degree}) = {math.cos(rad):.4f}")
                print(f"tan({degree}) = {math.tan(rad):.4f}")
            except ValueError:
                print("Invalid input!")

        elif choice == 4:
            print("\n1. Square\n2. Rectangle\n3. Triangle\n4. Circle")
            shape = input("Choose shape: ")

            try:
                if shape == '1':
                    side = float(input("Enter side: "))
                    print("Area of Square:", side**2)
                elif shape == '2':
                    l = float(input("Enter length: "))
                    w = float(input("Enter width: "))
                    print("Area of Rectangle:", l * w)
                elif shape == '3':
                    b = float(input("Enter base: "))
                    h = float(input("Enter height: "))
                    print("Area of Triangle:", 0.5 * b * h)
                elif shape == '4':
                    r = float(input("Enter radius: "))
                    print("Area of Circle:", math.pi * r**2)
                else:
                    print("Invalid shape choice.")
            except ValueError:
                print("Invalid numeric input!")

        elif choice == 5:
            break
        else:
            print("Invalid choice!")


# =====================================================
# ========== RANDOM DATA GENERATION ===================
# =====================================================

def random_operations():
    while True:
        print("\n=== Random Data Generation ===")
        print("1. Generate Random Number")
        print("2. Generate Random List Element")
        print("3. Create Random Password")
        print("4. Generate Random OTP")
        print("5. Back to Main Menu")

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input!")
            continue

        if choice == 1:
            print("Random Number:", random.randint(1, 100))

        elif choice == 2:
            fruits = ['apple', 'mango', 'orange', 'banana', 'cherry']
            print("Random Fruit:", random.choice(fruits))

        elif choice == 3:
            try:
                length = int(input("Enter password length: "))
                chars = string.ascii_letters + string.digits + string.punctuation
                password = ''.join(random.choice(chars) for _ in range(length))
                print("Random Password:", password)
            except ValueError:
                print("Invalid input!")

        elif choice == 4:
            otp = ''.join(str(random.randint(0, 9)) for _ in range(6))
            print("Your OTP:", otp)

        elif choice == 5:
            break
        else:
            print("Invalid choice!")


# =====================================================
# ========== UNIQUE IDENTIFIER GENERATION =============
# =====================================================

def generate_uuid():
    print("\n=== Generate Unique Identifier ===")
    print("UUID:", uuid.uuid4())


# =====================================================
# ========== MODULE ATTRIBUTE EXPLORATION =============
# =====================================================

def explore_module():
    name = input("Enter module name to explore: ")
    try:
        mod = importlib.import_module(name)
        print(f"\nAttributes in '{name}':\n", dir(mod))
    except ModuleNotFoundError:
        print("Module not found!")


# =====================================================
# ========== FILE OPERATIONS ==========================
# =====================================================

def file_operations():
    while True:
        print("\n=== File Operations ===")
        print("1. Create File")
        print("2. Write to File")
        print("3. Read from File")
        print("4. Append to File")
        print("5. Back to Main Menu")

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input!")
            continue

        if choice == 1:
            name = input("Enter file name: ")
            open(name, "w").close()
            print("File created successfully.")

        elif choice == 2:
            name = input("Enter file name: ")
            data = input("Enter text to write: ")
            with open(name, "w") as f:
                f.write(data)
            print("Data written successfully.")

        elif choice == 3:
            name = input("Enter file name: ")
            try:
                with open(name, "r") as f:
                    print("\n--- File Content ---")
                    print(f.read())
            except FileNotFoundError:
                print("File not found!")

        elif choice == 4:
            name = input("Enter file name: ")
            data = input("Enter text to append: ")
            with open(name, "a") as f:
                f.write("\n" + data)
            print("Data appended successfully.")

        elif choice == 5:
            break
        else:
            print("Invalid choice!")


# =====================================================
# ================== MAIN PROGRAM =====================
# =====================================================

def main():
    print("___________________________________________________")
    print("___________________________________________________")
    print("        Welcome to Multi-Utility Toolkit")
    print("___________________________________________________")
    print("___________________________________________________")

    while True:
        print("\n=== Main Menu ===")
        print("1. Datetime and Time Operations")
        print("2. Mathematical Operations")
        print("3. Random Data Generation")
        print("4. Generate Unique Identifier")
        print("5. File Operations")
        print("6. Explore Module Attributes")
        print("7. Exit")

        try:
            option = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input! Enter a number.")
            continue

        if option == 1:
            datetime_operations()
        elif option == 2:
            math_operations()
        elif option == 3:
            random_operations()
        elif option == 4:
            generate_uuid()
        elif option == 5:
            file_operations()
        elif option == 6:
            explore_module()
        elif option == 7:
            print("\n=== Thank You! Visit Again ===")
            break
        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()
