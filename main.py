import pygame
from game import Game
# from manette import *

WINDOW_SIZE = pygame.display.get_desktop_sizes()[0]
WINDOW_FLAGS = pygame.HWSURFACE | pygame.DOUBLEBUF | pygame.NOFRAME  # | pygame.RESIZABLE


pygame.init()
pygame.joystick.init()

joysticks = pygame.joystick.Joystick(0)
joysticks.init()
print(f"Joystick detected: {joysticks.get_name()}")

window = pygame.display.set_mode(WINDOW_SIZE, WINDOW_FLAGS)

pygame.display.set_caption("TrailBlazer")


background = pygame.image.load('img/racetrack.png')
background_size = background.get_size()
background = pygame.transform.scale(
    background, (background_size[0]*1.5, background_size[1]*1.5))
car_img = pygame.image.load('img/voiture.png').convert_alpha()
car_img_size = car_img.get_size()
car_img = pygame.transform.scale(
    car_img, (car_img_size[0]//4, car_img_size[1]//4))


car = Game(car_img, WINDOW_SIZE[0]//2, WINDOW_SIZE[1]//2)
car_sprites = pygame.sprite.Group()
car_sprites.add(car.player)
car.player.position = (16655, 9108)
car.player.turn(-80, True)

kevents = {
    "up": [pygame.K_UP, pygame.K_z],
    "down": [pygame.K_DOWN, pygame.K_s],
    "left": [pygame.K_LEFT, pygame.K_q],
    "right": [pygame.K_RIGHT, pygame.K_d],
    "handbrake": [pygame.K_SPACE],
    "gearup": [pygame.K_e],
    "geardown": [pygame.K_a],
    "leave": [pygame.K_ESCAPE]
}


clock = pygame.time.Clock()
done = False
last_command = None
joystick_axis_0 = 0
joystick_axis_4 = 0
joystick_axis_5 = 0
while not done:
running = True
while running:
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            car.pressed[event.key] = True
        elif event.type == pygame.KEYUP:
            car.pressed[event.key] = False
        if event.type == pygame.JOYAXISMOTION:
            if event.axis == 0:
                joystick_axis_0 = event.value
            if event.axis == 4 :
               joystick_axis_4 = event.value
            if event.axis == 5 :
               joystick_axis_5 = event.value

    if abs(joystick_axis_0) > 0.1: 
        car.player.turn(1.8 * joystick_axis_0)
    
    if abs(joystick_axis_4) > 0.1: 
        car.player.accelerate(-0.1 * (joystick_axis_4+1))

    if abs(joystick_axis_5) > 0.1: 
        car.player.accelerate(0.1 * (joystick_axis_5+1))

    if car.pressed.get(pygame.K_DOWN):
        car.player.accelerate(-0.1)
    else:
        if car.player.speed < 0:
            car.player.brake(-0.1)
    if car.pressed.get(pygame.K_UP):
        car.player.accelerate(0.1)
    else:
        if car.player.speed > 0:
            car.player.brake(0.1)
    if car.pressed.get(pygame.K_SPACE) or joysticks.get_button(2):
        if car.player.speed < 0:
            car.player.brake(-0.5)
        if car.player.speed > 0:
            car.player.brake(0.5)

    if car.pressed.get(pygame.K_LEFT):
        car.player.turn(-1.8)
    if car.pressed.get(pygame.K_RIGHT):
        car.player.turn(1.8)
    keypresses = [k for k, v in car.pressed.items() if v == True]

    for key in keypresses:
        if key in kevents["leave"]:
            running = False
            
        if key in kevents["down"]: # joysticks 4
            car.player.accelerate(-0.1)
        elif car.player.speed < 0:
            car.player.brake(-0.1)
            
        if key in kevents["up"]: # joysticks 5
            car.player.accelerate(0.1)
        elif car.player.speed > 0:
            car.player.brake(0.1)
            
		if key in kevents["handbrake"]: # joysticks 2
			if car.player.speed < 0:
            	car.player.brake(-0.5)
        	else:
            	car.player.brake(0.5)
			
        if key in kevents["left"]: # joysticks 13
            car.player.turn(-1.8)
        if key in kevents["right"]: # joysticks 14
            car.player.turn(1.8)


    car_sprites.update()
    window.blit(background, (-car.player.position.x, - car.player.position.y))
    car_sprites.draw(window)
    pygame.display.flip()
    
    clock.tick_busy_loop(60)
