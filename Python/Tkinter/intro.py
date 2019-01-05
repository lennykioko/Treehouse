import tkinter

root = tkinter.Tk()

text1 = tkinter.Label(
    root,
    text='Welcome to learning Tkinter with @kennethlove from Treehouse',
    bg='blue',
    fg='white',
)

text1.pack(fill=tkinter.BOTH, expand=True)
text2 = tkinter.Label(text='My name is Lenny Kioko, I am a software developer')
text2.pack()

root.mainloop()
