import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
screen = Screen()
screen.setup(600, 600)
screen.bgcolor("white")
screen.title("My snake game")
screen.tracer(0)

scoreboard = ScoreBoard()
food = Food()
snake = Snake()


screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")

turn_on = True

while turn_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    #Detect collision with food
    if snake.head.distance(food) <15:
        food.refresh()
        snake.extend()
        scoreboard.refresh()
    #Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.ycor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() < -280:
        scoreboard.game_over()
        turn_on=False

    #Detect collision with tail
    for segment in snake.segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            scoreboard.game_over()
            turn_on = False
screen.exitonclick()
