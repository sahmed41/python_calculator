### **Project Requirements: Python Command Line Calculator**

#### **1. Basic Operations & Functions**

* **Core Functions:** Create separate functions for addition, subtraction, multiplication, and division.
* **Function Return Values:** Each function must take two numbers as inputs (parameters) and **return** the result rather than printing it directly inside the function.

#### **2. Variables, Primitive Types & Input/Output**

* **User Interaction:** Use `input()` to prompt the user for their choice of operation and numbers.
* **Type Conversion:** Properly convert user inputs (which are strings by default) into appropriate numeric types (e.g., `float` or `int`) so math operations can be performed.
* **State Storage:** Use variables to store the current result, user inputs, and history.

#### **3. Control Flow (`if`, `elif`, `else`)**

* **Menu Selection:** Present a clear menu to the user listing available operations (e.g., `1. Add`, `2. Subtract`, etc.).
* **Branching:** Use `if-elif-else` statements to direct the program to the correct function based on the user's menu choice.

#### **4. Loops & Error Handling**

* **Continuous Execution:** Wrap the calculator in a `while` loop so the user can perform multiple calculations without restarting the program. Add an option to exit the loop (e.g., typing `'q'` or `'quit'`).
* **Input Validation & Exceptions:** Use `try-except` blocks to handle common errors gracefully:
* **ValueError:** Prevent crashes if the user types letters instead of numbers.
* **ZeroDivisionError:** Prevent crashes and display a friendly message if the user tries to divide by zero.



#### **5. Comments & Documentation**

* **Code Readability:** Add clean, descriptive comments (`#`) above your functions and complex blocks of code explaining *what* they do and *why*.




