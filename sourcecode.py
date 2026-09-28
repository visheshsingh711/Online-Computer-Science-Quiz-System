# Online Quiz Application with Student Login and Lifeline

def display_header():
    print("\n==============================================")
    print("      ONLINE COMPUTER SCIENCE QUIZ SYSTEM     ")
    print("==============================================")

def load_quiz_bank():
    return [
        {
            "question": "What is the correct file extension for Python files?",
            "options": ["A. .pt", "B. .py", "C. .pyt", "D. .python"],
            "half_options": ["A. .pt", "B. .py"],
            "answer": "B"
        },
        {
            "question": "Which of the following is NOT a valid variable name in Python?",
            "options": ["A. my_var", "B. _var", "C. 2myvar", "D. var2"],
            "half_options": ["A. my_var", "C. 2myvar"],
            "answer": "C"
        },
        {
            "question": "What keyword is used to create a function in Python?",
            "options": ["A. function", "B. define", "C. fun", "D. def"],
            "half_options": ["B. define", "D. def"],
            "answer": "D"
        },
        {
            "question": "Which data type is used to store True or False values?",
            "options": ["A. Boolean", "B. String", "C. Integer", "D. Float"],
            "half_options": ["A. Boolean", "C. Integer"],
            "answer": "A"
        }
    ]

def start_quiz_session():
    display_header()
    
    # Student login emulation
    student_name = input("Enter your Student Name to begin: ").strip()
    if not student_name:
        student_name = "Guest Student"
        
    quiz_questions = load_quiz_bank()
    final_score = 0
    total_q = len(quiz_questions)
    has_lifeline = True  # Student gets one 50-50 lifeline per session
    
    print(f"\nWelcome, {student_name}! You will answer {total_q} questions.")
    print("Type 'L' during any question to use your one-time 50-50 lifeline.\n")
    
    for idx, item in enumerate(quiz_questions, 1):
        print(f"Question {idx}: {item['question']}")
        for opt in item['options']:
            print(opt)
            
        while True:
            choice = input("Your answer (A, B, C, D) or 'L' for Lifeline: ").strip().upper()
            
            if choice == 'L':
                if has_lifeline:
                    print("\n[50-50 Lifeline Activated! Remaining Options:]")
                    for opt in item['half_options']:
                        print(opt)
                    has_lifeline = False
                    continue
                else:
                    print("Error: You have already used your lifeline for this quiz.")
                    continue
                    
            if choice in ["A", "B", "C", "D"]:
                break
            print("Invalid selection. Please enter A, B, C, D, or L.")
            
        if choice == item['answer']:
            print("Result Check: CORRECT!\n")
            final_score += 1
        else:
            print(f"Result Check: INCORRECT. The correct answer was {item['answer']}.\n")
            
    # Final performance summary calculation
    print("----------------------------------------------")
    print("               QUIZ REPORT CARD               ")
    print("----------------------------------------------")
    print(f"Student Name      : {student_name}")
    print(f"Total Correct     : {final_score} / {total_q}")
    
    score_percentage = (final_score / total_q) * 100
    print(f"Final Percentage  : {score_percentage:.1f}%")
    
    if score_percentage >= 75:
        print("Performance Grade : Excellent Pass")
    elif score_percentage >= 50:
        print("Performance Grade : Good Pass")
    else:
        print("Performance Grade : Needs Improvement")
    print("----------------------------------------------")

if __name__ == "__main__":
    start_quiz_session()
