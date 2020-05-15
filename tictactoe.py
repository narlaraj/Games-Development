from tkinter import *
from tkinter import messagebox

window = Tk()

window.title("Tic-tac-toe - Rajashekar Narla")
window.geometry("500x300")

xscr = 0
oscr = 0
tie = 0

lbl = Label(window, text=f"Overall Result : N/A   ", font=('Helvetica', '15'))
lbl.grid(row=0, column=0)

lbl1 = Label(window, text=" Last Won: N/A", font=('Helvetica', '10'))
lbl1.grid(row=1, column=4)

lbl2 = Label(window, text=f" Score : X={xscr}\n            O={oscr}\n          Tie={tie}", anchor='w',
             font=('Helvetica', '10'))
lbl2.grid(row=2, column=4)

lbl3 = Label(window, text="Player 1: X", font=('Helvetica', '10'))
lbl3.grid(row=1, column=0)
lbl4 = Label(window, text="Player 2: O", font=('Helvetica', '10'))
lbl4.grid(row=2, column=0)

turn = 1  # For first person turn.
is_disable = False


def clicked1():
    global turn
    if btn1["text"] == " ":  # For getting the text of a button
        if turn == 1:
            turn = 2
            btn1["text"] = "X"
        elif turn == 2:
            turn = 1
            btn1["text"] = "O"
        check()


def clicked2():
    global turn
    if btn2["text"] == " ":
        if turn == 1:
            turn = 2
            btn2["text"] = "X"
        elif turn == 2:
            turn = 1
            btn2["text"] = "O"
        check()


def clicked3():
    global turn
    if btn3["text"] == " ":
        if turn == 1:
            turn = 2
            btn3["text"] = "X"
        elif turn == 2:
            turn = 1
            btn3["text"] = "O"
        check()


def clicked4():
    global turn
    if btn4["text"] == " ":
        if turn == 1:
            turn = 2
            btn4["text"] = "X"
        elif turn == 2:
            turn = 1
            btn4["text"] = "O"
        check()


def clicked5():
    global turn
    if btn5["text"] == " ":
        if turn == 1:
            turn = 2
            btn5["text"] = "X"
        elif turn == 2:
            turn = 1
            btn5["text"] = "O"
        check()


def clicked6():
    global turn
    if btn6["text"] == " ":
        if turn == 1:
            turn = 2
            btn6["text"] = "X"
        elif turn == 2:
            turn = 1
            btn6["text"] = "O"
        check()


def clicked7():
    global turn
    if btn7["text"] == " ":
        if turn == 1:
            turn = 2
            btn7["text"] = "X"
        elif turn == 2:
            turn = 1
            btn7["text"] = "O"
        check()


def clicked8():
    global turn
    if btn8["text"] == " ":
        if turn == 1:
            turn = 2
            btn8["text"] = "X"
        elif turn == 2:
            turn = 1
            btn8["text"] = "O"
        check()


def clicked9():
    global turn
    if btn9["text"] == " ":
        if turn == 1:
            turn = 2
            btn9["text"] = "X"
        elif turn == 2:
            turn = 1
            btn9["text"] = "O"
        check()


flag = 1


