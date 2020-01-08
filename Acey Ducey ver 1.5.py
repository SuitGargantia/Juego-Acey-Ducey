# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 21:18:16 2019

@author: Daniel A. Peimbert y Rolando E.R
"""

import random
import time

money = 100

printTable = {
                1: "Ace",
                2: "2",
                3: "3",
                4: "4",
                5: "5",
                6: "6",
                7: "7",
                8: "8",
                9: "9",
                10: "10",
                11: "Jack",
                12: "Queen",
                13: "King",
            }

time.sleep(1.5)

print ("\tAcey Ducey Juego de cartas.\t\n")
time.sleep(1.5)
print("Creado por: CREATIVE COMPUTING  MORRISTOWN, NEW JERSEY")
print("Autor original: Bill Palmby de Prairie View, Ilinois")
print("Re-escrito por: Daniel "" y Rolando E.R\n")
time.sleep(2)
print("El juego de Acey Ducey se juega de esta manera", 
"\nEl dealer(la computadora) pone dos cartas boca arriba",
"\ny despues sacara una tercera carta que tambien pondra boca arriba",
"\ntiene la opcion de apostar o no dependiendo de si siente o no",
"\nque la tercera carta que saldra tendra un valor entre las dos primeras")
time.sleep(4)
print("si la tercera carta esta entre el valor numerico de las dos primeras",
"\nse le devolbera su dinero, en caso de que no pierde el dinero que aposto",
"\ny si la tercera carta coincide con el valor numérico de una de las dos primera",
"\nganara el tripe de la apuesta!!!, si no quiere apostar solo tecle 0",
"\nUsted cuenta con $100 para postar.")
time.sleep(4)


def controljuego():
    global money
    
    card1 = random.randint(1,13)
    card2 = random.randint(1,13)
    card3 = random.randint(1,13)


    while card1 == card2:
        card2 = random.randint(1,13)

    print('\nTienes un total de {}'.format(money))
    time.sleep(1)


    bet = int(input('¿Cual es tu apuesta? '))

    # No hace falta volver a comparar si es igual.
    # if bet <= money or bet == money:
    if bet <= money:
        money = money - bet


        print('\nEstas son las primeras dos cartas\n')

        print(printTable[card1], " | ", printTable[card2], "\n") 
        time.sleep(1)

        print("Tirando última carta...\n")

    else:
        print('No tienes suficiente dinero')

        # Aquí ya hay que salirse porque no se puede seguir
        return


    time.sleep(2)
    print(printTable[card3], "\n")
    time.sleep(0.5)


    # Algo más de teatro para que sea más interesante...
    print("Calculando resultado...\n")
    time.sleep(1.5)

    # Ahora de hecho hay que calcular el resultado. Las condiciones son sencillas.
    # Primero descartemos el caso más sencillo, que c3 sea igual a c1 o c2.

    if card3 == card1 or card3 == card2:

        money = money + (bet * 2)

  
        bet = bet * 3


        if card3 == card1:
                bet = bet * 3
                print("Tu carta es la misma que la primera lanzada. Ganas el triple!\n")
        else:
            bet = bet * 3
            print("Tu carta es la misma que la segunda lanzada. Ganas el triple!\n")

    else:
        # Aquí se pone un cachito más complicado, porque tenemos que saber qué carta es más alta que cuál.
        # Pero nada más requiere un nivel más de if.
        if card1 > card2:
            # En este punto sabemos que c1 es mayor a c2, así que ya podemos hacer lo siguiente...
            if card3 < card1 and card3 > card2:
                money = money + bet
                # Está en medio.
                print("Tu carta está entre las dos primeras lanzadas. Te devolvemos tu dinero!\n")
            else: 
                # Ya por último solo queda decirle que perdió.
                print("Tu carta no está entre las primeras lanzadas. pierdes tu dinero!\n")


        elif card1 < card2:
            # Misma cosa, ya sabemos quién es menor y lo único que cambia es la condición del if de adentro.
            if card3 > card1 and card3 < card2:
                # Está en medio. Le devolvemos el valor de la apuesta.
                money = money + bet
                print("Tu carta está entre las dos primeras lanzadas. Te devolvemos tu dinero!\n")
    
            else: 
                # Ya por último solo queda decirle que perdió.
                print("Tu carta no está entre las primeras lanzadas. pierdes tu dinero!\n")
                
while True:

    # Aquí haremos el control de saldo, si tiene más que cero lo dejamos jugar...

    if money > 0:
        prompt = input("Cuenta con ${} en su cuenta. ¿Quiere jugar? [s/n]:".format(money))

        if prompt == "s" or prompt == "si" or prompt == "sí":
            controljuego()
        else:
            print("\nEntendido. Hasta pronto\n")
            break

    # Cuando el jugador se quda sin dinero el juego lo saca
    else:
        print("Estás quebrado. Fuera!")
        break   

