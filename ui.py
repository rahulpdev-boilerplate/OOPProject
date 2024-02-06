from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        check_image = PhotoImage(file="./images/true.png")
        cross_image = PhotoImage(file="./images/false.png")
        self.check_button = Button(image=check_image, command=self.select_true, highlightthickness=0)
        self.cross_button = Button(image=cross_image, command=self.select_false, highlightthickness=0)
        self.score_label = Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(
            150, 125, width=280, text="Some question", fill=THEME_COLOR, font=("Arial", 20, "italic")
        )

        self.score_label.grid(column=1, row=0)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)
        self.cross_button.grid(column=1, row=2)
        self.check_button.grid(column=0, row=2)

        self.display_new_question()

        self.window.mainloop()

    def select_true(self):
        self.give_feedback(self.quiz.check_answer("true"))

    def select_false(self):
        self.give_feedback(self.quiz.check_answer("false"))

    def display_new_score(self):
        self.score_label.configure(text=f"Score: {self.quiz.score}")

    def display_new_question(self):
        self.canvas.config(bg="white")
        self.display_new_score()
        if self.quiz.still_has_questions():
            self.canvas.itemconfig(self.question_text, text=self.quiz.next_question())
        else:
            self.canvas.itemconfig(self.question_text, text=f"You've reached the end of the quiz. Your score is {self.quiz.score} / {self.quiz.question_number}.")
            self.check_button.config(state="disabled")
            self.cross_button.config(state="disabled")

    def give_feedback(self, correct_answer):
        if correct_answer:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.display_new_question)
