import pygame
from pygame.locals import *
import random

pygame.init()
pygame.font.init()

screen_width = 1400
screen_height = 1000

screen = pygame.display.set_mode((screen_width,screen_height))
title = pygame.display.set_caption("Space shooter")

icon = pygame.image.load('assets/icon.png')
pygame.display.set_icon(icon)

bg = pygame.image.load('assets/bg.png').convert()
bg = pygame.transform.scale(bg,(screen_width,screen_height))

clock = pygame.time.Clock()

health = 70
score = 0

class CrPlayer(pygame.sprite.Sprite):
    def __init__(self):
        super(CrPlayer, self).__init__()
        self.surf = pygame.image.load("assets/shooter rocket.png").convert_alpha()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.surf.get_rect()

    def update(self, pressed_keys):
        if pressed_keys[K_w]:
            self.rect.move_ip(0, -2)
        if pressed_keys[K_s]:
            self.rect.move_ip(0, 2)
        if pressed_keys[K_a]:
            self.rect.move_ip(-2, 0)
        if pressed_keys[K_d]:
            self.rect.move_ip(2, 0)
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > screen_width:
            self.rect.right = screen_width
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= screen_height:
            self.rect.bottom = screen_height

class CrEnemy(pygame.sprite.Sprite):
    def __init__(self):
        super(CrEnemy, self).__init__()
        self.surf = pygame.image.load("assets/shooter enemy.png").convert_alpha()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.surf.get_rect(
            center = (random.randint(screen_width + 20, screen_width + 100), random.randint(0, screen_height)))
        self.speed = random.randint(1,3)

    def update(self):
        self.rect.move_ip(-self.speed, 0)
        if self.rect.right < 0:
            self.kill()

class CrMeteor(pygame.sprite.Sprite):
    def __init__(self):
        super(CrMeteor, self).__init__()
        self.surf = pygame.image.load("assets/meteor for SpaceShooterGame.png").convert_alpha()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.surf.get_rect(
            center = (random.randint(screen_width + 20, screen_width + 100), random.randint(0, screen_height)))
        self.speed = random.randint(1,2)

    def update(self):
        self.rect.move_ip(-self.speed, 0)
        if self.rect.right < 0:
            self.kill()

class CrCrystal(pygame.sprite.Sprite):
    def __init__(self):
        super(CrCrystal, self).__init__()
        self.surf = pygame.image.load("assets/crystal for ssg.png").convert_alpha()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.surf.get_rect(
            center = (random.randint(screen_width + 20, screen_width + 100), random.randint(0, screen_height)))
        self.speed = 2.5

    def update(self):
        self.rect.move_ip(-self.speed, 0)
        if self.rect.right < 0:
            self.kill()

class CrSuperCrystal(pygame.sprite.Sprite):
    def __init__(self):
        super(CrSuperCrystal, self).__init__()
        self.surf = pygame.image.load("assets/supercrystal for ssg.png").convert_alpha()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.surf.get_rect(
            center = (random.randint(screen_width + 20, screen_width + 100), random.randint(0, screen_height)))
        self.speed = 3.5

    def update(self):
        self.rect.move_ip(-self.speed, 0)
        if self.rect.right < 0:
            self.kill()

class CrUltraCrystal(pygame.sprite.Sprite):
    def __init__(self):
        super(CrUltraCrystal, self).__init__()
        self.surf = pygame.image.load("assets/ultracrystal.png").convert_alpha()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.surf.get_rect(
            center = (random.randint(screen_width + 20, screen_width + 100), random.randint(0, screen_height)))
        self.speed = 3.5

    def update(self):
        self.rect.move_ip(-self.speed, 0)
        if self.rect.right < 0:
            self.kill()

class CrUltraSuperCrystal(pygame.sprite.Sprite):
    def __init__(self):
        super(CrUltraSuperCrystal, self).__init__()
        self.surf = pygame.image.load("assets/ultrasupercrystal.png").convert_alpha()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.surf.get_rect(
            center = (random.randint(screen_width + 20, screen_width + 100), random.randint(0, screen_height)))
        self.speed = 3.5

    def update(self):
        self.rect.move_ip(-self.speed, 0)
        if self.rect.right < 0:
            self.kill()

