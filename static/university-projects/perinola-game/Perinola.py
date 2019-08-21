# coding=UTF-8

import random

# Mensaje de bienvenida

input("""

                   `+/.
                   ///`
                  .o+-
       `.........`++/`
     `/-.:+++++++:o+-:`
    +oo+:.:+oo++/+/+o+/.
  -sooooo/--/oooooooooo+-`
 `soooooooo+:-::::::::///:`
 /sssssssssss:.oooooooooooo.
-ysssssssssso`osssssssssss+
syyyyyyyssss::yyysyyyyyyys.
+oosyyys+sso.ssys+syysssy:
::ssoyyy+ys.+yosy+yyosyoo`
-///+yhh+y/.syosy+yyoyyo.
 .syo/+yys.syyyhhyyhhyy+
  -yhhs//--oooooooooooo
   .yddd+:ssssssssso/-
    .ydh-hddddhyo/-
     .s++dhyo/-.``
      ..+:-..`
       ...
        """)

# Reglas de juego

reglas = input('\nDesean leer las reglas? (S/N): ')

if reglas == 's' or reglas == 'S' or reglas == 'Si' or reglas == 'si':
    input("""
* Los jugadores inician con tres fichas cada uno, y deben realizar una apuesta inicial.

* Luego, el jugador 1 comenzara con su turno; en cuanto termine, seguirá el jugador 2.

* El jugador deberá tirar la 'Perinola Virtual' y se le asignaran o retiraran las fichas que se indique.

* En caso de que un jugador se quede sin fichas, perderá automáticamente...

* En caso de que el pozo se quede sin fichas, se rellenara automáticamente.

* Si los jugadores pasan su turno y ninguno perdió, ganara quien tenga mas fichas, sino, se declarara un empate.

(En cuanto terminen de leer las reglas, opriman 'Enter' para poder comenzar)
""")

# Creacion de variables

jugador1 = input("\nJugador 1, ingresa tu nombre: ")
jugador2 = input("\nJugador 2, ingresa tu nombre: ")
fichas_j1 = 2
fichas_j2 = 2
pozo = 2
opciones = ("Toma 1", "Toma 2", "Pon 1", "Pon 2", "Todos ponen", "Toma todo")

# Inicio Primer Turno

input("\n" + jugador1 + ", pulsa 'Enter' para hacer girar la perinola\n")

perinola = random.choice(opciones)
print(perinola, "\n")

# Giro de Perinola

if perinola == "Toma 1":
    fichas_j1 += 1
    pozo -= 1

elif perinola == "Toma 2":
    fichas_j1 += 2
    pozo -= 2

elif perinola == "Pon 1":
    fichas_j1 -= 1
    pozo += 1

elif perinola == "Pon 2":
    fichas_j1 -= 2
    pozo += 2

elif perinola == "Todos ponen":
    fichas_j1 -= 1
    fichas_j2 -= 1
    pozo += 2

elif perinola == "Toma todo":
    fichas_j1 += pozo
    pozo = 0

# Control de pozo.

if pozo == 0:
    print("El pozo se ha quedado sin fichas, deben realizar las apuestas nuevamente\n")
    fichas_j1 -= 1
    fichas_j2 -= 1
    pozo = 2

# Muestra de resultados de la tirada

print("Fichas de", jugador1 + ":", fichas_j1, "\nFichas de", jugador2 + ":", fichas_j2, "\nPozo actual:", pozo, "\n")

# Control de fichas J1

if fichas_j1 == 0:
    print(jugador1 + ", te has quedado sin fichas!\n", jugador2 + ", eres el ganador!")

else:
    print(jugador2 + ", es tu turno.\n")
    input(jugador2 + ", pulsa 'Enter' para hacer girar la perinola.\n\n")

    # Inicio del segundo turno

    perinola = random.choice(opciones)
    print(perinola, "\n")

    # Giro de Perinola

    if perinola == "Toma 1":
        fichas_j2 += 1
        pozo -= 1

    elif perinola == "Toma 2":
        if pozo == 1:
            fichas_j2 += 1
            pozo -= 1
        else:
            fichas_j2 += 2
            pozo -= 2

    elif perinola == "Pon 1":
        fichas_j2 -= 1
        pozo += 2

    elif perinola == "Pon 2":
        if fichas_j2 == 1:
            fichas_j2 -= 1
            pozo += 1
        else:
            fichas_j2 -= 2
            pozo += 2

    elif perinola == "Todos ponen":
        fichas_j2 -= 1
        fichas_j1 -= 1
        pozo += 2

    elif perinola == "Toma todo":
        fichas_j2 += pozo
        pozo = 0


# Muestra de resultados despues de la segunda tirada

    print("Fichas de", jugador1 + ":", fichas_j1, "\nFichas de", jugador2 + ":", fichas_j2, "\nPozo actual:", pozo,
          "\n")
    if fichas_j2 == 0:
        print(jugador2 + ", te has quedado sin fichas!\n" + jugador1 + ", eres el ganador!")

if fichas_j1 != 0 and fichas_j2 != 0:

    if fichas_j1 > fichas_j2:
        print(jugador1 + ", tienes mas fichas que", jugador2 + ", eres el ganador!")

    elif fichas_j1 < fichas_j2:
        print(jugador2 + ", tienes mas fichas que", jugador1 + ", eres el ganador!")

    elif fichas_j1 == fichas_j2:
        print("Felicitaciones, esto fue un empate!")

# Mensaje de cierre

input("\nGracias por jugar a la Perinola virtual!")
