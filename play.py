# -*- coding: utf-8 -*-
"""
PLAY!!
"""
import pygame
pygame.init()
WINDOW = pygame.display.set_mode((800, 600))
pygame.display.set_caption('RRFOE')

IMG_MARSHAWN = pygame.image.load('images/run-marshwn-run.png')
IMG_MARSHAWN = pygame.transform.scale(IMG_MARSHAWN, (165, 256))
def run_marshawn_run(pos_x, pos_y):
    'run marshawn'
    WINDOW.blit(IMG_MARSHAWN, (pos_x, pos_y))

POS_X = (0)
POS_Y = (0)

CHANGE_X = 100
CHANGE_Y = 0

CRASHED = False

while not CRASHED:
    for event in pygame.event.get():
        WINDOW.fill((255, 255, 255))
        if event.type == pygame.QUIT:
            CRASHED = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                CHANGE_Y = 10
            elif event.key == pygame.K_UP:
                CHANGE_Y = -10
            elif event.key == pygame.K_LEFT:
                CHANGE_X = -10
            elif event.key == pygame.K_RIGHT:
                CHANGE_X = 10
            
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN or event.key == pygame.K_UP or event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                CHANGE_X = 0 
                CHANGE_Y = 0
            
        POS_X += CHANGE_X
        # POS_Y += CHANGE_Y

        if POS_X > 800:
            POS_X = 800

        run_marshawn_run(POS_X, POS_Y)

        print(event)
    pygame.display.update()
