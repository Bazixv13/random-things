import random
import os
import turtle
from turtle import Screen
import time

turtle.hideturtle()
t = turtle
screen = Screen()
wn = turtle.Screen()
screen.delay(100)
wn.bgcolor("black")
t.color("gainsboro")
wn.title("Losowanie".center(200))
t.speed(0)


def blad():
    t.up()
    t.goto(0, 0)
    t.down()
    wn.title("BŁĄD (wprowadzono nnieprawidłowe dane)".center(170))
    t.write("BŁĄD", move=False, font=("Comic Sans MS", 70, "bold", "italic"), align='center')
    t.up()
    t.goto(0, -40)
    t.down()
    time.sleep(0.5)
    t.write("Wprowadzono nieprawidłowe dane", move=False, font=("Comic Sans MS", 20, "bold", "italic"), align='center')
    time.sleep(2)
    t.up()
    t.goto(0, -278.5)
    t.down()
    t.write("Kliknij w dowolne miejsce by zamknąć.", move=False, font=("Comic Sans MS", 5, "italic"), align='center')
    wn.exitonclick()
    exit()


def zaduzaliczba():
    t.clearscreen()
    t.hideturtle()
    wn.bgcolor("black")
    t.color("gainsboro")
    t.up()
    t.goto(0, 0)
    t.down()
    wn.title("BŁĄD (wprowadzono zbyt duża ilosć liczb do pokazania w okienku)".center(130))
    t.write("BŁĄD", move=False, font=("Comic Sans MS", 70, "bold", "italic"), align='center')
    t.up()
    t.goto(0, -40)
    t.down()
    time.sleep(0.5)
    t.write("Jedna z liczb jest zbyt duża", move=False, font=("Comic Sans MS", 13, "bold", "italic"), align='center')
    time.sleep(2)
    t.up()
    t.goto(0, -278.5)
    t.down()
    t.write("Kliknij w dowolne miejsce by zamknąć.", move=False, font=("Comic Sans MS", 5, "italic"), align='center')
    wn.exitonclick()
    exit()


pozycjalosowanie4 = "560"
pozycjalosowanie3 = "268"
pozycjalosowanie = "0"
pozycjalosowanie2 = "0"
answer = 1
losowanie = ["None", "None"]
losowanie.pop()
losowanie.pop()
answer0 = 0
answerile = "None"
answerliczba1 = "None"
answerliczba2 = "None"
wn.title("Jeżeli chcesz wylosować liczbę napisz 1, Jeżeli chcesz zrobić niestandardowe losowanie napisz 2.".center(70))
answer0 = t.textinput("Wybierz rodzaj losowania", "Chcesz wylosować liczbę czy zrobić losowanie niestandardowe")

