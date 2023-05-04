import random
import time
import pygame
pygame.init()

class Button(pygame.sprite.Sprite):
    def __init__(self, color_off, color_on, color_sound, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.color_off = color_off
        self.color_on = color_on
        self.color_sound = color_sound
        self.x = x
        self.y = y
        self.image = pygame.Surface((200, 200))
        self.image.fill(self.color_off)
        self.rect = self.image.get_rect()
        self.rect.topleft = (self.x , self.y)
        self.clicked = False
        self.scoreFont = pygame.font.Font(None, 30)


    '''
    Draws button sprite onto pygame window when called
    '''
    def draw(self, screen):
        self.image = pygame.draw.rect(screen, self.color_off, (self.x, self.y, 200, 200))


    '''
    Used to check if given button is clicked/selected by player
    '''
    def selected(self, mouse_pos):
        if(self.rect.collidepoint(mouse_pos)):
            return True
        else:
            return False

        

    '''
    Illuminates button selected and plays corresponding sound.
    Sets button color back to default color after being illuminated.
    '''
    def update(self, screen):
        self.image = pygame.Surface((200, 200))
        self.image.fill(self.color_on)
        screen.blit(self.image, (self.x, self.y))
        pygame.mixer.Sound.play(self.color_sound)
        pygame.display.update()
        self.image.fill(self.color_off)
        screen.blit(self.image, (self.rect.x, self.rect.y))
        pygame.time.wait(500)
        pygame.display.update()

    '''
    Renders the updated score
    '''
    def scoreShow(self, screen, score):
        self.image = pygame.Surface((200, 200))
        self.image.fill(self.color_off)
        displayedScore=self.scoreFont.render(str(f'Score: {score}'),True,(0,0,0))
        screen.blit(displayedScore,(195, 480))
        pygame.display.update()
