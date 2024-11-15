from pygame import *

# colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 127, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)
cyan = (0, 255, 255)
pink = (255, 0, 255)


# window
init()
screen = display.set_mode(size=(960, 540), flags=RESIZABLE)
display.set_caption("")
Font = font.SysFont("monospace", 15)
running = True
clock = time.Clock()
screen.fill(green)

cars = sprite.Group()
while running:
    for Event in event.get():
        if Event.type == QUIT:
            running = False
    display.flip()
    clock.tick(60)

quit()
