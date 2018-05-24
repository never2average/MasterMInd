from tkinter import *
import statsmat,playmat
class create_gui:
    def __init__(self,name,no_of_tries,answer,difficulty):
        self.name=name
        self.no_of_tries=no_of_tries
        self.answer=answer
        self.difficulty=difficulty
        self.row_matrix=[]
        self.integrate()
        
    def integrate(self):
        self.main_screen=Tk()
        self.main_screen.state("zoomed")
        self.main_screen.configure(background='white')
        statsmat.statsmat(self.main_screen,self.name,self.no_of_tries,
                          self.answer,self.row_matrix,self.difficulty)
        playmat.Playmat(self.main_screen,self.row_matrix,self.name,
                        self.no_of_tries,self.difficulty)
        self.main_screen.mainloop()
