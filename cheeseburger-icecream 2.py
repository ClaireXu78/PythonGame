from tkinter import *

root = Tk()
root.geometry("775x500")

instruction = "↓ Click one of these button ↓"
left = "Option 1"
right = "Option 2"
ice_cream = "Ice Cream"
cheeseburger = "Cheeseburger"
leftLabel = "Question:"
rightLabel = "↓ Canvas ↓"
xOffSet = 70
yOffSet = 20


var = IntVar()
question = IntVar()
clinic = IntVar()

def drawCheeseburger():
    clearCanvas()
    canvas.create_oval(xOffSet+100, yOffSet+90, xOffSet+200, yOffSet+160, fill="tan")
    canvas.create_rectangle(xOffSet+100, yOffSet+115, xOffSet+200, yOffSet+135, fill="white", outline="white")
    canvas.create_rectangle(xOffSet+100, yOffSet+115, xOffSet+200, yOffSet+120, fill="chartreuse2", outline="chartreuse2")
    canvas.create_rectangle(xOffSet+100, yOffSet+120, xOffSet+200, yOffSet+125, fill="yellow", outline="yellow")
    canvas.create_rectangle(xOffSet+100, yOffSet+125, xOffSet+200, yOffSet+135, fill="sienna4", outline="sienna4")
    canvas.create_oval(xOffSet+120, yOffSet+105, xOffSet+123, yOffSet+108, fill="papaya whip")
    canvas.create_oval(xOffSet+130, yOffSet+100, xOffSet+133, yOffSet+103, fill="papaya whip")
    canvas.create_oval(xOffSet+145, yOffSet+102, xOffSet+148, yOffSet+105, fill="papaya whip")
    canvas.create_oval(xOffSet+160, yOffSet+100, xOffSet+163, yOffSet+103, fill="papaya whip")
    canvas.create_oval(xOffSet+170, yOffSet+105, xOffSet+173, yOffSet+108, fill="papaya whip")

def drawIceCream():
    clearCanvas()
    canvas.create_oval(xOffSet+125, yOffSet+100, xOffSet+175, yOffSet+150, fill="lemon chiffon", outline="lemon chiffon")
    canvas.create_polygon(xOffSet+120, yOffSet+125, xOffSet+180, yOffSet+125, xOffSet+150, yOffSet+200, fill='tan')
    canvas.create_oval(xOffSet+148, yOffSet+89, xOffSet+163, yOffSet+104, fill="salmon", outline="salmon")

def drawTooEarly():
    clearCanvas()
    canvas.create_text(xOffSet+150, yOffSet+100, text="Too early! You fell asleep!", font=("Comic Sans MS", 20))

def drawTooHot():
    clearCanvas()
    canvas.create_text(xOffSet+160, yOffSet+100, text="Too hot! You are melting!", font=("Comic Sans MS", 25))

def clearCanvas():
    canvas.create_rectangle(0, 0, 400, 300, fill="light blue", outline="light blue")

def leftPressed():
    quiz(True, var.get(), question.get(), clinic.get())

def rightPressed():
    quiz(False, var.get(), question.get(), clinic.get())

def quiz(buttonPressed, choose_icecream, question, clinic):
    if (question == 1):
        if not buttonPressed:
            if (choose_icecream == 1):
                drawIceCream()
            else:
                drawCheeseburger()
        else:
            if clinic == 730:
                drawTooEarly()
            else:
                drawTooHot()
    elif (question == 2):
        if not buttonPressed:
            if (choose_icecream == 1):
                drawIceCream()
            else:
                drawCheeseburger()
        else:
            if clinic == 730:
                drawTooEarly()
            else:
                drawTooHot()
    else:
        if buttonPressed:
            if (choose_icecream == 1):
                drawIceCream()
            else:
                drawCheeseburger()
        else:
            if clinic == 730:
                drawTooEarly()
            else:
                drawTooHot()

def displayQuestion1():
    clearCanvas()
    instruction = "What is Venice's zodiac sign?"
    left = "Scorpio"
    right = "Gemini"
    buttonInstruction.config(text=instruction)
    buttonLeftChoice.config(text=left)
    buttonRightChoice.config(text=right)

def displayQuestion2():
    clearCanvas()
    instruction = "What was Claire's friend she hangs out with the most before I came to Harker?"
    left = "Alexa"
    right = "Grace"
    buttonInstruction.config(text=instruction)
    buttonLeftChoice.config(text=left)
    buttonRightChoice.config(text=right)
    radioIce.config(text=ball)

def displayQuestion3():
    clearCanvas()
    instruction = "What does Claire prefer?"
    left = "Minecraft"
    right = "Roblox"
    buttonInstruction.config(text=instruction)
    buttonLeftChoice.config(text=left)
    buttonRightChoice.config(text=right)

canvasLabel = Label (root, text=rightLabel)
answerLabel = Label (root, text=leftLabel)
buttonInstruction = Button(root,text=instruction)
button1 = Radiobutton(root,text="1", variable=question, value=1, command=displayQuestion1)
button2 = Radiobutton(root,text="2", variable=question, value=2, command=displayQuestion2)
button3 = Radiobutton(root,text='3', variable=question, value=3, command=displayQuestion3)
clinicLeft = Radiobutton(root,text='TENNIS PRACTICE UwU ~ 7:30 AM', variable=clinic, value=730)
clinicRight = Radiobutton(root,text='SOCCER PRACTICE :3 ~ 4:30 PM', variable=clinic, value=430)
buttonLeftChoice = Button(root, text=left, command=leftPressed)
buttonRightChoice = Button(root, text=right, command=rightPressed)
radioIce = Radiobutton(root, text=ice_cream, variable=var, value=1)
radioCheese = Radiobutton(root, text=cheeseburger, variable=var, value=2)
canvas = Canvas(root, bg="light blue", height=300, width=450)

# pack each widget
canvasLabel.place(x=490, y=30)
answerLabel.place(x=95, y=30)
buttonInstruction.place(x=30, y=73)
button1.place(x=40, y=120)
button2.place(x=113, y=120)
button3.place(x=183, y=120)
clinicLeft.place(x=20, y=300)
clinicRight.place(x=20, y=370)
buttonLeftChoice.place(x=40, y=170)
buttonRightChoice.place(x=175, y=170)
radioIce.place(x=20, y=230)
radioCheese.place(x=145, y=230)
canvas.place(x=700, y=330)
canvas.pack(side=RIGHT, pady=10)
root.mainloop()
