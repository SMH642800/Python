import pygame
from pygame.sprite import Group
import random
import os   # 對應不同的os

FPS = 60
WIDTH = 500
HEIGHT = 600

DARK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
# RED = (255, 0, 0)
# BLUE = (0, 0, 255)
# YELLOW = (255, 255, 0)

# 遊戲初始化 & 創建視窗
pygame.init()
pygame.mixer.init()   # 音效初始化
screen = pygame.display.set_mode((WIDTH, HEIGHT))
# 更改標題名稱
pygame.display.set_caption('第一個遊戲')
# 頻率，確保每台電腦運作遊戲，遊玩體驗是一致的
clock = pygame.time.Clock()

# 載入圖片
background_img = pygame.image.load(os.path.join('img', 'background.png')).convert()   # 背景
player_img = pygame.image.load(os.path.join('img', 'player.png')).convert()   # 太空船
enemy_img = pygame.image.load(os.path.join('img', 'enemy.png')).convert()   # 敵人
player_mini_img = pygame.transform.scale(player_img, (25, 19))   # 剩餘次數 (小張的太空船)
player_mini_img.set_colorkey(DARK)
pygame.display.set_icon(player_mini_img)   # 更改視窗標題的圖示
# rock_img = pygame.image.load(os.path.join('img', 'rock.png')).convert()
bullet_img = pygame.image.load(os.path.join('img', 'bullet.png')).convert()   # 子彈
rocket_img_before = pygame.image.load(os.path.join('img', 'rocket.png')).convert()   # 火箭 (原檔案)
rocket_img = pygame.transform.scale(rocket_img_before, (49, 54))   # 火箭 (修改後)
rock_imgs = []   # 石頭
for i in range(7):
    rock_imgs.append(pygame.image.load(os.path.join('img', f'rock{i}.png')).convert())
explosion_animation = {}   # 爆炸動畫
explosion_animation['very_large'] = []
explosion_animation['large'] = []
explosion_animation['small'] = []
explosion_animation['player'] = []
for i in range(9):
    explosion_img = pygame.image.load(os.path.join('img', f'expl{i}.png')).convert()
    explosion_img.set_colorkey(DARK)
    explosion_animation['very_large'].append(explosion_img)  # 超大爆炸
    explosion_animation['large'].append(pygame.transform.scale(explosion_img, (75, 75)))   # 大爆炸
    explosion_animation['small'].append(pygame.transform.scale(explosion_img, (30, 30)))   # 小爆炸
    player_explosion_img = pygame.image.load(os.path.join('img', f'player_expl{i}.png')).convert()
    player_explosion_img.set_colorkey(DARK)
    explosion_animation['player'].append(player_explosion_img)   # 太空船爆炸
power_imgs = {}   # 寶物掉落
power_imgs['shield'] = pygame.image.load(os.path.join('img', 'shield.png')).convert()
power_imgs['gun'] = pygame.image.load(os.path.join('img', 'gun.png')).convert()


# 載入音樂、音效
shoot_sound = pygame.mixer.Sound(os.path.join('sound', 'shoot.wav'))   # 載入射擊音效
gun_sound = pygame.mixer.Sound(os.path.join('sound', 'pow1.wav'))   # 吃到增加攻擊力的音效
shield_sound = pygame.mixer.Sound(os.path.join('sound', 'pow0.wav'))   # 吃到shield的音效
die_sound = pygame.mixer.Sound(os.path.join('sound', 'rumble.ogg'))   # 玩家死亡音效
explosion_sounds = [
    # 載入石頭爆炸音效
    pygame.mixer.Sound(os.path.join('sound', 'expl0.wav')),
    pygame.mixer.Sound(os.path.join('sound', 'expl1.wav'))
]
pygame.mixer.music.load(os.path.join('sound', 'background.ogg'))   # 載入遊戲背景音樂
pygame.mixer.music.set_volume(0.5)   # 把背景音樂的音量調小


# font_name = pygame.font.match_font('arial')   # 使用"arial"字體
font_name = os.path.join('font.ttf')


# 載入文字
def draw_text(surf, text, size, x, y):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, WHITE)   # 文字渲染
    text_rect = text_surface.get_rect()   # 文字定位
    text_rect.centerx = x
    text_rect.top = y
    surf.blit(text_surface, text_rect)


