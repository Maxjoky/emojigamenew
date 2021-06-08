import pygame, sys, os, random, time

from pygame import *

# Game Initialisation
running = True

pygame.init()
pygame.display.set_caption("Emoji Rush")

# Images:
mad_emoji = pygame.image.load("mad_emoji.png")
bg_game = pygame.image.load("game_bg.jpg")
coin = pygame.image.load("Coin.png")

# Variables: 
clock = pygame.time.Clock()
emoji_x = 0
emoji_y = 0
coin_x = 0
coin_y = 0
vel = 3

# Colours:
BLACK = ((0, 0, 0))
WHITE = ((255, 255, 255))
RED = ((255, 255, 255))
GREEN = ((0, 255, 0))
BLUE = ((0, 0, 255))

width, height = 500, 500
screen = pygame.display.set_mode((width, height))

# Game Loop
while running:
    screen.fill(BLACK)

    clock.tick(60)
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Background image.
    screen.blit(bg_game, (0, 0))
    # Coin image.
    screen.blit(coin, (coin_x, coin_y))
    coin_x, coin_y = random.randint(0, 440), random.randint(0, 440)


    keys = pygame.key.get_pressed()
    
    emoji_x += (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]) * vel
    emoji_y += (keys[pygame.K_DOWN] - keys[pygame.K_UP]) * vel

    if emoji_x > 440:
        emoji_x = 440
    if emoji_x < -3:
        emoji_x = -3
    if emoji_y > 440:
        emoji_y = 440
    if emoji_y < -3:
        emoji_y = -3

    screen.blit(mad_emoji, (emoji_x, emoji_y))
    pygame.display.update()
