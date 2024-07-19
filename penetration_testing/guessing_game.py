def is_admin():
    while True:
        try:
            admin = int(input("Are you an admin? (1 for yes, 2 for no): "))
            if admin == 1:
                return True
            elif admin == 2:
                print("You have been logged out.")
                return False
            else:
                print("Invalid input. Please enter 1 or 2.")
        except ValueError:
            print("Invalid input. Please enter a number (1 or 2).")

def get_word_of_choice():
    return input("Admin, please input the word of choice: ").upper()

def create_harshed_words(word_of_choice):
    return ["*_*" for _ in word_of_choice]

def display_harshed_words(harshed_words):
    print("Current word state: " + ", ".join(harshed_words))

def get_user_guess():
    while True:
        guess = input("It's time to guess a word: ").upper()
        if len(guess) == 1 and guess.isalpha():
            return guess
        else:
            print("Invalid input. Please enter a single character.")

def play_game(word_of_choice, harshed_words):
    tries = 5
    guessed_indices = set()
    
    while tries > 0:
        display_harshed_words(harshed_words)
        guess = get_user_guess()
        
        if guess in word_of_choice:
            for i, char in enumerate(word_of_choice):
                if char == guess and i not in guessed_indices:
                    harshed_words[i] = guess
                    guessed_indices.add(i)
            if harshed_words == list(word_of_choice):
                print("You have successfully guessed correctly!")
                print(f'The word is: {word_of_choice}')
                return
        else:
            tries -= 1
            print(f"Incorrect guess. You have {tries} tries left.")
    
    print("Try again next time.")
# main function
def main():
    if is_admin():
        word_of_choice = get_word_of_choice()
        harshed_words = create_harshed_words(word_of_choice)
        play_game(word_of_choice, harshed_words)

if __name__ == "__main__":
    main()