# 新增石頭
def new_rock():
    rock = Rock()
    all_sprites.add(rock)
    rocks.add(rock)


# 新增敵人
def new_enemy():
    enemy = Enemy()
    all_sprites.add(enemy)
    enemys.add(enemy)


# 載入血量
def draw_health(surf, hp, x, y):
    if hp < 0:
        hp = 0
    # 血量條的長、高
    BAR_LENGTH = 200
    BAR_HEIGHT = 10
    fill = (hp/200) * BAR_LENGTH   # 血量百分比
    outline_rect = pygame.Rect(x, y, BAR_LENGTH, BAR_HEIGHT)   # 血量條外框位置
    fill_rect = pygame.Rect(x, y, fill, BAR_HEIGHT)   # 血量條顏色填充位置
    pygame.draw.rect(surf, GREEN, fill_rect)   # 血量條顏色
    pygame.draw.rect(surf, WHITE, outline_rect, 2)   # 血量條外框


# 載入剩餘次數
def draw_lives(surf, lives, img, x, y):
    for i in range(lives):
        img_rect = img.get_rect()
        img_rect.x = x + 30*i
        img_rect.y = y
        surf.blit(img, img_rect)


# 載入初始畫面
def draw_init():
    screen.blit(background_img, (0, 0))
    draw_text(screen, '太空生存戰', 64, WIDTH/2, HEIGHT/4)
    draw_text(screen, '← → : 左右移動太空船，↑ ↓ : 上下移動太空船', 22, WIDTH / 2, HEIGHT / 2 - 15)
    draw_text(screen, '空白鍵 : 發射子彈、R鍵 : 發射火箭', 22, WIDTH / 2, HEIGHT / 2 + 11)
    draw_text(screen, '案任意鍵開始遊戲', 18, WIDTH / 2, HEIGHT * 3/4)
    pygame.display.update()
    waiting = True
    while waiting:
        clock.tick(FPS)
        # 取得輸入
        for event in pygame.event.get():
            # 當event是關閉視窗時，停止運作
            if event.type == pygame.QUIT:
                pygame.quit()
                return True
            # 當event是按下按鍵後，跳出迴圈，開始遊戲
            elif event.type == pygame.KEYUP:
                waiting = False
                return False


