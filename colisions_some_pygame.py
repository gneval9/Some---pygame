#Maded and developed by gneval9 Software

import pygame
import sys
import random

pygame.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)

cord_x = 700
cord_y = 400

speed_x = 0
speed_y = 0

#size = (800, 500)
size_x = random.randint(200, 1400)
size_y = random.randint(200, 1400)

screen = pygame.display.set_mode((size_x, size_y))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                speed_x = -1
            if event.key == pygame.K_RIGHT:
                speed_x = 1
            if event.key == pygame.K_UP:
                speed_y = -1
            if event.key == pygame.K_DOWN:
                speed_y = 1
            
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                speed_x = 0
            if event.key == pygame.K_RIGHT:
                speed_x = 0
            if event.key == pygame.K_UP:
                speed_y = 0
            if event.key == pygame.K_DOWN:
                speed_y = 0
            


    screen.fill(BLACK)

   

    cord_x += speed_x
    cord_y += speed_y


    borde_arriba = pygame.draw.rect(screen, BLACK, (0, 0, 1000, 1))
    borde_abajo = pygame.draw.rect(screen, BLACK, (0, size_y, 1000, 1))
    borde_izquierda = pygame.draw.rect(screen, BLACK, (0, 0, 1, 1000))
    borde_derecha = pygame.draw.rect(screen, BLACK, (size_x, 0, 1, 1000))
    circulo = pygame.draw.circle(screen, RED, (cord_x, cord_y), radius=40)
    

    if circulo.colliderect(borde_arriba):
        if cord_y > 39:
            cord_y += 1

    if circulo.colliderect(borde_abajo):
        if cord_y > size_y - 39:
            cord_y -= 1

    if circulo.colliderect(borde_izquierda):
        if cord_x > 0:
            cord_x += 1

    if circulo.colliderect(borde_derecha):
        if cord_x > size_x - 39:
            cord_x -= 1


    pygame.display.flip()
