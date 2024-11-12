from pygame import *

init()

screen = display.set_mode(size=(960, 540), flags=RESIZABLE)

Font = font.SysFont("monospace", 15)

controllable_sprites = sprite.Group()

player_car = Car()
player_car.rect.x = 300
player_car.rect.y = 200

controllable_sprites.add(player_car)

running = True
clock = time.Clock()
screen.fill((128, 128, 128))

while running:
    for Event in event.get():
        if Event.type == QUIT:
            running = False
        elif Event.type == KEYDOWN:
            if Event.key == K_z:
                player_car.accelerate(2)
            elif Event.key == K_s:
                player_car.accelerate(-1)
    label = Font.render(str(player_car.current_velocity),
                        1, (255, 255, 0), (0, 0, 0))
    screen.blit(label, (100, 100))

    controllable_sprites.update()
    controllable_sprites.draw(screen)
    display.flip()
    clock.tick(60)

quit()
