import pygame
import random
import math
import pytmx
import random
weapon_information = [
    ["Small gun", 10, 100, "small_gun.png", 0, 0, 0],
    ["Fire gun", 15, 100, "fire_gun.png", 0, 0, 60],
    ["Frozen weapon", 15, 100, "frozen_weapon.png", 0, 0, 60],
    ["Poison gun", 15, 100, "poison_gun.jpg", 0, 0, 60],
    ["Electric gun", 20, 100, "electric_gun.jpg", 0, 0, 0],
    ["Heavy gun", 50, 100, "heavy_gun.jpg", 0, 0, 0],
    ["Laser gun", 25, 100, "laser_gun.png", 0, 0, 0],
    ["Water gun", 12, 100, "water_gun.png", 0, 0, 30],
    ["Wind gun", 18, 100, "wind_gun.png", 0, 0, 0],
    ["Light gun", 30, 100, "light_gun.png", 0, 0, 0],
    ["Shadow gun", 28, 100, "shadow_gun.png", 0, 0, 30],
    ["Crystal gun", 22, 100, "crystal_gun.png", 0, 0, 0],
    ["Bright gun", 35, 100, "bright_gun.png", 0, 0, 0],
    ["Magic gun", 40, 100, "magic_gun.png", 0, 0, 60],
    ["Ice crystal gun", 25, 100, "ice_crystal_gun.png", 0, 0, 60],
    ["Thunder gun", 35, 100, "thunder_gun.png", 0, 0, 0],
    ["Rainbow gun", 20, 100, "rainbow_gun.png", 0, 0, 30],
    ["Golden gun", 45, 100, "golden_gun.png", 0, 0, 0]
]

enemy_information = [
    ["Dog", 5, 50, 2, 2, 0],
    ["Soilder", 10, 100, 5, 0, 0],
    ["Magic monster", 15, 80, 3, 5, 0],
    ["Fire monster", 20, 100, 5, 0, 60],
    ["Ice monster", 15, 120, 8, 5, 60],
    ["Poison monster", 18, 90, 3, 5, 60],
    ["Ghost", 25, 70, 0, 15, 0],
    ["Stone monster", 30, 200, 20, 0, 0],
    ["Dragon", 50, 300, 15, 15, 60]
]

class Enemy(pygame.sprite.Sprite):
    def __init__(self,enemy_information,Image,spawning_location):
            super().__init__()
           
            self.name=enemy_information[0]
           
            self.damage=enemy_information[1]
           
            self.hp=enemy_information[2]
           
            self.physical_defence=enemy_information[3]
           
            self.magical_defence=enemy_information[4]
           
            self.special_effect=enemy_information[5]
           
            self.image = Image
           
            self.rect = self.image.get_rect(center=spawning_location)


    def move(self, keys, walls=None, bounds=None):
        dx = 0
        dy = 0


        if pygame.K_w in keys or pygame.K_UP in keys:
            dy -= self.speed
        if pygame.K_s in keys or pygame.K_DOWN in keys:
            dy += self.speed
        if pygame.K_a in keys or pygame.K_LEFT in keys:
            dx -= self.speed
        if pygame.K_d in keys or pygame.K_RIGHT in keys:
            dx += self.speed


        movement = pygame.math.Vector2(dx, dy)


        if movement.length() > 0:
            movement = movement.normalize() * self.speed


        self.rect.x += round(movement.x)


        if walls:
            for wall in walls:
                if self.rect.colliderect(wall):
                    if movement.x > 0:
                        self.rect.right = wall.left
                    elif movement.x < 0:
                        self.rect.left = wall.right


        self.rect.y += round(movement.y)


        if walls:
            for wall in walls:
                if self.rect.colliderect(wall):
                    if movement.y > 0:
                        self.rect.bottom = wall.top
                    elif movement.y < 0:
                        self.rect.top = wall.bottom

        if bounds:
            self.rect.clamp_ip(bounds)

    def attack(self, cursor_location):


        dx = cursor_location[0] - self.rect.centerx
        dy = cursor_location[1] - self.rect.centery


        if abs(dx) > abs(dy):
            if dx > 0:
                return pygame.Rect(self.rect.right, self.rect.centery - 35, 70, 70)
            return pygame.Rect(self.rect.left - 70, self.rect.centery - 35, 70, 70)


        if dy > 0:
            return pygame.Rect(self.rect.centerx - 35, self.rect.bottom, 70, 70)

        return pygame.Rect(self.rect.centerx - 35, self.rect.top - 70, 70, 70)

    def skill(self):
        if self.skill_unlocked and self.energy >= 30:
            self.energy -= 30
            return "Assassin dash activated"

        return None
    
    def update(self):
           
            self.rect.move_ip(velocity)
            
    def fire(self, player_location, cursor_location):
               
        direction = pygame.math.Vector2(cursor_location[0], cursor_location[1]) - pygame.math.Vector2(self.rect.center[0], self.rect.center[1]).normalize()*10
               
        Bullet_list.add(Bullets(player_location, direction))
       
    def attack(self,target):
            
        target.hp-=(self.damage-target.physical_defence)

