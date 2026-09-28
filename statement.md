# Online Computer Science Quiz System

## 1. Problem Statement

Students need a simple and interactive way to practice and test their knowledge of Computer Science and Python programming concepts.

The **Online Computer Science Quiz System** provides a console-based quiz application where students can answer multiple-choice questions, use a one-time 50-50 lifeline, and immediately receive feedback on their answers.

The system also calculates the student's final score, percentage, and performance grade after completing the quiz.

---

## 2. Scope of the Project

The scope of this project includes:

- Providing a student-friendly Computer Science quiz.
- Allowing students to enter their name before starting.
- Displaying multiple-choice questions with four answer options.
- Accepting answers from A, B, C, or D.
- Providing one 50-50 lifeline during the quiz.
- Validating user input and handling invalid selections.
- Checking answers immediately after each question.
- Calculating the total score and percentage.
- Displaying a final performance grade.
- Providing a simple command-line interface.

The current project does not include database storage, online accounts, password authentication, or a graphical user interface.

---

## 3. Target Users

The primary target users are:

- **Students** who want to practice Computer Science and Python concepts.
- **Beginners** learning Python programming.
- **Teachers/Instructors** who want a simple quiz demonstration.
- **Learners** who want immediate feedback on their answers.

---

## 4. High-Level Features

### Student Login

Allows the student to enter their name before beginning the quiz. If no name is entered, the system uses "Guest Student".

### Multiple-Choice Quiz

Provides Computer Science/Python questions with four possible answers:

- A
- B
- C
- D

### 50-50 Lifeline

Provides one 50-50 lifeline per quiz session. The lifeline displays two remaining answer options.

### Input Validation

Checks the student's input and displays an error message when an invalid option is entered.

### Immediate Answer Feedback

After every question, the system informs the student whether their answer is correct or incorrect.

### Score Calculation

Keeps track of the number of correct answers throughout the quiz.

### Percentage Calculation

Calculates the student's final percentage using the total number of correct answers.

### Performance Grade

Displays a performance grade based on the final percentage:

- **75% or above:** Excellent Pass
- **50%–74.9%:** Good Pass
- **Below 50%:** Needs Improvement

### Final Quiz Report

Displays the student's:

- Name
- Total correct answers
- Total questions
- Final percentage
- Performance grade
