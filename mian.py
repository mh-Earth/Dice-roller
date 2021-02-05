import pygame
import time
import random


# __________________________________________________________________________________________________________________
def roll(data):
    global dice_PositionX,dice_PositionY,size,display
    if data==1:
        pygame.draw.circle(display, (color), (dice_PositionX+size/2,dice_PositionY+size/2), size/10)
    elif data==2:
        pygame.draw.circle(display, (color), (dice_PositionX+(size/2-gaps),dice_PositionY+(size/2-gaps)), size/10)
        pygame.draw.circle(display, (color), (dice_PositionX+(size/2+gaps),dice_PositionY+(size/2+gaps)), size/10)
    elif data==3:
        pygame.draw.circle(display, (color), (dice_PositionX+(size/2-gaps),dice_PositionY+(size/2-gaps)), size/10)
        pygame.draw.circle(display, (color), (dice_PositionX+size/2,dice_PositionY+size/2), size/10)
        pygame.draw.circle(display, (color), (dice_PositionX+(size/2+gaps),dice_PositionY+(size/2+gaps)), size/10)
    elif data==4:
        pygame.draw.circle(display, (color), (dice_PositionX+size/2-gaps,dice_PositionY+size/2-gaps), size/10)
        pygame.draw.circle(display, (color), (dice_PositionX+size/2+gaps,dice_PositionY+size/2-gaps), size/10)
        pygame.draw.circle(display, (color), (dice_PositionX+size/2+gaps,dice_PositionY+size/2+gaps), size/10)
        pygame.draw.circle(display, (color), (dice_PositionX+size/2-gaps,dice_PositionY+size/2+gaps), size/10)
    elif data==5:
        pygame.draw.circle(display, (color), (dice_PositionX+size/2,dice_PositionY+size/2), size/10)
        pygame.draw.circle(display, (color), (dice_PositionX+size/2-gaps,dice_PositionY+size/2-gaps), size/10)
        pygame.draw.circle(display, (color), (dice_PositionX+size/2+gaps,dice_PositionY+size/2-gaps), size/10)
        pygame.draw.circle(display, (color), (dice_PositionX+size/2+gaps,dice_PositionY+size/2+gaps), size/10)
        pygame.draw.circle(display, (color), (dice_PositionX+size/2-gaps,dice_PositionY+size/2+gaps), size/10)
    elif data==6:
        pygame.draw.circle(display, (color), (dice_PositionX+size/2+gaps,dice_PositionY+size/2), size/10)
        pygame.draw.circle(display, (color), (dice_PositionX+size/2-gaps,dice_PositionY+size/2), size/10)
        pygame.draw.circle(display, (color), (dice_PositionX+size/2-gaps,dice_PositionY+size/2-gaps), size/10)
        pygame.draw.circle(display, (color), (dice_PositionX+size/2+gaps,dice_PositionY+size/2-gaps), size/10)
        pygame.draw.circle(display, (color), (dice_PositionX+size/2+gaps,dice_PositionY+size/2+gaps), size/10)
        pygame.draw.circle(display, (color), (dice_PositionX+size/2-gaps,dice_PositionY+size/2+gaps), size/10)


# __________________________________________________________________________________________________________________
size=150
gaps=size/4
max_ran=300
mini_ran=20
dice_PositionX=random.randint(mini_ran,600-size)
dice_PositionY=random.randint(mini_ran,600-size)

dice_PositionX_v=random.randint(10,max_ran)
dice_PositionY_v=10

if __name__=="__main__":
        

    pygame.init()
    # ___________________________________
    screen_wight=800
    screen_hight=800
    display=pygame.display.set_mode((screen_hight,screen_wight))
    pygame.display.set_caption(' $')
    # ___________________________________
    box=pygame.image.load('box.PNG')
    box=pygame.transform.scale(box,(screen_hight+40,screen_wight+40))

    dicePic=pygame.image.load('dicePic.png')
    dicePic=pygame.transform.scale(dicePic,(size,size))

    # ___________________________________
    running=True
    rolls=random.choice([1,2,3,4,5,6])
    color=(255,255,255)
    
    # ___________________________________
    clock=pygame.time.Clock()
    while running:
        display.blit(box,(-25,-23))
        if dice_PositionX>screen_hight-size:
            dice_PositionX_v=random.randint(mini_ran,max_ran)
            rolls=random.choice([1,2,3,4,5,6])
            dice_PositionX_v=dice_PositionX_v*-1

        if dice_PositionY>screen_hight-size:
            dice_PositionY_v=random.randint(mini_ran,max_ran)
            dice_PositionY_v=dice_PositionY_v*-1
            rolls=random.choice([1,2,3,4,5,6])

        if dice_PositionX<0:
            dice_PositionX_v=dice_PositionX_v*-1

        if dice_PositionY<0:
            dice_PositionY_v=dice_PositionY_v*-1
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                running=False
                quit()
            elif event.type==pygame.KEYDOWN:
                if event.key==pygame.K_ESCAPE:
                    running=False
                    quit()
                if event.key==pygame.K_SPACE:
                    rolls=random.choice([1,2,3,4,5,6])
                    color=(255,255,255)
            elif event.type==pygame.MOUSEBUTTONDOWN:
                mouse_pos=pygame.mouse.get_pos()
                dice_PositionX=mouse_pos[0]-size/2
                dice_PositionY=mouse_pos[1]-size/2
                dice_PositionX_v=0
                dice_PositionY_v=0
            elif event.type==pygame.MOUSEBUTTONUP:
                dice_PositionX_v=random.randint(10,max_ran)
                dice_PositionY_v=10
        display.blit(dicePic,(dice_PositionX,dice_PositionY))
        dice_PositionY+=dice_PositionY_v
        dice_PositionX+=dice_PositionX_v
        roll(rolls)
        clock.tick(60)
        pygame.display.update()
