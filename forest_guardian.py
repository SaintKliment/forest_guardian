import pygame
from enemy import Enemy, spawn_enemy  # Импортируем из enemy.py

# Инициализация PyGame
pygame.init()

# Размеры окна
WIDTH, HEIGHT = 1000, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Хранитель леса")

# Загрузка изображений
background_image = pygame.image.load("./assets/forest_background1.png")
background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))  # Масштабирование фона под размер окна

hero_image = pygame.image.load("./assets/forest_guardian.png")
original_width, original_height = hero_image.get_width(), hero_image.get_height()

# Уменьшаем героя в 5 раз
hero_scaled_width = original_width // 2.5
hero_scaled_height = original_height // 2.5
hero_image = pygame.transform.scale(hero_image, (hero_scaled_width, hero_scaled_height))

# Начальная позиция героя
hero_x = (WIDTH - hero_scaled_width) // 2
hero_y = (HEIGHT - hero_scaled_height) // 2 + 105
hero_speed = 0.1

# Прыжок
is_jumping = False
jump_speed = 10  # Увеличиваем начальную скорость прыжка (чтобы прыгать выше)
gravity = 1  # Уменьшаем силу гравитации (падение будет медленнее)
y_velocity = 0  # Вертикальная скорость

# Группы спрайтов
all_sprites = pygame.sprite.Group()
enemy_group = pygame.sprite.Group()

# Главный игровой цикл
running = True
spawn_timer = 0  # Таймер для спавна врагов

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Обработка нажатий клавиш
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:  # Клавиша A
        hero_x -= hero_speed
        hero_image = pygame.image.load("./assets/forest_guardian_mirror.png")
        hero_image = pygame.transform.scale(hero_image, (hero_scaled_width, hero_scaled_height))

    if keys[pygame.K_d]:  # Клавиша D
        hero_x += hero_speed
        hero_image = pygame.image.load("./assets/forest_guardian.png")
        hero_image = pygame.transform.scale(hero_image, (hero_scaled_width, hero_scaled_height))

    if keys[pygame.K_w] and not is_jumping:  # Клавиша W для прыжка
        is_jumping = True
        y_velocity = -jump_speed  # Устанавливаем начальную скорость для прыжка

    # Обработка движения по вертикали (гравитация)
    if is_jumping:
        hero_y += y_velocity
        y_velocity += gravity  # Каждый кадр добавляем гравитацию

        # Ограничиваем падение на землю
        if hero_y >= (HEIGHT - hero_scaled_height - 105):
            hero_y = HEIGHT - hero_scaled_height - 105
            is_jumping = False
            y_velocity = 0  # Обнуляем вертикальную скорость

    # Ограничение движения героя в пределах окна
    if hero_x < 0:
        hero_x = 0
    if hero_x > WIDTH - hero_scaled_width:
        hero_x = WIDTH - hero_scaled_width

    # Спавним врагов с интервалом
    spawn_timer += 1
    if spawn_timer > 100:  # Спавним врага каждые 100 кадров
        spawn_enemy(hero_y, WIDTH, enemy_group, all_sprites)
        spawn_timer = 0

    # Обновляем врагов
    all_sprites.update()

    # Рендеринг
    screen.blit(background_image, (0, 0))  # Рисуем фон
    screen.blit(hero_image, (hero_x, hero_y))  # Рисуем героя
    all_sprites.draw(screen)  # Рисуем врагов

    pygame.display.flip()  # Обновление экрана

pygame.quit()
