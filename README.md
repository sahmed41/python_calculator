
# 🧮 Python Command-Line Calculator

A clean, modular command-line calculator built in Python to practice and solidify core programming fundamentals. Designed and implemented with **pure human logic and zero AI coding assistance** to build genuine problem-solving muscle memory.

---

## 📖 About the Software

This calculator is designed to go beyond a standard single file script by incorporating clean software architecture principles. It separates the user interface and program state control from the underlying mathematical business logic.

### **Core Components & Architecture**
```text
python_calculator/
│
├── _engine/
│   ├── operations.py    # Core math functions (add, subtract, multiply, divide)
│
└── main.py              # Main entry point, control flow loop, and user 
```

- **`main.py` (The Controller & UI):** Handles the continuous execution loop, prompts the user for inputs, validates choices using modern Python `match` logic.   
- **`_engine/operations.py` (The Math Engine):** Houses pure functions for addition, subtraction, multiplication, and division. Each function accepts parameters, performs the calculation, and **returns** the result.   
   
## ✨ Features

- **Modular Architecture:** Clean separation of concerns between business logic and UI/control flow.    
- **Robust Error Handling:** Utilizes `try-except` blocks to catch invalid inputs, invalid strings or non-numeric entries, preventing the program from crashing.   
- **Continuous Execution:** Built inside a `while` loop so you can perform multiple calculations seamlessly in a single session.   
- **Graceful Exit:** Type `'x'` or `'X'` at any time to safely exit the program.    
- **Modern Python Routing:** Uses Python's clean `match` syntax for menu selection.    

## 🧠 Concepts Practiced

This project serves as a practical showcase of the following programming concepts:  
1. **Variables & Primitive Types** (`int`, `float`, `bool`, `str`)   
2. **Operators** (Arithmetic, Assignment, Logical)   
3. **Input/Output** (`input()`, `print()`)   
4. **Control Flow** (`if`, `elif`, `else`, `match`)   
5. **Loops** (`while` loops, and `continue` flow control)   
6. **Functions** (Parameters, `return` values, `docstrings`)   
7. **Comments & Documentation**    
8. **Error Handling** (`try-except`) 

## 🚀 User Guide: Getting Started

### Prerequisites

Make sure you have **Python 3.10 or higher** installed on your system (required for `match-case` support).
### Installation & Execution

1. Clone the repository to your local machine:

```bash
git clone https://github.com/sahmed41/python_calculator.git
```

2. Navigate into the project directory:

```bash
cd python_calculator
```

3. Run the application:

```bash
python main.py
```

### How to Use the Calculator

1. When prompted, enter your **first number** (or type `x` to quit).
2. Enter your **second number** (or type `x` to quit).
3. Select the desired operation from the menu:  
    - `1` - Add both numbers    
    - `2` - Subtract both numbers
    - `3` - Multiply both numbers
    - `4` - Divide both numbers
    - `x` - Exit the program
4. View the result and continue calculating as many times as you like!

## 👤 Author

**Shafeeq Ahmed Mohammed Waseen**
GitHub: [@sahmed41](https://github.com/sahmed41)
