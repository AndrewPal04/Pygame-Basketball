import pygame
from classes import Background, Button

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
    MISS_PATH = [(586, 350), (606, 307), (625, 269), (642, 238), (659, 212), (675, 192), 
    (690, 178), (704, 169), (717, 167), (729, 170), (740, 179), (751, 194), (760, 215), 
    (768, 242), (776, 274), (782, 313), (787, 357), (792, 407), (795, 462), (798, 524)
    ]
    path = []
    path_index =0
    shot_state ="idle"

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
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
        ball.draw(screen)
        player.draw(screen)
        meterCharging.draw(screen)
        

        pygame.display.update()
        clock.tick(60)

"""
Homework
Github: https://github.com/AndrewPal04/Pygame-Basketball
For homework, I want you to start building up the scoreboard.
You should start with the background for the score, and get
images for 1 through 9, so we can change the numbers depending
on how many times the user has made the shot!
Good Luck!
"""
