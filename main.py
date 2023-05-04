import pygame
import random
import time
from button import Button 

pygame.init()
clock = pygame.time.Clock()

# Constants
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
GREEN_ON = (0, 255, 0)
GREEN_OFF = (0, 100, 0)
RED_ON = (255, 0, 0)
RED_OFF = (100, 0, 0)
BLUE_ON = (0, 0, 255)
BLUE_OFF = (0, 0, 100)
YELLOW_ON = (255, 255, 0)
YELLOW_OFF = (100, 100, 0)
WHITE = (255, 255, 255)

# Pass in respective sounds for each color
GREEN_SOUND = pygame.mixer.Sound("bell1.wav") # bell1
RED_SOUND = pygame.mixer.Sound("bell2.wav") # bell2
BLUE_SOUND = pygame.mixer.Sound("bell3.wav") # bell3
YELLOW_SOUND = pygame.mixer.Sound("bell4.wav") # bell4

# Button Sprite Objects
green = Button(GREEN_OFF, GREEN_ON, GREEN_SOUND, 10, 10)
red = Button(RED_OFF, RED_ON, RED_SOUND, 260, 10)
blue = Button(BLUE_OFF, BLUE_ON, RED_SOUND, 10, 260)
yellow = Button(YELLOW_OFF, YELLOW_ON,YELLOW_SOUND, 260, 260)
scoreButton = Button(WHITE, 0, 0, 135, 470)

# Variables
colors = ["green", "red", "blue", "yellow"]
cpu_sequence = []
choice = ""
score = 0

'''
Draws game board
'''
def draw_board():
    green.draw(SCREEN)
    red.draw(SCREEN)
    blue.draw(SCREEN)
    yellow.draw(SCREEN)
    scoreButton.draw(SCREEN)
    scoreButton.scoreShow(SCREEN, score)

'''
Chooses a random color and appends to cpu_sequence.
Illuminates randomly chosen color.
'''
def cpu_turn():
    choice = random.choice(colors)
    cpu_sequence.append(choice)    
    if choice == "green":
        green.update(SCREEN)
    elif choice == "red":
        red.update(SCREEN)
    elif choice == "blue":
        blue.update(SCREEN)
    else:
        yellow.update(SCREEN)

'''
Plays pattern sequence that is being tracked by cpu_sequence
'''
def repeat_cpu_sequence():
    if(len(cpu_sequence) != 0):
        for color in cpu_sequence:
            if color == "green":
                green.update(SCREEN)
            elif color == "red":
                red.update(SCREEN)
            elif color == "blue":
                blue.update(SCREEN)
            else:
                yellow.update(SCREEN)
            pygame.time.wait(500)


'''
After cpu sequence is repeated the player must attempt to copy the same
pattern sequence.
The player is given 3 seconds to select a color and checks if the selected
color matches the cpu pattern sequence.
If player is unable to select a color within 3 seconds then the game is
over and the pygame window closes.
'''
def player_turn():
    turn_time = time.time()
    players_sequence = []
    while time.time() <= turn_time + 3 and len(players_sequence) < len(cpu_sequence):
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                pos = pygame.mouse.get_pos()
                if green.selected(pos):
                    green.update(SCREEN)
                    players_sequence.append("green")
                    check_sequence(players_sequence)
                    turn_time = time.time()
                elif red.selected(pos):
                    red.update(SCREEN) 
                    players_sequence.append("red") 
                    check_sequence(players_sequence) 
                    turn_time = time.time() 
                elif blue.selected(pos): 
                    blue.update(SCREEN) 
                    players_sequence.append("blue")
                    check_sequence(players_sequence) 
                    turn_time = time.time() 
                else:
                    yellow.update(SCREEN)
                    players_sequence.append("yellow")
                    check_sequence(players_sequence)
                    turn_time = time.time() 
    if not time.time() <= turn_time + 3:
        game_over()

'''
Checks if player's move matches the cpu pattern sequence
'''

def check_sequence(players_sequence):
    if players_sequence != cpu_sequence[:len(players_sequence)]:
        game_over()

'''
Quits game and closes pygame window
'''

def game_over():
    pygame.quit()
    quit()


'''
Updates the user's score and draws the block again
'''
def update_score():
    scoreButton.draw(SCREEN)
    scoreButton.scoreShow(SCREEN, score)

# Game Loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.display.quit()
            pygame.quit()
            quit()
    pygame.display.update()
    draw_board()
    repeat_cpu_sequence() 
    cpu_turn()
    player_turn()
    score += 1
    update_score()
    pygame.time.wait(1000)
    clock.tick(60)