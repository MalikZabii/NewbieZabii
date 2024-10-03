from turtle import Screen
from snake import Snake
from food import Food
import time
from scoreboard import Scoreboard


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
    scoreboard = Scoreboard()

    screen.listen()
    screen.onkey(snake.up, "Up")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.left, "Left")
    screen.onkey(snake.right, "Right")

    game_is_on = True
    recently_ate = False  # Flag to indicate if the snake recently ate

    while game_is_on:
        screen.update()
        time.sleep(0.1)

        snake.move()

        # Detect collision with wall
        if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
            game_is_on = False
            scoreboard.game_over()

        # Detect collision with food
        if snake.head.distance(food) < 15:
            food.refresh()  # Move the food to a new location
            snake.extend()  # Extend the snake by adding a new segment
            scoreboard.increase_score()  # Increase the score when food is eaten
            recently_ate = True  # Set flag to indicate snake just ate

        # Detect collision with tail
        # Skip collision check for one move after eating to avoid new segment triggering collision
        if not recently_ate:  # Only check tail collision if the snake hasn't recently eaten
            for segment in snake.segments[1:]:
                if snake.head.distance(segment) < 10:
                    game_is_on = False
                    scoreboard.game_over()
        else:
            recently_ate = False  # After one move, reset the flag

    # After game ends, allow restart
    try_again = screen.textinput(
        "Game Over", "Do you want to play again? (yes/no)")
    if try_again and try_again.lower() == "yes":
        reset_game()  # Restart the game
    else:
        screen.bye()  # Exit the game


if __name__ == "__main__":
    main()
