from turtle import *

speed('fastest')

# mudando de cabeca para baixo a turtle
rt(-90)

# angulo agudo entre
# a base e o galho y
angle = 30


# funcao para traçar o Y
def y(sz, level):
    if level>0:
        colormode(255)

        # dividindo o intrvalo para verde
        # em intervalos iguais para cada nivel
        # definindo cor de acordo
        # com o nivel atual
        pencolor(0, 255 // level, 0)

        # tracando a base
        fd(sz)

        rt(angle)

        # chamada recursiva para
        # o sub galho direito
        y(0.8*sz, level-1)

        pencolor(0, 255 // level, 0)

        lt(2*angle)

        # chamada recursiva para
        # o sub galho esquerdo
        y(0.8*sz, level-1)

        pencolor(0, 255 // level, 0)

        rt(angle)
        fd(-sz)


# tamanho da arvore 80 e nivel 7
y(80, 7)