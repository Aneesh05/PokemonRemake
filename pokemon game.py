import pygame as pg
import random
from sys import path
from sys import exit
import os

my_path = os.path.dirname(os.path.realpath(__file__))
os.chdir(my_path)
path.append(my_path)

#Colours
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
white = (255,255,255)
black = (0,0,0)

#Setup
pg.init()
screen = pg.display.set_mode((1000,800)) #set your window size, (x,y)
pg.display.set_caption("Pokémon Diamond")
clock = pg.time.Clock()

straight = (pg.image.load("straight.png"))
background = (pg.image.load("bg.png"))
youngster = (pg.image.load("youngster.png"))
lass = (pg.image.load("lass.png"))
battle = (pg.image.load("battle.png"))
select_arrow = (pg.image.load("select_arrow.png"))
lose = (pg.image.load("lose.png"))
win1 = (pg.image.load("win_screen.png"))
startscreen = (pg.image.load("start.png"))
X = 550
Y = 638
randnum = random.randint(1,60)
randnum2 = random.randint(1,60)
randnum3 = random.randint(1,60)
randnum4 = random.randint(1,60)
randnum5 = random.randint(1,60)
randnum6 = random.randint(1,60)
randnum7 = random.randint(1,60)
randnum8 = random.randint(1,60)
randnum9 = random.randint(1,60)
randnum10 = random.randint(1,60)
randnum11 = random.randint(1,60)
randnum12 = random.randint(1,60)

battleround = 0
old_space = 0
score = 0

trainer_battle_1 = pg.Rect(385, 620, 30, 130)
trainer_battle_2 = pg.Rect(615, 420, 30, 150)


#pokemon
chimchar = (pg.image.load("chimchar.png"))
turtwig = (pg.image.load("turtwig.png"))
dialga = (pg.image.load("dialga.png"))
palkia = (pg.image.load("palkia.png"))
umbreon = (pg.image.load("umbreon.png"))
roserade = (pg.image.load("Roserade.png"))
garchomp = (pg.image.load("garchomp.png"))
infernape = (pg.image.load("infernape.png"))
charizard = (pg.image.load("charizard.png"))
torttera = (pg.image.load("torttera.png"))
gardevoir = (pg.image.load("gardevoir.png"))
lapras = (pg.image.load("lapras.png"))

mode = 4

borders = []
borders.append(pg.Rect(0, 730, 630, 70))
#borders.append(pg.Rect(0,0,0,0))
#borders.append(pg.Rect(0,0,0,0))
#borders.append(pg.Rect(0,0,0,0))
#borders.append(pg.Rect(0,0,0,0))
#borders.append(pg.Rect(0,0,0,0))
#borders.append(pg.Rect(0,0,0,0))
#borders.append(pg.Rect(0,0,0,0))
#borders.append(pg.Rect(0,0,0,0))
#borders.append(pg.Rect(0,0,0,0))
#borders.append(pg.Rect(0,0,0,0))
#borders.append(pg.Rect(0,0,0,0))
#borders.append(pg.Rect(0,0,0,0))

class pokemon ():
    #class variables

    def __init__(self, hp,x,y,image):
        #Attributes
        self.hp = hp
        self.x = x
        self.y = y
        self.image = image

    def update(self):
        randnum = random.randint(1,60)
        randnum2 = random.randint(1,60)
        randnum3 = random.randint(1,60)
        randnum4 = random.randint(1,60)
        randnum5 = random.randint(1,60)
        randnum6 = random.randint(1,60)
        randnum7 = random.randint(1,60)
        randnum8 = random.randint(1,60)
        randnum9 = random.randint(1,60)
        randnum10 = random.randint(1,60)
        randnum11 = random.randint(1,60)
        randnum12 = random.randint(1,60)

    def draw(self):
        screen.blit(self.image, (self.x, self.y))

chimchar = pokemon(randnum, 170, 352, chimchar)
dialga = pokemon(randnum2, 170, 352, dialga)
umbreon = pokemon(randnum3, 170, 352, umbreon)
roserade = pokemon(randnum4, 170, 352, roserade)
garchomp = pokemon(randnum5, 170, 352, garchomp)
infernape = pokemon(randnum6, 170, 352, infernape)

