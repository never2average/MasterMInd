import create_game
import create_gui
from tkinter import *
import os
color_code={"1":"red","2":"blue",'3':"black",'4':"white",'5':"magenta",'6':"yellow",'7':"pink",'8':'green','9':"orange"}
class playgame:
    def _on_click_listener(self):
        self.player_name=self.Entry.get()
        if self.player_name=="":
            self.player_name="PLAYER1"
        self.no_of_tries=self.difficulty_map[self.iterator][1]
        self.difficulty=self.difficulty_map[self.iterator][0]
        self.root.destroy()
    def prev_click(self):
        self.iterator-=1
        if self.iterator<-5:
            self.iterator=-1
        Label(self.root,text=self.difficulty_map[self.iterator][0],font=('monotype corsiva',25,"italic"),bg="white"
              ,width=12).grid(row=2,column=2)
    def next_click(self):
        self.iterator+=1
        if self.iterator>4:
            self.iterator=0
        Label(self.root,text=self.difficulty_map[self.iterator][0],font=('monotype corsiva',25,"italic"),bg="white"
              ,width=12).grid(row=2,column=2)
    def first_screen(self):
        self.root=Tk()
        self.root.config(background="white")
        self.difficulty_map=[["EASY",18],["REGULAR",14],["MEDIUM",11],["HARD",9],["LEGENDARY",8]]

        Label(self.root,text="MASTERMIND",font=('monotype corsiva',45,"bold")
              ,fg="red",bg="white").grid(row=0,column=0,columnspan=4)
        
        Label(self.root,text="Enter Your In-Game Name:",font=('monotype corsiva',25,"italic"),bg="white").grid(row=1,column=0,sticky="e")

        self.Entry=Entry(self.root,font=('monotype corsiva',25,"italic"))
        self.Entry.grid(row=1,column=1,columnspan=3)
        
        Label(self.root,text="Choose Difficulty Level:",font=('monotype corsiva',25,"italic"),bg="white").grid(row=2,column=0,sticky="e")

        p1=PhotoImage(file=os.getcwd()+'//dependencies//left_arrow.png',master=self.root)
        Button(self.root,image=p1,command=self.prev_click).grid(row=2,column=1)

        self.iterator=0
        Label(self.root,text=self.difficulty_map[self.iterator][0],font=('monotype corsiva',25,"italic")
              ,width=12,bg="white").grid(row=2,column=2)

        
        p2=PhotoImage(file=os.getcwd()+'//dependencies//right_arrow.png',master=self.root)
        Button(self.root,image=p2,command=self.next_click).grid(row=2,column=3)
        

        Button(self.root,text="Begin Game",font=('copperplate gothic bold',25,"italic")
               ,command=self._on_click_listener).grid(row=3,column=0,columnspan=4)
        
        self.root.mainloop()

    def convert(self,string):
        l=[]
        for i in string:
            l.append(color_code[i])
        return l
    
    def actual_game(self):
        self.first_screen()
        self.answer=self.convert(create_game.create_game())
        self.game=create_gui.create_gui(self.player_name,self.no_of_tries,self.answer,self.difficulty)