if answer0 == "wylosować" or answer0 == "wylosować liczbę" or answer0 == "1" or answer0 == "wylosowac liczbe" or answer0 == "wylosować liczbe" or answer0 == "liczbe" or answer0 == "liczbę":
    answerliczba1 = t.textinput("Wybrano losowanie liczby.", "Chcesz wylosować liczbę od :")
    answerliczba2 = t.textinput("Wybrano losowanie liczby.", "do :")
    wn.title(f"Losujesz liczbę od {answerliczba1} do {answerliczba2}.".center(170))

    if int(answerliczba2) == int(answerliczba1):
        blad()
    if int(answerliczba2) - int(answerliczba1) > 2:
        answerile = t.textinput("", "Ile liczb chcesz wylosować?")
        if int(answerile) > 320:
            zaduzaliczba()
        if int(answerliczba2) > 999999999 or int(answerliczba1) > 999999999:
            zaduzaliczba()
        if int(answerile) <= 0:
            blad()
        if int(answerile) <= int(answerliczba2) - int(answerliczba1):
            for i in range(0, int(answerile)):

                print(f"y  {pozycjalosowanie}    ,   x  {pozycjalosowanie2}")
                if int(answerile) > 10 and int(answerile) < 39:
                    t.up()
                    t.goto(0, int(pozycjalosowanie3) - int(pozycjalosowanie))
                    t.down()
                    t.write(random.randint(int(answerliczba1), int(answerliczba2)), move=False, align='center',
                            font=("Comic Sans MS", 10, "bold", "italic"))
                    pozycjalosowanie = int(pozycjalosowanie) + 14
                if int(answerile) >= 40:
                    t.up()
                    t.goto(-335 + int(pozycjalosowanie2), int(pozycjalosowanie3) - int(pozycjalosowanie))
                    t.down()
                    t.write(random.randint(int(answerliczba1), int(answerliczba2)), move=False, align='left',
                            font=("Comic Sans MS", 10, "bold", "italic"))
                    pozycjalosowanie = int(pozycjalosowanie) + 14
                    if pozycjalosowanie == 560:
                        pozycjalosowanie2 = int(pozycjalosowanie2) + 80
                        pozycjalosowanie3 = "268"
                        pozycjalosowanie = "0"

                if int(answerile) < 10:
                    t.up()
                    t.goto(0, 220 - int(pozycjalosowanie))
                    t.down()
                    t.write(random.randint(int(answerliczba1), int(answerliczba2)), move=False, align='center',
                            font=("Comic Sans MS", 30, "bold", "italic"))
                    pozycjalosowanie = int(pozycjalosowanie) + 40
elif answer0 == "2" or answer0 == "customowe losowanie" or answer0 == "niestandardowe losowanie" or answer0 == "customowe" or answer0 == "niestandardowe":

    answer = (turtle.textinput("Wybrano niestandardowe losowanie.",
                               f"Ile niestandardowych elementów chcesz dodać do losowania? (min. 2 elementy)"))
    if answer == "1" or answer == "0":
        blad()

    for i in range(0, int(answer)):
        losowanie.append(turtle.textinput("Losowanie", f"Podaj {len(losowanie) + 1} element"))
        answer = "0"

    wn.title(f"losuję z {losowanie}")
    time.sleep(0.5)
    wn.title(f"losuję dowolny z {len(losowanie)} niestandardowych elementów")

    answer2 = (turtle.textinput("Losowanie", f"Czy chcesz wylosować 1 niestandardowy element czy 2?"))
    wylosowany_parametr = losowanie[random.randint(0, len(losowanie) - 1)]
    os.system('CLS')
    if answer2 == 1:
        wn.title("Wylosowany niestandardowy element który został wylosowany to :".center(150))

    if answer2 == "1":
        t.up()
        t.goto(-340, 260)
        t.down()
        t.write("♡", move=False, font=("Comic Sans MS", 20, "bold"))
        t.up()
        t.goto(0, 0)
        t.down()
        t.write(wylosowany_parametr, move=False, font=("Comic Sans MS", 50, "bold", "italic"), align='center')
    elif answer2 == "2":
        t.up()
        t.goto(-340, 260)
        t.down()
        t.write("♡", move=False, font=("Comic Sans MS", 20, "bold"))
        t.up()
        t.goto(0, 75)
        t.down()
        t.write(wylosowany_parametr, move=False, font=("Comic Sans MS", 20, "bold", "italic"), align='center')
        t.up()
        t.goto(0, -25)
        t.down()
        t.write("+", move=False, font=("Comic Sans MS", 50, "bold", "italic"), align='center')
        t.up()
        t.goto(0, -75)
        t.down()
        t.write(losowanie[random.randint(0, len(losowanie) - 1)], move=False,
                font=("Comic Sans MS", 20, "bold", "italic"),
                align='center')
    else:
        blad()

else:
    blad()

time.sleep(6.9)
t.clearscreen()
t.hideturtle()
wn.bgcolor("black")
t.color("gainsboro")
wn.title("Te okienko zamknie się automatycznie za 6.9 sekundy".center(150))
time.sleep(6.9)
exit()
