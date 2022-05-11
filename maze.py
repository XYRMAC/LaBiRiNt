#создай игру "Лабиринт"!
from pygame import *
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (65, 65))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < win_width - 80:
            self.rect.x += self.speed
        if keys[K_UP] and self.rect.y < win_width > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 80:
            self.rect.y += self.speed

class Enemy(GameSprite):
    direction = "left"
    def update(self):
        if self.rect.x <= 470:
            self.direction = "right"
        if self.rect.x >= win_width - 85:
            self.direction = "left"

        if self.direction == "left":
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed    

class Wall(sprite.Sprite):
   def __init__(self, color_1, color_2, color_3, wall_x, wall_y, wall_width, wall_height):
       super().__init__()
       self.color_1 = color_1
       self.color_2 = color_2
       self.color_3 = color_3
       self.width = wall_width
       self.height = wall_height
       # картинка стены - прямоугольник нужных размеров и цвета
       self.image = Surface((self.width, self.height))
       self.image.fill((color_1, color_2, color_3))
       # каждый спрайт должен хранить свойство rect - прямоугольник
       self.rect = self.image.get_rect()
       self.rect.x = wall_x
       self.rect.y = wall_y
   def draw_wall(self):
       window.blit(self.image, (self.rect.x, self.rect.y))

window = display.set_mode((700, 500))
display.set_caption("Лабиринт")
background = transform.scale(image.load("beach.jpg"), (700, 500))

win_height = 500
win_width = 700
player = Player("4844788.png", 5, win_height - 80, 4)
KYBA = Enemy("Kat.png", 5, win_height - 160, 4)
COKPOBISCHE = GameSprite("treasure.png", 5, win_height - 400, -70)
w1 = Wall(154, 205, 50, 100, 20, 450, 10)
w3 = Wall(164, 75, 50, 100, 300, 15, 38)
w4 = Wall(154, 75, 50, 150, 150, 15, 60)
w2 = Wall(154, 205, 50, 50, 240, 350, 10)

game = True
finish = False
clock = time.Clock()
FPS = 60
mixer.init()
#mixer.music.load("Катюша - Кадышева Надежда _ Золотое кольцо - backingtrackx.com.mp3")
#mixer.music.play()
money = mixer.Sound("kick.ogg")
kick = mixer.Sound("kick.ogg")

font.init()
font = font.SysFont("Arial", 70)
win = font.render("YOU WIN!", True, (255, 215, 0))
lose = font.render("YOU LOSE!", True, (255, 215, 0))



while game:
    for e in event.get():
        if e.type == QUIT:
            game = False


    if finish != True:
        window.blit(background,(0, 0))
        player.update()
        KYBA.update()
        player.reset()
        KYBA.reset()
        COKPOBISCHE.reset()

        w1.draw_wall()
        w2.draw_wall()
        w3.draw_wall()
        w4.draw_wall()

        if sprite.collide_rect(player, COKPOBISCHE):
            window.blit(win, (200, 200))
            finish = True
            money.play()
        
        if sprite.collide_rect(player, KYBA) or sprite.collide_rect(player, w1) or sprite.collide_rect(player, w2) or sprite.collide_rect(player, w3):
            finish = True
            window.blit(lose, (200, 200))
            kick.play()



    display.update()
    clock.tick(FPS)

