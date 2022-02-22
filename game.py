import random
import phrase

class Game:
    def __init__(self, guesses=0, missed=0):
        self.phrases = ['double tap', 'ace in the hole', 'holy grail', 'goofy goober', 'rubiks cube']
        self.active_phrase = None
        self.guesses = guesses
        self.missed = missed
        self.guessed_letters = []
    
    def welcome(self):
        print('\nWelcome to Phrase Hunters')
    
    def get_random_phrase(self):
        self.active_phrase = True
        return self.phrases[random.randint(0, len(self.phrases)-1)]
    
    def get_guess(self):
        guess = input('\nGuess a letter:  ').lower()
        if guess in self.guessed_letters:
            print('You have already guessed that one')
            guess = input('Guess another letter:  ').lower()
        if len(guess)>1:
            guess = input('Please make a valid guess  ')
        self.guessed_letters.append(guess)
        self.guesses +=1
        return guess
    
    def game_over(self):
        print(f'\nGreat job! You did it in {self.guesses} guesses!')
        print(f'You missed {self.missed} times out of {self.guesses}')
        play_again = input('Would you like to play again? y or n  ').lower()
        if play_again == 'y':
            Game.start()
        else:
            print('Thank you for playing!')
    
    @classmethod
    def start(cls):
        game = Game()
        game.welcome()
        the_phrase = phrase.Phrase(game.get_random_phrase())
        the_phrase.display()
        while game.active_phrase == True:
            the_guess = game.get_guess()
            print('   ø:',*list(set(game.guessed_letters)-set(the_phrase)), sep=" ")
            if the_phrase.check_letter(the_guess):
                the_phrase.display()
                if the_phrase.check_complete():
                    game.active_phrase = False
            else:
                the_phrase.display()
                game.missed+=1
                print('Incorrect, please try again')
        game.game_over()