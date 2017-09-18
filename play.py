# -*- coding: utf-8 -*-
"""
PLAY!!
"""
import pygame
pygame.init()
pygame.display.set_mode((800, 600))
pygame.display.set_caption('RRFOE')

CRASHED = False

while not CRASHED:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            CRASHED = True
        print(event)
    pygame.display.update()
