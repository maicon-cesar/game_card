import pygame
import sys
import os
from random import shuffle

DEFAULT_WINDOW_SIZE = (727, 451)
DEFAULT_IMAGE_SIZE = (226, 280)
DEFAULT_IMAGE_POSITION = (250,78)
COLOR_BLACK = (0,0,0)

class Game():  
    ___suits = "CDHS"
    ___ranks = "234567890JQKA"
    ___deck  = []
    ___option = None
    ___score = 0

    def __init__(self):
        self.shuffle_deck()

    def shuffle_deck(self):
        for suit in self.___suits:
            for rank in self.___ranks:
                self.___deck.append(rank + suit)
        shuffle(self.___deck)

    def set_option(self, option):
        self.___option = option

    def get_card(self):
        if len(self.___deck) > 0:
            return self.___deck.pop(0)
        else:
            return None

    def get_count_deck(self):
        return len(self.___deck)

    def get_rate(self):
        if len(self.___deck) == 52:
            return 0
        return int(self.___score*100/(52-len(self.___deck)))

    def get_score(self):
        return self.___score
    
    def get_option(self):
        return self.___option

    def get_color(self, card):
        suit = card[1]
        if suit == self.___suits[0] or suit == self.___suits[3]:
            return "black"
        return "red"

    def scores(self):
        self.___score += 1

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

class Label():
    ___label = ""
    ___location = None
    ___fontsys = None

    def __init__(self, txt, location, font, size):
        self.___fontsys = pygame.font.SysFont(font, size)
        self.___location = location

    def draw_label(self, screen, txt):
        self.___label = self.___fontsys.render(txt, 1, (255,255,255))
        screen.blit(self.___label, self.___location)
    
os.system('clear')
game = Game()

pygame.init()
pygame.font.init()
screen = pygame.display.set_mode(DEFAULT_WINDOW_SIZE)
pygame.display.set_caption('Exercise Python Maicon')

background = Sprite('images/background.png', (0,50), (0,0))
card_image = Sprite('images/deck/back.png', DEFAULT_IMAGE_POSITION, DEFAULT_IMAGE_SIZE)
emoticon_sad   = Sprite('images/sad.png', (640, 5), (35, 35))
emoticon_happy = Sprite('images/happy.png', (640, 5), (45, 35))

button_red   = Button('Red', 10, 400)
button_black = Button('Black', 160, 400)
button_play  = Button('Play', 410, 400)

title_lbl = Label('Which color do you think this card is?', (10,10), pygame.font.get_default_font(), 35)
score_lbl = Label('Score: 0', (640, 65), pygame.font.get_default_font(), 20)
rate_lbl  = Label('Rate: 0%', (640, 85), pygame.font.get_default_font(), 20)
deck_lbl  = Label('Deck: 52', (640, 105), pygame.font.get_default_font(), 20)
result_lbl= Label('You got it!', (530, 10), pygame.font.get_default_font(), 30)

while True:
    mouse = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            if button_play.click(mouse):
                if game.get_option() == None:
                    continue
                card = game.get_card()
                if card == None:
                    continue
                if game.get_option() == game.get_color(card):
                    game.scores()
                del(card_image)
                card_image = Sprite(f'images/deck/{card}.png', DEFAULT_IMAGE_POSITION, DEFAULT_IMAGE_SIZE)

            if button_red.click(mouse):
                game.set_option("red")
                button_black.set_selected(False)
                button_red.set_selected(True)

            if button_black.click(mouse):
                game.set_option("black")
                button_red.set_selected(False)
                button_black.set_selected(True)

    screen.fill(COLOR_BLACK)
    screen.blit(background.image, background.rect)
    screen.blit(card_image.image, card_image.rect)
    screen.blit(emoticon_sad.image, emoticon_sad.rect)
    screen.blit(emoticon_happy.image, emoticon_happy.rect)

    title_lbl.draw_label(screen, 'Which color do you think this card is?')
    score_lbl.draw_label(screen, f'Score: {game.get_score()}')
    rate_lbl.draw_label(screen, f'Rate: {game.get_rate()}%')
    deck_lbl.draw_label(screen, f'Deck: {game.get_count_deck()}')
    result_lbl.draw_label(screen, 'You got it!')

    button_red.draw_button(screen, mouse)
    button_black.draw_button(screen, mouse)
    button_play.draw_button(screen, mouse)

    pygame.display.flip()