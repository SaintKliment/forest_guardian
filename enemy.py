# enemy.py
import pygame
import random

# Настройки врагов
enemy_width, enemy_height = 50, 50  # Размер врага
enemy_speed = 0.75 # Скорость врага

class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("./assets/enemy.png")  # Подставьте путь к изображению врага
        self.image = pygame.transform.scale(self.image, (enemy_width, enemy_height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = enemy_speed

    def update(self):
        # Двигаем врага влево или вправо
        self.rect.x -= self.speed  # Пример движения

# Функция для спавна врагов
def spawn_enemy(hero_y, WIDTH, enemy_group, all_sprites):
    # Случайно выбираем, с какой стороны появится враг
    side = random.choice(["left", "right"])

    if side == "left":
        x = -enemy_width  # Немного за пределами экрана слева
    else:
        x = WIDTH + enemy_width  # Немного за пределами экрана справа

    # Спавним врага на той же вертикальной позиции, что и герой
    enemy = Enemy(x, hero_y)
    enemy_group.add(enemy)
    all_sprites.add(enemy)
