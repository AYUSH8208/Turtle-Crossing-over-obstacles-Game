import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
screen = Screen()
screen.listen()
screen.setup(width=600, height=600)
screen.tracer(0)
car_manager = CarManager()
scoreboard=Scoreboard()


player=Player()
game_is_on = True
screen.onkey(fun=player.move,key="Up")
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_car()


 #  detect collision with cars
    for car in car_manager.all_cars:
        if player.distance(car) < 30:
            game_is_on = False
            scoreboard.game_over()

#     detect successful crossing
    if player.ycor() > 280:
        player.refresh()
        car_manager.level_up()
        scoreboard.update()












screen.exitonclick()