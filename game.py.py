import os
import pygame
import random

pygame.init()

tab_height = 600
tab_width = 1100

window = pygame.display.set_mode((tab_width,tab_height))

jump = pygame.image.load(r'C:\Users\HP\Desktop\Py\DinoJump.png')

duck = [pygame.image.load(r'C:\Users\HP\Desktop\Py\DinoDuck1.png'),
            pygame.image.load(r'C:\Users\HP\Desktop\Py\DinoDuck2.png')]

run = [pygame.image.load(r'C:\Users\HP\Desktop\Py\Dinoduringrun1.png'),
       pygame.image.load(r'C:\Users\HP\Desktop\Py\Dinoduringrun2.png')]

trap_obs = [pygame.image.load(r'C:\Users\HP\Desktop\Py\Trap1.jpg'),pygame.image.load(r'C:\Users\HP\Desktop\Py\ss.png')]

small_cactus_obs = [pygame.image.load(r'C:\Users\HP\Desktop\Py\Small_Cactus_1.png'),
                    pygame.image.load(r'C:\Users\HP\Desktop\Py\Small_Cactus_2.png'),
                    pygame.image.load(r'C:\Users\HP\Desktop\Py\Small_Cactus_3.png')]

big_cactus_obs = [pygame.image.load(r'C:\Users\HP\Desktop\Py\Big_Cactus_1.png'),
                  pygame.image.load(r'C:\Users\HP\Desktop\Py\Big_Cactus_2.png'),
                  pygame.image.load(r'C:\Users\HP\Desktop\Py\Big_Cactus_3.png')]

cloud = pygame.image.load(r'C:\Users\HP\Desktop\Py\Cloud.png')

bird_obs = [pygame.image.load(r'C:\Users\HP\Desktop\Py\BirdWingUp.png'),
            pygame.image.load(r'C:\Users\HP\Desktop\Py\BirdWingDown.png')]

field_track = pygame.image.load(r'C:\Users\HP\Desktop\Py\TrackField.png')

extra_points = pygame.image.load(r'C:\Users\HP\Desktop\Py\100Points.jpg')

fast = pygame.image.load(r'C:\Users\HP\Desktop\Py\Fast.png')

bomb_obs = [pygame.image.load(r'C:\Users\HP\Desktop\Py\Bomb1.png'),
            pygame.image.load(r'C:\Users\HP\Desktop\Py\Bomb2.png')]

gameover = pygame.image.load(r'C:\Users\HP\Desktop\Py\GameOver.png')

class Obstacles:
    def __init__(self, img, type):
        self.image = img
        self.type = type
        self.rect = self.image[self.type].get_rect()
        self.rect.x = tab_width

    def update(self):
        self.rect.x -= speed
        if self.rect.x < -self.rect.width:
            obstacles.pop()

    def draw(self, window):
        window.blit(self.image[self.type], self.rect)


class Small_Cactus(Obstacles):
    def __init__(self, img):
        self.type = random.randint(0, 2)
        super().__init__(img, self.type)
        self.rect.y = 325


class Big_Cactus(Obstacles):
    def __init__(self, img):
        self.type = random.randint(0, 2)
        super().__init__(img, self.type)
        self.rect.y = 300

class Points():
    def __init__(self,img):
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.y = 325
        self.rect.x = tab_width+5000
    def update(self):
        self.rect.x -= speed
        if self.rect.x < -self.rect.width:
            point.pop()
    def draw(self,window):
        window.blit(self.image, self.rect)

class Fast():
    def __init__(self,img):
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.y = 325
        self.rect.x = tab_width+10000
    def update(self):
        self.rect.x -= speed
        if self.rect.x < -self.rect.width:
            speedlist.pop()
    def draw(self,window):
        window.blit(self.image, self.rect)

