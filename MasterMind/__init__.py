__author__="Priyesh Srivastava"
#This is a program that generates the game "MasterMind"
__version__="1.0.0"
__all__=["create_gui","get_pins","create_game",
         "play_game","advanced_uix","playmat","statsmat"]


def get_pins(guess,answer):
    import get_pins
    """
    This function returns the number of red and white pins that
    a particular guess should be awarded  
    """
    return get_pins.get_pins(guess,answer)


def create_game():
    import create_game
    """
    This particular function generates a random sequence of 4 digits once
    at the beginning of every game. 
    """
    return create_game.create_game()


def advanced_uix():
    import advanced_uix
    """
    This particular function is present to generate specific ui elements
    to develop gui more easily
    """

def playmat():
    import playmat
    """This particular function will be able to create the playmat that shows to the user their
    previous 5 guesses along with the pins allotted for each guess"""
    

def statsmat():
    import statsmat
    """This function will be able to create the statsmat that handles all the statistical parts
    of the game such as keeping count of tries remaining,player name etc."""


def create_gui():
    import create_gui
    """
    This particular function generates the interactive gui for the
    entire mastermind game using the Tkinter library. 
    """
    create_gui.create_gui()    


def play_game():
    import play_game
    """
    This particular function is actually responsible for allowing the entire game being
    compiled as a single unit, accepting and passing on various values of parameters.
    Setting the game up,displaying the game window and ending the game.
    """
    game=play_game.playgame()
    game.actual_game()
    
    
if __name__=="__main__":
    play_game()
