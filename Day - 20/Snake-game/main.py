from turtle import Screen
from snake import Snake
from food import Food
import time


def reset_game():
    screen.clear()  # Clear the screen and start a new game
    main()


def main():
    global screen
    screen = Screen()
    screen.setup(width=600, height=600)
    screen.bgcolor("black")
    screen.title("My Snake Game")
    screen.tracer(0)

    snake = Snake()
    food = Food()

    screen.listen()
    screen.onkey(snake.up, "Up")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.left, "Left")
    screen.onkey(snake.right, "Right")

    game_is_on = True
    while game_is_on:
        screen.update()
        time.sleep(0.1)

        snake.move()

        # Detect collision with wall
        if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
            game_is_on = False

            # Display "Try Again" button
            screen.clearscreen()
            screen.bgcolor("black")
            screen.title("Game Over")

            try_again_button = screen.textinput(
                "Game Over", "Press Enter to Try Again")
            if try_again_button is not None:
                reset_game()

    screen.exitonclick()


if __name__ == "__main__":
    main()
