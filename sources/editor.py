import pygame
from Fusion import fusion

pygame.init()


WINDOW_SIZE = pygame.display.get_desktop_sizes()[0]
screen = pygame.display.set_mode((WINDOW_SIZE[0], WINDOW_SIZE[1]))
pygame.display.set_caption("Pygame Rectangle")


GREEN = (0, 255, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
PINK = (255, 192, 203)


select_color = GREEN
palette_rotation = 0
rectangles = []


palette = [
    {"rect": pygame.Rect(10, 10, 50, 50), "color": RED},
    {"rect": pygame.Rect(10, 70, 50, 50), "color": BLUE},
    {"rect": pygame.Rect(10, 130, 50, 50), "color": GREEN},
    {"rect": pygame.Rect(10, 190, 50, 50), "color": WHITE}
]


images = {
    "route": pygame.image.load("img/img mini/route droite.png").convert_alpha(),
    "route_minia": pygame.image.load("img/palette/route droite.png").convert_alpha(),
    "tournant": pygame.image.load("img/img mini/tournant.png").convert_alpha(),
    "tournant_minia": pygame.image.load("img/palette/tournant.png").convert_alpha(),
    "fond": pygame.image.load("img/img mini/fond.png").convert_alpha(),
    "fond_minia": pygame.image.load("img/palette/fond.png").convert_alpha(),
}


color_to_image = {
    BLUE: "route",
    RED: "tournant",
    GREEN: "fond",
}


rotatable_images = {BLUE, RED}


ni = WINDOW_SIZE[0] // 100 - 2
nj = WINDOW_SIZE[1] // 100
placed_tiles = [[None for _ in range(ni)] for _ in range(nj)]

for j in range(nj):
    for i in range(ni):
        rect = pygame.Rect(100 + 105 * i, 10 + 105 * j, 100, 100)
        rectangles.append({"rect": rect, "color": GREEN, "rotation": 0})
        placed_tiles[j][i] = {"image": "fond",
                              "rotation": 0, "position": rect.topleft}


def rotate_image(image, angle):
    """Rotate an image while keeping its center."""
    return pygame.transform.rotate(image, angle)


running = True
while running:
    screen.fill((0, 0, 0))

    for rect_info in rectangles:
        pygame.draw.rect(screen, rect_info["color"], rect_info["rect"])

        rotated_image = None
        if rect_info["color"] in color_to_image:
            img_name = color_to_image[rect_info["color"]]
            rotated_image = rotate_image(
                images[img_name], rect_info["rotation"])

        if rotated_image:
            img_rect = rotated_image.get_rect(center=rect_info["rect"].center)
            screen.blit(rotated_image, img_rect)

    for rect_info in palette:
        pygame.draw.rect(screen, rect_info["color"], rect_info["rect"])
        if rect_info["color"] in color_to_image:
            img_name = color_to_image[rect_info["color"]] + "_minia"
            rotated_palette = rotate_image(images[img_name], palette_rotation)
            screen.blit(rotated_palette, rect_info["rect"])

    rotate_button = pygame.Rect(25, 250, 25, 25)
    pygame.draw.rect(screen, PINK, rotate_button)

    save_button = pygame.Rect(10, WINDOW_SIZE[1] - 50, 75, 25)
    pygame.draw.rect(screen, WHITE, save_button)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            for rect_info in palette:
                if rect_info["rect"].collidepoint(event.pos):
                    select_color = rect_info["color"]
                    if select_color in rotatable_images:
                        rect_info["rotation"] = palette_rotation

            for idx, rect_info in enumerate(rectangles):
                if rect_info["rect"].collidepoint(event.pos):
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

            if save_button.collidepoint(event.pos):
                img = fusion(512 * ni, 512 * nj)

                for row in placed_tiles:
                    for tile in row:
                        if tile:
                            img.putpixel(tile["image"], tile["rotation"])

                img.saver()
                img.new_img.show()

    pygame.display.flip()

pygame.quit()
