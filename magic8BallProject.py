from tkinter import *
import random


# class generates 8ball generator
class EightBallGen:

    # constructor
    def __init__(self, master):
        frame1 = Frame(master)
        frame1.pack()
        frame2 = Frame(master)
        frame2.pack(side=BOTTOM)

        self.questionHistoryItems = ['Questions', '']
        self.answerHistoryItems = ['Answers', ' ']
        self.userInput = StringVar()

        self.questionDirection = Label(frame1, text="What question would you like to ask the 8-Ball? :D")
        self.questionDirection.pack()

        self.entry = Entry(frame1, width=40, textvariable=self.userInput)
        self.entry.focus_set()
        self.entry.pack()

        self.answerTextbox = Label(frame1, text=" ")
        self.answerTextbox.pack()

        self.answerGen = Button(frame1, text="Generate Answer", command=self.displayhistory)
        self.answerGen.pack(side=LEFT)

        self.quitButton = Button(frame1, text="Quit", command=frame1.quit())
        self.quitButton.pack(side=LEFT)

        self.questionHistTextbox = Text(frame2)
        self.questionHistTextbox.pack(side=LEFT)

        self.answerHistTextbox = Text(frame2)
        self.answerHistTextbox.pack(side=LEFT)

    # displays history in two frames created in the constructor
    def displayhistory(self):
        # displays questions of the history textbox
        self.questionHistoryItems.append(self.userInput.get())
        self.questionHistTextbox.delete("1.0", "end")
        for item in self.questionHistoryItems:
            self.questionHistTextbox.insert(END, item + '\n')

        # displays the answers to those questions in the history textbox
        hist2 = self.printanswer()
        self.answerHistoryItems.append(hist2)
        self.answerHistTextbox.delete("1.0", "end")
        for item in self.answerHistoryItems:
            self.answerHistTextbox.insert(END, item + '\n')

        self.entry.delete(0,END)

    # returns randomized answer
    def printanswer(self):
        value = random.randint(1, 8)
        text = ""
        if value == 1:
            answer = " It is certain."
        elif value == 2:
            answer = "It is decidedly so"
        elif value == 3:
            answer = "Yes definitely."
        elif value == 4:
            answer = "Ask again later."
        elif value == 5:
            answer = "Cannot predict now."
        elif value == 6:
            answer = "My reply is no."
        elif value == 7:
            answer = "My sources say no."
        else:
            answer = "Very doubtful."

        # puts answer in text box on screen
        self.answerTextbox.config(text=answer)

        # returns answer
        return answer


root = Tk()
g = EightBallGen(root)
root.mainloop()
