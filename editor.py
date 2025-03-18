import pygame
pygame.init()
from Fusion import fusion
# Configuration de la fenêtre
WINDOW_SIZE = pygame.display.get_desktop_sizes()[0]
screen = pygame.display.set_mode((WINDOW_SIZE[0], WINDOW_SIZE[1]))
pygame.display.set_caption("Pygame Rectangle")

# Couleurs
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
PINK = (255, 192, 203)
PURPLE=(128,0,128)

select_color = GREEN
palette_rotation = 0 
rectangles = []
palette = []

palette.append({"rect": pygame.Rect(10, 10, 50, 50), "color": RED})
palette.append({"rect": pygame.Rect(10, 70, 50, 50), "color": BLUE})
palette.append({"rect": pygame.Rect(10, 130, 50, 50), "color": GREEN})
palette.append({"rect": pygame.Rect(10, 190, 50, 50), "color": WHITE})
palette.append({"rect": pygame.Rect(10, 190, 50, 50), "color": WHITE})

route = pygame.image.load('img/img mini/route droite.png').convert_alpha()
route_minia = pygame.image.load('img/palette/route droite.png').convert_alpha()
tournant = pygame.image.load('img/img mini/tournant.png').convert_alpha()
tournant_minia = pygame.image.load('img/palette/tournant.png').convert_alpha()
fond = pygame.image.load('img/img mini/fond.png').convert_alpha()
fond_minia = pygame.image.load('img/palette/fond.png').convert_alpha()

rotatable_images = {BLUE, RED}
ni=17
nj=10
for i in range(ni):
    ti = 105 * i
    for j in range(nj):
        tj = 105 * j
        rect = pygame.Rect(100 + ti, 10 + tj, 100, 100)
        rectangles.append({"rect": rect, "color": GREEN, "rotation": 0})

def rotate_image(image, angle):
    """Retourne l'image avec une rotation donnée."""
    return pygame.transform.rotate(image, angle)

running = True
while running: 

    for rect_info in rectangles:
        pygame.draw.rect(screen, rect_info["color"], rect_info["rect"])
        
        rotated_image = None
        if rect_info["color"] == BLUE:
            rotated_image = rotate_image(route, rect_info["rotation"])
        elif rect_info["color"] == GREEN:
            rotated_image = fond
        elif rect_info["color"] == RED:
            rotated_image = rotate_image(tournant, rect_info["rotation"])
        
        if rotated_image:
            img_rect = rotated_image.get_rect(center=rect_info["rect"].center)
            screen.blit(rotated_image, img_rect)

    for rect_info in palette:
        pygame.draw.rect(screen, rect_info["color"], rect_info["rect"])
        if rect_info["color"] == BLUE:
            rotated_palette = rotate_image(route_minia, palette_rotation)
            screen.blit(rotated_palette, rect_info["rect"])
        elif rect_info["color"] == GREEN:
            screen.blit(fond_minia, rect_info["rect"])
        elif rect_info["color"] == RED:
            rotated_palette = rotate_image(tournant_minia, palette_rotation)
            screen.blit(rotated_palette, rect_info["rect"])
    rotate_button = pygame.Rect(25, 250, 25, 25)
    pygame.draw.rect(screen, PINK, rotate_button)
    pygame.draw.rect(screen, WHITE, pygame.Rect(10, WINDOW_SIZE[1]-50, 75, 25))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            for rect_info in palette:
                if rect_info["rect"].collidepoint(event.pos):
                    select_color = rect_info["color"]
                    if select_color in rotatable_images:
                        rect_info["rotation"] = palette_rotation  

            for rect_info in rectangles:
                if rect_info["rect"].collidepoint(event.pos):
                    rect_info["color"] = select_color
                    if select_color in rotatable_images:
                        rect_info["rotation"] = palette_rotation  

            if rotate_button.collidepoint(event.pos):
                palette_rotation = (palette_rotation + 90) % 360
            if pygame.Rect(10, WINDOW_SIZE[1]-50, 75, 25).collidepoint(event.pos):
                img=fusion(512*ni,512*nj)
                for rect_info in rectangles:
                    for j in range(nj):
                        img.putpixel()

    pygame.display.flip()

pygame.quit()