turtwig = pokemon(randnum7, 670, 150, turtwig)
palkia = pokemon(randnum8, 670, 150, palkia)
charizard = pokemon(randnum9, 670, 150, charizard)
torttera = pokemon(randnum10, 670, 150, torttera)
gardevoir = pokemon(randnum11, 670, 150, gardevoir)
lapras= pokemon(randnum12, 670, 150, lapras)

class enemy_trainer ():
    #class variables

    def __init__(self, x,y,image, pokemon1, pokemon2):
        #Attributes
        self.x = x
        self.y = y
        self.image = image
        self.pokemon1 = pokemon1
        self.pokemon2 = pokemon2
        self.hitbox = pg.Rect(self.x, self.y, 30, 150)


    def draw(self):
        screen.blit(self.image, (self.x, self.y))

lass1 = enemy_trainer (500, 100, lass, gardevoir, lapras)
youngster1 = enemy_trainer (370, 620, youngster, turtwig, palkia )
youngster2 = enemy_trainer (600, 400, youngster,charizard, torttera )


class trainer ():
    #class variables

    walk_right = []
    walk_right.append(pg.image.load("right_1.png"))
    walk_right.append(pg.image.load("right_2.png"))
    walk_right.append(pg.image.load("right_3.png"))
    walk_right.append(pg.image.load("right_4.png"))

    walk_left = []
    walk_left.append(pg.image.load("left_1.png"))
    walk_left.append(pg.image.load("left_2.png"))
    walk_left.append(pg.image.load("left_3.png"))
    walk_left.append(pg.image.load("left_4.png"))

    walk_up = []
    walk_up.append(pg.image.load("up_1.png"))
    walk_up.append(pg.image.load("up_2.png"))
    walk_up.append(pg.image.load("up_3.png"))
    walk_up.append(pg.image.load("up_4.png"))

    walk_down = []
    walk_down.append(pg.image.load("down_1.png"))
    walk_down.append(pg.image.load("down_2.png"))
    walk_down.append(pg.image.load("down_3.png"))
    walk_down.append(pg.image.load("down_4.png"))



    bike_right = []
    bike_right.append(pg.image.load("right1.png"))
    bike_right.append(pg.image.load("right2.png"))
    bike_right.append(pg.image.load("right3.png"))


    bike_left = []
    bike_left.append(pg.image.load("left1.png"))
    bike_left.append(pg.image.load("left2.png"))
    bike_left.append(pg.image.load("left3.png"))


    bike_up = []
    bike_up.append(pg.image.load("bikeup1.png"))
    bike_up.append(pg.image.load("bikeup2.png"))


    bike_down = []
    bike_down.append(pg.image.load("bikedown1.png"))
    bike_down.append(pg.image.load("bikedown2.png"))




    run_right = []
    run_right.append(pg.image.load("right-1.png"))
    run_right.append(pg.image.load("right-2.png"))
    run_right.append(pg.image.load("right-3.png"))
    run_right.append(pg.image.load("right-4.png"))

    run_left = []
    run_left.append(pg.image.load("left-1.png"))
    run_left.append(pg.image.load("left-2.png"))
    run_left.append(pg.image.load("left-3.png"))
    run_left.append(pg.image.load("left-4.png"))

    run_up = []
    run_up.append(pg.image.load("up-1.png"))
    run_up.append(pg.image.load("up-2.png"))

    run_down = []
    run_down.append(pg.image.load("down-1.png"))
    run_down.append(pg.image.load("down-2.png"))





    def __init__(self, pokemon1, pokemon2, pokemon3, pokemon4, pokemon5, pokemon6):
        #Attributes
        self.hitbox = pg.Rect(850, 750, 50, 50)
        self.speedx = 0
        self.speedy = 0
        self.pokemon1 = pokemon1
        self.pokemon2 = pokemon2
        self.pokemon3 = pokemon3
        self.pokemon4 = pokemon4
        self.pokemon5 = pokemon5
        self.pokemon6 = pokemon6


        self.right_walk_image = 0
        self.left_walk_image = 0

        self.down_walk_image = 0
        self.up_walk_image = 0

        self.right_bike_image = 0
        self.left_bike_image = 0

        self.up_bike_image = 0
        self.down_bike_image = 0

        self.right_run_image = 0
        self.left_run_image = 0

        self.up_run_image = 0
        self.down_run_image = 0

    def update(self):
        self.hitbox[0] +=self.speedx
        self.hitbox[1] +=self.speedy
        keys = pg.key.get_pressed()


        self.right_walk_image += 1
        if self.right_walk_image == 4:
            self.right_walk_image = 0


        self.left_walk_image += 1
        if self.left_walk_image == 4:
            self.left_walk_image = 0






        self.up_walk_image += 1
        if self.up_walk_image == 4:
            self.up_walk_image = 0


        self.down_walk_image += 1
        if self.down_walk_image == 4:
            self.down_walk_image = 0





        self.right_bike_image += 1
        if self.right_bike_image == 3:
            self.right_bike_image = 0



        self.left_bike_image += 1
        if self.left_bike_image == 3:
            self.left_bike_image = 0




        self.up_bike_image += 1
        if self.up_bike_image == 2:
            self.up_bike_image = 0



        self.down_bike_image += 1
        if self.down_bike_image == 2:
            self.down_bike_image = 0


        self.right_run_image += 1
        if self.right_run_image == 4:
            self.right_run_image = 0


        self.left_run_image += 1
        if self.left_run_image == 4:
            self.left_run_image = 0



        self.up_run_image += 1
        if self.up_run_image == 2:
            self.up_run_image = 0


        self.down_run_image += 1
        if self.down_run_image == 2:
            self.down_run_image = 0



        if keys[pg.K_a] ==True:
            self.speedx = -10
            self.speedy = 0

        elif keys[pg.K_d] ==True:
            self.speedx = 10
            self.speedy = 0
        else:
            self.speedx = 0


        if keys[pg.K_w] ==True:
            self.speedy = -10
            self.speedx = 0
        elif keys[pg.K_s] ==True:
            self.speedy = 10
            self.speedx = 0
        else:
            self.speedy = 0



        if keys[pg.K_a] == True and keys[pg.K_f]:
            self.speedx = -15
            self.speedy = 0

        elif keys[pg.K_d] == True and keys[pg.K_f]:
            self.speedx = 15
            self.speedy = 0


        if keys[pg.K_a] == True and keys[pg.K_f]:
            self.speedx = -15
            self.speedy = 0

        elif keys[pg.K_d] == True and keys[pg.K_f]:
            self.speedx = 15
            self.speedy = 0

        if keys[pg.K_w] == True and keys[pg.K_f]:
            self.speedy = -15
            self.speedx = 0

        elif keys[pg.K_s] == True and keys[pg.K_f]:
            self.speedy = 15
            self.speedx = 0






        if keys[pg.K_a] == True and keys[pg.K_v]:
            self.speedx = -20
            self.speedy = 0

        elif keys[pg.K_d] == True and keys[pg.K_v]:
            self.speedx = 20
            self.speedy = 0



        if keys[pg.K_w] == True and keys[pg.K_v]:
            self.speedy = -20
            self.speedx = 0

        elif keys[pg.K_s] == True and keys[pg.K_v]:
            self.speedy = 20
            self.speedx = 0



    def draw(self):
        if self.speedx == 10:
            screen.blit(trainer.walk_right[self.right_walk_image], (self.hitbox[0], self.hitbox[1]))
        if self.speedx == -10:
            screen.blit(trainer.walk_left[self.left_walk_image], (self.hitbox[0], self.hitbox[1]))


        if self.speedy == 10:
            screen.blit(trainer.walk_down[self.down_walk_image], (self.hitbox[0], self.hitbox[1]))
        if self.speedy == -10:
            screen.blit(trainer.walk_up[self.up_walk_image], (self.hitbox[0], self.hitbox[1]))



        if self.speedx == 15:
            screen.blit(trainer.run_right[self.right_walk_image], (self.hitbox[0], self.hitbox[1]))
        if self.speedx == -15:
            screen.blit(trainer.run_left[self.left_walk_image], (self.hitbox[0], self.hitbox[1]))


        if self.speedy == 15:
            screen.blit(trainer.run_down[self.down_run_image], (self.hitbox[0], self.hitbox[1]))
        if self.speedy == -15:
            screen.blit(trainer.run_up[self.up_run_image], (self.hitbox[0], self.hitbox[1]))





        if self.speedy == 0 and self.speedx == -0:
            screen.blit(straight, (self.hitbox[0], self.hitbox[1]))



        if self.speedx == 20:
            screen.blit(trainer.bike_right[self.right_bike_image], (self.hitbox[0], self.hitbox[1]))
        if self.speedx == -20:
            screen.blit(trainer.bike_left[self.left_bike_image], (self.hitbox[0], self.hitbox[1]))



        if self.speedy == 20:
            screen.blit(trainer.bike_down[self.down_bike_image], (self.hitbox[0], self.hitbox[1]))
        if self.speedy == -20:
            screen.blit(trainer.bike_up[self.up_bike_image], (self.hitbox[0], self.hitbox[1]))


        if trainer1.hitbox.colliderect(border):
            self.speedx = 0
            self.speedy = 0
        if trainer1.hitbox.colliderect(border) and self.speedx == 0:
            trainer1.hitbox.left = border.right




