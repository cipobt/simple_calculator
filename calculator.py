# functions
def get_input():
    '''
    Requesting two numbers and an arithmetic operation from the user
    :return: These three input values as num1, num2, operation
    '''
    list_ope = ['+', '-', '*', '/']
    while True:
        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            operation = input("Enter the operation (+, -, *, /): ")
            while operation not in list_ope:
                print("Invalid option!")
                operation = input("Enter the operation (+, -, *, /): ")
            break
        except ValueError:
            print("Invalid option!")
    return num1, num2, operation


def calculate(num1, num2, operation):
    '''
    Calculates the arithmetic operation chosen by the user with the given two numbers
    :param num1: User's input
    :param num2: User's input
    :param operation: Arithmetic operation chosen by the user
    :return: Result of the valid arithmetic operation or None
    '''
    if operation == "+":
        return num1 + num2
    elif operation == "-":
        return num1 - num2
    elif operation == "*":
        return num1 * num2
    elif operation == "/":
        return num1 / num2
    else:
        return None


def file_exists(filename):
    '''
    Verifies the existence of the file
    :param filename: User's input
    :return: Boolean value
    '''
    try:
        with open(filename):
            pass
        return True
    except FileNotFoundError:
        return False


def read_from_file(filename):
    '''
    Reads from .txt file chosen by the user
    :param filename: User's input
    :return: equations list or None is file doesn't exist
    '''
    equations = []
    try:
        with open(filename, "r") as f:
            for line in f:
                equation = line.strip()
                equations.append(equation)
        return equations
    except FileNotFoundError:
        return None


def write_to_file(num1, num2, operation, result):
    '''
    Adds the values from User's input and the result of the operation to the file equations.txt
    :param num1: User's input
    :param num2: User's input
    :param operation: User's input
    :param result: Result of valid arithmetic operation
    :return: Nothing
    '''
    filename = "equations.txt"
    if not file_exists(filename):
        with open(filename, "w"):
            pass
    with open(filename, "a") as f:
        f.write(f"{num1} {operation} {num2} {result}\n")


def print_equations_and_results(equations):
    '''
    Display the content of the .txt file chosen by the user and stored in the list equations
    :param equations: list that stores contents of the .txt file chosen by the user
    :return: Nothing
    '''
    if equations is None:
        print("File not found!")
        return
    for equation in equations:
        num1, operation, num2, result = equation.split(" ")
        print(f"{num1} {operation} {num2} = {result}")


# main
print("\nWelcome to the Basic Calculator!\n")
while True:
    try:
        option = int(input("Enter 1 to calculate, 2 to read from file: "))
        if option != 1 and option != 2:
            raise ValueError

        else:
            break
    except ValueError:
        print("Invalid option!")

if option == 1:
    while True:
        try:
            num1, num2, operation = get_input()
            result = round(calculate(num1, num2, operation), 2)
            if result is None:
                print("Invalid operation!")

            else:
                print(f"{num1} {operation} {num2} = {result}")
                write_to_file(num1, num2, operation, result)
                break
        except ValueError:
            print("Invalid input!")
        except ZeroDivisionError:
            print("Cannot divide by zero!")

elif option == 2:
    while True:
        filename = input("Enter filename: ")
        if file_exists(filename):
            break
        else:
            print("File not found!")
    equations = read_from_file(filename)
    print_equations_and_results(equations)
