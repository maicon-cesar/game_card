import pygame
import sys
from random import shuffle

class Game():  
    ___suits = "CDHS"
    ___ranks = "234567890JQKA"
    ___deck  = []
    ___option = ""
    ___score = 0

    def __init__(self):
        self.shuffle_deck()

    def shuffle_deck(self):
        for suit in self.___suits:
            for rank in self.___ranks:
                self.___deck.append(rank + suit)
        shuffle(self.___deck)
        print(self.___deck)

    def get_card(self):
        if len(self.___deck) > 0:
            return self.___deck.pop(0)

    def get_color(self, card):
        suit = card[1]
        if suit == self.___suits[0] or suit == self.___suits[2]:
            return "black"
        return "red"

class Sprite(pygame.sprite.Sprite):
    def __init__(self, image_file, location, scale):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image_file)
        if scale != (0,0):
            self.image = pygame.transform.scale(self.image, scale)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location

class Button():
    ___text = None
    ___x = 0
    ___y = 0
    ___fill = 2
    ___selected = False


    def __init__(self, text, x, y):
        self.___x = x
        self.___y = y
        color = (255,255,255)
        smallfont = pygame.font.SysFont('Corbel', 25)
        self.___text = smallfont.render(text, True, color)

    def set_selected(self, status):
        self.___selected = status
        if self.___selected == True:
            self.___fill = 0
        else:
            self.___fill = 2

    def draw_button(self, screen, mouse):
        color_light = (170,170,170)
        color_dark = (100,100,100)

        if self.___x <= mouse[0] <= self.___x+140 and self.___y <= mouse[1] <= self.___y+40:
            pygame.draw.rect(screen, color_light, [self.___x, self.___y, 140, 40], self.___fill, 9)
        else: 
            pygame.draw.rect(screen, color_dark, [self.___x, self.___y, 140, 40], self.___fill, 9)

        screen.blit(self.___text, (self.___x+50, self.___y+9))

    def click(self, mouse):
        if self.___x <= mouse[0] <= self.___x+140 and self.___y <= mouse[1] <= self.___y+40:
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
DEFAULT_IMAGE_POSITION = (250,78)
card_image = Sprite('images/deck/back.png', DEFAULT_IMAGE_POSITION, DEFAULT_IMAGE_SIZE)

txt='Which color do you think this card is?'
pygame.font.init()
fonte=pygame.font.get_default_font()
fontesys=pygame.font.SysFont(fonte, 35)
txttela = fontesys.render(txt, 1, (255,255,255))

button_red = Button('Red', 0, 400)
button_black = Button('Black', 150, 400)
button_show = Button('Show', 400, 400)

game = Game()

while True:
    mouse = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            if button_show.click(mouse):
                card =  game.get_card()
                del(card_image)
                card_image = Sprite(f'images/deck/{card}.png', DEFAULT_IMAGE_POSITION, DEFAULT_IMAGE_SIZE)

            if button_red.click(mouse):
                button_black.set_selected(False)
                button_red.set_selected(True)

            if button_black.click(mouse):
                button_red.set_selected(False)
                button_black.set_selected(True)

    screen.fill(COLOR_BLACK)
    screen.blit(background.image, background.rect)
    screen.blit(card_image.image, card_image.rect)
    screen.blit(txttela,(5,10))

    button_red.draw_button(screen, mouse)
    button_black.draw_button(screen, mouse)
    button_show.draw_button(screen, mouse)

    pygame.display.flip()