class Bird(Obstacles):

    def __init__(self, img):
        self.type = 0
        super().__init__(img, self.type)
        self.rect.y = 250
        self.count = 0

    def draw(self, window):
        if self.count >= 9:
            self.count = 0
        window.blit(self.image[self.count // 5], self.rect)
        self.count += 1

class Trap(Obstacles):

    def __init__(self,img):
        self.type = random.randint(0, 1)
        super().__init__(img, self.type)
        self.rect.y = 345

class Bomb(Obstacles):

    def __init__(self, img):
          self.type = random.randint(0, 1)
          super().__init__(img, self.type)
          self.rect.y = 335


class Cloud:
    def __init__(self):
        self.image = cloud
        self.x_pos = tab_width + random.randint(800, 1000)
        self.y_pos = random.randint(50, 100)
        self.width = self.image.get_width()

    def update(self):
        self.x_pos -= speed
        if self.x_pos < -self.width:
            self.x_pos = tab_width + random.randint(2500, 3000)
            self.y_pos = random.randint(50, 100)

    def draw(self, window):
        window.blit(self.image, (self.x_pos, self.y_pos))


class Dinosaur:
    x_pos = 80

    y_pos = 310

    duck_pos = 340

    velocity = 8.5

    def __init__(self):

        self.duck_img = duck

        self.run_img = run

        self.jump_img = jump

        self.dino_duck_pos = False

        self.dino_run_pos = True

        self.dino_jump_pos = False

        self.jump_vel = self.velocity

        self.count_index = 0

        self.image = self.run_img[0]

        self.dino_rect = self.image.get_rect()

        self.dino_rect.x = self.x_pos

        self.dino_rect.y = self.y_pos

    def update(self, userkeyinput):

        if self.dino_duck_pos:
            self.duckfunc()

        if self.dino_run_pos:
            self.dinorunfunc()

        if self.dino_jump_pos:
            self.dinojumpfunc()

        if self.count_index >= 10:
            self.count_index = 0

        if userkeyinput[pygame.K_UP] and not self.dino_jump_pos:
            self.dino_duck_pos = False
            self.dino_run_pos = False
            self.dino_jump_pos = True

        elif userkeyinput[pygame.K_DOWN] and not self.dino_jump_pos:
            self.dino_duck_pos = True
            self.dino_run_pos = False
            self.dino_jump_pos = False

        elif not (self.dino_jump_pos or userkeyinput[pygame.K_DOWN]):
            self.dino_duck_pos = False
            self.dino_run_pos = True
            self.dino_jump_pos = False

    def duckfunc(self):

            self.image = self.duck_img[self.count_index // 5]
            self.dino_rect = self.image.get_rect()
            self.dino_rect.x = self.x_pos
            self.dino_rect.y = self.duck_pos
            self.count_index += 1

    def dinorunfunc(self):

            self.image = self.run_img[self.count_index // 5]
            self.dino_rect = self.image.get_rect()
            self.dino_rect.x = self.x_pos
            self.dino_rect.y = self.y_pos
            self.count_index += 1

    def dinojumpfunc(self):

            self.image = self.jump_img
            if self.dino_jump_pos:
                self.dino_rect.y -= self.jump_vel * 4
                self.jump_vel -= 0.8

            if self.jump_vel < -self.velocity:
                self.dino_jump_pos = False
                self.jump_vel = self.velocity

    def draw(self, window):
            window.blit(self.image,(self.dino_rect.x, self.dino_rect.y))


def main():
    runtill = True

    pygame.display.set_caption('DINO RUN')

    time = pygame.time.Clock()

    global speed, x_cart_ft, y_cart_ft, score, obstacles,point,speedlist

    Dino_player = Dinosaur()

    cloud_obj = Cloud()

    speed = 20

    x_cart_ft = 0

    y_cart_ft = 380

    score = 0

    font = pygame.font.Font('freesansbold.ttf', 20)

    obstacles = []

    point = []

    speedlist = []

    death_count = 0

    def Scorefunc():
        global score, speed
        score += 1
        if score % 100 == 0:
            speed += 1
        text = font.render("Points : " + str(score), True, (0, 0, 0))
        textRect = text.get_rect()
        textRect.center = (1000, 40)
        window.blit(text, textRect)

    def fieldtrackfunc():
        global x_cart_ft, y_cart_ft
        img_width = field_track.get_width()
        window.blit(field_track, (x_cart_ft, y_cart_ft))
        window.blit(field_track, (img_width + x_cart_ft, y_cart_ft))
        if x_cart_ft <= -img_width:
            window.blit(field_track, (img_width + x_cart_ft, y_cart_ft))
            x_cart_ft = 0
        x_cart_ft -= speed

    while runtill:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                runtill = False
                pygame.quit()

        window.fill((255, 255, 255))

        userkeyinput = pygame.key.get_pressed()

        Dino_player.draw(window)

        Dino_player.update(userkeyinput)

        if len(obstacles) == 0:

            if random.randint(0, 5) == 0:
                obstacles.append(Small_Cactus(small_cactus_obs))
            elif random.randint(0, 5) == 1:
                obstacles.append(Big_Cactus(big_cactus_obs))
            elif random.randint(0, 5) == 2:
                obstacles.append(Bird(bird_obs))
            elif random.randint(0, 5) == 3 :
                obstacles.append(Trap(trap_obs))
            elif random.randint(0, 5) == 4 :
                obstacles.append(Bomb(bomb_obs))

        if len(point)==0:
            point.append(Points(extra_points))

        if len(speedlist)==0:
            speedlist.append(Fast(fast))
        for obstacle in obstacles:
            obstacle.draw(window)
            obstacle.update()
            point[0].draw(window)
            point[0].update()
            speedlist[0].draw(window)
            speedlist[0].update()
            if Dino_player.dino_rect.colliderect(obstacle.rect):
                pygame.time.delay(2000)
                death_count += 1
                menu(death_count)
            if len(point)!=0 and Dino_player.dino_rect.colliderect(point[0].rect):
                score+=100
                pygame.draw.rect(window,(255,0,0),Dino_player.dino_rect,2)

            if len(speedlist) != 0 and Dino_player.dino_rect.colliderect(speedlist[0].rect):
                speed += 1
                pygame.draw.rect(window, (255, 0, 0), Dino_player.dino_rect, 2)

        fieldtrackfunc()

        cloud_obj.draw(window)

        cloud_obj.update()

        Scorefunc()

        time.tick(30)

        pygame.display.update()


def menu(death_count):
    global score
    runn = True
    while runn:
        window.fill((255, 255, 255))
        font = pygame.font.Font('freesansbold.ttf', 30)

        if death_count == 0:
            text = font.render('Press any key to start ', True, (0, 0, 0))
        elif death_count > 0:
            text = font.render('Press any key to Restart ', True, (0, 0, 0))
            scores = font.render('Your Score  : ' + str(score), True, (0, 0, 0))
            scoresRect = scores.get_rect()
            scoresRect.center = (tab_width // 2, tab_height // 2 + 50)
            window.blit(scores, scoresRect)
            window.blit(gameover, (tab_width // 2 + 20, tab_height // 2 + 140))
        textRect = text.get_rect()
        textRect.center = (tab_width // 2, tab_height // 2 )
        window.blit(text, textRect)
        window.blit(run[0], (tab_width // 2 - 20, tab_height // 2 - 140))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                runn = False
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    runn = False
                    pygame.quit()
            if event.type == pygame.KEYDOWN:
                main()

menu(death_count=0)










