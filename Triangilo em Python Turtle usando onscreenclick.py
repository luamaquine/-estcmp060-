import turtle

# Metodo Screen () para obter a tela
wn = turtle.Screen()

# Criando tess object
tess = turtle.Turtle()


def triangle(x, y):
    # Usado para tirar a caneta
    tess.penup()

    # Usado para mover o cursor nas posicoes x
    # e y
    tess.goto(x, y)

    # Usado para desenhar na caneta
    tess.pendown()
    for i in range(3):
        # mover cursor 100 unidades
        # digite forward
        tess.forward(100)

        # virar cursor 120 graus para esquerda
        tess.left(120)

        # de novo ,mover cursor 100 unidades
        # digite forward
        tess.forward(100)


# funcao especial embutida para enviar a
# posicao atual do cursor para o triangulo
turtle.onscreenclick(triangle, 1)

turtle.listen()

# segure a tela
turtle.done()
