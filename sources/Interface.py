import pygame
from Player import Game
from Chrono import Minuteur
from Score import Score
from bot import Fantome
import math
from PIL import Image
import time
import os
from controls import Controls
pygame.init()
pygame.joystick.init()


def Start(Map):
    """This function runs the code of the editor.
    It is used to prevent the code to run on import"""

    class Ball(pygame.sprite.Sprite):
        def __init__(self, x, y):
            super().__init__()
            self.image = pygame.Surface((10, 10), pygame.SRCALPHA)
            pygame.draw.circle(self.image, (255, 0, 0), (5, 5), 5)
            self.rect = self.image.get_rect(center=(x, y))

        def update(self, x, y):
            self.rect.center = (x, y)

    def draw_needle(angle):
        """This function draws the speedometer needle."""
        pygame.draw.circle(window, BLACK, CENTER, RADIUS, 3, True, True)
        pygame.draw.line(window, BLACK, (0, 75), (150, 75), 3)

        angle_rad = math.radians(((angle+1)*4-90))
        needle_length = RADIUS - 10
        needle_x = CENTER[0] + needle_length * \
            math.cos(angle_rad - math.pi / 2)
        needle_y = CENTER[1] + needle_length * \
            math.sin(angle_rad - math.pi / 2)

        pygame.draw.line(window, RED, CENTER, (needle_x, needle_y), 4)
        pygame.draw.circle(window, BLACK, CENTER, 5)

        pygame.display.flip()

    def paused(pause, fantome, Map):
        """This function pauses the game."""
        text = policebigger.render("Save the replay", 1, (255, 255, 255))
        text2 = policebigger.render("Load a Replay", 1, (255, 255, 255))
        while pause:
            rect = pygame.Rect(
                WINDOW_SIZE[0]//2-225, WINDOW_SIZE[1]//2+100, 400, 50)
            pygame.draw.rect(window, (255, 0, 0), rect)
            rect2 = pygame.Rect(
                WINDOW_SIZE[0]//2-225, WINDOW_SIZE[1]//2+200, 400, 50)
            pygame.draw.rect(window, (255, 0, 0), rect2)
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_p:
                        pause = False
                        return True
                    elif event.key == pygame.K_ESCAPE:
                        pause = False
                        return False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if rect.collidepoint(event.pos):
                        newpath = f'Map/{Map}/replay'
                        if not os.path.exists(newpath):
                            os.makedirs(newpath)
                        x = int(sum(1 for entry in os.scandir(
                            f"Map/{Map}/replay") if entry.is_file()))
                        fantome.save(fantome.lst, f"Replay{Map}_{x+1}", Map)
                    if rect2.collidepoint(event.pos):
                        dossiers = [entry.name for entry in os.scandir(
                            f"Map/{Map}/replay") if entry.is_file()]
                        x = int(sum(1 for entry in os.scandir(
                            f"Map/{Map}/replay") if entry.is_file()))
                        window.fill((128, 128, 128))
                        Choice = True
                        lst = []
                        lstrect = []
                        for i in range(1, 8):
                            for j in range(1, 8):
                                rect = (200*i, 110*j)
                                temp = pygame.Rect(
                                    rect[0]-100, rect[1]-60, 180, 100)
                                lstrect.append(temp)
                                pygame.draw.rect(window, (255, 0, 0), temp)
                                lst.append(rect)
                        lsttextload = ["" for i in range(len(lst))]
                        for i in range(len(lst)):
                            if i < x:
                                lsttextload[i] = police.render(
                                    (f"{dossiers[i]}"), True, (255, 255, 255))
                                window.blit(
                                    lsttextload[i], (lst[i][0]-100, lst[i][1]-20))
                            else:
                                lsttextload[i] = police.render(
                                    (f"None"), True, (255, 255, 255))
                                window.blit(
                                    lsttextload[i], (lst[i][0]-100, lst[i][1]-20))
                        while Choice:
                            pygame.display.flip()
                            for event in pygame.event.get():
                                if event.type == pygame.MOUSEBUTTONDOWN:
                                    for i in range(len(lstrect)):
                                        if lstrect[i].collidepoint(event.pos):
                                            if i <= x:
                                                temp = fantome.lecture(
                                                    f"Map/{Map}/replay/{dossiers[i]}")
                                                Choice = False
                                                pause = False
                                                return temp
            window.blit(text, (WINDOW_SIZE[0]//2-225, WINDOW_SIZE[1]//2+100))
            window.blit(text2, (WINDOW_SIZE[0]//2-225, WINDOW_SIZE[1]//2+200))
            pygame.display.update()
            clock.tick(15)

        return (x, y)

    WINDOW_SIZE = pygame.display.get_desktop_sizes()[0]
    WINDOW_FLAGS = pygame.HWSURFACE | pygame.DOUBLEBUF | pygame.NOFRAME  # | pygame.RESIZABLE

    Gameover = False

    window = pygame.display.set_mode(WINDOW_SIZE, WINDOW_FLAGS)

    pygame.display.set_caption("TrailBlazer")
    police = pygame.font.Font(None, 36)
    policebigger = pygame.font.Font(None, 72)

    background = pygame.image.load(f"Map/{Map}/{Map}.png")
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

    car.player.turn(-80, True)

    fantome = Fantome()

    chrono = Minuteur()
    score = Score()

    chrono.run()

    clock = pygame.time.Clock()
    running = True

    # Couleurs
    CENTER = (75, 75)
    RADIUS = 75
    BLACK = (0, 0, 0)
    RED = (200, 0, 0)

    ball = Ball(car.player.position.x, car.player.position.y)

    ball_sprites = pygame.sprite.Group()
    ball_sprites.add(ball)

    controls = Controls(car)

    car.player.position = (300, 716)
    car.player.positionBot = car.player.position
    try:
        while running:
            if fantome.Play == False:
                keys = pygame.key.get_pressed()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    controls.pressed[event.key] = True
                    if event.key == pygame.K_p:
                        p = policebigger.render(f"Pause", True, (255, 0, 0))
                        window.blit(
                            p, (WINDOW_SIZE[0]/2-100, WINDOW_SIZE[1]/2-50))
                        running = paused(True, fantome, Map)
                        if running != True and running != False:
                            fantome.lst = running
                            running = True
                            fantome.Play = True
                            car.player.speed = 0
                            car.player.position = car.player.positionBot
                            car.player.heading = 0
                            car.player.turn(-80, True)
                elif event.type == pygame.KEYUP:
                    controls.pressed[event.key] = False

            if fantome.Play == False:
                keypresses = controls.updateControls()

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
            else:
                keypresses = fantome.playing()

            draw_needle(abs(car.player.speed))

            x, y = int(car.player.position.x +
                       (WINDOW_SIZE[0]//2)), int(car.player.position.y+(WINDOW_SIZE[1]//2))

            color = background.get_at((x, y))
            if color == (0, 162, 232, 255):
                chrono = Minuteur()
                chrono.run()
                chrono.timer = True
            elif color == (237, 28, 36, 255):
                chrono.timer = False
            elif color.g > 150 and color.r < 100 and color.b < 100:
                running = False
                Gameover = True
                fantome.lst = []
                fantome.i = 0
        # clock.tick_busy_loop(60)
        if Gameover == True:
            gameover = policebigger.render("Game Over", True, (255, 0, 0))
            window.blit(
                gameover, (WINDOW_SIZE[0]//2-150, WINDOW_SIZE[1]//2-50))
            pygame.display.update()
            time.sleep(2)
    except Exception as e:
        print(f"An error occured: {e}")
        pygame.quit()
        raise e


pygame.quit()
