import pygame
from Player import Game
from controls import Controls
from Chrono import Minuteur
from Score import Score
from Replay.bot import Fantome
import math
pygame.init()
pygame.joystick.init()

WINDOW_SIZE = pygame.display.get_desktop_sizes()[0]
WINDOW_FLAGS = pygame.HWSURFACE | pygame.DOUBLEBUF | pygame.NOFRAME  # | pygame.RESIZABLE

window = pygame.display.set_mode(WINDOW_SIZE, WINDOW_FLAGS)

pygame.display.set_caption("TrailBlazer")
police = pygame.font.Font(None, 36)
policebigger = pygame.font.Font(None, 72)


background = pygame.image.load('img/new_race.png')
background_size = background.get_size()
background = pygame.transform.scale(
    background, (background_size[0], background_size[1]))
car_img = pygame.image.load('img/voiture.png').convert_alpha()
car_img_size = car_img.get_size()
car_img = pygame.transform.scale(
    car_img, (car_img_size[0]//4, car_img_size[1]//4))

car = Game(car_img, WINDOW_SIZE[0]//2, WINDOW_SIZE[1]//2)

car_sprites = pygame.sprite.Group()
car_sprites.add(car.player)


fantome = Fantome()

chrono = Minuteur()
score = Score()

controls = Controls(car)

running = True

chrono.run()

clock = pygame.time.Clock()

# Couleurs
CENTER = (75, 75)
RADIUS = 75
BLACK = (0, 0, 0)
RED = (200, 0, 0)


def draw_needle(angle):
    """This function draws the speedometer needle."""
    pygame.draw.circle(window, BLACK, CENTER, RADIUS, 3, True, True)
    pygame.draw.line(window, BLACK, (0, 75), (150, 75), 3)

    angle_rad = math.radians(((angle+1)*4-90))
    needle_length = RADIUS - 10
    needle_x = CENTER[0] + needle_length * math.cos(angle_rad - math.pi / 2)
    needle_y = CENTER[1] + needle_length * math.sin(angle_rad - math.pi / 2)

    pygame.draw.line(window, RED, CENTER, (needle_x, needle_y), 4)
    pygame.draw.circle(window, BLACK, CENTER, 5)

    pygame.display.flip()


def paused(pause):
    """This function pauses the game."""
    while pause:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    pause = False
                    return True
                elif event.key == pygame.K_ESCAPE:
                    pause = False
                    return False
        pygame.display.update()
        clock.tick(15)


car.player.positionBot = car.player.position

try:
    while running:
        if fantome.Play == False:
            keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                controls.pressed[event.key] = 1
                if event.key == pygame.K_p:
                    p = policebigger.render(f"Pause", True, (255, 0, 0))
                    window.blit(p, (WINDOW_SIZE[0]/2-100, WINDOW_SIZE[1]/2-50))
                    chrono.pauser()
                    running = paused(True)
                    chrono.pauser()
                if event.key == pygame.K_b:
                    fantome.Play = True
                    car.player.speed = 0
                    car.player.position = car.player.positionBot
                    car.player.heading = 0
                    car.player.turn(-80, True)
                    print(fantome.lst)
            elif event.type == pygame.JOYBUTTONDOWN:
                controls.pressed[event.button] = 1
            elif event.type == pygame.KEYUP:
                controls.pressed[event.key] = 0
            elif event.type == pygame.JOYBUTTONUP:
                controls.pressed[event.button] = 0
            elif event.type == pygame.JOYAXISMOTION:
                controls.pressed["gamepad_axis_" +
                                 str(event.axis)] = event.value
        controls.updateControls()
        if fantome.Play == False:
            keypresses = [k for k, v in controls.pressed.items() if v == True]

        speed = police.render(
            (f"Speed :{abs(round(car.player.speed, 1))}"), True, (255, 255, 255))

        chrono.affichage()
        minuteur = police.render(
            (f"{chrono}"), True, (255, 255, 255))

        score.calculscore(car.player.speed, chrono.timer)
        scr = police.render(
            (f"{score}"), True, (255, 255, 255))

        car_sprites.update()
        window.blit(
            background, (-car.player.position.x, - car.player.position.y))
        window.blit(speed, (25, 100))
        window.blit(minuteur, ((WINDOW_SIZE[0]//2)-75, 10))
        window.blit(scr, (25, 150))
        car_sprites.draw(window)

        if fantome.Play == False:
            fantome.add_movement(keypresses)
            car.player.positionBot = (16655, 9108)
        else:
            keypresses = fantome.playing()
        print(car.position)
        draw_needle(abs(car.player.speed))
        clock.tick_busy_loop(60)

except Exception as e:
    print(f"An error occured: {e}")
    pygame.quit()
    raise e
