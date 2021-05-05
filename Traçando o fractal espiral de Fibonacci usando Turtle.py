# Fibonacci
# f(n)= f(n-1)+ f(n-2)
#f(0)=0, f(1)=1
import turtle #Modulo tartaruga
import math

def fiboplot(n):
    a = 0
    b = 1
    quadrado_a = a
    quadrado_b = b

    # Mudando a cor das linhas para azul
    x.pencolor("blue")

    # Montando o primeiro quadrado
    x.forward(b * factor)
    x.left(90)
    x.forward(b * factor)
    x.left(90)
    x.forward(b * factor)
    x.left(90)
    x.forward(b * factor)

    # Continuando com a serie Fibonacci
    temp = quadrado_b
    quadrado_b = quadrado_b + quadrado_a
    quadrado_a = temp
    # Montando os quadrados restantes
    for i in range(1, n):
        x.backward(quadrado_a * factor)
        x.right(90)
        x.forward(quadrado_b * factor)
        x.left(90)
        x.forward(quadrado_b * factor)
        x.left(90)
        x.forward(quadrado_b * factor)

        # Continuando com a serie Fibonacci
        temp = quadrado_b
        quadrado_b = quadrado_b + quadrado_a
        quadrado_a = temp

    # Colocando a caneta no começo da Espiral
    x.penup()
    x.setposition(factor, 0)
    x.seth(0)
    x.pendown()

    # Mudando a cor da linha para Vermelho
    x.pencolor("red")

    # Espiral pelo Fibonacci
    x.left(90)
    for i in range(n):
        print(b)
        fdwd = math.pi * b * factor / 2
        fdwd /= 90
        for j in range(90):
            x.forward(fdwd)
            x.left(1)
        temp = a
        a = b
        b = temp + b


# 'Factor' significa o numero de mutiplicações
# Factor que expande ou encolhe a escala
# do grafico por um determinado valor
factor = 1

# Receber dados para ver quantidade que
# nosso algoritmo irá rodar
n = int(input('Coloque o numero de interações (deve ser > 1): '))

# Traçando o fractal espiral de Fibonacci
# e dizendo o numero Fibonacci correspondente
if n > 0:
    print("Serie Fibonacci para", n, "elementos :")
    x = turtle.Turtle()
    x.speed(100)
    fiboplot(n)
    turtle.done()
else:
    print("Numero de interações devem ser > 0")
