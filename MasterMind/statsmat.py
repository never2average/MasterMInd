from tkinter import *
from tkinter.messagebox import *
import advanced_uix, get_pins,playmat

class statsmat:
    
    def __init__(self,root,name,tries,answer,row_matrix,difficulty):
        self.frame=Frame(root,height=2,width=32)
        self.frame.configure(background="black")
        self.frame.grid(row=0,column=1)
        self.no_of_tries=tries
        self.name=name
        self.root=root
        self.difficulty=difficulty
        self.answer=answer
        self.row_matrix=row_matrix
        self.populatestatsmat()
        
    def put_in_choices(self,root,List):
        for i in range(len(List)):
            advanced_uix.ultra_mod_button(List[i],root,List,1+i)
        for j in range(4-len(List)):
            Button(root,text="Choose a\nBall",height=2,width=8,font=('Copperplate Gothic Bold',25)
                  ,bg="grey",state='disabled').grid(row=4,column=len(List)+j+1)
    
    def populatestatsmat(self):
        self.guess=[]
        advanced_uix.Extras(self.frame)
        l=[self.name,"Number of tries remaining:"+str(self.no_of_tries),"Current Guess:"]
        for i in range(3):
            Label(self.frame,text=l[i],height=2,width=32,font=('Copperplate Gothic Bold',25),
                  bg="blue").grid(row=i+1,column=1,columnspan=4)

        self.put_in_choices(self.frame,self.guess)
        Label(self.frame,text="rubbi\nsh",height=1,width=20,font=('Copperplate Gothic Bold',41)
              ,bg="Black").grid(row=5,column=1,columnspan=5)

        l1=["red","blue","black","white","magenta","yellow","pink","green","orange"]
        for A in range(9):
            advanced_uix.Mod_Button(l1[A],self.frame,self.guess,6+A//4,1+A%4)

        self.submission=Button(self.frame,text="Submit Answer",height=2,width=25
                               ,font=('Copperplate Gothic Bold',25),command=self.submitchoice)
        if self.no_of_tries==0:
            self.submission.config(text="Reveal Guess")
        self.submission.grid(row=8,column=2,columnspan=3)

    def submitchoice(self):
        if self.no_of_tries==0:
            self.submission.config(state="disabled")
            showinfo("","Your mastermind skills need some improvement")
            p=playmat.Playmat(self.root,self.row_matrix,self.name,self.no_of_tries,self.difficulty)
            p.display_answer(self.answer)
        else:
            if len(self.guess)!=4:
                showinfo('','please choose 4 balls in order to make a valid guess')
            else:
                self.no_of_tries-=1
                l=get_pins.get_pins(self.guess,self.answer)
                self.row_matrix.append([self.guess,l])
                self.populatestatsmat()
                playmat.Playmat(self.root,self.row_matrix,self.name,self.no_of_tries,self.difficulty)
