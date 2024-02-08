 #                             __ ___                           
 #  __ _ _ __   _____   ____ _| |/ _ \                          
 # / _` | '_ \ / _ \ \ / / _` | | (_) |                         
 #| (_| | | | |  __/\ V / (_| | |\__, |                         
 # \__, |_| |_|\___| \_/_\__,_|_| _/_/                          
 # |___/            / ___|  ___  / _| |___      ____ _ _ __ ___ 
 #                  \___ \ / _ \| |_| __\ \ /\ / / _` | '__/ _ \
 #                   ___) | (_) |  _| |_ \ V  V / (_| | | |  __/
 #                  |____/ \___/|_|  \__| \_/\_/ \__,_|_|  \___|

import pygame
import sys
import random

pygame.init()


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)



DR = 255
DG = 000
DB = 000
DASH_COLOR = (DR, DG, DB)


speed_x = 0
speed_y = 0


size_x = random.randint(200, 1400)
size_y = random.randint(200, 1400)

cord_x = size_x / 2
cord_y = size_y / 2

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

    R = random.randint(0, 255)
    G = random.randint(0, 255)
    B = random.randint(0, 255)

    RGB = (R, G, B)
    
    cord_x += speed_x
    cord_y += speed_y

    DR += 5
    DG += 5
    DB += 5
    
    if DR == 255 and DG == 255 and DB == 255:
        DASH_COLOR == RGB

    DR == DR + 1
    DG == DG + 1
    DB == DB + 1



    circulo = pygame.draw.circle(screen, RED, (cord_x, cord_y), radius=40)
    dash_orb = pygame.draw.circle(screen, DASH_COLOR, (cord_x, cord_y), radius=10)




#Colisiones

    borde_arriba = pygame.draw.rect(screen, BLACK, (0, 0, 1000, 1))
    borde_abajo = pygame.draw.rect(screen, BLACK, (0, size_y, 1000, 1))
    borde_izquierda = pygame.draw.rect(screen, BLACK, (0, 0, 1, 1000))
    borde_derecha = pygame.draw.rect(screen, BLACK, (size_x, 0, 1, 1000))

    

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
