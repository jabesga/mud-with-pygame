import pygame
import sys

pygame.init()

WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Lost in somewhere")

font = pygame.font.SysFont('comicsansms', 36)

message = ''

mapa = [
['[  ]', '[  ]', '[  ]', '[  ]', '[  ]'],
['[  ]', '[  ]', '[  ]', '[  ]', '[  ]'],
['[  ]', '[  ]', '[  ]', '[  ]', '[  ]'],
['[  ]', '[  ]', '[  ]', '[  ]', '[  ]'],
['[  ]', '[  ]', '[  ]', '[  ]', '[  ]'],
]

pos_x = 4
pos_y = 2
mapa[4][2] = '[x]'

def imprimir_mapa():
    global mapa
    x = WIDTH - 250
    y = 0
    for row in mapa:
        result = ''
        for col in row:
            result += col
        text = font.render(result, 0, (0, 0, 250))
        screen.blit(text, (x,y))
        y += 40

def imprimir_nota():
    text = font.render('MUEVETE CON WASD', 0, (0, 0, 0))
    screen.blit(text, (0,0))

def actualizar_posicion(nueva_pos_x, nueva_pos_y):
    global pos_x
    global pos_y
    mapa[pos_x][pos_y] = '[  ]'
    mapa[nueva_pos_x][nueva_pos_y] = '[x]'
    pos_x = nueva_pos_x
    pos_y = nueva_pos_y



mapa_fondos = [
{'pos_x': 0, 'pos_y': 0, 'imagen' : 'images/3.jpg'},
{'pos_x': 0, 'pos_y': 1, 'imagen' : 'images/3.jpg'},
{'pos_x': 0, 'pos_y': 2, 'imagen' : 'images/1.jpg'},
{'pos_x': 0, 'pos_y': 3, 'imagen' : 'images/3.jpg'},
{'pos_x': 0, 'pos_y': 4, 'imagen' : 'images/3.jpg'},
{'pos_x': 1, 'pos_y': 0, 'imagen' : 'images/3.jpg'},
{'pos_x': 1, 'pos_y': 1, 'imagen' : 'images/3.jpg'},
{'pos_x': 1, 'pos_y': 2, 'imagen' : 'images/2.jpg'},
{'pos_x': 1, 'pos_y': 3, 'imagen' : 'images/2.jpg'},
{'pos_x': 1, 'pos_y': 4, 'imagen' : 'images/3.jpg'},
{'pos_x': 2, 'pos_y': 0, 'imagen' : 'images/3.jpg'},
{'pos_x': 2, 'pos_y': 1, 'imagen' : 'images/1I.jpg'},
{'pos_x': 2, 'pos_y': 2, 'imagen' : 'images/1.jpg'},
{'pos_x': 2, 'pos_y': 3, 'imagen' : 'images/1D.jpg'},
{'pos_x': 2, 'pos_y': 4, 'imagen' : 'images/3.jpg'},
{'pos_x': 3, 'pos_y': 0, 'imagen' : 'images/3.jpg'},
{'pos_x': 3, 'pos_y': 1, 'imagen' : 'images/3.jpg'},
{'pos_x': 3, 'pos_y': 2, 'imagen' : 'images/3.jpg'},
{'pos_x': 3, 'pos_y': 3, 'imagen' : 'images/3.jpg'},
{'pos_x': 3, 'pos_y': 4, 'imagen' : 'images/3.jpg'},
{'pos_x': 4, 'pos_y': 0, 'imagen' : 'images/3.jpg'},
{'pos_x': 4, 'pos_y': 1, 'imagen' : 'images/3.jpg'},
{'pos_x': 4, 'pos_y': 2, 'imagen' : 'images/3.jpg'},
{'pos_x': 4, 'pos_y': 3, 'imagen' : 'images/3.jpg'},
{'pos_x': 4, 'pos_y': 4, 'imagen' : 'images/3.jpg'},
]

def actualizar_fondo():
    global pos_x
    global pos_y
    for pos in mapa_fondos:
        if pos_x == pos['pos_x'] and pos_y == pos['pos_y']:
            image = pygame.image.load(pos['imagen'])
            screen.blit(image, (0,0))
            break
        
def move(key):
    pintar_pantalla()
    global pos_x
    global pos_y
    if pos_x > 0:
        if key == 'w':
            nueva_pos_x = pos_x - 1
            actualizar_posicion(nueva_pos_x, pos_y)
    if pos_y > 0:
        if key == 'a':
            nueva_pos_y = pos_y - 1
            actualizar_posicion(pos_x, nueva_pos_y)        
    if pos_x < 4:
        if key == 's':
            nueva_pos_x = pos_x + 1
            actualizar_posicion(nueva_pos_x, pos_y)                
    if pos_y < 4:
        if key == 'd':
            nueva_pos_y = pos_y + 1
            actualizar_posicion(pos_x, nueva_pos_y)

    actualizar_fondo()
    imprimir_mapa()
    imprimir_nota()

def pintar_pantalla():
    screen.fill((250, 250, 250))
    

special_keys = [pygame.K_BACKSPACE, pygame.K_RETURN]
movement_keys = [pygame.K_w,pygame.K_a,pygame.K_s,pygame.K_d]

pintar_pantalla()
actualizar_fondo()
imprimir_mapa()
imprimir_nota()
while True:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key in movement_keys:
                move(event.unicode)
            if event.key and event.key not in movement_keys + special_keys:
                message += event.unicode
#            if event.key == pygame.K_BACKSPACE:
#                pintar_pantalla()
#                message = message[:-1]
#            if event.key == pygame.K_RETURN:
#                pintar_pantalla()    
    pygame.display.flip()