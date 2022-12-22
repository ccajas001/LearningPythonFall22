# Learning Project TIQC
# Intern: Camille Cajas
# Final Project Name = Magic 8-ball Answer Generator

from tkinter import *
import random

# class generates 8ball generator
class EightBallGen:

    # constructor
    def __init__(self, master):
        # frame for entry and buttons
        frame1 = Frame(master)
        frame1.pack()

        # frame for history lists
        frame2 = Frame(master)
        frame2.pack(side=BOTTOM)

        # history lists
        self.questionHistoryItems = ['Questions', '']
        self.answerHistoryItems = ['Answers', '']

        # user input variable
        self.userInput = StringVar()

        # label to display directions to the user
        self.questionDirection = Label(frame1, text="What question would you like to ask the 8-Ball? :D")
        self.questionDirection.pack()

        # user input widget
        self.entry = Entry(frame1, width=40, textvariable=self.userInput)
        self.entry.focus_set()
        self.entry.pack()

        # answer label that displays answer for latest question
        self.answerLabel = Label(frame1, text="")
        self.answerLabel.pack(side=BOTTOM)

        # button that updates list and displays answer
        self.answerGen = Button(frame1, text="Generate Answer", command=self.displayhistory)
        self.answerGen.pack(side=BOTTOM)

        # question and history text boxes
        self.questionHistTextbox = Text(frame2)
        self.questionHistTextbox.pack(side=LEFT)

        self.answerHistTextbox = Text(frame2)
        self.answerHistTextbox.pack(side=LEFT)



    # displays history in two frames created in the constructor
    def displayhistory (self):

        # ensures user input at least something
        if self.userInput.get() != '':

            # takes user input and adds it to questions list
            self.questionHistoryItems.append(self.userInput.get())

            # updates text in question history text widget by deleting former text and
            # replacing with updated list
            self.questionHistTextbox.delete("1.0", "end")
            for item in self.questionHistoryItems:
                self.questionHistTextbox.insert(END, item + '\n')

            # gets answer from function give8ballanswer() and adss to answers list
            answer = self.give8ballanswer()
            self.answerHistoryItems.append(answer)

            # updates text in answer history text widget by deleting former text and
            # replacing with updated list
            self.answerHistTextbox.delete("1.0", "end")
            for item in self.answerHistoryItems:
                self.answerHistTextbox.insert(END, item + '\n')

            # updated answer label for last asked question
            self.answerLabel.config(text=answer)

            # deletes user's input from entry widget to make space for new question
            self.entry.delete(0, END)

    # returns randomized answer
    def give8ballanswer (self):
        value = random.randint(1, 8)
        answer = ""
        if value == 1:
            answer = "It is certain."
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

        # returns answer
        return answer


root = Tk()

# instance of EightBallGen class using Tkinter
g = EightBallGen(root)


# lets the window stay on the screen
root.mainloop()
