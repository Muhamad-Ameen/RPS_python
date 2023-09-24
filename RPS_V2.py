import random
from tkinter import *

choices = ["rock", "paper", "scissor"]


# create class to calculate points
class points:
    computer_point = 0
    player_point = 0


# Create Function of Rock Button
def Rock():
    computer_choice = random.choice(choices)
    if computer_choice == "rock":
        var.set("Draw")
        color = "yellow"
    elif computer_choice == "paper":
        var.set("Lose")
        color = "red"
        points.computer_point += 1
    elif computer_choice == "scissor":
        var.set("Win")
        color = "green"
        points.player_point += 1

    label.config(fg=f"{color}")


# Create Function of Paper Button
def Paper():
    computer_choice = random.choice(choices)
    if computer_choice == "rock":
        var.set("Win")
        color = "green"
        points.player_point += 1
    elif computer_choice == "paper":
        var.set("Draw")
        color = "yellow"
    elif computer_choice == "scissor":
        var.set("Lose")
        color = "red"
        points.computer_point += 1

    label.config(fg=f"{color}")


# Create Function of Scissor Button
def Scissor():
    computer_choice = random.choice(choices)
    if computer_choice == "rock":
        var.set("Lose")
        color = "red"
        points.computer_point += 1
    elif computer_choice == "paper":
        var.set("Win")
        color = "green"
        points.player_point += 1
    elif computer_choice == "scissor":
        var.set("Draw")
        color = "yellow"

    label.config(fg=f"{color}")


# Managing The Result Button
def Result():
    root.destroy()
    root2 = Tk()
    root2.geometry("200x200")
    if points.player_point > points.computer_point:
        message = "You win"
        color2 = "green"
    elif points.player_point < points.computer_point:
        message = "You lose"
        color2 = "red"
    else:
        message = "draw"
        color2 = "yellow"
    label_result = Label(root2,
                         text=f"Your Point :- {points.player_point}\nComputer Point :- {points.computer_point}",
                         font="50")
    label_result.pack()
    Label(root2, text=f"{message}",
          font=50,
          fg=color2,
          background="gray").pack(side="top")
    root2.mainloop()


# Creating a Window
root = Tk()
root.geometry("1080x720")
root.title("Rock Paper Scissor")

var = StringVar()

# Creating Buttons
Button(root,
       text=" Rock  ",
       activebackground="gray",
       bd=10,
       bg="white",
       justify="left",
       font=400,
       command=Rock).pack(ipadx=50,
                          ipady=25,
                          side="top")
Button(root,
       text=" Paper ",
       activebackground="gray",
       bd=10,
       bg="white",
       font=30,
       command=Paper).pack(ipadx=50,
                           ipady=25,
                           side="top")
Button(root,
       text="Scissor",
       activebackground="gray",
       bd=10,
       bg="white",
       font=30,
       command=Scissor).pack(ipadx=50,
                             ipady=25,
                             side="top")
Button(root,
       text="Result",
       activebackground="gray",
       font=20,
       command=Result).pack(side="bottom")
label = Label(textvariable=var,
              font=30,
              bd=10,
              bg="gray")
label.pack(ipadx="10",
           ipady="5",
           side="bottom")

root.mainloop()
