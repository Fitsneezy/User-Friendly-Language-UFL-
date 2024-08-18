# User-Friendly-Language (UFL) Launch Edition
Welcome to the UFL Launch Edition! This guide will help you get started with using UFL, a simple and user-friendly programming language designed for easy scripting and automation.

# Overview
UFL is designed to be easy to learn and use, even for beginners. The Launch Edition includes the core features you need to start creating your own scripts and applications.

# Getting Started
Prerequisites
Python: UFL scripts are run using Python. Ensure Python is installed on your system. [Download Python Here](https://www.python.org/downloads/release/python-3125/).
UFL Compiler: Download the UFL compiler from the GitHub Releases page.
Installation
Download the UFL Launch Edition package from the GitHub Releases page.
Open the .xml file in Notepad++'s user defined language import.
Running UFL Scripts
Open a terminal or command prompt.

Navigate to the directory where you extracted the UFL files.

Run the UFL interpreter with your script by executing the following command:

python ufl_studio.py path/to/your_script.ufl

Replace path/to/your_script.ufl with the path to your UFL script.

# Example Script
Here’s a basic example of a UFL script:

ufl
Copy code
let x = 10
let y = 5

say("Sum: " + (x + y))
To run this script:

Save it as example.ufl.

Execute the following command in your terminal:

python ufl_studio.py example.ufl

# Writing UFL Scripts
Keywords

let: Defines a variable.

say: Outputs text to the console.

ifthis: Conditional statement for true cases.

orelse: Conditional statement for false cases.

foreverloop: Creates an infinite loop.

Operators

=: Assignment

+: Addition

-: Subtraction

*: Multiplication

/: Division

Comments
Open: //

Line: |

Close: \\

Handling Errors
If your script encounters errors, the interpreter will display error messages in the terminal. Review these messages to debug your script.

# Contributing
If you have suggestions or find bugs, feel free to open an issue or contribute to the repository.

chatgpt made this description btw