trainer1 = trainer (chimchar, dialga, garchomp, infernape, umbreon, roserade)




t1 = 1
t2 = 1
t3 = 1


while True:

    while mode == 0:
        pg.event.pump()
        #1. UPDATES
        #Move objects to new locations based on speed

        trainer1.update()

        #2. INPUTS
        #Check all input devices (Ex: Keyboard / Mouse)



        #3. EVENTS
        #Set of if-statements for different events of interest (Ex. Objects colliding, moving off screen etc.)

        if trainer1.hitbox.colliderect(youngster1.hitbox) and t1 == 1:
            trainer2 = youngster1
            mode = 1
            t1 = 0

        if trainer1.hitbox.colliderect(youngster2.hitbox) and t2 ==1:
            trainer2 = youngster2
            trainer1.pokemon1 = trainer1.pokemon3
            trainer1.pokemon2 = trainer1.pokemon4
            mode = 1
            t2 = 0

        if trainer1.hitbox.colliderect(lass1.hitbox) and t3 ==1:
            trainer1.pokemon1 = trainer1.pokemon5
            trainer1.pokemon2 = trainer1.pokemon6
            trainer2 = lass1
            mode = 1
            t3 = 0

        #4. DRAWING
        #Draw the current state of everything in the game (frame)
        for border in borders:
            pg.draw.rect(screen, white, border)


        screen.blit(background,(0,0))
        youngster1.draw()
        youngster2.draw()
        lass1.draw()




        trainer1.draw()


        pg.display.flip()

        #5. CLOCK
        #Set how many frame per second the game will run at
        clock.tick(30)



    while mode == 1:
        pg.event.pump()
        #1. UPDATES
        #Move objects to new locations based on speed
        trainer1.pokemon1.update()
        trainer1.pokemon2.update()
        trainer1.pokemon3.update()
        trainer1.pokemon4.update()
        trainer1.pokemon5.update()
        trainer1.pokemon6.update()

        trainer2.pokemon1.update()
        trainer2.pokemon2.update()


        #2. INPUTS
        #Check all input devices (Ex: Keyboard / Mouse)

        keys = pg.key.get_pressed()
        mx, my = pg.mouse.get_pos()
        L,M,R = pg.mouse.get_pressed()

        #3. EVENTS
        #Set of if-statements for different events of interest (Ex. Objects colliding, moving off screen etc.)

        pg.draw.ellipse(screen, blue, (mx,my,10,10))
        print(mx)
        print(my)


        #4. DRAWING
        #Draw the current state of everything in the game (frame)

        screen.blit(battle,(0,0))


        if battleround == 0:
            trainer1.pokemon1.draw()
            trainer2.pokemon1.draw()

        if battleround == 1:
            trainer1.pokemon2.draw()
            trainer2.pokemon2.draw()





        screen.blit(select_arrow,(X,Y))

        if keys[pg.K_UP] == True:
            Y = Y-75
        if keys[pg.K_LEFT] == True:
            X = X-190
        if keys[pg.K_DOWN] == True:
            Y = Y+75
        if keys[pg.K_RIGHT] == True:
            X = X+190

        if X > 922 or X < 525 or Y > 765 or Y < 585 :
            Y = 638
            X = 550


        if X == 550 and Y == 638 and keys[pg.K_SPACE] == True and old_space == 0:

            if battleround == 1:

                if trainer1.pokemon2.hp > trainer2.pokemon2.hp:
                    score = score +1
                else:
                    score = score

            if battleround == 0:
                if trainer1.pokemon1.hp > trainer2.pokemon1.hp:
                    score = score +1
                    battleround = 1
                else:
                    score = score
                    battleround = 1


        if keys [pg.K_p] == True:
            if score == 0:
                mode = 3
            else:
                mode = 2

        pg.draw.ellipse(screen, blue, (mx,my,10,10))
        print(score)
        print(battleround)


        pg.display.flip()

        #5. CLOCK
        #Set how many frame per second the game will run at
        clock.tick(30)
        old_space = keys[pg.K_SPACE]







    while mode == 2:
        battleround = 0
        pg.event.pump()
        #1. UPDATES
        #Move objects to new locations based on speed



        #2. INPUTS
        #Check all input devices (Ex: Keyboard / Mouse)

        keys = pg.key.get_pressed()
        mx, my = pg.mouse.get_pos()
        L,M,R = pg.mouse.get_pressed()

        #3. EVENTS
        #Set of if-statements for different events of interest (Ex. Objects colliding, moving off screen etc.)


        #4. DRAWING
        #Draw the current state of everything in the game (frame)
        screen.blit(win1,(0,0))

        if  keys[pg.K_SPACE] == True:
            mode = 0


        pg.draw.ellipse(screen, blue, (mx,my,10,10))
        print(mx)
        print(my)


        pg.display.flip()

        #5. CLOCK
        #Set how many frame per second the game will run at
        clock.tick(30)



    while mode == 3  :
        battleround = 0
        pg.event.pump()
        #1. UPDATES
        #Move objects to new locations based on speed



        #2. INPUTS
        #Check all input devices (Ex: Keyboard / Mouse)

        keys = pg.key.get_pressed()
        mx, my = pg.mouse.get_pos()
        L,M,R = pg.mouse.get_pressed()

        #3. EVENTS
        #Set of if-statements for different events of interest (Ex. Objects colliding, moving off screen etc.)


        #4. DRAWING
        #Draw the current state of everything in the game (frame)
        screen.blit(lose,(0,0))

        if  keys[pg.K_SPACE] == True:
            mode = 0
            t1 = 1
            t2 = 1
            t3 = 1
            trainer1.hitbox[0] = 850
            trainer1.hitbox[1] = 750

        pg.draw.ellipse(screen, blue, (mx,my,10,10))
        print(mx)
        print(my)




        pg.display.flip()

        #5. CLOCK
        #Set how many frame per second the game will run at
        clock.tick(30)

    while mode == 4:
        pg.event.pump()
        #1. UPDATES
        #Move objects to new locations based on speed

        keys = pg.key.get_pressed()
        mx, my = pg.mouse.get_pos()
        L,M,R = pg.mouse.get_pressed()


        #2. INPUTS
        #Check all input devices (Ex: Keyboard / Mouse)

        if  keys[pg.K_SPACE] == True:
            mode = 0

        #3. EVENTS
        #Set of if-statements for different events of interest (Ex. Objects colliding, moving off screen etc.)


        #4. DRAWING
        #Draw the current state of everything in the game (frame)
        screen.blit(startscreen,(0,0))




        pg.display.flip()

        #5. CLOCK
        #Set how many frame per second the game will run at
        clock.tick(30)