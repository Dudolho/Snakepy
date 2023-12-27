from tkinter import *
import random
from settings import *




class Snake(): #Cobra
    def __init__(self, canvas):
        self.body_size = BODY_PARTS # tamanho do corpo
        self.coordinates = [] #coordenadas iniciais
        self.squares = [] #lista de partes do corpo da cobra

        for i in range(0, BODY_PARTS): #setando as coordenadas
            self.coordinates.append([0, 0])
        
        for x, y in self.coordinates: #adicionando os quadrados da cobra
            square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR, tag="snake")
            self.squares.append(square)


class Food(): #Comida
    def __init__(self, canvas):
        #Gerando as posições que vão aparecer as comidas
        #pegamos a largura do jogo e dividimos pelo tamanho da comida para conseguir as coordenadas possiveis, depois multiplicamos o valor escolhido aleatoriamente pela largura dos objetos 
        x = random.randint(0, int((GAME_WIDTH / SPACE_SIZE)) - 1) * SPACE_SIZE 
        y = random.randint(0, int((GAME_HEIGHT / SPACE_SIZE)) - 1) * SPACE_SIZE

        self.coordinates = [x, y] #coordenadas geradas guardadas em uma lista

        #adicionando na tela
        canvas.create_oval(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=FOOD_COLOR, tag="food")