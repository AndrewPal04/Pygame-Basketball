import pygame

# print(pygame.font.get_fonts()) #Shows you which fonts you can use
class Text():
    def __init__(self, surface, text, size, color, x, y, font):
        self.font=font
        font_name=pygame.font.match_font(self.font)
        self.surface=surface
        self.text=text
        self.size=size
        self.font=pygame.font.Font(font_name,self.size)
        self.color=color
        self.x=x
        self.y=y
    def draw(self):
        text_surface = self.font.render(self.text,True,self.color)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (self.x,self.y)
        self.surface.blit(text_surface,text_rect)

class Player(pygame.sprite.Sprite):
    def __init__(self, image, scale, x, y):  
        pygame.sprite.Sprite.__init__(self)
        width = image.get_width()  
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        
    def update(self):
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_w]:
            self.rect.y -= 5
        if keystate[pygame.K_a]:
            self.rect.x -= 5
        if keystate[pygame.K_s]:
            self.rect.y += 5
        if keystate[pygame.K_d]:
            self.rect.x += 5
        
        if self.rect.left > 1000:
            self.rect.right = 0
        if self.rect.right < 0:
            self.rect.left = 1000
        if self.rect.bottom < 0:
            self.rect.top =600
        if self.rect.top > 600:
           self.rect.bottom =0
           
    def update2(self, target):
        if self.rect.x > target.rect.x:
            self.rect.x -= 5
        if self.rect.x < target.rect.x:
            self.rect.x += 5
        if self.rect.y < target.rect.y:
            self.rect.y +=5
        if self.rect.y > target.rect.y:
            self.rect.y -=5
        
        if self.rect.left > 1000:
            self.rect.right = 0
        if self.rect.right < 0:
            self.rect.left = 1000
        if self.rect.bottom < 0:
            self.rect.top =600
        if self.rect.top > 600:
            self.rect.bottom =0

class Button(pygame.sprite.Sprite):
    def __init__(self,image,scale,x,y):
        pygame.sprite.Sprite.__init__(self)
        width = image.get_width()
        height = image.get_height()
        self.image =pygame.transform.scale(image,(int(width*scale),int(height*scale)))
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)
        self.clicked = False #include new variable
    def draw(self, screen):
        screen.blit(self.image,(self.rect.x,self.rect.y))
        pressed = False
        pos =pygame.mouse.get_pos()

        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] ==1 and self.clicked == False:
                self.clicked = True
                pressed = True
        if pygame.mouse.get_pressed() == 0 :
            self.click = False
        return pressed


class Background(pygame.sprite.Sprite):
    def __init__(self, image, scale, x, y):  
        pygame.sprite.Sprite.__init__(self)
        width = image.get_width()  
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        
    def draw(self, screen):
            screen.blit(self.image,(self.rect.x,self.rect.y))