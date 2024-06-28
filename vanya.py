import pygame
import os

pygame.init()

display = pygame.display.set_mode((700,700))
clock = pygame.time.Clock()

go_right = False
go_left = False
go_up = False
go_down = False

dir_path = os.path.dirname(__file__)
img_path = os.path.abspath(dir_path + "/textures")

geroi = pygame.Rect(50,50,35,35)

#изумрудная стена - 1
#арбуз - 2
#герой - 3
#пустота - 0
#алмазная стена - 5

wall = pygame.image.load(img_path + '/floor.png')               #cтена
hero = pygame.image.load(img_path + '/smile.png')               #игрок
hero = pygame.transform.scale(hero, (35,35))
finish = pygame.image.load(img_path + '/watermelon.png')        #garbuz
wall2 = pygame.image.load(img_path + '/floor2.png')             #ctena2

textures = [ #14 Ha 14
    [1,5,1,5,1,5,1,5,1,5,1,5,1,5],
    [5,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,5,1,5,1,5,1,5,1,5,1,5,0,5],
    [5,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,1,5,1,5,1,5,1,5,1,5,1,5],
    [5,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,5,1,5,1,5,1,5,1,5,1,5,0,5],
    [5,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,5,1,5,1,5,1,5,1,5,1,5,0,5],
    [5,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,1,5,1,5,1,5,1,5,1,5,1,5],
    [5,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,2,5],
    [5,1,5,1,5,1,5,1,5,1,5,1,5,1]
]
rects = []
rects_textures = []
good_rects = []
bad_rects = []

x = 0
y = 0

for texture in textures:
    for i in texture:
        kvadrat = pygame.Rect(x, y, 50, 50)
        rects.append(kvadrat)
        rects_textures.append(i)
        if i == 1 or i == 5:
            bad_rects.append(kvadrat)
        if i == 2 :
            good_rects.append(kvadrat)
        x += 50 
    y += 50
    x = 0  

font = pygame.font.SysFont("Arial", 50)
text = font.render("YOU WIN", True, (0,255,0))
       

game = True
while game:
    display.fill((50.2,50.2,50.2))

    for i in range(196):
        if rects_textures[i] == 1:
            display.blit(wall,rects[i])
        if rects_textures[i] == 2:
            display.blit(finish,rects[i])
        if rects_textures[i] == 3:
            display.blit(hero,rects[i])
        if rects_textures[i] == 5:
            display.blit(wall2,rects[i])
    
    display.blit(hero,geroi)

    #pygame.draw.rect(display, (255,0,0), geroi)

    for bad in bad_rects:
        if geroi.colliderect(bad):
            geroi.x = 50
            geroi.y = 50
    for good in good_rects:
        if geroi.colliderect(good):
            display.fill((0,0,0))
            display.blit(text, (220,200))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                go_right = True
            if event.key == pygame.K_a:
                go_left = True
            if event.key == pygame.K_w:
                go_up = True
            if event.key == pygame.K_s:
                go_down = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_d:
                go_right = False
            if event.key == pygame.K_a:
                go_left = False
            if event.key == pygame.K_w:
                go_up = False
            if event.key == pygame.K_s:
                go_down = False
            
    if go_left == True:
        geroi.x -= 6
    if go_right == True:
        geroi.x += 6
    if go_up == True:
        geroi.y -= 6
    if go_down == True:
        geroi.y += 6

    pygame.display.flip()
    clock.tick(60)