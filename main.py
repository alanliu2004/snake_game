from turtle import Screen
from snake import Snake
import time
from food import Food
from score_board import ScoreBoard

game_is_on = True
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)
scoreboard = ScoreBoard()
snake = Snake()
food = Food()
screen.update()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

while game_is_on:
    screen.update()
    time.sleep(0.05)
    snake.move()

    #Detect collision with food
    if snake.head.distance(food) < 15:
        scoreboard.eat()
        food.refresh()
        snake.grow()

    #Detect collision with wall
    if snake.head.xcor() >= 300 or snake.head.xcor() <= -300 or snake.head.ycor() >= 300 or snake.head.ycor() <= -300:
        game_is_on = False
        scoreboard.game_over()

    #Detect collision with tail
    for seg in snake.all_segments[1:]:
        if snake.head.distance(seg) < 10:
            game_is_on = False
            scoreboard.game_over()


screen.exitonclick()