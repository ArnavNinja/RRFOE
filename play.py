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

CRASHED = False

while not CRASHED:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            CRASHED = True

        WINDOW.fill((255, 255, 255))
        run_marshawn_run(POS_X, POS_Y)

        print(event)
    pygame.display.update()
