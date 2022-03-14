from turtle import Turtle, Screen
import time

from snake import Snake
from food import Food
from scoreboard import Scoreboard

# board game
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("green")
screen.title("Snake Game")
#disable default Turtle animation
screen.tracer(0)


#snake animation
game_is_on = True

#creo a la serpiente
snake = Snake()

#creando comida
food = Food()

#crear tabllero
scoreboard = Scoreboard()


#METODO ESCUCH DE LAS TECLAS
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")



while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

    #detectar colision de comida
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.increase_score()
        snake.extend()

    #detector de colisiones de paredes
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()

    #DECTETOR DE COLISION SEGMENTO SEPIENTE
    for segment in snake.segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()
        


screen.exitonclick()