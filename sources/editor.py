import pygame
from Fusion import fusion
import os
pygame.init()

def Start():
    WINDOW_SIZE = pygame.display.get_desktop_sizes()[0]
    screen = pygame.display.set_mode((WINDOW_SIZE[0], WINDOW_SIZE[1]))
    pygame.display.set_caption("Pygame Rectangle")

    GREEN = (0, 255, 0)
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)
    BLUE = (0, 0, 255)
    PINK = (255, 192, 203)
    VIOLET = (238,130,238)
    GRAY = (200, 200, 200)
    # BOX
    font = pygame.font.Font(None, 16)
    font2=pygame.font.Font(None, 24)
    font3=pygame.font.Font(None, 32)
    text_box = font2.render("Name :",1,(255,255,255))
    input_box = pygame.Rect(10, WINDOW_SIZE[1] - 85, 75, 25)
    color_active = pygame.Color('dodgerblue2')
    color_inactive = GRAY
    color = color_inactive
    active = False
    text = ""

    Save=font3.render("Save",1,(0,0,0))
    select_color = GREEN
    palette_rotation = 0
    rectangles = []


    palette = [
        {"rect": pygame.Rect(10, 10, 50, 50), "color": RED},
        {"rect": pygame.Rect(10, 70, 50, 50), "color": BLUE},
        {"rect": pygame.Rect(10, 130, 50, 50), "color": GREEN},
        {"rect": pygame.Rect(10, 190, 50, 50), "color": WHITE},
        {"rect": pygame.Rect(10, 250, 50, 50), "color": VIOLET},
    ]


    images = {
        "route": pygame.image.load("img/img mini/route droite.png").convert_alpha(),
        "route_minia": pygame.image.load("img/palette/route droite.png").convert_alpha(),
        "tournant": pygame.image.load("img/img mini/tournant.png").convert_alpha(),
        "tournant_minia": pygame.image.load("img/palette/tournant.png").convert_alpha(),
        "fond": pygame.image.load("img/img mini/fond.png").convert_alpha(),
        "fond_minia": pygame.image.load("img/palette/fond.png").convert_alpha(),
        "arrivee": pygame.image.load("img/img mini/Arrivee.png").convert_alpha(),
        "arrivee_minia" : pygame.image.load("img/palette/Arrivee.png").convert_alpha(),
        "depart" : pygame.image.load("img/img mini/Depart.png").convert_alpha(),
        "depart_minia" : pygame.image.load("img/palette/Depart.png").convert_alpha()
    }
    rotate_img=pygame.image.load("img/palette/rotate.png").convert_alpha()

    color_to_image = {
        BLUE: "route",
        RED: "tournant",
        GREEN: "fond",
        WHITE: "depart",
        VIOLET: "arrivee",
    }


    rotatable_images = {BLUE, RED,WHITE,VIOLET}


    ni = WINDOW_SIZE[0] // 100 - 2
    nj = WINDOW_SIZE[1] // 100
    placed_tiles = [[None for _ in range(ni)] for _ in range(nj)]

    for j in range(nj):
        for i in range(ni):
            rect = pygame.Rect(100 + 105 * i, 10 + 105 * j, 100, 100)
            rectangles.append({"rect": rect, "color": GREEN, "rotation": 0})
            placed_tiles[j][i] = {"image": "fond", "rotation": 0, "position": rect.topleft}


    def rotate_image(image, angle):
        return pygame.transform.rotate(image, angle)

    running = True
    placed_tiles[1][1] = {"image": "depart", "rotation": 0, "position": rectangles[1 * ni + 1]["rect"].topleft}
    placed_tiles[2][1] = {"image": "arrivee", "rotation": 0, "position": rectangles[2 * ni + 1]["rect"].topleft}
    rectangles[1 * ni + 1]["color"] = WHITE
    rectangles[2 * ni + 1]["color"] = VIOLET
    while running:
        screen.fill((0, 0, 0))  
        screen.blit(text_box, (10, WINDOW_SIZE[1]-100))
        
        for rect_info in rectangles:
            pygame.draw.rect(screen, rect_info["color"], rect_info["rect"])

            rotated_image = None
            if rect_info["color"] in color_to_image:
                img_name = color_to_image[rect_info["color"]]
                rotated_image = rotate_image(images[img_name], rect_info["rotation"])

            if rotated_image:
                img_rect = rotated_image.get_rect(center=rect_info["rect"].center)
                screen.blit(rotated_image, img_rect)

        
        for rect_info in palette:
            pygame.draw.rect(screen, rect_info["color"], rect_info["rect"])
            if rect_info["color"] in color_to_image:
                img_name = color_to_image[rect_info["color"]] + "_minia"
                rotated_palette = rotate_image(images[img_name], palette_rotation)
                screen.blit(rotated_palette, rect_info["rect"])

        
        rotate_button = pygame.Rect(25, 310, 25, 25)
        pygame.draw.rect(screen, PINK, rotate_button)

        
        save_button = pygame.Rect(10, WINDOW_SIZE[1] - 50, 75, 25)
        pygame.draw.rect(screen, WHITE, save_button)

        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if active:
                    if event.key == pygame.K_BACKSPACE:
                        text = text[:-1]
                    else:
                        text += event.unicode
            if event.type == pygame.MOUSEBUTTONDOWN:
                for rect_info in palette:
                
                    if rect_info["rect"].collidepoint(event.pos):
                        select_color = rect_info["color"]
                        if select_color in rotatable_images:
                            rect_info["rotation"] = palette_rotation  
                
                
                for idx, rect_info in enumerate(rectangles):
                    if (idx//ni, idx%ni) in [(1, 1), (2, 1)]:
                        continue
                    elif rect_info["rect"].collidepoint(event.pos):
                        rect_info["color"] = select_color
                        rect_info["rotation"] = palette_rotation if select_color in rotatable_images else 0

                        
                        row = idx // ni  
                        col = idx % ni  

                        
                        placed_tiles[row][col] = {
                            "image": color_to_image.get(select_color, "fond"),
                            "rotation": rect_info["rotation"],
                            "position": rect_info["rect"].topleft
                        }

                
                if rotate_button.collidepoint(event.pos):
                    palette_rotation = (palette_rotation + 90) % 360

                if input_box.collidepoint(event.pos):
                        active = True
                else:
                    active = False
                if active==True:
                    color = color_active 
                else : 
                    color =color_inactive
                
                
                if save_button.collidepoint(event.pos):
                    if not os.path.exists(f"Map/{text}"):
                        img = fusion(512 * ni, 512 * nj)
                        xi=0
                        yj=0
                        for row in placed_tiles:
                            xi+=1
                            for tile in row:
                                yj=(yj%20)+1
                                if tile:
                                    img.putpixel(tile["image"],(xi,yj), tile["rotation"])

                        img.saver(text)


        txt_surface = font.render(text, True, WHITE)
        screen.blit(txt_surface, (input_box.x + 5, input_box.y + 10))
        screen.blit(rotate_img,(25,310))
        pygame.draw.rect(screen, color, input_box, 2)
        screen.blit(Save, (15, WINDOW_SIZE[1]-50))
        pygame.display.flip()

    pygame.quit()
