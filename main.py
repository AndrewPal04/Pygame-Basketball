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

    #Objects
    #backgroudn
    halfCourtImg =pygame.image.load("halfCourt.png") 
    halfCourt = Background(halfCourtImg,0.8,screen_width/2,screen_height/2)

    #Alternative
    # courtImg=pygame.image.load("BC.png")
    # court="BC"(courtImg,1, screen_width/2, screen_height/2)

    shot1Img=pygame.image.load("shot1.png")
    shot2Img=pygame.image.load("shot2.png")
    shot3Img=pygame.image.load("shot3.png")
    player=Background(shot1Img, 0.4, 550, 590)

    meter = 0
    charging = False

    BALLImg=pygame.image.load("basketball.png")
    ball=Background(BALLImg, 0.25, 550, 590)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        keystate = pygame.key.get_pressed()
        wasCharging = charging

        if keystate[pygame.K_SPACE]:
            charging = True
        if not keystate[pygame.K_SPACE]:
            charging = False

        if charging:
            meter += 3
            if meter > 100:
                meter = 100
        else:
            meter -= 5
            if meter < 0:
                meter = 0
                
        if meter < 33:
            player=Background(shot1Img, 0.4, 550, 590)
            ball=Background(BALLImg, 0.25, 550, 590)
        elif meter < 66:
            player=Background(shot2Img, 0.4, 550, 590)
            ball=Background(BALLImg, 0.25, 560, 445)
        else:
            player=Background(shot3Img, 0.4, 540, 530)
            ball=Background(BALLImg, 0.25, 586, 350)

       
        if not charging and wasCharging:
            release = meter
            if 67 <= release <= 85:
                print("make")
            else:
                print("miss")


        halfCourt.draw(screen)
        ball.draw(screen)
        player.draw(screen)
        

        pygame.display.update()
        clock.tick(60)

"""
Homework
Github: https://github.com/AndrewPal04/Pygame-Basketball
For homework, I want you to either find images, have AI
create images, or make your own images for the shot meter
(at least 3) so that we can add in the meter for when
the user is charging their shot. Try to add a new
Background object (like the player) where it can change
pictures to each different image when the user charges
the shot.
Good Luck!
"""