# 建立Player class，繼承pygame的sprite class
class Player(pygame.sprite.Sprite):
    # 初始化
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(player_img, (50, 38))   # 顯示太空船
        self.image.set_colorkey(DARK)   # 消除載入圖片後黑色的區塊
        self.rect = self.image.get_rect()   # 定位太空船
        self.radius = 20   # 碰種判斷區域大小 (圓形)
        # pygame.draw.circle(self.image, RED, self.rect.center, self.radius)
        self.rect.centerx = WIDTH/2
        self.rect.bottom = HEIGHT - 10
        self.speedx = 8   # 設定太空船橫移速度
        self.speedy = 5   # 設定太空船縱移速度
        self.health = 200   # 太空船生命值
        self.lives = 3   # 太空船生命次數
        self.hidden = False   # 判斷太空船是否在隱藏中
        self.hide_time = 0   # 隱藏時間
        self.gun = 1   # 太空船一開始的攻擊力
        self.gun_time = 0   # 吃到gun之後持續的時間
        self.score = 0   # 目前分數
        self.pre_score = 0   # 記錄前一個級距的分數

    def update(self):
        now = pygame.time.get_ticks()   # 現在的時間

        # 吃到寶物增加攻擊力持續的時間
        if self.gun > 1 and now - self.gun_time > 5000:   # 增加攻擊力持續5秒後
            self.gun -= 1
            self.gun_time = now

        # 太空船顯示出來
        if self.hidden and (now - self.hide_time) > 1000:   # 當hidden時間已超過n毫秒
            self.hidden = False
            self.rect.centerx = WIDTH / 2
            self.rect.bottom = HEIGHT - 10

        # 擷取鍵盤按鍵的動作
        key_pressed = pygame.key.get_pressed()
        if key_pressed[pygame.K_RIGHT]:
            self.rect.x += self.speedx
        if key_pressed[pygame.K_LEFT]:
            self.rect.x -= self.speedx
        if key_pressed[pygame.K_UP]:
            self.rect.y -= self.speedy
        if key_pressed[pygame.K_DOWN]:
            self.rect.y += self.speedy

        # 判斷太空船是否超出視窗界線，若超出則不再移動
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.top < 10:
            self.rect.top = 10
        if self.rect.bottom > HEIGHT - 10 and self.hidden is False:   # 若超出下方界線 & 不是hidden狀態
            self.rect.bottom = HEIGHT - 10

    # 子彈射擊動作
    def shoot_bullet(self):
        if not(self.hidden):
            # 根據目前的攻擊力來判斷射出子彈的數量
            if self.gun == 1:
                bullet = Bullet(self.rect.centerx, self.rect.top)
                all_sprites.add(bullet)
                bullets.add(bullet)
                shoot_sound.play()
            elif self.gun == 2:
                bullet1 = Bullet(self.rect.left, self.rect.centery)
                bullet2 = Bullet(self.rect.right, self.rect.centery)
                all_sprites.add(bullet1)
                all_sprites.add(bullet2)
                bullets.add(bullet1)
                bullets.add(bullet2)
                shoot_sound.play()
            elif self.gun >= 3:
                bullet1 = Bullet(self.rect.left-10, self.rect.centery)
                bullet2 = Bullet(self.rect.right+10, self.rect.centery)
                bullet3 = Bullet(self.rect.centerx, self.rect.top)
                all_sprites.add(bullet1)
                all_sprites.add(bullet2)
                all_sprites.add(bullet3)
                bullets.add(bullet1)
                bullets.add(bullet2)
                bullets.add(bullet3)
                shoot_sound.play()

    # 火箭射擊動作
    def shoot_rocket(self):
        if not (self.hidden):
            rocket = Rocket(self.rect.centerx, self.rect.top)
            all_sprites.add(rocket)
            rockets.add(rocket)
            shoot_sound.play()

    # 太空船死亡後，復活前一段時間內，太空船先隱藏起來
    def hide(self):
        self.hidden = True
        self.hide_time = pygame.time.get_ticks()
        self.rect.center = (WIDTH/2, HEIGHT+500)

    # 當太空船吃到gun時
    def gunup(self):
        self.gun += 1
        self.gun_time = pygame.time.get_ticks()


