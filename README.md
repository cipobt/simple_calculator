# Basic Calculator with File Operations

This is a simple console-based calculator application written in Python. The program allows the user to perform basic arithmetic operations (addition, subtraction, multiplication, division) between two numbers and also to read previously stored equations from a file.

## Functions Included:

- `get_input()` : Requesting two numbers and an arithmetic operation from the user
- `calculate(num1, num2, operation)` : Calculates the arithmetic operation chosen by the user with the given two numbers
- `file_exists(filename)` : Verifies the existence of the file
- `read_from_file(filename)` : Reads from .txt file chosen by the user
- `write_to_file(num1, num2, operation, result)` : Adds the values from User's input and the result of the operation to the file equations.txt
- `print_equations_and_results(equations)` : Display the content of the .txt file chosen by the user and stored in the list equations

## How to Use:

1. Run the python script.
2. Follow the interactive prompts in the console.
3. To perform a calculation:
    - Enter 1 when asked "Enter 1 to calculate, 2 to read from file: ".
    - Enter the first number, second number, and the operation.
    - The program will print the result and store it in a file named "equations.txt".
4. To read from a file:
    - Enter 2 when asked "Enter 1 to calculate, 2 to read from file: ".
    - Enter the filename from which you want to read. The file should be in the same directory as the python script.
    - If the file exists, the program will read and print the content.

## Requirements:

- Python 3.x

## Known Issues:

- Division by zero is not allowed and will throw a "Cannot divide by zero!" error.
- Only supports simple arithmetic operations (addition, subtraction, multiplication, and division).
- Input error handling is in place, but more complex mathematical expressions or edge cases may not be handled.

## Future Improvements:

- Implement error handling for more complex mathematical expressions.
- Add support for more operations like modulo, exponentiation, etc.
- Improve file reading capability to allow reading from different directories.
- Improve the user interface for a more intuitive and rich experience.

## Contribute:

Feel free to fork this project and make your own changes. I'm always keen to learn from others, so pull requests are most welcome!
