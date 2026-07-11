# 🐍 Python Self-Learning Journey: Zero to Internship-Ready

Welcome to my dedicated Python learning repository! This project tracks my daily progress, chapter by chapter, as I build my fundamental and advanced programming skills over the summer. Every concept learned is immediately applied through daily mini-capstone projects.

---

## 🗺️ The Roadmap

This curriculum is structured from foundational concepts to specialized, internship-ready skills.

*   **Chapter 1:** Core Python (Foundation)
*   **Chapter 2:** Data Structures (Foundation)
*   **Chapter 3:** OOP & Files (Intermediate)
*   **Chapter 4:** Advanced Python (Intermediate)
*   **Chapter 5:** Data & Algorithms (Advanced)
*   **Chapter 6:** Python for AI/ML (Advanced)
*   **Chapter 7:** Backend / Web (Specialized)
*   **Chapter 8:** Don't get stuck (Frontend)
*   **Chapter 9:** Internship-Ready Skills (Specialized)

---

## 📖 Chapter 1: Core Python
*Currently focusing on mastering the absolute fundamentals of Python syntax and logic.*

### Topics Covered:
*   **Output & Input:** Utilizing the `print()` function, f-strings & formatting, the `input()` function, and type casting from input.
*   **Variables & Data Types:** Working with `int`, `float`, `str`, `bool`, and `None` types.
*   **Variables & Data Types (Advanced):** Using the `type()` function, understanding dynamic typing, and adhering to variable naming rules.
*   **Operators:** Applying arithmetic (`+`, `-`, `*`, `/`, `//`, `%`, `**`), comparison (`==`, `!=`, `<`, `>`), logical (`and`, `or`, `not`), and assignment operators, while following operator precedence.
*   **Control Flow:** Implementing `if` / `elif` / `else` statements, nested conditionals, ternary expressions, `while` loops, `for` loops, the `range()` function, and `break` / `continue` / `pass` statements.
*   **Strings (Deep Dive):** Utilizing indexing & slicing, string methods (`split`, `join`, `strip`, `replace`, `find`), multiline strings, string formatting, and understanding string immutability.

---

## 🚀 Daily Learning Log & Capstone Projects

### 🟢 Day 1: Inputs, Types, and Basic Math
**Concepts Applied:** `input()`, f-strings, type casting, basic arithmetic operations.

*   **Mini-Exercise - Profile Card:** Built a program that asks the user for their name, age, and GPA, and prints a neatly formatted profile card using f-strings and type casting.
*   **Capstone Project - Student Fee Calculator:** Developed a CLI program that generates a formatted semester invoice.
    *   Takes user input for name, age, and enrolled credit hours.
    *   Calculates tuition using a constant rate of $850 per credit hour.
    *   Adds a one-time constant semester fee of $200.
    *   Applies a 10% junior discount to the total if the student is under 18.

### 🟢 Day 2: Data Types & Variables
**Concepts Applied:** Dynamic typing, type conversion, constants, and complex mathematical formatting.

*   **Capstone Project - Student Fee Calculator:** Developed a CLI program that generates a formatted semester invoice.
    *   Takes user input for name, age, and enrolled credit hours.
    *   Calculates tuition using a constant rate of $850 per credit hour.
    *   Adds a one-time constant semester fee of $200.
    *   Applies a 10% junior discount to the total if the student is under 18.

### 🟢 Day 3: Arithmetic Operators & Boolean Logic
**Concepts Applied:** Arithmetic operators, comparison operators, and complex boolean expressions.

*   **Capstone Project - UTD Scholarship Eligibility Checker:** Created a logic-heavy evaluation program that determines scholarship awards based on strict criteria.
    *   **Rules implemented:** GPA must be 3.5 or above, at least 30 credit hours completed, age between 17 and 25 (inclusive), and zero academic violations.
    *   **Logic:** Eligibility is calculated on a single line utilizing `and`, `or`, and `not` operators.
    *   **Calculation:** If eligible, the award amount is calculated by multiplying credit hours by a constant scholarship rate of $150. If not eligible, the award defaults to $0.

### 🟢 Day 4: Control Flow & Complex Logic
**Concepts Applied:** `if` / `elif` / `else` statements, nested conditionals, ternary expressions, boolean logic.

*   **Capstone Project - Airport Check-in System:** Built a robust CLI program to handle full passenger processing with strict rule enforcement.
    *   Implemented conditional baggage fee calculations including overweight penalties and a strict maximum bag limit.
    *   Engineered nested logic to determine seat upgrade eligibility based on loyalty tier and flight duration.
    *   Created a hard-stop boarding verification system checking valid passports and no-fly lists before processing any further logic.

### 🟢 Day 5: Loops & Iteration
**Concepts Applied:** `for` loops, `while` loops, the `range()` function, and utilizing external modules.

* **Capstone Project - Number Guessing Game (Roast Edition):** Developed an interactive, loop-driven CLI game where the user has 7 attempts to guess a randomly generated number between 1 and 100.
    * Integrated the `random` module to generate a secure secret number.
    * Implemented a `for` loop to enforce strict turn limits and iterate through the user's attempts.
    * Engineered tiered conditional logic to dynamically "roast" the user based on the numerical distance between their guess and the secret number.
    * Created targeted win/loss conditions that output custom messages based on the exact iteration the loop was broken.
