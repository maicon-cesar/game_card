import sys, pygame
from pygame import font

class Sprite(pygame.sprite.Sprite):
    def __init__(self, image_file, location, scale):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image_file)
        if scale != (0,0):
            self.image = pygame.transform.scale(self.image, scale)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location

class Button():
    pass

pygame.init()

DEFAULT_WINDOW_SIZE = 727, 441
screen = pygame.display.set_mode(DEFAULT_WINDOW_SIZE)
pygame.display.set_caption('Exercise Python Maicon')
COLOR_BLACK = 0,0,0


# Inicia btn exit
color = (255,255,255) 
color_light = (170,170,170)
color_dark = (100,100,100) 
width = 0#screen.get_width() 
height = 0#screen.get_height() 
smallfont = pygame.font.SysFont('Corbel', 35) 
text = smallfont.render('Exit', True, color) 
  

background = Sprite('images/background.png', [0,50], (0,0))

DEFAULT_IMAGE_SIZE = (226, 280)
DEFAULT_IMAGE_POSITION = (270,78)
card_image = Sprite('images/deck/back.png', DEFAULT_IMAGE_POSITION, DEFAULT_IMAGE_SIZE)

txt='Which color do you think this card is?'
pygame.font.init()
fonte=pygame.font.get_default_font()
fontesys=pygame.font.SysFont(fonte, 30)
txttela = fontesys.render(txt, 1, (255,255,255))

while True:
    mouse = pygame.mouse.get_pos() 

    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        
        if event.type == pygame.MOUSEBUTTONDOWN: 
            if width/2 <= mouse[0] <= width/2+140 and height/2 <= mouse[1] <= height/2+40:
                sys.exit()

    screen.fill(COLOR_BLACK)
    screen.blit(background.image, background.rect)
    screen.blit(card_image.image, card_image.rect)
    screen.blit(txttela,(5,10))

    if width/2 <= mouse[0] <= width/2+140 and height/2 <= mouse[1] <= height/2+40:
        pygame.draw.rect(screen, color_light, [width/2, height/2, 140, 40], 3, 3)
    else: 
        pygame.draw.rect(screen, color_dark, [width/2, height/2, 140, 40], 3, 3)

    screen.blit(text, (width/2+50,height/2+9))

    pygame.display.flip()