from turtle import Turtle, Screen
from snake import Snake
from scoreboard import Score
from food import Food
import time

screen = Screen()
screen.bgcolor("black")
screen.tracer(0)
screen.setup(600,600)
screen.title(titlestring="Snake game")


snake = Snake()
food = Food()
score = Score()


screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # detecting collision with food of snake
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.score_update()

    # detecting collision with wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        is_game_on = False
        score.game_over()

    # collision with own tail
    for segments in snake.segments[1:]:
        # if segments == snake.head:
        #     pass
        if snake.head.distance(segments) < 10:
            is_game_on = False
            score.game_over()

screen.exitonclick()

