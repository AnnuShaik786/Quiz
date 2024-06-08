#PYTHON CODE:-

def login():
    """
    Function to handle user login.
    """
    Creat_username = input("Create Your username: ")
    Creat_password = input("Create Your password: ")
    
    username = input("Enter Your username: ")
    password = input("Enter Your password: ")
    
    if Creat_username == username and Creat_password == password:
        print(f"Hello! {username} you logged in successfully.")
        print('''                  Welcome to the Quiz Challenge!

Test your knowledge with this fun and engaging quiz.

Each Correct answer carries +1000 marks.
Each Wrong answer carries -1000 marks.

Answer each question to the best of your ability and see how you score at the end.

Are you ready? Let's begin! 
''')
        return True
    else:
        print("Invalid credentials.")
        return False

def ask_question(question, correct_answer):
    """
    Function to ask a question and check the answer.
    Returns True if the answer is correct, else False.
    """
    user_answer = input(question + " ")
    if user_answer.lower() == correct_answer.lower():
        print("Correct!")
        return True
    else:
        print("Incorrect. The correct answer is:", correct_answer)
        return False

def main():
    # Login
    if not login():
        return
    
    
    score = 0

    # Question 1
    question1 = "1.What is the capital of India?"
    answer1 = "Delhi"
    if ask_question(question1, answer1):
        score = score + 1000
    else:
        score = score - 1000

    # Question 2
    question2 = "2.What is the national sport of India?"
    answer2 = "Hockey"
    if ask_question(question2, answer2):
        score = score + 1000
    else:
        score = score - 1000
        
    # Question 3
    question3 = "3.In which year India got independence?"
    answer3 = "1947"
    if ask_question(question3, answer3):
        score = score + 1000
    else:
        score = score - 1000


     # Question 4
    question4 = "4Chemical formula of Gold?"
    answer4 = "Au"
    if ask_question(question4, answer4):
        score = score + 1000
    else:
        score = score - 1000

    # Question 5
    question5 = "5.Which planet has the most moons?"
    answer5 = "Saturn"
    if ask_question(question5, answer5):
        score = score + 1000
    else:
        score = score - 1000

    print("Your final score is: ", score)

if __name__ == "__main__":
    main()
