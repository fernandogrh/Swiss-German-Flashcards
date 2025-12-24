from tkinter import *
import pandas
import random

background_color = "#B1DDC6"
current_card = {}
to_learn = {}

try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/swiss_german_english_vocab.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")
total_cards = len(to_learn)

def next_card():
    global current_card, flip_timer
    if not to_learn:
        canvas.itemconfig(card_title, text="🎉 Done!", fill="black")
        canvas.itemconfig(card_word, text="You have learned all the words!", fill="black", font=("Arial", 40, "italic"))
        canvas.itemconfig(card_background, image=flashcard_front)
        return
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="Swiss German", fill="black")
    canvas.itemconfig(card_word, text=current_card["Swiss German"], fill="black")
    canvas.itemconfig(card_background, image=flashcard_front)
    flip_timer = window.after(3000, flip_card)

def flip_card():
    global current_card
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_background, image=flashcard_back)

def known_cards():
    if current_card in to_learn:
        to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)
    update_progress()
    next_card()

def  update_progress():
    learned =  total_cards - len(to_learn)
    progress_label.config(text=f"Progress: {learned} / {total_cards}")

window = Tk()
window.title("FR Flashcard Program")
window.geometry("860x700")
window.minsize(500, 500)
window.config(padx=50, pady=50, bg=background_color)

flip_timer = window.after(3000, flip_card)

canvas = Canvas(window, width=800, height=526)
flashcard_front = PhotoImage(file="images/card_front.png")
flashcard_back = PhotoImage(file="images/card_back.png")
card_background = canvas.create_image(400, 263, image=flashcard_front)
card_title = canvas.create_text(400, 150, text="", font=("Arial", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Arial", 60, "bold"))
canvas.config(bg=background_color, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

progress_label = Label(text=f"Progress: 0 / {total_cards}", font=("Arial", 14, "bold"), bg=background_color)
progress_label.grid(row=2, column=0, columnspan=2, pady=10)

x_button = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=x_button, highlightthickness=0, command=next_card)
wrong_button.grid(row=1, column=0)

checkmark_button = PhotoImage(file="images/right.png")
right_button = Button(image=checkmark_button, highlightthickness=0, command=known_cards)
right_button.grid(row=1, column=1)

next_card()
update_progress()
window.mainloop()
