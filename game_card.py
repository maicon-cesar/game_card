"""
First Python study exercise.
Maicon Cesar Canales de Oliveira
2023, january
"""

import pygame
import sys
import os
from random import shuffle

DEFAULT_WINDOW_SIZE    = (727, 451)
DEFAULT_IMAGE_SIZE     = (226, 280)
DEFAULT_IMAGE_POSITION = (250,78)

COLOR_BLACK            = (0,0,0)
COLOR_RED              = (255,0,0)
COLOR_WHITE            = (255,255,255)

STATE_PLAY             = 0
STATE_RESULT_WON       = 1
STATE_RESULT_MISS      = 2

class Game():  
    ___suits = "CDHS"
    ___ranks = "234567890JQKA"
    ___deck  = []
    ___option = None
    ___score = 0
    ___status = None    

    def __init__(self):
        self.___status = STATE_PLAY
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

    def set_status(self, status):
        self.___status = status

    def get_status(self):
        return self.___status


class Sprite(pygame.sprite.Sprite):
    def __init__(self, image_file, location, scale):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image_file)
        if scale != (0,0):
            self.image = pygame.transform.scale(self.image, scale)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location

class Button():
    ___font = None
    ___text = None
    ___text_color = []
    ___label = ""
    ___x = 0
    ___y = 0
    ___fill = 2
    ___selected = False

    def __init__(self, label, x, y):
        self.___x = x
        self.___y = y
        self.___font = pygame.font.SysFont('Corbel', 25)
        self.___text_color = COLOR_WHITE
        self.set_text(label)

    def set_selected(self, status):
        self.___selected = status
        if self.___selected == True:
            self.___fill = 0
        else:
            self.___fill = 2

    def get_selected(self):
        return self.___selected            

    def set_text(self, label):
        self.___label = label
        self.___text = self.___font.render(label, True, self.___text_color)

    def draw_button(self, screen, mouse, text_color):
        color_light = (170,170,170)
        color_dark = (100,100,100)

        if self.___x <= mouse[0] <= self.___x+140 and self.___y <= mouse[1] <= self.___y+40:
            pygame.draw.rect(screen, color_light, [self.___x, self.___y, 140, 40], self.___fill, 9)
        else: 
            pygame.draw.rect(screen, color_dark, [self.___x, self.___y, 140, 40], self.___fill, 9)

        self.___text = self.___font.render(self.___label, True, text_color)
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
        self.___label = self.___fontsys.render(txt, 1, COLOR_WHITE)
        screen.blit(self.___label, self.___location)

def main():
    os.system('clear')
    game = Game()

    pygame.init()
    pygame.font.init()
    screen = pygame.display.set_mode(DEFAULT_WINDOW_SIZE)
    pygame.display.set_caption('Exercise Python Maicon')

    background     = Sprite('images/background.png', (0,50), (0,0))
    card_image     = Sprite('images/deck/back.png', DEFAULT_IMAGE_POSITION, DEFAULT_IMAGE_SIZE)
    emoticon_sad   = Sprite('images/sad.png', (660, 5), (35, 35))
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
                    if game.get_status() != STATE_PLAY:
                        del(card_image)
                        card_image = Sprite(f'images/deck/back.png', DEFAULT_IMAGE_POSITION, DEFAULT_IMAGE_SIZE)
                        button_play.set_text('Play')
                        game.set_status(STATE_PLAY)
                        button_red.set_selected(False)
                        button_black.set_selected(False)
                        game.set_option(None) 
                        continue
                    else:
                        button_play.set_text('Next')
                    card = game.get_card()
                    if card == None:
                        continue
                    if game.get_option() == game.get_color(card):
                        game.scores()
                        game.set_status(STATE_RESULT_WON)
                    else:
                        game.set_status(STATE_RESULT_MISS)
                    del(card_image)
                    card_image = Sprite(f'images/deck/{card}.png', DEFAULT_IMAGE_POSITION, DEFAULT_IMAGE_SIZE)
                if game.get_status() == STATE_PLAY:    
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

        title_lbl.draw_label(screen, 'Which color do you think this card is?')
        score_lbl.draw_label(screen, f'Score: {game.get_score()}')
        rate_lbl.draw_label(screen, f'Rate: {game.get_rate()}%')
        deck_lbl.draw_label(screen, f'Deck: {game.get_count_deck()}')

        if game.get_status() == STATE_PLAY:
            pass
        elif game.get_status() == STATE_RESULT_WON:
            result_lbl.draw_label(screen, 'You got it!')
            screen.blit(emoticon_happy.image, emoticon_happy.rect)
        else:
            result_lbl.draw_label(screen, 'You missed!')
            screen.blit(emoticon_sad.image, emoticon_sad.rect)

        if button_red.get_selected():
            button_red.draw_button(screen, mouse, COLOR_RED)
        else:
            button_red.draw_button(screen, mouse, COLOR_WHITE)

        if button_black.get_selected():
            button_black.draw_button(screen, mouse, COLOR_BLACK)
        else:
            button_black.draw_button(screen, mouse, COLOR_WHITE)

        button_play.draw_button(screen, mouse, COLOR_WHITE)

        pygame.display.flip()

if __name__ == "__main__":
    main()