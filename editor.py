import pygame

pygame.init()


WINDOW_SIZE = pygame.display.get_desktop_sizes()[0]
screen = pygame.display.set_mode((WINDOW_SIZE[0], WINDOW_SIZE[1]))
pygame.display.set_caption("Pygame Rectangle")

GREEN = (0, 255, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
select_color = RED
rectangles = []
palette = []
palette.append({"rect": pygame.Rect(10, 10, 50, 50), "color": RED})
palette.append({"rect": pygame.Rect(10, 70, 50, 50), "color": BLUE})
palette.append({"rect": pygame.Rect(10, 130, 50, 50), "color": GREEN})
palette.append({"rect": pygame.Rect(10, 190, 50, 50), "color": WHITE})
for i in range(17):
    ti = 105 * i
    for j in range(10):
        tj = 105 * j
        rect = pygame.Rect(100+ti, 10+tj, 100, 100)
        rectangles.append({"rect": rect, "color": GREEN})


running = True
while running:

    for rect_info in rectangles:
        pygame.draw.rect(screen, rect_info["color"], rect_info["rect"])
    for rect_info in palette:
        pygame.draw.rect(screen, rect_info["color"], rect_info["rect"])
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            for rect_info in rectangles:
                if rect_info["rect"].collidepoint(event.pos):
                    rect_info["color"] = select_color
            for rect_info in palette:
                if rect_info["rect"].collidepoint(event.pos):
                    select_color = rect_info["color"]
    pygame.display.flip()

pygame.quit()
