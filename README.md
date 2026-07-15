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

### 🟢 Day 6: Strings in Detail
**Concepts Applied:** Advanced string manipulation, string methods (`.lower()`, `.isalnum()`, `.isdigit()`, `.strip()`, `.replace()`), string indexing, and membership operators.

* **Capstone Project - Username Validator & Generator:** Built a backend-style signup validation system that checks user input against strict security rules and auto-generates clean alternatives.
    * Enforced comprehensive validation rules: length constraints, alphanumeric restrictions, banned word lists, and blocked prefixes.
    * Engineered an auto-correction algorithm to sanitize invalid inputs by stripping whitespace, replacing invalid characters, and dynamically appending safe prefixes/suffixes based on the specific validation failure.
    * Utilized membership (`in`) and boolean logic to evaluate multiple failure conditions simultaneously rather than stopping at the first error.

---

## 📖 Chapter 2: Data Structures
*Transitioning from basic variables to structured data collections, starting with lists and mutability.*

### 🟢 Day 7: Lists & Complex Iteration
**Concepts Applied:** Lists, string-to-list conversion, nested loops, state tracking, and edge-case handling.

* **Capstone Project - Wordle (CLI Edition):** Built a fully functional, terminal-based clone of the game Wordle.
    * Implemented character-by-character evaluation using lists to determine exact matches (`✓`), partial matches (`?`), and incorrect letters (`✗`).
    * Engineered advanced validation logic to accurately handle duplicate letters without double-counting (ensuring a guess with multiple identical letters only triggers partial matches if the secret word actually contains multiples).
    * Created a persistent game state that stores and prints the history of all previous guesses above the current prompt.
    * Added input sanitization to reject invalid guess lengths without penalizing the player's attempt count.

### 🟢 Day 8: Tuples & Immutability
**Concepts Applied:** `tuple`, `collections.namedtuple`, tuple unpacking, state management, and input validation.

* **Capstone Project - Pokémon Battle Simulator:** Developed a turn-based, two-player CLI battle game utilizing immutable data structures to manage character stats.
    * Structured the Pokémon roster using `namedtuple` to securely store base attributes (Name, Max HP, Attack, Defense).
    * Grouped individual attacks as lists of tuples `(Name, Power, Accuracy)` and seamlessly extracted them during combat using tuple unpacking.
    * Engineered a dynamic combat loop that tracks real-time HP in a separate variable to respect the immutability of the base `namedtuple`.
    * Implemented RNG-based accuracy checks and a scaling damage formula `max(1, power + atk - def)`.
    * Built robust input validation loops to ensure players can only select valid roster numbers and move options without crashing the program.

### 🟢 Day 9: Mastering Data Processing & Tuple Unpacking
**Concepts Applied:** Advanced iteration, tuple unpacking, conditional filtering, and list sorting.

* **Project - Student Academic Tracker:** Built an academic performance processing system to categorize students based on GPA and credit requirements.
    * Leveraged tuple unpacking `(name, gpa, credits)` directly within a `for` loop to cleanly access data.
    * Implemented dual-criteria filtering logic to identify students for "Honors" and "Academic Support" categories.
    * Mastered list sorting with custom parameters to display GPA rankings in descending order for Honors and ascending order for Support.
    * Demonstrated the ability to process raw data collections into organized, actionable reports.