class CrUltraMaxCrystal(pygame.sprite.Sprite):
    def __init__(self):
        super(CrUltraMaxCrystal, self).__init__()
        self.surf = pygame.image.load("assets/ultramaxcrystal.png").convert_alpha()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.surf.get_rect(
            center = (random.randint(screen_width + 20, screen_width + 100), random.randint(0, screen_height)))
        self.speed = 3.5

    def update(self):
        self.rect.move_ip(-self.speed, 0)
        if self.rect.right < 0:
            self.kill()

class CrCoin(pygame.sprite.Sprite):
    def __init__(self):
        super(CrCoin, self).__init__()
        self.surf = pygame.image.load("assets/coin for ssg.png").convert_alpha()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.surf.get_rect(
            center = (random.randint(screen_width + 20, screen_width + 100), random.randint(0, screen_height)))
        self.speed = 3.5

    def update(self):
        self.rect.move_ip(-self.speed, 0)
        if self.rect.right < 0:
            self.kill()


Player = CrPlayer()
all_s = pygame.sprite.Group()
all_s.add(Player)
enemies = pygame.sprite.Group()
meteors = pygame.sprite.Group()
crystals = pygame.sprite.Group()
super_crystals = pygame.sprite.Group()
ultra_crystals = pygame.sprite.Group()
ultra_super_crystals = pygame.sprite.Group()
ultra_max_crystals = pygame.sprite.Group()
coins = pygame.sprite.Group()

AddEnemy = pygame.USEREVENT + 1
pygame.time.set_timer(AddEnemy, 1200)

AddMeteor = pygame.USEREVENT + 2
pygame.time.set_timer(AddMeteor, 3000)

AddCrystal = pygame.USEREVENT + 3
pygame.time.set_timer(AddCrystal, 5000)

AddSuperCrystal = pygame.USEREVENT + 4
pygame.time.set_timer(AddSuperCrystal, 8000)

AddUltraCrystal = pygame.USEREVENT + 5
pygame.time.set_timer(AddUltraCrystal, 20000)

AddUltraSuperCrystal = pygame.USEREVENT + 6
pygame.time.set_timer(AddUltraSuperCrystal, 60000)

AddUltraMaxCrystal = pygame.USEREVENT + 7
pygame.time.set_timer(AddUltraMaxCrystal, 300000)

AddCoin = pygame.USEREVENT + 8
pygame.time.set_timer(AddCoin, 10000)

run = True

health_font = pygame.font.SysFont("Unispace", 60, bold=True)

gameOver = pygame.font.SysFont("Unispace", 200, bold=True)
gameOver_surface = gameOver.render(f"GAME OVER", True, (255, 255, 255))

gameOverScore = pygame.font.SysFont("Unispace", 100, bold=True)
gameOverScore_surface = gameOverScore.render(f"Final Score: {score}", True, (255, 255, 255))

score_font = pygame.font.SysFont("Unispace", 70, bold=True)
score_surface = score_font.render(f"Score: {score}", True, (255, 255, 255))

def game_over():
    global score

    gameOverScore_surface = gameOverScore.render(f"Final Score: {score}", True, (255, 255, 255))

    screen.blit(gameOver_surface, (300, 320))
    screen.blit(gameOverScore_surface, (450, 500))

    pygame.display.update()
    pygame.time.delay(5000)

def crupdate_score():
    global score
    global score_surface

    score += 10

    score_surface = score_font.render(f"Score: {score}", True, (255, 255, 255))

def scrupdate_score():
    global score
    global score_surface

    score += 20

    score_surface = score_font.render(f"Score: {score}", True, (255, 255, 255))

def ucrupdate_score():
    global score
    global score_surface

    score += 30

    score_surface = score_font.render(f"Score: {score}", True, (255, 255, 255))

def uscrupdate_score():
    global score
    global score_surface

    score += 50

    score_surface = score_font.render(f"Score: {score}", True, (255, 255, 255))

