from tkinter import *
from tkinter.messagebox import showinfo
import os

class Extras:
    def __init__(self,root):
        self.frame=Frame(root)
        self.frame.grid(row=0,column=1,columnspan=5)
        self.fillframe()
    def leaderboard(self):
        fobj=open(os.getcwd()+'//dependencies//record.txt','r')
        Read=fobj.read()
        fobj.close()
        L=Read.split('\n')
        L.pop(-1)
        winners_only=[]
        for i in L:
            temp=i.split(' ')
            if temp[2]=="W":
                winners_only.append(temp[:2:])
        winners_only.sort(key= lambda x:int(x[1]))
        self.root=Tk()
        n=len(winners_only)
    
        Label(self.root,height=1,width=15,text="PLAYER NAME",fg="blue"
               ,font=('Copperplate Gothic Bold',20)).grid(row=0,column=0)

        Label(self.root,height=1,width=15,text="GAMES PLAYED",fg="blue"
                ,font=('Copperplate Gothic Bold',20)).grid(row=0,column=1)

        for i in range(n):
            Label(self.root,height=1,width=15,text=winners_only[i][0],fg="green yellow",bg="black"
                   ,font=('Copperplate Gothic Bold',20)).grid(row=i+1,column=0)

            Label(self.root,height=1,width=15,text=winners_only[i][1],fg="white",bg="black"
                    ,font=('Copperplate Gothic Bold',20)).grid(row=i+1,column=1)

        self.root.mainloop()
    def help(self):
        self.help_root=Tk()
        fobj=open(os.getcwd()+'//dependencies//rules.txt','r')
        Text_Variable=fobj.read()
        fobj.close()
        Label(self.help_root,text=Text_Variable,font=('Copperplate Gothic Bold',20),fg="green yellow",bg="black").grid(row=0,column=0)
        self.help_root.mainloop()
    def fillframe(self):
        Button(self.frame,height=1,width=10,text="Leaderboard",fg="green yellow",bg="black"
               ,font=('Copperplate Gothic Bold',41),command=self.leaderboard).grid(row=0,column=0)

        Button(self.frame,height=1,width=10,text="HELP",fg="green yellow",bg="black"
                       ,font=('Copperplate Gothic Bold',41),command=self.help).grid(row=0,column=1)




class ultra_mod_button:
    def __init__(self,color,root,List,_column):
        self.color=color
        self.list=List
        self.fg="black"
        self.root=root
        self.column=_column
        if self.color=="black":
            self.fg="white"
        Button(root,text="Ball",height=2,width=8,font=('Copperplate Gothic Bold',25)
                   ,bg=self.color,fg=self.fg,command=self.on_click_listener).grid(row=4,column=_column)
    def on_click_listener(self):
        self.list.pop(self.column-1)
        self.put_in_choices(self.root,self.list)
    def put_in_choices(self,root,List):
        for i in range(len(List)):
            ultra_mod_button(List[i],root,List,1+i)
        for j in range(4-len(List)):
            Button(root,text="Choose a\nBall",height=2,width=8,font=('Copperplate Gothic Bold',25)
                  ,bg="grey",state='disabled').grid(row=4,column=len(List)+j+1)
        

class Mod_Button:
    """
    The following class contains the modified button with a builtin in listener
    """
    def __init__(self,color,root,List,_row,_column):
        self.color=color
        self.list=List
        self.fg="black"
        self.root=root
        if self.color=="black":
            self.fg="white"
        Button(root,text="Ball",height=2,width=8,font=('Copperplate Gothic Bold',25)
                   ,bg=self.color,fg=self.fg,command=self.on_click_listener).grid(row=_row,column=_column)
    def on_click_listener(self):
        if len(self.list)<4:
            self.list.append(self.color)
            self.put_in_choices(self.root,self.list)
        else:
            showinfo('','You have already selected 4 balls.Please unselect one of the balls in order to make a selection available.')

    def put_in_choices(self,root,List):
        for i in range(len(List)):
            ultra_mod_button(List[i],root,List,1+i)
        for j in range(4-len(List)):
            Button(root,text="Choose a\nBall",height=2,width=8,font=('Copperplate Gothic Bold',25)
                  ,bg="grey",state='disabled').grid(row=4,column=len(List)+j+1)



class Row:
    """
    The following class contains the descriptions to create one individual row of the playmat
    that contains one guess taken by the player
    """
    def __init__(self,root,List,pins,row,bias):
        self.list=List
        self.pins=pins
        self.row=row
        self.bias=bias
        self.frame=Frame(root,height=2,width=32)
        self.frame.configure(background="green")
        self.frame.grid(row=self.row,column=0)
        self.fill_frame()
    def fill_frame(self):
        Label(self.frame,text="",height=2,width=2,font=('Copperplate Gothic Bold',27),
              bg="brown").grid(row=self.row,column=0)
        if self.bias != -1:
            Label(self.frame,text="Attempt no:"+str(self.row+self.bias+1),font=('Copperplate Gothic Bold',27),
                  width=12,height=2,fg="black",bg="green").grid(row=self.row,column=1)
        else:
            Label(self.frame,text="My Guess Was:",font=('Copperplate Gothic Bold',27),width=12,height=2,
                  fg="black",bg="green").grid(row=self.row,column=1)
        for i in range(4):
            Button(self.frame,text=str(i+1),height=2,width=5,font=('Copperplate Gothic Bold',20),bg=self.list[i]
                   ,state="disabled").grid(row=self.row,column=2+i)
        Label(self.frame,text="",height=2,width=2,font=('Copperplate Gothic Bold',27),
              fg="blue",bg="green").grid(row=self.row,column=6)
        for j in range(self.pins[0]):
            Button(self.frame,text="",width=1,font=('Copperplate Gothic Bold',10),bg="red"
                   ,state="disabled").grid(row=self.row,column=7+j)
        for k in range(self.pins[1]):
            Button(self.frame,text="",width=1,font=('Copperplate Gothic Bold',10),bg="white"
                   ,state="disabled").grid(row=self.row,column=7+self.pins[0]+k)
        for l in range(4-(self.pins[1]+self.pins[0])):
            Button(self.frame,text="",width=1,font=('Copperplate Gothic Bold',10),bg="grey"
                   ,state="disabled").grid(row=self.row,column=10-l)
        
        Label(self.frame,text="",height=2,width=3,font=('Copperplate Gothic Bold',27),
              bg="brown").grid(row=self.row,column=11)
        
        Label(self.frame
              ,text="",width=106,font=('Copperplate Gothic Bold',10),
              bg="white").grid(row=self.row+1,column=0,columnspan=12)


class EmptyRow:
    def __init__(self,_row,root):
        self.frame=Frame(root)
        self.frame.configure(background="white")
        self.frame.grid(row=_row,column=0)
        
        Label(self.frame
              ,text="",height=2,width=40,font=('Copperplate Gothic Bold',27),
              bg="green").grid(row=1,column=0)

        Label(self.frame
              ,text="",width=40,font=('Copperplate Gothic Bold',1),
              bg="white").grid(row=2,column=0)


