import pygame
from pygame.locals import *
import Interface
import editor
import os

if __name__ == "__main__":
    pygame.init()
    WINDOW_SIZE = pygame.display.get_desktop_sizes()[0]
    fenetre = pygame.display.set_mode((WINDOW_SIZE[0], WINDOW_SIZE[1]))
    
    
    fond = pygame.image.load("img/fond_menu.png")
    
    WHITE = (128, 128, 128)
    
    
    font=pygame.font.Font(None, 72)
    font2=pygame.font.Font(None, 48)
    text = font.render("TrailBlazer",1,(255,255,255))
    Play = font.render("Play",1,(255,255,255))
    Create = font.render("Create",1,(255,255,255))
    Quit = font.render("Quit",1,(255,255,255))
     
    continuer = 1
    
    while continuer:
     
        for event in pygame.event.get():
            if event.type == QUIT:
                continuer = 0
        fenetre.blit(fond,(0,0))
        fenetre.blit(text, (WINDOW_SIZE[0]//2-150, 150))
        rect = pygame.Rect(WINDOW_SIZE[0]//2-100, WINDOW_SIZE[1]//2, 155, 50)
        pygame.draw.rect(fenetre, (255,0,0), rect)
        rect2 = pygame.Rect(WINDOW_SIZE[0]//2-100, WINDOW_SIZE[1]//2+60, 155, 50)
        pygame.draw.rect(fenetre, (255,0,0), rect2)
        rect3 = pygame.Rect(WINDOW_SIZE[0]//2-100, WINDOW_SIZE[1]//2+120, 155, 50)
        pygame.draw.rect(fenetre, (255,0,0), rect3)
        fenetre.blit(Play, (WINDOW_SIZE[0]//2-75, WINDOW_SIZE[1]//2))
        fenetre.blit(Create, (WINDOW_SIZE[0]//2-100, WINDOW_SIZE[1]//2+60))
        fenetre.blit(Quit, (WINDOW_SIZE[0]//2-75, WINDOW_SIZE[1]//2+120))
        pygame.display.flip()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if rect.collidepoint(event.pos):
                dossiers = [entry.name for entry in os.scandir(f"Map") if entry.is_dir()]
                x=int(sum(1 for entry in os.scandir(f"Map") if entry.is_dir()))
                fenetre.fill(WHITE)
                Choice=True
                lst=[]
                lstrect=[]
                for i in range(1,8):
                        for j in range(1,8):
                            rect=(200*i,110*j)
                            temp=pygame.Rect(rect[0]-100,rect[1]-60,180,100)
                            lstrect.append(temp)
                            pygame.draw.rect(fenetre, (255,0,0), temp)
                            lst.append(rect)
                lsttextload=["" for i in range(len(lst))]
                for i in range(len(lst)):
                        if i<x:
                            lsttextload[i] = font2.render((f"{dossiers[i]}"), True, (255, 255, 255))
                            fenetre.blit(lsttextload[i],(lst[i][0]-100,lst[i][1]-20))
                        else :
                            lsttextload[i] = font.render((f"None"), True, (255, 255, 255))
                            fenetre.blit(lsttextload[i],(lst[i][0]-100,lst[i][1]-20))
                while Choice:
                    pygame.display.flip()
                    for event in pygame.event.get():
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            for i in range(len(lstrect)):
                                if lstrect[i].collidepoint(event.pos):
                                    if i<=x:  
                                        Interface.Start(f"{dossiers[i]}")
                                        Choice=False
                                        continuer=False
            if rect2.collidepoint(event.pos):
                editor.Start()
                continuer=False
            if rect3.collidepoint(event.pos):
                continuer=False
            
    pygame.quit()
