import pygame

pygame.init()


WINDOW_SIZE = pygame.display.get_desktop_sizes()[0]
screen = pygame.display.set_mode((WINDOW_SIZE[0]-300, WINDOW_SIZE[1]-200))
pygame.display.set_caption("Pygame Rectangle")

GREEN = (0, 255, 0)
WHITE = (255, 255, 255)


rectangles = []  

for i in range(17):
    ti = 105 * i
    for j in range(7):
        tj = 105 * j
        rect = pygame.Rect(10+ti, 10+tj, 100, 100)
        rectangles.append({"rect": rect, "color": GREEN})


running = True
while running:


    for rect_info in rectangles:
        pygame.draw.rect(screen, rect_info["color"], rect_info["rect"])
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            for rect_info in rectangles:
                if rect_info["rect"].collidepoint(event.pos):  
                    rect_info["color"] = (255, 0, 0) if rect_info["color"] == GREEN else GREEN

    pygame.display.flip()  

pygame.quit()