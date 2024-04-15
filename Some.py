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
import random
import time
import tkinter as tk
import threading
import sys




#Definir colores

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255,0 ,0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

player_color = RED



def play():

    pygame.init()

    game_over = False

    time = 0

    speedup = 0.1

    size = (800, 500)

    pygame.mouse.set_visible(0)

    #Crear ventana
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('Some - By gneval9 Software')

    #Reloj de FPS
    clock = pygame.time.Clock()

    #Coordenadas
    cord_x = random.randint(0,760)
    cord_y = random.randint(0,460)

    square_cord_x = random.randint(0,760)
    square_cord_y = random.randint(0,460)

    square_cord_x2 = random.randint(0,760)
    square_cord_y2 = random.randint(0,460)

    square_cord_x3 = random.randint(0,760)
    square_cord_y3 = random.randint(0,460)

    #Velocidad
    initial_speed = 8

    speed_x = 0
    speed_y = 0

    square_speed_x = 3
    square_speed_y = 2.5

    square_speed_x2 = -4
    square_speed_y2 = -3.5

    square_speed_x3 = 6
    square_speed_y3 = -4.5



    #Bucle principal

    while game_over == False:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                break
                game_over = True

            mouse_pos = pygame.mouse.get_pos()
            mouse_x = mouse_pos[0]
            mouse_y = mouse_pos[1]
            mouse_pressed = pygame.mouse.get_pressed()

            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    speed_x = initial_speed * -1
                if event.key == pygame.K_RIGHT:
                    speed_x = initial_speed

                if event.key == pygame.K_DOWN:
                    speed_y = initial_speed
                if event.key == pygame.K_UP:
                    speed_y = initial_speed * -1


            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    speed_x = 0
                if event.key == pygame.K_RIGHT:
                    speed_x = 0

                if event.key == pygame.K_DOWN:
                    speed_y = 0
                if event.key == pygame.K_UP:
                    speed_y = 0


        if (square_cord_x > 760 or square_cord_x < 0):
            square_speed_x *= -1
            speedup *= -1

        if (square_cord_y > 460 or square_cord_y < 0):
            square_speed_y *= -1
            speedup *= -1


        if (square_cord_x2 > 760 or square_cord_x2 < 0):
            square_speed_x2 *= -1
            speedup *= -1

        if (square_cord_y2 > 460 or square_cord_y2 < 0):
            square_speed_y2 *= -1
            speedup *= -1

        if (square_cord_x3 > 760 or square_cord_x3 < 0):
            square_speed_x3 *= -1
            speedup *= -1


        if (square_cord_y3 > 460 or square_cord_y3 < 0):
            square_speed_y3 *= -1
            speedup *= -1


        #---Logica---#
        cord_x += speed_x
        cord_y += speed_y

        square_cord_x += square_speed_x
        square_cord_y += square_speed_y

        square_cord_x2 += square_speed_x2
        square_cord_y2 += square_speed_y2

        square_cord_x3 += square_speed_x3
        square_cord_y3 += square_speed_y3

        square_speed_x += speedup
        square_speed_y += speedup

        square_speed_x2 += speedup
        square_speed_y2 += speedup
        
        square_speed_x3 += speedup
        square_speed_y3 += speedup
        


        RGB = (random.randint(0,255), random.randint(0,255), random.randint(0,255))







    
        #Color de fondo
        screen.fill(BLACK)

        #---Zona de dibujo---#

        enemy1 = pygame.draw.rect(screen, RGB, (square_cord_x, square_cord_y, 40, 40))
        enemy2 = pygame.draw.rect(screen, RGB, (square_cord_x2, square_cord_y2, 50, 50))
        enemy3 = pygame.draw.rect(screen, RGB, (square_cord_x3, square_cord_y3, 60, 40))
        player = pygame.draw.circle(screen, player_color, (cord_x, cord_y), 30)


        
        #cursor = pygame.draw.rect(screen, RED, (mouse_x, mouse_y, 20, 20))



        #Colisiones
        if player.colliderect(enemy1) or player.colliderect(enemy2) or player.colliderect(enemy3):
            game_over = True
            break






    
            







        borde_arriba = pygame.draw.rect(screen, BLACK, (0, 0, 1000, 1))
        borde_abajo = pygame.draw.rect(screen, BLACK, (0, 499, 1000, 1))
        borde_izquierda = pygame.draw.rect(screen, BLACK, (0, 0, 1, 1000))
        borde_derecha = pygame.draw.rect(screen, BLACK, (799, 0, 1, 1000))

        

        if player.colliderect(borde_arriba):
            if cord_y > -32:
                cord_y += 8

        if player.colliderect(borde_abajo):
            if cord_y > 400 - 32:
                cord_y -= 8

        if player.colliderect(borde_izquierda):
            if cord_x > -32:
                cord_x += 8

        if player.colliderect(borde_derecha):
            if cord_x > 700 - 32:
                cord_x -= 8

        #Actualizar pantalla
        time += 0.0166666666
        pygame.display.flip()
        clock.tick(60)
        print(time)
       

    if game_over:
        screen.fill(BLACK)  # Poner la pantalla en negro

        # Crear un texto "Game Over" en rojo y centrado en la pantalla
        font = pygame.font.Font(None, 36)
        text = font.render("Game Over", True, RED)
        text_rect = text.get_rect(center=(400, 250))
        screen.blit(text, text_rect)
        
        
        

    if time < 1:
        print("Spawn error")

   
    

def menu():

    pygame.init()

    game_over = False

    time = 0

    speedup = 0.1

    size = (800, 500)

    pygame.mouse.set_visible(0)

    #Crear ventana
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('Some - By gneval9 Software')

    #Reloj de FPS
    clock = pygame.time.Clock()

    # Font Setup
    font = pygame.font.Font(None, 60)  # Selecciona la fuente y el tamaño del texto

    # Renderizar texto
    text = font.render("PLAY", True, BLACK)  # Renderiza el texto en blanco

    # Posición del texto
    text_rect = text.get_rect()
    text_rect.center = (397, 313)






    #Bucle principal

    while game_over == False:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True

            mouse_pos = pygame.mouse.get_pos()
            mouse_x = mouse_pos[0]
            mouse_y = mouse_pos[1]
            mouse_pressed = pygame.mouse.get_pressed()


    
        #Color de fondo
        screen.fill(BLACK)

        #---Zona de dibujo---#
        square = pygame.draw.rect(screen, WHITE, (310, 260, 180, 106))
        play_button = pygame.draw.rect(screen, GREEN, (320, 270, 160, 86))
        screen.blit(text, text_rect)
        cursor = pygame.draw.rect(screen, RED, (mouse_x, mouse_y, 20, 20))


    
        if cursor.colliderect(play_button):
            if mouse_pressed[0]:
                play_button = pygame.draw.rect(screen, BLUE, (320, 270, 160, 86))
                screen.blit(text, text_rect)
                cursor = pygame.draw.rect(screen, RED, (mouse_x, mouse_y, 20, 20))
                play()
    
        #Actualizar pantalla
        time += 0.0166666666
        pygame.display.flip()
        clock.tick(60)
      
       


menu()




#11-01-2024 / 15-04-2024
