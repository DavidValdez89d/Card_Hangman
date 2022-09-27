import random
from utils.hangman_image import hangman_image


#Just for this game
class Hangman:
    #Is the same for all the games
    possible_words: list[str] = ['becode', 'learning', 'mathematics', 'sessions']

    def __init__(self):
        """
        Class that contains all the blocks for the Hangman game
        """
        self.word_to_find: list[str] = [letter for letter in random.choice(self.possible_words).upper()] #returns a list of LETTERS of the word
        self.word_letters: set[str] = set(self.word_to_find)
     
        self.lives: int = 5
        self.turn_count: int = 0  #total number of turns
        self.error_count: int = 0  #total of whrong guesses
        
        self.user_guess_letter: str = ""  #User input
        self.used_guessed_letters: set[str] = set()  #All letters so far
        self.correctly_guessed_letters: list[str]= []  #Correct letters
        self.wrongly_guessed_letters: list[str]  = []  #Wrong letters
        #self.well_guessed_letters: list[str] = []  error
        
        self.valid_english_letters: set[str] = {'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'}
    
    def play(self):
        """
        Function that will loop in the main loop of the game
        :contains the input and score text
        :params: user_input
        """
        #Message for each turn ----------
        print(f'Well guessed letters: {" ".join(self.correctly_guessed_letters)}, Bad guessed letters: {" ".join(self.wrongly_guessed_letters)}, Live: {self.lives}, Error count: {self.error_count}, Turn count: {self.turn_count}')
        
        hangman_word = [letter if letter in self.used_guessed_letters else '_' for letter in "".join(self.word_to_find)]
        
        print(hangman_image[self.lives])
        print ('Hangman: ', ' '.join(hangman_word),'\n')


        #Turn count ---------------
        self.turn_count = self.turn_count + 1

        #Get input ----------------
        self.user_guess_letter: str = input('Please enter one leter (A-Z):').upper()
        
        #Validate input
        if len(self.user_guess_letter) !=  1 :
            print(f'Error, {self.user_guess_letter} is not a valid input')
        
            #check letter Hangman
        elif self.user_guess_letter in self.valid_english_letters - self.used_guessed_letters :
            self.used_guessed_letters.add(self.user_guess_letter)
            
            #Score
            if self.user_guess_letter in self.word_letters:
                self.word_letters.remove(self.user_guess_letter)
                self.correctly_guessed_letters.append(self.user_guess_letter)
                print('')
            
            #Losse a life point, gain an error point
            else:
                self.wrongly_guessed_letters.append(self.user_guess_letter)
                #Lives count --------------
                self.lives = self.lives - 1

                #Error count --------------
                self.error_count = self.error_count + 1
                print(f'{self.user_guess_letter} not in word')
        
        elif self.user_guess_letter in self.used_guessed_letters:
            print(f'\n{self.user_guess_letter} already used, chosse another letter')
        else:
            print(f'\nNot a valid letter!\n')



    def game_over(self):
        """
        Function that will run if lives = 0
        """
        #exit the game and show the answer
        print(hangman_image[self.lives])
        print (f'...game over...\n The word was :\n{" ".join(self.word_to_find)}')
        
    
    def well_played(self):
        """
        Function that will run if user guess word
        """
        #exit the game
        print(f'You found the word: {" ".join(self.word_to_find)} in {self.turn_count} turns with {self.error_count} errors!')


    
    def start_game(self):
        """
        Main function that will run the code
        """
        #Main loop
        while len(self.word_letters) > 0 and self.lives > 0 :
            self.play()
        #Exit if losse
        if self.lives == 0:
            self.game_over()
        #Exit if win
        else:
            self.well_played()
        

if __name__ == '__main__':
    Hangman()
    
        

