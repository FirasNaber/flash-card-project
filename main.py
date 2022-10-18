from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526)
card_front_img = PhotoImage(file="images/card_front.png")
canvas.create_image(400, 263, image=card_front_img)
canvas.create_text(400, 150, text="Title", font=("Arial", 40, "italic"))
canvas.create_text(400, 263, text="word", font=("Arial", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

# Incorrect Button
incorrect_img = PhotoImage(file="images/wrong.png")
incorrect_button = Button(image=incorrect_img, highlightthickness=0)
incorrect_button.grid(column=0, row=1)

# Correct Button
correct_img = PhotoImage(file="images/right.png")
correct_button = Button(image=correct_img, highlightthickness=0)
correct_button.grid(column=1, row=1)

window.mainloop()
