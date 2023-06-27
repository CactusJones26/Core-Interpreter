# The Core Interpreter

How to execute:

Make sure that the Core code text file is in the same directory as main.py
In a terminal, run "python3 main.py (insert name of text file containing Core code) (insert name of data text file containing data)"
    Ex: "python3 main.py test.txt data.txt"

The Core Interpreter works with the following logic:
    1. Tokenizes the Core Program
    2. Parses Core program
    3. Pretty Prints the Core Program following the indentation style that exists in Python
    4. Executes the Core Program

Note: The Core Interpreter will read from an additional file if there are any "read" statements with the code

Testing:
    The Interpreter was tested using several test Core files as well as test data files.
    For the test files, I found what the expected output should be and compared it to 
    what the Interpreter outputted into the console.
