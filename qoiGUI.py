import random
from inputProcessor import *
from tkinter import *
from speechToText import *

class Qoi:
    def __init__(self, master):
        self.resultsArray = []
        self.master = master
        master.title("Qoi")

        self.message = "Hi there, how can I help?"
        self.label_text = StringVar()
        self.label_text.set(self.message)
        self.label = Label(master, width=80, textvariable=self.label_text, font=("Courier", 14))

        self.entry = Entry(master, width=80, font=("Courier", 14))

        self.find_button = Button(master, text="Find Answer", font=("Courier", 14), command=self.find_pressed)
        self.voice_button = Button(master, text="Use Voice", font=("Courier", 14), command=self.voice_pressed)
        
        self.label.grid(row=0, column=0, columnspan=5, sticky=W+E)
        self.entry.grid(row=1, column=1, columnspan=5, sticky=W+E)
        self.entry.focus()
        self.find_button.grid(row=2, column=3)
        self.voice_button.grid(row=2, column=2)

    def find_pressed(self):
        if len(self.entry.get()) == 0:
            return;
        self.label= Label(self.master, width=80, font=("Courier", 14), text="Review your answer below...")
        self.label.grid(row=0, column=0, columnspan=5, sticky=W+E)
        
        entryText = self.entry.get()
        
        self.entry.destroy()
        self.find_button.destroy()
        self.voice_button.destroy()
        
        inputText = []
        inputP = inputProcessor()
        inputText= inputP.getSummary(entryText)
        self.resultsArray = inputText
        
        self.button_1 = Button(self.master, fg='black', bg='light grey' ,
                               text="Get Answer", font=("Courier", 14), command=self.button_1_pressed)
        self.button_1.grid(row=1, column=0, columnspan=5, sticky=W+E)
        self.button_2 = Button(self.master, fg='black', bg='light grey' ,
                               text="Get Statistics", font=("Courier", 14), command=self.button_2_pressed)
        self.button_2.grid(row=2, column=0, columnspan=5, sticky=W+E)
        self.button_3 = Button(self.master, fg='black', bg='light grey' ,
                               text="Reset", font=("Courier", 14), command=self.button_3_pressed)
        self.button_3.grid(row=3, column=0, columnspan=5, sticky=W+E)
        

    def button_1_pressed(self):
        root1 = Tk()
        root1.title("Summary")
        self.label2= Text(root1, width=80, height=20, font=("Courier", 14), wrap=WORD)
        self.label2.insert('1.0', self.resultsArray[0])
        self.label2.grid(row=0, column=0, columnspan=5, sticky=W+E)

    def button_2_pressed(self):
        root2 = Tk()
        root2.title("Statistics")
        
        self.label3= Label(root2, width=80, text="Amount of character\'s extracted: ", font=("Courier", 14))
        self.label3.grid(row=0, column=0, columnspan=5, sticky=W+E)
        self.label3= Label(root2, width=80, text="Amount of character\'s summarised to: ", font=("Courier", 14))
        self.label3.grid(row=2, column=0, columnspan=5, sticky=W+E)
        self.label3= Label(root2, width=80, text=self.resultsArray[1], font=("Courier", 14))
        self.label3.grid(row=1, column=0, columnspan=5, sticky=W+E)
        self.label3= Label(root2, width=80, text=self.resultsArray[2], font=("Courier", 14))
        self.label3.grid(row=3, column=0, columnspan=5, sticky=W+E)

    def button_3_pressed(self):
        self.button_1.destroy()
        self.button_2.destroy()
        self.button_3.destroy()
        self.__init__(self.master)

    def voice_pressed(self):
        s1 = SpeechToText()
        speechText = s1.recognizeSpeech()
        self.entry.delete(0,END)
        self.entry.insert(0,speechText)
        self.find_pressed()
        
root = Tk()
my_gui = Qoi(root)
root.mainloop()
