from tkinter import *
import advanced_uix
import os

difficulty_map={"EASY":18,"REGULAR":14,"MEDIUM":11,"HARD":9,"LEGENDARY":8}
        

def congrats(root=None,name=""):
    if root != None:
        root.destroy()
    root2=Tk()
    Image=PhotoImage(file=os.getcwd()+"//dependencies//congratulation.png",master=root2)
    Label(root2,image=Image).grid(row=0,column=0)
    Label(root2,text=name,font=('monotype corsiva',50,"italic")).grid(row=1,column=0)
    Label(root2,text="You have successfully defeated me\n in the game of mastermind",font=('monotype corsiva',25,"italic")).grid(row=2,column=0)
    root2.after(5000, lambda: root2.destroy())
    root2.mainloop()


class Playmat:
    def __init__(self,root,row_matrix,name,no_of_tries,difficulty):
        if len(row_matrix)>5:
            temp=row_matrix[-1:-6:-1]
            self.rowmatrix=temp[::-1]
        else:
            self.rowmatrix=row_matrix
        self.bias=len(row_matrix)-len(self.rowmatrix)
        self.frame=Frame(root)
        self.frame.grid(row=0,column=0)
        self.populateframe()
        if row_matrix !=[]:
            last_element=row_matrix[-1]
            if last_element[1][0]==4:
                congrats(root,name)
                fobj=open(os.getcwd()+'//dependencies//record.txt',"a")
                fobj.write(name+" "+str(difficulty_map[difficulty]-no_of_tries)+" "+"W"+"\n")
                fobj.close()
                root.destroy()
    def populateframe(self):
        for i in range(min(5,len(self.rowmatrix))):
            advanced_uix.Row(self.frame,self.rowmatrix[i][0],self.rowmatrix[i][1],i,self.bias)
        for j in range(min(5,len(self.rowmatrix)),8):
            advanced_uix.EmptyRow(j,self.frame)
    def display_answer(self,answer):
        
        for i in range(min(5,len(self.rowmatrix))):
            advanced_uix.Row(self.frame,self.rowmatrix[i][0],self.rowmatrix[i][1],i,self.bias)
        advanced_uix.Row(self.frame,answer,[4,0],5,-1)
        for j in range(6,8):
            advanced_uix.EmptyRow(j,self.frame)
        
