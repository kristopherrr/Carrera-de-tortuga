from turtle import *
from random import randint

#configuraciones iniciales
bgcolor('green')
speed(10)
penup()
goto(-140,140)



#dibujo de la pista
for paso in range(15):
    write(paso, align='center')
    right(90)
    forward(10)
    pendown()
    for _ in range(15):
        forward(5)
        penup()
        forward(5)
        pendown()
    penup()
    backward(160)
    left(90)
    forward(20)


# Dibujar la línea de inicio
pendown()
goto(-140,130)
goto(-140,-30)
penup()
forward(5)

# Dibujar la línea de meta
goto(140,130)
pendown()
goto(140,-30)
penup()
forward(5)


# Crear las tortugas
tortugas = []
colores = ['red', 'blue', 'orange', 'yellow', 'purple']
posiciones = [110, 80, 50, 20, -10]

for i in range(5):
    tortuga = Turtle()
    tortuga.color(colores[i])
    tortuga.shape('turtle')

    tortuga.penup()
    tortuga.goto(-160, posiciones[i])
    tortuga.pendown()

    tortugas.append(tortuga)

# Hacer que todas las tortugas avancen al mismo tiempo
ganador = None
for girar in range(105):
    for tortuga in tortugas:
        tortuga.forward(randint(1,5))
        if tortuga.xcor() >= 140 and ganador is None:
            ganador = tortuga

# Hacer que la tortuga ganadora gire al final
if ganador is not None:
    ganador.right(360)

#mantener la pantalla
done()
