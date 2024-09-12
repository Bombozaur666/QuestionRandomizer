import random
import tkinter as tk
from variables import QUESTIONS_PATH, FONT, ENCODING, RESOLUTION


class Randomizer:
    def __init__(self):

        self.questions = self.readFile()

        self.root = tk.Tk()
        self.root.geometry(RESOLUTION)

        self.buttonFrame = tk.Frame(self.root)
        self.buttonFrame.columnconfigure(0, weight=1)
        self.buttonFrame.columnconfigure(1, weight=1)

        self.randomButton = tk.Button(self.buttonFrame, text='Wylosuj pytanie', font=(FONT, 18),
                                      command=self.randomQuestion)
        self.randomButton.grid(row=0, column=0, sticky=tk.W + tk.E)

        self.addButton = tk.Button(self.buttonFrame, text='Dodaj pytanie', font=(FONT, 18), command=self.addQuestion)
        self.addButton.grid(row=0, column=1, sticky=tk.W + tk.E)

        self.buttonFrame.pack(fill='x')

        self.questionsFrame = tk.Label(self.root, text='Question....', font=(FONT, 85), wraplength=3000)
        self.questionsFrame.pack(padx=50, pady=300)

        self.questionNewBox = tk.Text(self.root, height=5, font=(FONT, 16))
        self.questionNewBox.pack(side=tk.BOTTOM, pady=(0, 100))

        self.root.mainloop()

    def readFile(self) -> list[str]:
        with open(QUESTIONS_PATH, 'r', encoding=ENCODING) as file:
            return [line.rstrip('\n') for line in file]

    def addQuestion(self) -> None:
        question = self.questionNewBox.get("1.0", tk.END)
        with open(QUESTIONS_PATH, "a", encoding=ENCODING) as file:
            file.write(question)
        self.questions.append(question)

    def randomQuestion(self) -> None:
        try:
            index = random.randint(0, len(self.questions) - 1)
            self.questionsFrame.config(text=self.questions[index])
            self.questions.pop(index)
        except ValueError:
            self.questionsFrame.config(text="Add more questions to continue")


Randomizer()
