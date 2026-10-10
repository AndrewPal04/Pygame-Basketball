import pygame
from classes import Background, Button, Text
import time

#Function to move the ball through the list
def advance_ball(ball, path, index):
    if index < len(path):
        ball.rect.center = path[index]
        index += 1
    else:
        index = len(path)
    return index

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

    meter1Img=pygame.image.load("meter1.png")
    meter2Img=pygame.image.load("meter2.png")
    meter3Img=pygame.image.load("meter3.png")
    meter4Img=pygame.image.load("meter4.png")
    meter5Img=pygame.image.load("meter5.png")
    meterCharging = Background(meter1Img, 0.2, 420, 480)

    meter = 0
    charging = False

    BALLImg=pygame.image.load("basketball.png")
    ball=Background(BALLImg, 0.25, 550, 590)

    #Ball movement
    MAKE_PATH = [(586, 350), (585, 310), (584, 274), (583, 242), (582, 215), (582, 191), 
    (582, 171), (582, 156), (582, 144), (583, 137), (583, 134), (584, 135), (586, 140), 
    (587, 149), (589, 162), (590, 179), (592, 200), (595, 225), (597, 254), (600, 288), 
    (610, 341), (621, 394), (631, 448), (642, 501), (652, 554)
    ]
    MISS_PATH = [ (586, 350), (596, 328), (606, 307),(616, 288), (625, 269), (634, 253),
    (642, 238), (651, 225), (659, 212),(667, 202), (675, 192), (683, 184),(690, 178), (697, 173), 
    (704, 169),(711, 167), (717, 167), (723, 168),(729, 170), (735, 174), (740, 179),(746, 186), 
    (751, 194), (756, 204),(760, 215), (764, 228), (768, 242),(772, 258), (776, 274), (779, 293),
    (782, 313), (785, 334), (787, 357),(789, 382), (792, 407), (793, 434),(795, 462), (796, 491), (798, 524)
    ]
    
    path = []
    path_index =0
    shot_state ="idle"
    score1 = 0
    score2 = 0

    #score images
    scoreboardIMG = pygame.image.load("scoreboard.png")
    n0IMG = pygame.image.load("0.png")
    n1IMG = pygame.image.load("1.png")
    n2IMG = pygame.image.load("2.png")
    n3IMG = pygame.image.load("3.png")
    n4IMG = pygame.image.load("4.png")
    n5IMG = pygame.image.load("5.png")
    n6IMG = pygame.image.load("6.png")
    n7IMG = pygame.image.load("7.png")
    n8IMG = pygame.image.load("8.png")
    n9IMG = pygame.image.load("9.png")

    scores = [n0IMG, n1IMG, n2IMG, n3IMG, n4IMG, n5IMG, n6IMG, n7IMG, n8IMG, n9IMG]

    scoreboard = Background(scoreboardIMG,0.39,600,120)
    score1BG = Background(scores[score1], 0.6, 565, 135)
    score2BG =  Background(scores[score2], 0.6, 635, 135)

    #Timer
    timer = 60
    start = time.time()

    timeText = Text(screen, str(timer), 50, (8,0,0), 1000, 50, "ocraextended")

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        end = time.time()
        timePassed = end-start
        if timePassed >= 1:
            timer -= 1
            start = time.time()
            timeText = Text(screen, str(timer), 50, (8,0,0), 1000, 50, "agencyfb")

        keystate = pygame.key.get_pressed()
        wasCharging = charging

        #For checking coordinates: 
        if event.type == pygame.MOUSEBUTTONDOWN:
            print(pygame.mouse.get_pos())

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

        if meter < 10:
            meterCharging = Background(meter1Img, 0.2, 420, 480)

        elif meter < 33:
            player=Background(shot1Img, 0.4, 550, 590)
            ball=Background(BALLImg, 0.25, 550, 590)
            meterCharging = Background(meter2Img, 0.2, 420, 480)

        elif meter < 50:
            meterCharging = Background(meter3Img, 0.2, 420, 480)
            
        elif meter < 66:
            player=Background(shot2Img, 0.4, 550, 590)
            ball=Background(BALLImg, 0.25, 560, 445)
            meterCharging = Background(meter4Img, 0.2, 420, 480)

        elif meter < 70:
            meterCharging = Background(meter5Img, 0.2, 420, 480)
        else:
            player=Background(shot3Img, 0.4, 540, 530)
            ball=Background(BALLImg, 0.25, 586, 350)
            meterCharging = Background(meter4Img, 0.2, 420, 480)
            

       
        if not charging and wasCharging:
            release = meter
            if 67 <= release <= 85:
                print("make")
                path = MAKE_PATH
                if score1 != 9 or score2 != 9:
                    score2 += 1
                    if score2 > 9:
                        score2 = 0
                        score1 += 1
                    score1BG = Background(scores[score1], 0.6, 565, 135)
                    score2BG =  Background(scores[score2], 0.6, 635, 135)
            else:
                print("miss")
                path = MISS_PATH
            path_index =0
            shot_state = "flying"

        if shot_state == "flying":
            path_index =advance_ball(ball, path, path_index)
            if path_index >=len(path):
               shot_state ="idle"

            

        halfCourt.draw(screen)
        scoreboard.draw(screen)
        score1BG.draw(screen)
        score2BG.draw(screen)
        ball.draw(screen)
        player.draw(screen)
        meterCharging.draw(screen)
        timeText.draw()

        
        
        

        pygame.display.update()
        clock.tick(60)

"""
Homework
Github: https://github.com/AndrewPal04/Pygame-Basketball
For homework, I want you to use the following slideshow
template to begin working on your final presentation slides!
Try to complete as many slides as you can, and now that you
created a program that has amazing visual images, make sure
to add some of the pictures into your slideshow as backgrounds,
extra pictures, or however you want.
https://docs.google.com/presentation/d/1SvjGVSDHrpJ3E__emNbEpPLVFicQvc0u9rTCRFXXVmg/edit?usp=sharing

"""