def umcrupdate_score():
    global score
    global score_surface

    score += 75

    score_surface = score_font.render(f"Score: {score}", True, (255, 255, 255))

def coins_update_score():
    global score
    global score_surface

    score += 15

    score_surface = score_font.render(f"Score: {score}", True, (255, 255, 255))

while run:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                run = False
            if event.key == K_x:
                run  = False
        elif event.type == QUIT:
            run = False


        elif event.type == AddEnemy:
            new_enemy = CrEnemy()
            enemies.add(new_enemy)
            all_s.add(new_enemy)

        elif event.type == AddMeteor:
            new_meteor = CrMeteor()
            meteors.add(new_meteor)
            all_s.add(new_meteor)

        elif event.type == AddCrystal:
            new_crystal = CrCrystal()
            crystals.add(new_crystal)
            all_s.add(new_crystal)

        elif event.type == AddSuperCrystal:
            new_super_crystal = CrSuperCrystal()
            super_crystals.add(new_super_crystal)
            all_s.add(new_super_crystal)

        elif event.type == AddUltraCrystal:
            new_ultra_crystal = CrUltraCrystal()
            ultra_crystals.add(new_ultra_crystal)
            all_s.add(new_ultra_crystal)

        elif event.type == AddUltraSuperCrystal:
            new_ultra_super_crystal = CrUltraSuperCrystal()
            ultra_super_crystals.add(new_ultra_super_crystal)
            all_s.add(new_ultra_super_crystal)

        elif event.type == AddUltraMaxCrystal:
            new_ultra_max_crystal = CrUltraMaxCrystal()
            ultra_max_crystals.add(new_ultra_max_crystal)
            all_s.add(new_ultra_max_crystal)

        elif event.type == AddCoin:
            new_coins = CrCoin()
            coins.add(new_coins)
            all_s.add(new_coins)

    pressed_keys = pygame.key.get_pressed()
    Player.update(pressed_keys)
    enemies.update()
    meteors.update()
    crystals.update()
    super_crystals.update()
    ultra_crystals.update()
    ultra_super_crystals.update()
    ultra_max_crystals.update()
    coins.update()

    if pygame.sprite.spritecollideany(Player, enemies):
        en = pygame.sprite.spritecollideany(Player, enemies)
        en.kill()
        health -= 5

    if pygame.sprite.spritecollideany(Player, meteors):
        me = pygame.sprite.spritecollideany(Player, meteors)
        me.kill()
        health -= 10

    if pygame.sprite.spritecollideany(Player, crystals):
        cr = pygame.sprite.spritecollideany(Player, crystals)
        cr.kill()
        health += 5
        crupdate_score()

    if pygame.sprite.spritecollideany(Player, super_crystals):
        scr = pygame.sprite.spritecollideany(Player, super_crystals)
        scr.kill()
        health += 10
        scrupdate_score()

    if pygame.sprite.spritecollideany(Player, ultra_crystals):
        ucr = pygame.sprite.spritecollideany(Player, ultra_crystals)
        ucr.kill()
        health += 20
        ucrupdate_score()

    if pygame.sprite.spritecollideany(Player, ultra_super_crystals):
        uscr = pygame.sprite.spritecollideany(Player, ultra_super_crystals)
        uscr.kill()
        health += 50
        uscrupdate_score()

    if pygame.sprite.spritecollideany(Player, ultra_max_crystals):
        umcr = pygame.sprite.spritecollideany(Player, ultra_max_crystals)
        umcr.kill()
        health += 75
        umcrupdate_score()

    if pygame.sprite.spritecollideany(Player, coins):
        coin = pygame.sprite.spritecollideany(Player, coins)
        coin.kill()
        health += 50
        coins_update_score()

    if health <= 0:
        game_over()
        run = False

    screen.blit(bg, (0, 0))
    for entity in all_s:
        screen.blit(entity.surf, entity.rect)

    health_surface = health_font.render(f"HEALTH: {health}", True, (255, 255, 255))
    screen.blit(health_surface, (1000, 900))

    score_surface = score_font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(score_surface, (700, 900))

    clock.tick(256)
    pygame.display.flip()
