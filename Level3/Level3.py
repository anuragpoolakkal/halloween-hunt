
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
61
62
63
64
65
66
67
68
69
70
71
72
73
74
75
76
77
78
79
80
81
82
83
84
85
86
87
88
89
90
91
92
93
94
95
96
97
98
99
100
101
102
103
104
105
106
107
108
109
110
111
112
113
114
115
116
117
118
119
120
121
122
123
124
125
126
127
128
import pygame
from pygame.locals import *
import sys
import random
 
pygame.init()
vec = pygame.math.Vector2 
 
HEIGHT = 450
WIDTH = 400
ACC = 0.5
FRIC = -0.12
FPS = 60
 
FramePerSec = pygame.time.Clock()
 
displaysurface = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Game")
 
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.surf = pygame.Surface((30, 30))
        self.surf.fill((255,255,0))
        self.rect = self.surf.get_rect()
   
        self.pos = vec((10, 360))
        self.vel = vec(0,0)
        self.acc = vec(0,0)
 
    def move(self):
        self.acc = vec(0,0.5)
        pressed_keys = pygame.key.get_pressed()
                
        if pressed_keys[K_LEFT]:
            self.acc.x = -ACC
        if pressed_keys[K_RIGHT]:
            self.acc.x = ACC
                 
        self.acc.x += self.vel.x * FRIC
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc
         
        if self.pos.x > WIDTH:
            self.pos.x = 0
        if self.pos.x < 0:
            self.pos.x = WIDTH         
        self.rect.midbottom = self.pos
 
    def jump(self):
        hits = pygame.sprite.spritecollide(self, platforms, False)
        if hits:
           self.vel.y = -15
 
    def update(self):
        hits = pygame.sprite.spritecollide(P1 ,platforms, False)
        if P1.vel.y > 0:        
            if hits:
                self.vel.y = 0
                self.pos.y = hits[0].rect.top + 1
 
class platform(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = pygame.Surface((random.randint(50,100), 12))
        self.surf.fill((0,255,0))
        self.rect = self.surf.get_rect(center = (random.randint(0,WIDTH-10),
                                                 random.randint(0, HEIGHT-30)))
 
    def move(self):
        pass
 
 
def plat_gen():
    while len(platforms) < 7 :
        width = random.randrange(50,100)
        p  = platform()             
        p.rect.center = (random.randrange(0, WIDTH - width),
                             random.randrange(-50, 0))
        platforms.add(p)
        all_sprites.add(p)
 
PT1 = platform()
P1 = Player()
 
PT1.surf = pygame.Surface((WIDTH, 20))
PT1.surf.fill((255,0,0))
PT1.rect = PT1.surf.get_rect(center = (WIDTH/2, HEIGHT - 10))
 
all_sprites = pygame.sprite.Group()
all_sprites.add(PT1)
all_sprites.add(P1)
 
platforms = pygame.sprite.Group()
platforms.add(PT1)
 
for x in range(random.randint(5, 6)):
    pl = platform()
    platforms.add(pl)
    all_sprites.add(pl)
 
 
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:    
            if event.key == pygame.K_SPACE:
                P1.jump()
 
    if P1.rect.top <= HEIGHT / 3:
        P1.pos.y += abs(P1.vel.y)
        for plat in platforms:
            plat.rect.y += abs(P1.vel.y)
            if plat.rect.top >= HEIGHT:
                plat.kill()
         
    displaysurface.fill((0,0,0))
    P1.update()
    plat_gen()
 
    for entity in all_sprites:
        displaysurface.blit(entity.surf, entity.rect)
        entity.move()
 
    pygame.display.update()
    FramePerSec.tick(FPS)