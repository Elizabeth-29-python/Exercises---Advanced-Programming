import random

def load_jokes(file_path):
    with open(file_path, 'r', encoding= 'ISO-8859-1') as file:
        return [line.strip().split('?') for line in file if '?' in line]
    
def tell_joke(jokes):#this will be the set up and punchline for each joke
    setup, punchline = random.choice(jokes)
    print(f"Alexa: {setup}?")
    input("Press Enter to hear the punch... (Don't worry I won't make you wait too long!)")
    print(f"Alexa: {punchline} (Ha! Get it?)")

    def main(): 
        joke = load_jokes('resources/randomJokes.txt')
        #randomJokes.txt will cointain dataset of random jokes compiled. 

        print("Alexa: Ready to tickle your funnt bone! just say 'Alexa Tell me a joke'!")

        while True:
            user_input = input("You: ").lower().strip()

            if user_input == "alex tell me a joke":
                tell_joke(jokes)
            elif user_input in ["quit", "exit", "bye"]:
                print("Alexa: Goodbye! Remmeber, laughter is the best medicine... unless you have a broken rid!")
                break
            else:
                print("Alexa: I'm sorry, I didn't understand that. Try saying 'Alex tell me a joke'!")

if __name__ == "__main__":
    main()