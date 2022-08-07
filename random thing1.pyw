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

answer = 1
losowanie = ["None", "None"]
losowanie.pop()
losowanie.pop()
answer0 = 0
answerile = "None"
answerliczba1 = "None"
answerliczba2 = "None"
wn.title("Jeżeli chcesz wylosować liczbę napisz 1, Jeżeli dowolny parametr napisz 2.".center(70))
answer0 = t.textinput("Wybierz rodzaj losowania","Chcesz wylosować liczbę czy dowolny parametr?")
if answer0 == "liczbę" or answer0 == "liczbe" or answer0 == "1":
    answerliczba1 = t.textinput("Wybrano losowanie liczby.","Chcesz wylosować liczbę od :")
    answerliczba2 = t.textinput("Wybrano losowanie liczby.", "do :")
    wn.title(f"Losujesz liczbę od {answerliczba1} do {answerliczba2}.".center(170))
    if int(answerliczba2) - int(answerliczba1) > 2:
        answerile = t.textinput("","Ile liczb chcesz wylosować?")
        if int(answerile) <= int(answerliczba2) - int(answerliczba1):
            for i in range(0,int(answerile)):
                t.write(random.randint(int(answerliczba1),int(answerliczba2)), move=False ,align='center', font=("Comic Sans MS", 50, "bold", "italic"))
elif answer0 == "2" or answer0 == "dowolny parametr" or answer0 == "dowolny" or answer0 == "parametr":

    answer = (turtle.textinput("Wybrano niestandardowe losowanie.", f"Ile parametrów chcesz dodać do losowania? (min. 2 paramtry)"))
    if answer == "1" or answer == "0":
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
        t.write("Kliknij w dowolne miejsce by zamknąć lub okienko zamknie się automatycznie za 5 sekund", move=False,
                font=("Comic Sans MS", 5, "italic"), align='center')
        wn.exitonclick()
        time.sleep(5)
        exit()

    for i in range(0, int(answer)):
        losowanie.append(turtle.textinput("Losowanie", f"Podaj {len(losowanie) + 1} parametr"))
        answer = "0"

    print(f"losuję {losowanie}")
    print(f"losuję dowolny z {len(losowanie)} parametrów")


    answer2 = (turtle.textinput("Losowanie", f"Czy chcesz wylosować 1 parametr czy 2 parametry?"))
    wylosowany_parametr = losowanie[random.randint(0, len(losowanie) - 1)]
    os.system('CLS')
    wn.title("Wylosowany parametr to :")

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
        t.write(losowanie[random.randint(0, len(losowanie) - 1)], move=False, font=("Comic Sans MS", 20, "bold", "italic"),
                align='center')
    else:
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
        t.write("Kliknij w dowolne miejsce by zamknąć lub okienko zamknie się automatycznie za 5 sekund", move=False,
                font=("Comic Sans MS", 5, "italic"), align='center')
        wn.exitonclick()
        time.sleep(5)
        exit()

else:
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
    t.write("Kliknij w dowolne miejsce by zamknąć.", move=False,
            font=("Comic Sans MS", 5, "italic"), align='center')
    wn.exitonclick()
    exit()

time.sleep(5)
t.clearscreen()
t.hideturtle()
wn.bgcolor("black")
t.color("gainsboro")
wn.title("Te okienko zamknie się automatycznie za 6.9 sekundy".center(150))
time.sleep(6.9)
exit()
