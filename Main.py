from utils.game import Hangman

while True:
    game = Hangman()
    game.start_game()
    continue_game: str = input('Do want to play again ? (y / n)').upper()
    if continue_game != 'Y':
        break