from tkinter import *
from random import choice
import pandas as pd
from os.path import exists

BACKGROUND_COLOR = "#B1DDC6"

if exists("data/words_to_learn.csv"):
    df = pd.read_csv("data/words_to_learn.csv")
else:
    df = pd.read_csv("data/arabic_words.csv")
words_list = df.to_dict(orient="records")
random_dict = choice(words_list)


def correct_click():
    global random_dict
    # Remove the current word dictionary from the list
    words_list.pop(words_list.index(random_dict))
    # Show new card
    random_dict = choice(words_list)
    canvas.itemconfig(canvas_img, image=card_front_img)
    canvas.itemconfig(displayed_text, text="Arabic", fill="black")
    canvas.itemconfig(displayed_word, text=random_dict["Arabic"], fill="black")
    root.after(3000, flip_card)
    updated_df = pd.DataFrame(words_list)
    updated_df.to_csv("data/words_to_learn.csv", index=False)

def wrong_click():
    global random_dict
    # Show new card
    random_dict = choice(words_list)
    canvas.itemconfig(canvas_img, image=card_front_img)
    canvas.itemconfig(displayed_text, text="Arabic", fill="black")
    canvas.itemconfig(displayed_word, text=random_dict["Arabic"], fill="black")
    root.after(3000, flip_card)


def flip_card():
    canvas.itemconfig(canvas_img, image=card_back_img)
    canvas.itemconfig(displayed_text, text="English", fill="white")
    canvas.itemconfig(displayed_word, text=random_dict["English"], fill="white")


root = Tk()
root.title("Flashy")
root.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
canvas = Canvas(width=800, height=526)

canvas_img = canvas.create_image(400, 263, image=card_front_img)
displayed_text = canvas.create_text(400, 150, text="Arabic", font=("Arial", 40, "italic"))
displayed_word = canvas.create_text(400, 263, text=random_dict["Arabic"], font=("Arial", 60, "bold"))

canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

# Incorrect Button
incorrect_img = PhotoImage(file="images/wrong.png")
incorrect_button = Button(image=incorrect_img, highlightthickness=0, border=0, command=wrong_click)
incorrect_button.grid(column=0, row=1)

# Correct Button
correct_img = PhotoImage(file="images/right.png")
correct_button = Button(image=correct_img, highlightthickness=0, border=0, command=correct_click)
correct_button.grid(column=1, row=1)

root.after(3000, flip_card)

root.mainloop()
