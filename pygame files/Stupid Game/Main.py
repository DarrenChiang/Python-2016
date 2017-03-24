import pygame as pg
import os
import math
import random

from Sprite import *
from Environments import *
from Units import *
from Enemy import *


class StupidGame:
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    CYAN = (0, 255, 255)
    YELLOW = (255, 255, 0)
    GRAY = (120, 120, 120)
    DARK_GRAY = (60, 60, 60)
    LIGHT_GRAY = (120, 120, 120)
    
    def __init__(self, caption, win_size, fps):
        self.running = True
        self.window = None
        self.size = win_size
        self.caption = caption
        self.clock = None
        self.fps = fps
        
        self.player_entities = None
        self.player_projectiles = None
        self.other_entities = None
        self.other_projectiles = None
        self.map_entities = None

        self.enemies = None

    def load_player_entities(self):
        self.player_entities = Group_Plus()
        player_info = {'name': 'player',
                       'dimensions': (35, 42),
                       'max hp': 500}   
        self.player = Shooter(player_info)
        self.player_entities.add(self.player)

        self.player.center(self.window)
        self.player.setImage(self.player.adjustImage(self.select_image('pointer.png')))
        self.player_spd = 5

    def load_map_entities(self):
        self.map_entities = Group_Plus()

        w, h = self.size
        map_info = {'dimensions': (w * 1.5, h * 1.5),
                    'color': self.GRAY}
        self.map = Sprite_Plus(map_info)
        
        self.map.center(self.window)

        s = 300
        img = pg.transform.scale(self.select_image('tile.jpg'), (s, s))
        w, h = self.map.getDimensions()
        num_x = int(w / s)
        num_y = int(h / s)
        for x in range(num_x):
            for y in range(num_y):
                tile_info = {'dimensions' : (s, s),
                             'coordinate' : (self.map.getLeft() + x * s + s / 2, self.map.getTop() +  y * s + s / 2)}
                tile = Sprite_Plus(tile_info)
                tile.setImage(img)
                self.map_entities.add(tile)

    def load_other_entities(self):
        self.other_entities = Group_Plus()
        self.enemies = Enemy_Group(self.player, self.map)
        enemy_info = {'name': 'bot',
                      'dimensions': (30, 30),
                      'max hp': 60,
                      'color': self.RED}

        img = pg.transform.scale(self.select_image('grunt.png'), (30, 30))

        for i in range(20):
            enemy = Shooter(enemy_info)
            x = random.randint(self.map.getLeft() + 15, self.map.getRight() - 15)
            y = random.randint(self.map.getTop() + 15, self.map.getBottom() - 15)
            enemy.setCoordinate((x, y))
            enemy.setImage(img)
            a = random.randint(0, 360)
            enemy.vector.set_magnitude(3)
            enemy.vector.set_angle(a)
            self.other_entities.add(enemy)
            self.enemies.add(Enemy(enemy, 'grunt'))

        boss_info = {'name': 'bot',
                     'dimensions': (100, 100),
                     'max hp': 1000,
                     'color': self.RED}
        boss = Special_Shooter(boss_info)
        x = random.randint(self.map.getLeft() + 50, self.map.getRight() - 50)
        y = random.randint(self.map.getTop() + 50, self.map.getBottom() - 50)
        boss.setCoordinate((x, y))
        boss.setImage(boss.adjustImage(self.select_image('boss.png')))
        self.other_entities.add(boss)
        self.enemies.add(Boss(boss, 'boss'))

    def load_projectiles(self):
        self.player_projectiles = Group_Plus()
        self.other_projectiles = Group_Plus()
        w, h = self.player.getDimensions()
        w /= 4
        h /= 4
        img = pg.transform.scale(self.select_image('beam1.png'), (int(w), int(h)))
        proj_info = {'name': 'standard',
                     'max hp': 1,
                     'side': 'player',
                     'projectile speed': 10,
                     'dimensions': (self.player.getWidth() / 4, self.player.getHeight() / 4),
                     'color': self.CYAN,
                     'damage': 20,
                     'image': img,
                     'interact groups': [self.other_entities, self.other_projectiles]}
        self.player.set_projectiles(proj_info, self.player_projectiles)
        imge = pg.transform.scale(self.select_image('beam2.png'), (10, 20))
        proj_info = {'name': 'standard',
                     'max hp': 1,
                     'side': 'enemy',
                     'projectile speed': 6,
                     'dimensions': (10, 20),
                     'color': self.YELLOW,
                     'damage': 20,
                     'image': imge,
                     'interact groups': [self.player_projectiles, self.player_entities]}
        imgbe = pg.transform.scale(self.select_image('beam3.png'), (30, 30))
        largeProj = {'name': 'standard',
                     'max hp': 180,
                     'side': 'enemy',
                     'projectile speed': 4,
                     'dimensions': (30, 30),
                     'color': self.GREEN,
                     'damage': 30,
                     'image': imgbe,
                     'interact groups': [self.player_entities]}
        for e in self.enemies.list:
            if e.type == 'grunt':
                e.sprite.set_projectiles(proj_info, self.other_projectiles)
            else:
                e.sprite.set_projectiles(largeProj, self.other_projectiles)        

    def load_assets(self):
        imageNames = os.listdir('Images')
        self.images = [(name, pg.image.load('Images//' + name).convert_alpha()) for name in imageNames]

    def select_image(self, name):
        for image in self.images:
            if image[0] == name:
                return image[1]

    def init(self):
        pg.init()
        self.window = pg.display.set_mode(self.size)
        self.clock = pg.time.Clock()
        pg.display.set_caption(self.caption)

        self.load_assets()

        
        self.load_map_entities()
        self.load_player_entities()
        self.load_other_entities()
        self.load_projectiles()

        self.environment = Track_Player(self.player, self.map, 200)
        self.environment.add(self.player_entities)
        self.environment.add(self.player_projectiles)
        self.environment.add(self.other_entities)
        self.environment.add(self.other_projectiles)
        self.environment.add(self.map_entities)
        
        self.m_down = False

    def event(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.running = False
            elif event.type == pg.MOUSEBUTTONDOWN:
                self.m_down = True
            elif event.type == pg.MOUSEBUTTONUP:
                self.m_down = False

        keys = pg.key.get_pressed()

        if keys[pg.K_w] and keys[pg.K_a]:
            self.environment.move(self.player_spd, 135)
        elif keys[pg.K_w] and keys[pg.K_d]:
            self.environment.move(self.player_spd, 45)
        elif keys[pg.K_s] and keys[pg.K_a]:
            self.environment.move(self.player_spd, -135)
        elif keys[pg.K_s] and keys[pg.K_d]:
            self.environment.move(self.player_spd, -45)
        elif keys[pg.K_a]:
            self.environment.move(self.player_spd, 180)
        elif keys[pg.K_d]:
            self.environment.move(self.player_spd, 0)
        elif keys[pg.K_w]:
            self.environment.move(self.player_spd, 90)
        elif keys[pg.K_s]:
            self.environment.move(self.player_spd, -90)
        else:
            self.environment.move(0, 0)       

    def update(self):
        self.player.projectile_limit(self.map)

        if self.m_down:
            self.player.target('mouse')
            self.player.attack()

        if self.player_entities.has(self.player) == False or len(self.enemies.list) <= 0:
            self.running = False

        if self.player.getLeft() < self.map.getLeft():
            self.player.setX(self.map.getLeft() + self.player.getWidth() / 2)
        if self.player.getRight() > self.map.getRight():
            self.player.setX(self.map.getRight() - self.player.getWidth() / 2)
        if self.player.getTop() < self.map.getTop():
            self.player.setY(self.map.getTop() + self.player.getHeight() / 2)
        if self.player.getBottom() > self.map.getBottom():
            self.player.setY(self.map.getBottom() - self.player.getHeight() / 2)

        self.enemies.update()
        
        self.map_entities.update()
        self.player_entities.update()
        self.player_projectiles.update()
        self.other_projectiles.update()
        self.other_entities.update()

    def render(self):
        self.window.fill(self.BLACK)     
        self.draw()
        pg.display.flip()
        self.clock.tick(self.fps)

    def draw(self):
        self.map_entities.draw(self.window)
        self.player_projectiles.draw(self.window)
        self.other_projectiles.draw(self.window)
        self.player_entities.draw(self.window)
        self.other_entities.draw(self.window)

    def end(self):
        pass

    def execute(self):
        self.init()
        while self.running:
            self.event()
            self.update()
            self.render()
        self.end()
        
size = (1000, 600)
game = StupidGame('Game', size, 60)
game.execute()
