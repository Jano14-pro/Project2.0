from tkinter import*

win = Tk()
win.geometry("500x500")
win.title("KDJ Tk Project1")

nav_Frame = Frame(win,width = 100,height = 100,bg = "black" )
nav_Frame.place(relx=0.1,rely=0.1,)

second_Frame = Frame(win,width = 100,height = 100,bg = "black" )
second_Frame.place(relx=0.4,rely=0.1,)

third_Frame = Frame(win,width = 100,height = 100,bg = "black" )
third_Frame.place(relx=0.7,rely=0.1,)

fourth_Frame = Frame(win,width = 100,height = 100,bg = "grey" )
fourth_Frame.place(relx=0.1,rely=0.4,)

fifth_Frame = Frame(win,width = 100,height = 100,bg = "grey" )
fifth_Frame.place(relx=0.4,rely=0.4,)

sixth_Frame = Frame(win,width = 100,height = 100,bg = "grey" )
sixth_Frame.place(relx=0.7,rely=0.4,)

seventh_Frame = Frame(win,width = 100,height = 100,bg = "gold" )
seventh_Frame.place(relx=0.1,rely=0.7,)

eighth_Frame = Frame(win,width = 100,height = 100,bg = "gold" )
eighth_Frame.place(relx=0.4,rely=0.7,)

ninth_Frame = Frame(win,width = 100,height = 100,bg = "gold" )
ninth_Frame.place(relx=0.7,rely=0.7,)


win.mainloop()