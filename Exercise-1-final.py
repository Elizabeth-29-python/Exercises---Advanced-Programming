import random 
def displayMenu ():
    print("Choose Difficulty level")
    print("1. Easy")
    print("2. Moderate")
    print("3. Advanced")

    while True:
        try:
            choice = int(input("Select difficulty (1-3): "))
            if 1 <= choice <= 3:
                return choice
            else:
                print("Please enter a number between 1 and 3.")
        except ValueError:
            print("Invalid input. Please eneter a number.")

#randomInt function with the min and max values are based on the difficulty level 
def randomInt(difficulty):
    if difficulty == 1:
        return random.radiant(0,9)
    elif difficulty == 2:
        return random.randint(10,99)
    else:
        return random.randint(100,999)
    
#decideOperation is placed to randomly decide whether the problem is an addition or subtraction problem and returns to a char.
def decideOperation():
    return random.choice(['+', '-'])

#displayOProblem function displays the question to the user and accepts their answers
def displayProblem(num1, num2, operation):
    print(f"{num1} {operation} {num2} = ")
    while True:
        try:
            answer = int(input("Your Answer: "))
            return answer
        except ValueError:
            print("Invalid input. Please enter a number.")

#isCorrect function is added to check the users answer was correct and has the right output of an appropriate message
def isCorrect(num1, num2, operation, user_answer):
    if operation == '+':
        correct_answer = num1 + num2
    else:
        correct_answer = num1 - num2 
        return user_answer == correct_answer, correct_answer
    
#displayResults is a function that tell the users the final score out of 100 and rank the user based ont their total score
def displayResults(score):
    print(f"\nYour final score: {score} out of 100")
    if score >= 90:
        print("Rank: A+")
    elif score >= 80:
        print("Rank: A")
    elif score >= 70:
        print("Rank: B")
    elif score >= 60:
        print("Rank: C")
    else:
        print ("Rank: D")

def playQuiz():
    difficulty = displayMenu()
    score = 0
    
    for _ in range(10):
        num1 = randomInt(difficulty) 
        num2 = randomInt(difficulty)
        operation = decideOperation()

    for attempt in range(2):
        user_answer = displayProblem(num1, num2, operation)
        correct, correct_answer = isCorrect(num1, num2, operation, user_answer)
        
        if correct:
            print("Correct!")
            score += 10 if attempt == 0 else 5
            break
        else: 
            if attempt == 0:
                print("Incorrect. Please try again.")
            else:
                print(f"Incorrect. The correct answer is {correct_answer}.")

    displayResults(score)
    
    return input("Would you like to play again? (yes/no): ").lower().startswith('y')

def main():
    print("Welcome to the Arithmetic Quiz!")
    while True: 
        if not playQuiz():
            print("Thanks for playing. Goodbye!")
            break

if __name__ == "__main__":
    main()
