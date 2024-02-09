

import pygame
import random as rd
import sys
import os
pygame.init()

sound1 = pygame.mixer.Sound('oh.mp3')
sound2 = pygame.mixer.Sound('sound1.wav')


def load_image(name):
    fullname = os.path.join(name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    return image


screen_width = 600
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("SPACE INVADERS")


class Ship(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = load_image("ship.png")
        self.rect = self.image.get_rect(topleft=(175, 500))
        self.speed = 10
        self.mask = pygame.mask.from_surface(self.image)

    def update(self, keys):
        if keys == 'moveleft' and self.rect.x > 10:
            self.rect.x -= self.speed
        if keys == 'moveright' and self.rect.x < 540:
            self.rect.x += self.speed


class Heart(pygame.sprite.Sprite):
    def __init__(self, xpos, ypos):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(load_image("heart.png"), (35, 30))
        self.rect = self.image.get_rect(topleft=(xpos, ypos))

    def update(self):
        screen.blit(self.image, self.rect)


class Enemylaser(pygame.sprite.Sprite):
    def __init__(self, xpos, ypos):
        pygame.sprite.Sprite.__init__(self)
        self.image = load_image("laser11.png")
        self.rect = self.image.get_rect(topleft=(xpos, ypos))
        self.mask = pygame.mask.from_surface(self.image)

    def update(self):
        self.rect.y += 1
        if self.rect.y < 0 or self.rect.y > 600:
            self.kill()


class Laser(pygame.sprite.Sprite):

    def __init__(self, xpos, ypos):
        pygame.sprite.Sprite.__init__(self)
        self.image = load_image("laser.png")
        self.rect = self.image.get_rect(topleft=(xpos, ypos))
        self.mask = pygame.mask.from_surface(self.image)

    def update(self):
        self.rect.y -= 10
        if self.rect.y < 0 or self.rect.y > 600:
            self.kill()


class Alien(pygame.sprite.Sprite):
    def __init__(self, pic1, pic2):

        pygame.sprite.Sprite.__init__(self)
        self.directionway = "right"
        self.animlist = []
        self.animationcount = 1
        self.alien_sprites = pygame.sprite.Group()
        aliens = [pic1, pic2]

        alien1, alien2 = load_image(aliens[0]), load_image(aliens[1])
        self.animlist.append(pygame.transform.scale(alien1, (40, 35)))
        self.animlist.append(pygame.transform.scale(alien2, (40, 35)))
        self.image = aliens[self.animationcount]
        self.stop = 0
        self.mask = pygame.mask.from_surface(self.animlist[0])
        self.mask = pygame.mask.from_surface(self.animlist[1])

    def update(self, x=-1, y=-1):

        if x != -1:
            self.x = x

        if y != -1:
            self.y = y
        self.stop += 1
        if self.directionway == "right":
            if self.x <= 540:
                self.x += 1
            else:
                
                self.directionway = 'left'
        if self.directionway == "left":
            if self.x >= 60:
                self.x -= 1
            else:
                self.directionway = 'right'

        if self.stop == 50:
            self.animationcount += 1

            if self.animationcount > 1:
                self.animationcount = 0

            self.image = self.animlist[self.animationcount]
            self.rect = self.image.get_rect(topleft=(self.x, self.y))
            self.stop = 0
        else:
            self.image = self.animlist[self.animationcount]
            self.rect = self.image.get_rect(topleft=(self.x, self.y))


clock = pygame.time.Clock()
FPS = 144

star = Ship()


star.update(None)
aliengroup = pygame.sprite.Group()
enemylasergroup = pygame.sprite.Group()


def alienmaker(aliensquantity=1):
    if aliensquantity == 1:
        for i in aliengroup:
            i.kill()

        for i in enemylasergroup:
            i.kill()
        c = 30
        for i in range(8):
            alien = Alien("alien11.png", "alien12.png")
            alien2 = Alien("enemy1_1.png", "enemy1_2.png")
            alien3 = Alien("enemy1_1.png", "enemy1_2.png")
            alien4 = Alien("enemy3_1.png", "enemy3_2.png")
            alien.update(c, 50)
            alien2.update(c, 100)
            alien3.update(c, 150)
            alien4.update(c, 200)
            aliengroup.add(alien)
            aliengroup.add(alien2)
            aliengroup.add(alien3)
            aliengroup.add(alien4)
            c += 60
    elif aliensquantity == 2:
        for i in aliengroup:
            i.kill()

        for i in enemylasergroup:
            i.kill()
        c = 30
        for i in range(8):
            alien = Alien("alien11.png", "alien12.png")
            alien2 = Alien("enemy1_1.png", "enemy1_2.png")
            alien3 = Alien("enemy1_1.png", "enemy1_2.png")
            alien4 = Alien("enemy3_1.png", "enemy3_2.png")
            alien5 = Alien("alien11.png", "alien12.png")
            alien.update(c, 50)
            alien2.update(c, 100)
            alien3.update(c, 150)
            alien4.update(c, 200)
            alien5.update(c, 250)
            aliengroup.add(alien)
            aliengroup.add(alien2)
            aliengroup.add(alien3)
            aliengroup.add(alien4)
            aliengroup.add(alien5)
            c += 60


enemylaser = None

laser = None
lasergroup = pygame.sprite.Group()

heartsgroup = pygame.sprite.Group()

font = pygame.font.Font('fontx.ttf', 25)
text2 = font.render('LEVEL2', True, 'WHITE')


def heartmaker(hearts=1):
    if hearts == 1:
        for i in heartsgroup:
            i.kill()
        heartxpos = 10
        for i in range(1):
            heart = Heart(heartxpos, 560)
            heartsgroup.add(heart)
            heartsgroup.update()
            heartxpos += 40
    elif hearts == 3:
        for i in heartsgroup:
            i.kill()
        heartxpos = 10
        for i in range(3):
            heart = Heart(heartxpos, 560)
            heartsgroup.add(heart)
            heartsgroup.update()
            heartxpos += 40


bones = pygame.transform.scale(load_image('dead.png'), (100,  100))
back = pygame.transform.scale(load_image('background.jpg'), (600, 600))

font = pygame.font.Font('fontx.ttf', 35)
text1 = font.render('PRESS ANY KEY TO START', True, 'WHITE')
font2 = pygame.font.Font('fontx.ttf', 25)

leveltext1 = font2.render('LEVEL 1', True, 'WHITE')
leveltext2 = font2.render('LEVEL 2', True, 'WHITE')


def show_splash():
    # Показываем заставку
    running = True
    while running:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                exit()
            elif event.type == pygame.KEYDOWN:
                running = False

        startin_x_posistion_for_alien = 15
        algrp = pygame.sprite.Group()

        for i in range(20):
            alien = Alien("enemy1_1.png", "enemy1_1.png")
            alien.update(startin_x_posistion_for_alien, 300)
            algrp.add(alien)
            startin_x_posistion_for_alien += 60

        screen.blit(back, (0, 0))
        screen.blit(text1, (50, 200))
        algrp.draw(screen)
        algrp.update()
        pygame.display.update()
        clock.tick(FPS)


def play_level(level=1):
    star_state = 'stop'
    # running level 1
    if level == 1:
        heartmaker(hearts=3)
        alienmaker(aliensquantity=1)
    elif level == 2:
        heartmaker(hearts=1)
        alienmaker(aliensquantity=2)
    running = True
    while running:
        if len(heartsgroup) == 0:
            running = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    star_state = 'moveleft'
                elif event.key == pygame.K_d:
                    star_state = 'moveright'
                elif event.key == pygame.K_SPACE:
                    laser = Laser(star.rect.x+22, star.rect.y+5)
                    lasergroup.add(laser)
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_a:
                    star_state = 'stop'
                elif event.key == pygame.K_d:
                    star_state = 'stop'
            star.update(keys=star_state)

        # стреляем в чужих
        for alien in aliengroup:
            for laser in lasergroup:
                if pygame.sprite.collide_mask(laser, alien):
                    laser.kill()
                    alien.kill()
                    sound2.play()
                    break

        # стреляют чужие
        listrandom = list(range(1, 2000+1))

        for alien in aliengroup:
            if rd.choice(listrandom) == 8:
                enemylaser = Enemylaser(alien.rect.x+19, alien.rect.y-5)
                enemylasergroup.add(enemylaser)

        # проверка на попадание в корабль
        for enemylas in enemylasergroup:
            for redthing in heartsgroup:
                if pygame.sprite.collide_mask(enemylas, star):
                    enemylas.kill()
                    redthing.kill()
                    sound1.play()
                    break
        if not aliengroup:
            return 'dead'

        screen.blit(back, (0, 0))
        if level == 1:
            screen.blit(leveltext1, (480, 10))
        elif level == 2:
            screen.blit(leveltext2, (480, 10))
        aliengroup.update()
        enemylasergroup.update()
        lasergroup.update()
        heartsgroup.update()

        aliengroup.draw(screen)
        enemylasergroup.draw(screen)
        lasergroup.draw(screen)
        heartsgroup.draw(screen)
        screen.blit(star.image, star.rect)
        pygame.display.update()
        clock.tick(FPS)


def show_dead_screen():
    # заставка смерти
    fontxx = pygame.font.Font('fontx.ttf', 35)
    text3 = fontxx.render("YOU'RE DEAD!", True, 'RED')
    text4 = fontxx.render('PRESS ANY KEY TO RESTART', True, 'WHITE')
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            elif event.type == pygame.KEYDOWN:
                return

        screen.blit(back, (0, 0))
        screen.blit(text3, (160, 200))
        screen.blit(bones, (230, 250))
        screen.blit(text4, (30, 360))
        pygame.display.update()
        clock.tick(FPS)


trophy = load_image('mystery.png')


def winscreen():
    fontxx = pygame.font.Font('fontx.ttf', 25)
    text3 = fontxx.render("You completed space invaders!", True, 'GREEN')
    text6 = fontxx.render('PRESS ANY KEY TO PLAY AGAIN', True, 'GREEN')
    xpos = 200
    ypos = 250

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            elif event.type == pygame.KEYDOWN:
                return

        screen.blit(back, (0, 0))
        screen.blit(text3, (60, 200))
        screen.blit(text6, (60, 400))
        screen.blit(trophy, (xpos, ypos))
        pygame.display.update()
        clock.tick(FPS)


show_splash()
while True:

    deadscreen = True
    playlevelmain = play_level(level=1)
    if playlevelmain == 'dead':
        playlevel2main = play_level(level=2)
        if playlevel2main == 'dead':
            winscreen()
            deadscreen = False
    if deadscreen is True:
        show_dead_screen()