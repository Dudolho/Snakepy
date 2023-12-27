from tkinter import *
import random
from Snake_Food import Snake, Food
from settings import *

##########FUNÇÕES############### 

#função para movimentar a cobra
def next_turn(snake, food):
    x, y = snake.coordinates[0]

    #verificando as direções e alterando os valores
    if direction == "up":
        y -= SPACE_SIZE
    elif direction == "down":
        y += SPACE_SIZE
    elif direction == "left":
        x -= SPACE_SIZE
    elif direction == "right":
        x += SPACE_SIZE
    
    snake.coordinates.insert(0, (x, y)) #inserindo as coordenadas novas

    square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR) #novo quadrado para a cobra

    snake.squares.insert(0, square)

    #adicionar um quadrado ao encontrar a coordenada da comida
    if x == food.coordinates[0] and y == food.coordinates[1]:
        #incrementar o score
        global score
        score += 1
        label.config(text = "score: {}".format(score))

        #deletar o objeto da comida e criando outro
        canvas.delete("food")
        food = Food(canvas)
    else:
    #deletando uma parte da cobra
        del snake.coordinates[-1] 
        canvas.delete(snake.squares[-1])
        del snake.squares[-1]
    
    #verificar se existe uma colisão
    if check_collision(snake):
        game_over() #fim de jogo

    else:
        window.after(SPEED, next_turn, snake, food) #adicionando uma nova parte a cobra

#função para capturar a mudança de direção
def change_direction(new_direction):
    
    global direction

    if new_direction == 'left':
        if direction != 'right':
            direction = new_direction

    elif new_direction == 'up':
        if direction != 'down':
            direction = new_direction

    elif new_direction == 'down':
        if direction != 'up':
            direction = new_direction


    elif new_direction == 'right':
        if direction != 'left':
            direction = new_direction

#função que verifica a colisão
def check_collision(snake):
    x, y = snake.coordinates[0] #recuperar as coordenadas da cobra

    #Retornar True caso a cobra passe da linha da tela
    if x < 0 or x >= GAME_WIDTH: #
        return True
    elif y < 0 or y >= GAME_HEIGHT:
        return True

    #Retornar True caso a cobra enconste nela mesma
    for body_part in snake.coordinates[1:]:
        if x == body_part[0] and y == body_part[1]:
            return True
    return False

def game_over():
    #deletar tudo da tela
    canvas.delete(ALL)

    #tela de game over
    canvas.create_text(canvas.winfo_width() / 2, canvas.winfo_height() / 2, font=('consolas', 70), text="Fim de Jogo", fill=SNAKE_COLOR, tag="gameover")

#INICIO DO CODIGO PRINCIPAL
window = Tk() #janela tkinter
window.title('Jogo da Cobrinha') #titulo da janela
window.resizable(False, False) #impede a janela de ser redimensionalizada

score = 0 #pontos iniciais
direction = 'down' #direção inicial

label = Label(window, text="score: {}".format(score), font=("Consolas", 40)) #Criando a Label para o score
label.pack() #adicionando na janela

canvas = Canvas(window, bg=BACKGROUND_COLOR, height=GAME_HEIGHT, width=GAME_WIDTH) #criando a tela
canvas.pack() #adicionando a tela

window.update() #atualizando a janela

##############CENTRALIZANDO A JANELA########################
window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x = int((screen_width / 2) - (window_width / 2))
y = int((screen_height / 2) - (window_height / 2) - 40)

window.geometry(f'{window_width}x{window_height}+{x}+{y}')
############################################################

##############captudando as teclas do teclado############
window.bind('<Left>', lambda event: change_direction('left'))
window.bind('<Right>', lambda event: change_direction('right'))
window.bind('<Up>', lambda event: change_direction('up'))
window.bind('<Down>', lambda event: change_direction('down'))

snake = Snake(canvas)
food = Food(canvas)

next_turn(snake, food)



window.mainloop() #loop da janela