Bullet_list = pygame.sprite.Group()

velocity = pygame.math.Vector2(0,0)

class Bullets(pygame.sprite.Sprite):
    def __init__(self, spawning_location, Direction):
       
        super().__init__()
       
        self.image = pygame.Surface([10, 10])
        self.image.fill((227, 174, 27))
       
        self.rect = self.image.get_rect(center=spawning_location)
       
        self.direction = Direction

    def update(self):
        self.rect.move_ip(self.direction)
       
        if self.rect.top < 0 or self.rect.left < 0 or self.rect.right > 800 or self.rect.bottom > 600:
           
            self.kill()
#small gun, fire gun(burning=60),frozen weapon(frozen=60),poison gun(poison=60),electric gun(damage-20),heavy gun(damage will very big)
class Weapon(pygame.sprite.Sprite):
    def __init__(self,weapon_information,Image,spawning_location):
        super().__init__()
       
        self.name = weapon_information[0]
       
        self.damage = weapon_information[1]
       
        self.hp = weapon_information[2]
       
        self.image = Image
       
        self.physical_defence = weapon_information[4]
       
        self.magical_defence = weapon_information[5]
       
        self.special_effect = weapon_information[6]
       
        self.rect = self.image.get_rect(center=spawning_location)
   
    def update(self):
       
        self.rect.move_ip(velocity)

    def fire(self, player_location, cursor_location):
       
        direction = pygame.math.Vector2(cursor_location[0], cursor_location[1]) - pygame.math.Vector2(self.rect.center[0], self.rect.center[1]).normalize()*10
       
        print(direction)
       
        Bullet_list.add(Bullets(player_location, direction))
    def attack(self,target):
               
        target.hp-=(self.damage-target.physical_defence)

class Block(pygame.sprite.Sprite):
   
    def __init__(self, color, width, height):
       super().__init__()
       
       self.image = pygame.Surface([width, height])
       
       self.image.fill(color)
       
       self.rect = self.image.get_rect(center =(200, 300))

block1 = Block((255, 100, 98),10,10)

pygame.init()
screen = pygame.display.set_mode((800, 600))

tiled_map = pytmx.load_pygame("choose_char/choose_char.tmx", pixelalpha=True)

tiled_map = pytmx.load_pygame("MAP1/m1.tmx", pixelalpha=True)

background = pygame.Surface((800,600)).convert_alpha()

def draw_image_layers():
    global background
   
    for layer in tiled_map.visible_layers:
       
        if isinstance(layer, pytmx.TiledTileLayer):
           
            for x, y, gid in layer:
               
                tile_image = tiled_map.get_tile_image_by_gid(gid)
               
                if tile_image:
                   
                    pixel_x = x * tiled_map.tilewidth
                    pixel_y = y * tiled_map.tileheight
                   
                    background.blit(tile_image, (pixel_x, pixel_y))

draw_image_layers()

wall_layer = tiled_map.get_layer_by_name("Walls")

for obj in wall_layer:
    print(obj.name, obj.x, obj.y, obj.width, obj.height)

wall = []

for obj in wall_layer:
   
    wall.append(pygame.Rect(obj.x, obj.y, obj.width, obj.height))

game_active = True

while game_active:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_active = False
   
    screen.blit(background, (0,0))
    
    pygame.display.update()
    
    pygame.time.Clock().tick(60)












       













       



















        