def check():
    global flag
    global tie

    restart["state"] = DISABLED
    b1 = btn1["text"]
    b2 = btn2["text"]
    b3 = btn3["text"]
    b4 = btn4["text"]
    b5 = btn5["text"]
    b6 = btn6["text"]
    b7 = btn7["text"]
    b8 = btn8["text"]
    b9 = btn9["text"]
    flag = flag + 1
    if b1 == b2 and b1 == b3 and b1 == "O" or b1 == b2 and b1 == b3 and b1 == "X":
        win(btn1["text"])
    if b4 == b5 and b4 == b6 and b4 == "O" or b4 == b5 and b4 == b6 and b4 == "X":
        win(btn4["text"])
    if b7 == b8 and b7 == b9 and b7 == "O" or b7 == b8 and b7 == b9 and b7 == "X":
        win(btn7["text"])
    if b1 == b4 and b1 == b7 and b1 == "O" or b1 == b4 and b1 == b7 and b1 == "X":
        win(btn1["text"])
    if b2 == b5 and b2 == b8 and b2 == "O" or b2 == b5 and b2 == b8 and b2 == "X":
        win(btn2["text"])
    if b3 == b6 and b3 == b9 and b3 == "O" or b3 == b6 and b3 == b9 and b3 == "X":
        win(btn3["text"])
    if b1 == b5 and b1 == b9 and b1 == "O" or b1 == b5 and b1 == b9 and b1 == "X":
        win(btn1["text"])
    if b7 == b5 and b7 == b3 and b7 == "O" or b7 == b5 and b7 == b3 and b7 == "X":
        win(btn7["text"])
    if flag == 10:
        messagebox.showinfo("Tie", "Match Tied!!!  Try again :)")
        restart["state"] = NORMAL
        tie += 1
        lbl1["text"] = " Last Result: Tie"
        lbl2["text"] = f" Score : X={xscr}\n            O={oscr}\n          Tie={tie}"


def win(player):
    global xscr
    global oscr
    global tie

    if player == 'X':
        xscr += 1
    else:
        oscr += 1
    if xscr > oscr:
        lbl["text"] = f"Overall Result : X WON "
    elif oscr > xscr:
        lbl["text"] = f"Overall Result : O WON "
    else:
        lbl["text"] = f"Overall Result : TIE   "

    ans = "Game complete " + player + " wins "
    lbl1["text"] = " Last Result: " + player + " Won"
    lbl2["text"] = f" Score : X={xscr}\n            O={oscr}\n          Tie={tie}"
    restart["state"] = NORMAL
    messagebox.showinfo("Congratulations", ans)


#    window.destroy()  # is used to close the program

def restart_game():
    global turn
    global flag

    btn1["text"] = " "
    btn2["text"] = " "
    btn3["text"] = " "
    btn4["text"] = " "
    btn5["text"] = " "
    btn6["text"] = " "
    btn7["text"] = " "
    btn8["text"] = " "
    btn9["text"] = " "
    turn = 1
    flag = 1


def exit_game():
    window.destroy()


btn1 = Button(window, text=" ", bg="Blue", fg="White", width=3, height=1, font=('Helvetica', '20'), command=clicked1)
btn1.grid(column=1, row=1)
btn2 = Button(window, text=" ", bg="Blue", fg="White", width=3, height=1, font=('Helvetica', '20'), command=clicked2)
btn2.grid(column=2, row=1)
btn3 = Button(window, text=" ", bg="Blue", fg="White", width=3, height=1, font=('Helvetica', '20'), command=clicked3)
btn3.grid(column=3, row=1)
btn4 = Button(window, text=" ", bg="Blue", fg="White", width=3, height=1, font=('Helvetica', '20'), command=clicked4)
btn4.grid(column=1, row=2)
btn5 = Button(window, text=" ", bg="Blue", fg="White", width=3, height=1, font=('Helvetica', '20'), command=clicked5)
btn5.grid(column=2, row=2)
btn6 = Button(window, text=" ", bg="Blue", fg="White", width=3, height=1, font=('Helvetica', '20'), command=clicked6)
btn6.grid(column=3, row=2)
btn7 = Button(window, text=" ", bg="Blue", fg="White", width=3, height=1, font=('Helvetica', '20'), command=clicked7)
btn7.grid(column=1, row=3)
btn8 = Button(window, text=" ", bg="Blue", fg="White", width=3, height=1, font=('Helvetica', '20'), command=clicked8)
btn8.grid(column=2, row=3)
btn9 = Button(window, text=" ", bg="Blue", fg="White", width=3, height=1, font=('Helvetica', '20'), command=clicked9)
btn9.grid(column=3, row=3)

restart = Button(window, text="Restart", width=6, height=1, font=('Helvetica', '10'), command=restart_game)
restart.grid(column=1, row=5)

exit = Button(window, text="Exit", width=6, height=1, font=('Helvetica', '10'), command=exit_game)
exit.grid(column=2, row=5)

window.mainloop()
