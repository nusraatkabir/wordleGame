import random
def give_instructions():
    print('''\n Wordle is a word guessing game.
    You have 5 attempts
    (C) means the letter is in the word and in the correct position.
    (WP) means the letter is in the word but not in the correct position.
    (NT) means the letter is not there in the word itself.  

    Best of Luck''')

words =['this', 'five', 'help', 'pink', 'lake', 'cats'] 
hidden_word= random.choice(words)
def check_word (guess):
    if hidden_word == guess:
            print("Congrats!! You did it.")
            return True
    else:
            result = ""
            for i,j in zip(guess, hidden_word):
                if i == j:
                    result = result + "(C)"
                elif i in hidden_word:
                    result = result + "(WP)"
                else:
                    result = result + "(NT)" 
            print(result)
            return False
def main():
     attempt = 5
     give_instructions()
     while attempt > 0:
          guess = input("Enter a four letter word:")
          if check_word(guess):
               break
          else: 
               attempt -= 1 #attempt = attempt -1
               print(f"You have {attempt} attempts left.")
     else:
        print('Game Over')

main()
