from turtle import Screen
from turtle_graphic import TurtleGraphic
from car import Car
from scoreboard import Scoreboard
import time


screen = Screen()
screen.setup(600, 600)
screen.title("Turtle Crossing Game")
screen.tracer(0)

turtle_graphic = TurtleGraphic()
car = Car()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(turtle_graphic.up, "Up")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car.create_car()
    car.move()


    #Detect collision with car
    for every_car in car.all_cars:
        if every_car.distance(turtle_graphic) < 20:
            game_is_on = False
            scoreboard.game_over()


        #Detect collision with wall
        if turtle_graphic.ycor() > 280:
            turtle_graphic.go_to_start()
            car.update_speed()
            scoreboard.level()

screen.exitonclick()