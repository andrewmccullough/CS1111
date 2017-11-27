import pygame
import gamebox
import random

camera = gamebox.Camera(800, 600)
character = gamebox.from_color(200, 275, "yellow", 50, 50)
character.xspeed = 10
character.yspeed = 8

# from_color(CENTER x from left, CENTER y from top, color, width, height)

walls = [
    gamebox.from_color(600, 100, "white", 10, 200),
    gamebox.from_color(600, 500, "white", 10, 200)
]

counter = 0
alive = True
CoD = ""

def end_game ():
    gamebox.stop_loop()

def tick (keys):
    global counter
    global alive
    global CoD

    if alive == True:

        if pygame.K_SPACE in keys:
            character.y = character.y - 40

        character.x = character.x + character.xspeed
        character.y = character.y + character.yspeed

        camera.clear("black")
        camera.draw(character)

        counter = counter + 1

        if counter % 50 == 0:
            start_break = random.randint(100, 300)
            break_height = random.randint(200, 350)

            top_wall = gamebox.from_color(camera.x + 600, start_break / 2, "white", 10, start_break)
            walls.append(top_wall)

            bottom_wall_height = 600 - start_break - break_height
            bottom_wall = gamebox.from_color(camera.x + 600, bottom_wall_height / 2 + start_break + break_height, "white", 10, bottom_wall_height)
            walls.append(bottom_wall)

        for wall in walls:
            if character.touches(wall):
                CoD = "hit a wall"
                alive = False

            if (wall.x < camera.x - 400):
                walls.remove(wall)

            camera.draw(wall)

        if character.y <= 0:
            CoD = "hit the top"
            alive = False
        elif character.y + 50 >= 600:
            CoD = "hit the ground"
            alive = False

        camera.x = camera.x + character.xspeed
        camera.display()

    else:
        currently_at = camera.x

        message = "You died when you " + CoD + ". Your score was " + str(round(counter / 30)) + ". Press q to quit."

        score = gamebox.from_text(currently_at, 300, message, "Arial", 30, "green")
        camera.clear("black")
        camera.draw(score)
        camera.display()

        if pygame.K_q in keys:
            end_game()

ticks_per_second = 30
gamebox.timer_loop(ticks_per_second, tick)
