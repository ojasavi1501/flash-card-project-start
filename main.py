from tkinter import *
import pandas
import random
BACKGROUND_COLOR = "#B1DDC6"
pd = pandas.read_csv('flash-card-project-start/data/french_words.csv')
abc = pd.to_dict(orient="records")
print(abc)
xyz = {}
_fword = ""
_eword = ""


def English_words():
    canvas.itemconfig(canvas_image, image=photo_image3)
    canvas.itemconfig(flan_text, text='English')
    canvas.itemconfig(flan_words, text=xyz.get('English'))


def blah():

    for i in abc:
        for n in i.values():
            if n == _eword:
                abc.remove(i)

    new_words = pandas.DataFrame(abc)
    new_words.to_csv(
        'flash-card-project-start/data/learn_words.csv', index=False)

    French_words()


def French_words():
    global xyz, timer, _fword, _eword

    tk.after_cancel(timer)
    xyz = random.choice(abc)

    _fword = xyz.get('French')
    _eword = xyz.get('English')

    canvas.itemconfig(canvas_image, image=photo_image)
    canvas.itemconfig(flan_text, text='French')
    canvas.itemconfig(flan_words, text=_fword)

    print(xyz)

    new_words = pandas.DataFrame(abc)
    new_words.to_csv(
        'flash-card-project-start/data/learn_words.csv', index=False)

    timer = tk.after(3000, func=English_words)


tk = Tk()
tk.configure(padx=50, pady=50, bg=BACKGROUND_COLOR)

timer = tk.after(3000, func=English_words)

canvas = Canvas()
canvas.config(height=526, width=800, bg=BACKGROUND_COLOR, highlightthickness=0)

photo_image1 = PhotoImage(file='flash-card-project-start/images/right.png')
photo_image2 = PhotoImage(file='flash-card-project-start/images/wrong.png')
photo_image3 = PhotoImage(file='flash-card-project-start/images/card_back.png')
photo_image = PhotoImage(
    file='flash-card-project-start/images/card_front.png')


canvas_image = canvas.create_image(400, 263, image=photo_image)

flan_text = canvas.create_text(
    400, 150, text='French', font=('Ariel', 40, 'italic'))
flan_words = canvas.create_text(
    400, 260, text='', font=('Ariel', 60, 'bold'))

canvas.grid(column=0, row=0, columnspan=2)


yes_btn = Button(image=photo_image1, highlightthickness=0,
                 height=100, width=100, command=blah)
yes_btn.grid(column=0, row=1, pady=40)

no_btn = Button(image=photo_image2, highlightthickness=0,
                height=100, width=100, command=French_words)
no_btn.grid(column=1, row=1, pady=40)


French_words()
tk.mainloop()
