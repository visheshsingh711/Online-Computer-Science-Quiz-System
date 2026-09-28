# README.md

````markdown
# Online Computer Science Quiz System

## 1. Project Title

**Online Quiz Application with Student Login and Lifeline**

---

## 2. Overview of the Project

The **Online Computer Science Quiz System** is a simple Python-based console application designed to conduct a multiple-choice Computer Science quiz.

The application allows a student to:

- Enter their name before starting the quiz.
- Answer multiple-choice questions.
- Use a one-time **50-50 Lifeline**.
- Receive immediate feedback after each answer.
- View their total score and percentage at the end.
- Receive a performance grade based on their final percentage.

The quiz currently contains **4 Python-related questions**.

---

## 3. Features

### Student Login

The program asks the student to enter their name before starting the quiz.

If no name is entered, the program automatically uses:

```text
Guest Student
````

### Multiple-Choice Questions

Each question contains four possible answers:

* A
* B
* C
* D

The student must select one of these options.

### 50-50 Lifeline

The student receives **one lifeline per quiz session**.

By entering:

```text
L
```

the program removes two options and displays the remaining two options.

The lifeline can only be used once during the quiz.

### Input Validation

The program checks whether the entered answer is valid.

Valid inputs are:

```text
A
B
C
D
L
```

If an invalid option is entered, the program asks the student to enter a valid choice.

### Instant Result Checking

After each question, the program immediately displays whether the answer is correct or incorrect.

### Quiz Report Card

At the end of the quiz, the program displays:

* Student name
* Total correct answers
* Total number of questions
* Final percentage
* Performance grade

### Performance Grading

The application calculates the student's performance using the following criteria:

| Percentage   | Performance Grade |
| ------------ | ----------------- |
| 75% or above | Excellent Pass    |
| 50% – 74.9%  | Good Pass         |
| Below 50%    | Needs Improvement |

---

## 4. Technologies / Tools Used

The project is developed using:

* **Python 3**
* Python `input()` function for user interaction
* Python `print()` function for displaying information
* Lists and dictionaries for storing quiz questions
* `for` loops for processing questions
* `while` loops for input validation
* `if / elif / else` statements for decision making
* Functions for organizing the program

### Main Functions

The program contains the following main functions:

#### `display_header()`

Displays the title/header of the quiz system.

#### `load_quiz_bank()`

Creates and returns the list of quiz questions, options, correct answers, and 50-50 lifeline options.

#### `start_quiz_session()`

Controls the complete quiz session, including:

* Student login
* Question display
* Answer input
* Lifeline usage
* Answer checking
* Score calculation
* Final report card

---

## 5. Project Structure

A simple project structure can be:

```text
Online-Quiz-Application/
│
├── quiz.py
└── README.md
```


---

## 6. Steps to Install & Run the Project

### Step 1: Install Python

Install **Python 3** on your computer if it is not already installed.

You can check whether Python is installed by running:

```bash
python --version
```

or:

```bash
python3 --version
```

### Step 2: Save the Program

Save the provided Python code in a file named:

```text
quiz.py
```

### Step 3: Open the Terminal

Navigate to the folder containing `quiz.py`.

For example:

```bash
cd Online-Quiz-Application
```

### Step 4: Run the Program

On Windows:

```bash
python quiz.py
```

On macOS/Linux:

```bash
python3 quiz.py
```

### Step 5: Enter Student Name

When the program asks:

```text
Enter your Student Name to begin:
```

enter your name and press **Enter**.

The quiz will then begin.

---

## 7. Instructions for Testing

The following test cases can be used to verify that the program works correctly.

### Test 1: Student Login

**Input:**

```text
Rahul
```

**Expected result:**

```text
Welcome, Rahul! You will answer 4 questions.
```

---

### Test 2: Empty Student Name

When the student presses Enter without entering a name:

**Expected result:**

```text
Welcome, Guest Student! You will answer 4 questions.
```

---

### Test 3: Correct Answer

For the first question, the correct answer is:

```text
B
```

Entering `B` should display:

```text
Result Check: CORRECT!
```

and increase the score by 1.

---

### Test 4: Incorrect Answer

Enter an incorrect option such as:

```text
A
```

for the first question.

**Expected result:**

```text
Result Check: INCORRECT. The correct answer was B.
```

---

### Test 5: Invalid Input

Enter an invalid option such as:

```text
X
```

**Expected result:**

```text
Invalid selection. Please enter A, B, C, D, or L.
```

The program should continue asking for a valid answer.

---

### Test 6: 50-50 Lifeline

During a question, enter:

```text
L
```

**Expected result:**

```text
[50-50 Lifeline Activated! Remaining Options:]
```

Only two options should be displayed.

The student can then enter A, B, C, or D according to the remaining options.

---

### Test 7: Using Lifeline Twice

After using the lifeline once, enter:

```text
L
```

again.

**Expected result:**

```text
Error: You have already used your lifeline for this quiz.
```

The program should continue asking for an answer.

---

### Test 8: Final Score

After answering all four questions, the program should display the quiz report card.

Example:

```text
----------------------------------------------
               QUIZ REPORT CARD
----------------------------------------------
Student Name      : Rahul
Total Correct     : 4 / 4
Final Percentage  : 100.0%
Performance Grade : Excellent Pass
----------------------------------------------
```

---




