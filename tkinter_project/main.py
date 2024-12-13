import tkinter
window = tkinter.Tk()
window.title("My first GUI program")
window.minsize(width=500,height=300)

my_lable = tkinter.Label(text= "Iam a Label",font = ("Arial",24,"bold"))
my_lable.pack()

my_lable["text"] = "Avengers Essemble"
my_lable.config(text="Avengers Essemble")

def button_click():
    print("I got clicked")
    new_text = input.get()
    my_lable.config(text=new_text)

button = tkinter.Button(text="Click me",command=button_click)
button.pack()

input = tkinter.Entry()
input.pack()


window.mainloop()