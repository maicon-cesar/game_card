import sys, pygame

class Sprite(pygame.sprite.Sprite):
    def __init__(self, image_file, location, scale):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image_file)
        if scale != (0,0):
            self.image = pygame.transform.scale(self.image, scale)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location

class Button():
    text = None
    x = 0
    y = 0

    def __init__(self, text, x, y):
        self.x = x
        self.y = y
        color = (255,255,255)
        smallfont = pygame.font.SysFont('Corbel', 35) 
        self.text = smallfont.render(text, True, color) 


    def draw_button(self, screen, mouse):
        color_light = (170,170,170)
        color_dark = (100,100,100)

        if self.x <= mouse[0] <= self.x+140 and self.y <= mouse[1] <= self.y+40:
            pygame.draw.rect(screen, color_light, [self.x, self.y, 140, 40], 3, 3)
        else: 
            pygame.draw.rect(screen, color_dark, [self.x, self.y, 140, 40], 3, 3)

        screen.blit(self.text, (self.x+50, self.y+9))

    def click(self, mouse):
        if self.x <= mouse[0] <= self.x+140 and self.y <= mouse[1] <= self.y+40:
            return True
        else:
            return False
    
pygame.init()

DEFAULT_WINDOW_SIZE = 727, 441
screen = pygame.display.set_mode(DEFAULT_WINDOW_SIZE)
pygame.display.set_caption('Exercise Python Maicon')
COLOR_BLACK = 0,0,0

background = Sprite('images/background.png', [0,50], (0,0))

DEFAULT_IMAGE_SIZE = (226, 280)
DEFAULT_IMAGE_POSITION = (270,78)
card_image = Sprite('images/deck/back.png', DEFAULT_IMAGE_POSITION, DEFAULT_IMAGE_SIZE)

txt='Which color do you think this card is?'
pygame.font.init()
fonte=pygame.font.get_default_font()
fontesys=pygame.font.SysFont(fonte, 30)
txttela = fontesys.render(txt, 1, (255,255,255))

button_red = Button('RED', 0, 400)
button_black = Button('BLACK', 200, 400)
button_exit = Button('Exit', 400, 400)

while True:
    mouse = pygame.mouse.get_pos() 

    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            if button_exit.click(mouse):
                sys.exit()

    screen.fill(COLOR_BLACK)
    screen.blit(background.image, background.rect)
    screen.blit(card_image.image, card_image.rect)
    screen.blit(txttela,(5,10))

    button_red.draw_button(screen, mouse)
    button_black.draw_button(screen, mouse)
    button_exit.draw_button(screen, mouse)

    pygame.display.flip()