# 建立Rocks class，繼承pygame的sprite class
class Rock(pygame.sprite.Sprite):
    # 初始化
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image_original = random.choice(rock_imgs)   # 顯示石頭原始圖片狀態
        self.image_original.set_colorkey(DARK)   # 消除載入圖片後黑色的區塊
        self.image = self.image_original.copy()
        self.rect = self.image.get_rect()  # 定位石頭
        self.radius = int(self.rect.width * 0.85 / 2)     # 碰種判斷區域大小 (圓形)
        # pygame.draw.circle(self.image, RED, self.rect.center, self.radius)
        self.rect.x = random.randrange(0, WIDTH - self.rect.width)   # width_random_position = random (視窗寬度 - 石頭寬度)
        self.rect.y = random.randrange(-180, -100)   # (在 y=-180 ~ -100 之間生成rocks)
        self.speedy = random.randrange(2, 8)   # rocks掉落速度隨機
        self.speedx = random.randrange(-3, 3)
        self.total_degree = 0   # 總共旋轉角度
        self.rotate_degree = random.randrange(-3, 3)   # 旋轉度數

    def rotate(self):
        self.total_degree += self.rotate_degree
        self.total_degree = self.total_degree % 360   # 超過360度，重製成0度
        self.image = pygame.transform.rotate(self.image_original, self.total_degree)
        center = self.rect.center
        self.rect = self.image.get_rect()
        self.rect.center = center

    def update(self):
        # 石頭旋轉
        self.rotate()

        # 石頭掉落
        self.rect.y += self.speedy
        self.rect.x += self.speedx

        # 判斷石頭是否超出視窗界線，若超出則重置位置
        if self.rect.top > HEIGHT or self.rect.left > WIDTH or self.rect.right < 0:
            self.rect.x = random.randrange(0, WIDTH - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            self.speedy = random.randrange(2, 10)
            self.speedx = random.randrange(-3, 3)


# 建立Enemy class，繼承pygame的sprite class
class Enemy(pygame.sprite.Sprite):
    # 初始化
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(enemy_img, (90, 67))  # 顯示敵人
        self.image.set_colorkey(DARK)  # 消除載入圖片後黑色的區塊
        self.rect = self.image.get_rect()  # 定位敵人
        self.radius = int(self.rect.width * 0.85 / 2)  # 碰種判斷區域大小 (圓形)
        # pygame.draw.circle(self.image, RED, self.rect.center, self.radius)
        self.rect.x = random.randrange(0, WIDTH - self.rect.width)  # width_random_position = random (視窗寬度 - 石頭寬度)
        self.rect.y = random.randrange(-120, -80)  # (在 y=-180 ~ -100 之間生成rocks)
        self.speedy = 3 # rocks掉落速度隨機
        self.speedx = random.randrange(-2, 2) # rocks掉落速度隨機
        self.health = 20  # 敵人生命值
        self.shoot_time = 0

    def update(self):
        now = pygame.time.get_ticks()  # 現在的時間

        # 敵人掉落
        self.rect.y += self.speedy
        self.rect.x += self.speedx

        # 判斷敵人是否超出視窗界線，若超出則重置位置
        if self.rect.top > HEIGHT or self.rect.left > WIDTH or self.rect.right < 0:
            self.rect.x = random.randrange(0, WIDTH - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            self.speedy = 3
            self.speedx = random.randrange(-2, 2)

    # 敵人子彈射擊
    def shoot_bullet(self, player):
        now = pygame.time.get_ticks()  # 現在的時間

        if player.score - player.pre_score >= 1000:
            player.pre_score += 1000
            # if EnemyCommonSetting.shoot_gap_time == 0:
            #     EnemyCommonSetting.shoot_gap_time = 0
            # else:
            #    EnemyCommonSetting.shoot_gap_time -= 100
            EnemyCommonSetting.shoot_gap_time = max(EnemyCommonSetting.shoot_gap_time - 100, 0)

        print(EnemyCommonSetting.shoot_gap_time, player.score, player.pre_score)

        if now - self.shoot_time > EnemyCommonSetting.shoot_gap_time:   # 敵人子彈發射的時間間隔
            bullet1 = Enemy_Bullet(self.rect.centerx, self.rect.top)
            all_sprites.add(bullet1)
            enemy_bullets.add(bullet1)
            self.shoot_time = now


# 建立Enemy_bullet class，繼承pygame的sprite class
class Enemy_Bullet(pygame.sprite.Sprite):
    # 初始化
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = bullet_img  # 顯示bullet
        self.image.set_colorkey(DARK)    # 消除載入圖片後黑色的區塊
        self.rect = self.image.get_rect()  # 定位bullet
        self.rect.centerx = x
        self.rect.bottom = y
        self.speedy = 10   # 子彈速度
        self.radius = int(self.rect.width)

    def update(self):
        # 子彈射出
        self.rect.y += self.speedy

        # 判斷bullet是否超出視窗界線，若超出則delete
        if self.rect.top > HEIGHT:
            self.kill()


class EnemyCommonSetting:
    shoot_gap_time = 1000   # 設籍時間間隔為1秒


# 建立Bullet class，繼承pygame的sprite class
class Bullet(pygame.sprite.Sprite):
    # 初始化
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = bullet_img  # 顯示bullet
        self.image.set_colorkey(DARK)    # 消除載入圖片後黑色的區塊
        self.rect = self.image.get_rect()  # 定位bullet
        self.rect.centerx = x
        self.rect.bottom = y
        self.speedy = -10   # 子彈速度

    def update(self):
        # 子彈射出
        self.rect.y += self.speedy

        # 判斷bullet是否超出視窗界線，若超出則delete
        if self.rect.bottom < 0:
            self.kill()


# Rocket class，繼承pygame的sprite class
class Rocket(pygame.sprite.Sprite):
    # 初始化
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = rocket_img  # 顯示rocket
        self.image.set_colorkey(DARK)    # 消除載入圖片後黑色的區塊
        self.rect = self.image.get_rect()  # 定位rocket
        self.rect.centerx = x
        self.rect.bottom = y
        self.speedy = -5   # 火箭速度
        self.radius = int(self.rect.width * 0.85 / 2)

    def update(self):
        # 子彈射出
        self.rect.y += self.speedy

        # 判斷rocket是否超出視窗界線，若超出則delete
        if self.rect.bottom < 0:
            self.kill()


# 建立explosion class，繼承pygame的sprite class
class Explosion(pygame.sprite.Sprite):
    # 初始化
    def __init__(self, center, size):
        pygame.sprite.Sprite.__init__(self)
        self.size = size
        self.image = explosion_animation[self.size][0]  # 顯示爆炸圖片
        self.rect = self.image.get_rect()  # 定位圖片
        self.rect.center = center
        self.frame = 0
        self.last_update = pygame.time.get_ticks()   # 紀錄圖片最露更新的時間
        self.frame_rate = 50   # 經過n毫秒後更新下一張圖片

    def update(self):
        now = pygame.time.get_ticks()  # 現在的時間
        # (現在的時間 - 最後一次更新的時間) 是否大於n毫秒
        if now - self.last_update > self.frame_rate:
            self.last_update = now
            self.frame += 1
            if self.frame == len(explosion_animation[self.size]):
                self.kill()
            else:
                self.image = explosion_animation[self.size][self.frame]
                center = self.rect.center
                self.rect = self.image.get_rect()
                self.rect.center = center


# 建立寶物的class
class Power(pygame.sprite.Sprite):
    # 初始化
    def __init__(self, center):
        pygame.sprite.Sprite.__init__(self)
        self.type = random.choice(['shield', 'gun'])   # 隨機掉落其中一個寶物
        self.image = power_imgs[self.type]  # 顯示寶物
        self.image.set_colorkey(DARK)    # 消除載入圖片後黑色的區塊
        self.rect = self.image.get_rect()  # 定位寶物
        self.rect.center = center
        self.speedy = 2   # 寶物掉落速度

    def update(self):
        # 寶物掉落
        self.rect.y += self.speedy

        # 判斷寶物是否超出視窗界線，若超出則delete
        if self.rect.top > HEIGHT:
            self.kill()


all_sprites: Group = pygame.sprite.Group()   # 整個遊戲的Group
rocks = pygame.sprite.Group()   # 創立一個石頭的Group
bullets = pygame.sprite.Group()   # 創立一個子彈的Group
rockets = pygame.sprite.Group()   # 創立一個火箭的Group
powers = pygame.sprite.Group()   # 創立一個寶物的Group
player = Player()
all_sprites.add(player)   # 生成太空船
enemy_bullets = pygame.sprite.Group()   # 敵人射出的子彈
enemys = pygame.sprite.Group   # 產生敵人
for i in range(4):
    new_enemy()
for i in range(8):   # 產生石頭
    new_rock()
pygame.mixer.music.play(-1)


# 遊戲迴圈
show_init = True
running = True
while running:
    # 判斷是否要顯示初始畫面
    if show_init:
        close = draw_init()
        if close:
            break
        show_init = False
        all_sprites: Group = pygame.sprite.Group()  # 整個遊戲的Group
        rocks = pygame.sprite.Group()  # 創立一個石頭的Group
        bullets = pygame.sprite.Group()  # 創立一個子彈的Group
        rockets = pygame.sprite.Group()  # 創立一個火箭的Group
        powers = pygame.sprite.Group()  # 創立一個寶物的Group
        player = Player()
        all_sprites.add(player)  # 生成太空船
        enemy_bullets = pygame.sprite.Group()   # 敵人射出的子彈
        enemys = pygame.sprite.Group()   # 產生敵人
        for i in range(4):
            new_enemy()
        for i in range(8):  # 產生石頭
            new_rock()

    # 每秒中最多能執行N次，FPS = frame
    clock.tick(FPS)
    # 取得輸入
    for event in pygame.event.get():
        # 當event是關閉視窗時，停止運作
        if event.type == pygame.QUIT:
            running = False
        # 當event是按下按鍵
        elif event.type == pygame.KEYDOWN:
            # 當空白鍵按下去時，射出子彈
            if event.key == pygame.K_SPACE:
                player.shoot_bullet()
            # 當按下R鍵時，射出火箭
            if event.key == pygame.K_r:
                player.shoot_rocket()

    # 敵人子彈射擊
    for enemy in enemys:
        enemy.shoot_bullet(player)

    # 更新遊戲
    all_sprites.update()

    # 子彈、火箭和敵人子彈相撞
    hits_bullet = pygame.sprite.groupcollide(enemy_bullets, bullets, True, True)  # 子彈和敵人子彈撞擊到後消除
    hits_rocket = pygame.sprite.groupcollide(enemy_bullets, rockets, True, True)  # 子彈和敵人子彈撞擊到後消除

    # 石頭、敵人和子彈相撞
    hits_rocks = pygame.sprite.groupcollide(rocks, bullets, True, True)   # 子彈和石頭撞擊到
    hits_enemys = pygame.sprite.groupcollide(enemys, bullets, True, True)  # 子彈和敵人撞擊到
    for hit in hits_rocks:   # 每射擊掉一個石頭就補回一個石頭
        random.choice(explosion_sounds).play()   # 隨機撥放石頭爆炸的音效
        player.score += hit.radius   # 根據石頭半徑大小增加相對應的分數
        explosion = Explosion(hit.rect.center, 'large')   # 當子彈撞到石頭，產生大爆炸的動畫
        all_sprites.add(explosion)
        # 掉寶率 (5%)
        if random.random() > 0.95:
            pow = Power(hit.rect.center)
            all_sprites.add(pow)
            powers.add(pow)
        new_rock()
    for hit in hits_enemys:   # 每射擊掉一個敵人就補回一個敵人
        random.choice(explosion_sounds).play()   # 隨機撥放爆炸的音效
        player.score += hit.radius   # 根據敵人半徑大小增加相對應的分數
        explosion = Explosion(hit.rect.center, 'large')   # 當子彈撞到石頭，產生大爆炸的動畫
        all_sprites.add(explosion)
        # 掉寶率 (10%)
        if random.random() > 0.9:
            pow = Power(hit.rect.center)
            all_sprites.add(pow)
            powers.add(pow)
        new_enemy()

    # 石頭和火箭碰撞
    # hits = {
    #   collided_rock_1: [collided_rocket_1, collided_rocket_2, ....],
    #   collided_rock_2: [collided_rocket_3, collided_rocket_4, ....],
    #   ...
    # }
    # first collision
    hits_rocks_rockets = pygame.sprite.groupcollide(
        groupa=rocks, groupb=rockets, dokilla=True, dokillb=True, collided=pygame.sprite.collide_circle
    )
    # process first hits
    for hit in hits_rocks_rockets:  # 每射擊掉一個石頭就補回一個石頭
        random.choice(explosion_sounds).play()  # 隨機撥放石頭爆炸的音效
        player.score += hit.radius  # 根據石頭半徑大小增加相對應的分數
        explosion = Explosion(hit.rect.center, 'very_large')  # 當子彈撞到石頭，產生大爆炸的動畫
        all_sprites.add(explosion)
        # 掉寶率 (5%)
        if random.random() > 0.95:
            pow = Power(hit.rect.center)
            all_sprites.add(pow)
            powers.add(pow)
        new_rock()

    for collided_rock, collided_rocket_list in hits_rocks_rockets.items():
        # scale up the radius of collided rocket for explosion
        collided_rockets = pygame.sprite.Group()
        for collided_rocket in collided_rocket_list:
            collided_rocket.radius = 100
            collided_rockets.add(collided_rocket)
        # second collision with the explosion of the collided rockets
        explosion_hits = pygame.sprite.groupcollide(
            groupa=rocks, groupb=collided_rockets, dokilla=True, dokillb=False, collided=pygame.sprite.collide_circle
        )
        # process second hits of explosion
        for hit in explosion_hits:  # 每射擊掉一個石頭就補回一個石頭
            random.choice(explosion_sounds).play()  # 隨機撥放石頭爆炸的音效
            player.score += hit.radius  # 根據石頭半徑大小增加相對應的分數
            explosion = Explosion(hit.rect.center, 'very_large')  # 當子彈撞到石頭，產生大爆炸的動畫
            all_sprites.add(explosion)
            # 掉寶率 (5%)
            if random.random() > 0.95:
                pow = Power(hit.rect.center)
                all_sprites.add(pow)
                powers.add(pow)
            new_rock()

    ##########################
    # 石頭和火箭相撞
    '''
    hits = pygame.sprite.groupcollide(rocks, rockets, True, True)  # 子彈和石頭撞擊到
    for hit in hits:  # 每射擊掉一個石頭就補回一個石頭
        random.choice(explosion_sounds).play()  # 隨機撥放石頭爆炸的音效
        score += hit.radius  # 根據石頭半徑大小增加相對應的分數
        explosion = Explosion(hit.rect.center, 'very_large')  # 當子彈撞到石頭，產生大爆炸的動畫
        all_sprites.add(explosion)
        # 掉寶率 (10%)
        if random.random() > 0.9:
            pow = Power(hit.rect.center)
            all_sprites.add(pow)
            powers.add(pow)
        new_rock()
    '''
    ##########################

    # 太空船被石頭、敵人撞擊，碰撞判斷以圓形為斷斷
    hits_rocks = pygame.sprite.spritecollide(player, rocks, True, pygame.sprite.collide_circle)
    hits_enemys = pygame.sprite.spritecollide(player, enemys, True, pygame.sprite.collide_circle)
    hits_enemys_bullets = pygame.sprite.spritecollide(player, enemy_bullets, True, pygame.sprite.collide_circle)
    for hit in hits_rocks:
        new_rock()
        player.health -= hit.radius   # 根據撞到的石頭大小來扣相應血量
        explosion = Explosion(hit.rect.center, 'small')  # 當石頭撞到太空船，產生小爆炸的動畫
        all_sprites.add(explosion)
        # 若血條歸零
        if player.health <= 0:
            death_explosion = Explosion(player.rect.center, 'player')   # 爆炸死亡動畫
            all_sprites.add(death_explosion)
            die_sound.play()
            player.lives -= 1
            player.health = 200
            player.hide()
    for hit in hits_enemys:
        new_enemy()
        player.health -= hit.radius   # 根據撞到的石頭大小來扣相應血量
        explosion = Explosion(hit.rect.center, 'small')  # 當石頭撞到太空船，產生小爆炸的動畫
        all_sprites.add(explosion)
        # 若血條歸零
        if player.health <= 0:
            death_explosion = Explosion(player.rect.center, 'player')   # 爆炸死亡動畫
            all_sprites.add(death_explosion)
            die_sound.play()
            player.lives -= 1
            player.health = 200
            player.hide()
    for hit in hits_enemys_bullets:
        player.health -= hit.radius   # 根據撞到的石頭大小來扣相應血量
        explosion = Explosion(hit.rect.center, 'small')  # 當石頭撞到太空船，產生小爆炸的動畫
        all_sprites.add(explosion)
        # 若血條歸零
        if player.health <= 0:
            death_explosion = Explosion(player.rect.center, 'player')   # 爆炸死亡動畫
            all_sprites.add(death_explosion)
            die_sound.play()
            player.lives -= 1
            player.health = 200
            player.hide()

    # 寶物跟太空船相撞
    hits = pygame.sprite.spritecollide(player, powers, True)
    for hit in hits:
        # 吃到增加血量
        if hit.type == 'shield':
            player.health += 20
            if player.health > 100:
                player.health = 100
            shield_sound.play()
        # 吃到增加攻擊力
        if hit.type == 'gun':
            player.gunup()
            gun_sound.play()

    # 若已經沒有次數 & 爆炸的動畫已結束
    if player.lives == 0 and not(death_explosion.alive()):
        show_init = True
        EnemyCommonSetting.shoot_gap_time = 1000   # 敵人子彈射擊時間間隔重製

    # 畫面顯示
    screen.fill(DARK)   # fill(R,G,B) -> 視窗填充顏色
    screen.blit(background_img, (0, 0))   # 把背景圖片在 (0,0) 位置畫出來
    all_sprites.draw(screen)   # 把all_sprites group里全部的東西都顯示出來
    draw_text(screen, str(player.score), 22, WIDTH/2, 10)   # 顯示分數
    draw_health(screen, player.health, 5, 15)   # 顯示血量條
    draw_lives(screen, player.lives, player_mini_img, WIDTH-100, 15)   # 顯示剩餘次數
    pygame.display.update()