import pygame
from classes import Background, Button

pygame.init()
screen_width = 1400
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()

#Creating objects
bgImg=pygame.image.load("background.png")
bg = Background(bgImg,1, screen_width/2, screen_height/2)

p1Img=pygame.image.load("singlebtn.png")
Sbtn =Button(p1Img, 0.4,700,200)

game=""

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    bg.draw(screen)
    
    if Sbtn.draw(screen):
        game = "single"
        break


    pygame.display.update()
    clock.tick(60)

if game == "single":
    screen_width = 1200
    screen_height = 800
    screen = pygame.display.set_mode((screen_width, screen_height))

    halfCourtImg =pygame.image.load("halfCourt.png") 
    halfCourt = Background(halfCourtImg,0.8,screen_width/2,screen_height/2)
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        halfCourt.draw(screen)

        pygame.display.update()
        clock.tick(60)

