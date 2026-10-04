import pygame
import sys
import time

pygame.init()

WIDTH = 1000
HEIGHT = 800

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Communication 2024 v1.3 — Samsung 12 kg")

clock = pygame.time.Clock()

# ============================================================
# ЦВЕТА
# ============================================================

WHITE = (245, 245, 245)
BLACK = (20, 20, 20)
DARK = (35, 38, 42)
GRAY = (110, 115, 120)
LIGHT_GRAY = (205, 208, 212)
GREEN = (50, 190, 90)
RED = (220, 55, 55)
BLUE = (65, 120, 210)
YELLOW = (230, 190, 45)

# ============================================================
# ШРИФТЫ
# ============================================================

def get_font(size, bold=False):
    return pygame.font.SysFont("arial", size, bold=bold)

FONT_SMALL = get_font(22)
FONT = get_font(28)
FONT_BIG = get_font(36, True)
FONT_HUGE = get_font(46, True)

# ============================================================
# ПРОГРАММЫ
# ============================================================

programs = [
    "Хлопок",
    "Синтетика",
    "Быстрая",
    "Детские вещи",
    "Ежедневная",
    "Удаление пятен",
    "Полоскание + Отжим",
    "Отжим",
    "Ручная стирка",
    "Шерсть",
    "Верхняя одежда",
    "Интенсивная стирка + Eco",
    "Постельное бельё"
]

# Максимальная температура для каждой программы

max_temperature = [
    95,  # Хлопок
    60,  # Синтетика
    40,  # Быстрая
    60,  # Детские вещи
    60,  # Ежедневная
    60,  # Удаление пятен
    40,  # Полоскание + Отжим
    0,   # Отжим
    40,  # Ручная стирка
    40,  # Шерсть
    60,  # Верхняя одежда
    60,  # Интенсивная стирка + Eco
    60   # Постельное бельё
]

# ============================================================
# ЗАДАНИЯ
# ============================================================

missions = [
    "КУХОННАЯ ОДЕЖДА + КЕТЧУП",
    "ПОСТЕЛЬНОЕ БЕЛЬЁ + ПОДУШКИ + НАВОЛОЧКИ",
    "КУРТКИ + ПОЛОТЕНЦЕ",
    "2 ПОДУШКИ",
    "ТЮЛЬ",
    "ШКОЛЬНЫЙ РЮКЗАК",
    "ИГРУШКА — МЕДВЕДЬ",
    "ДЖИНСЫ + ДЖИНСОВЫЕ ШОРТЫ",
    "2 ПОСТЕЛЬНЫХ БЕЛЬЯ",
    "ОДЕЖДА МАЛЫША + БЕЛЬЁ МАЛЫША",
    "2 КУРТКИ + 3 ПОЛОТЕНЦА",
    "НАВОЛОЧКА ДИВАНА",
    "КОВРИК ДЛЯ ТУАЛЕТА",
    "БОЛЬШАЯ СУМКА",
    "КУХОННОЕ ПОЛОТЕНЦЕ",
    "СВИТЕРЫ"
]

# ============================================================
# ПРАВИЛЬНЫЕ НАСТРОЙКИ
# ============================================================
#
# программа, температура, обороты, полоскания
#
# Здесь теперь 13 программ.
# Детские вещи и Постельное бельё имеют отдельные настройки.

correct = [
    (0, 60, 1200, 2),   # Хлопок
    (1, 40, 1000, 3),   # Синтетика
    (2, 40, 1000, 2),   # Быстрая
    (3, 60, 1000, 3),   # Детские вещи
    (4, 30, 800, 2),    # Ежедневная
    (5, 40, 800, 2),    # Удаление пятен
    (6, 30, 800, 2),    # Полоскание + Отжим
    (7, 0, 1200, 1),    # Отжим
    (8, 40, 800, 2),    # Ручная стирка
    (9, 40, 600, 2),    # Шерсть
    (10, 40, 1000, 2),  # Верхняя одежда
    (11, 60, 1000, 2),  # Интенсивная стирка + Eco
    (12, 40, 800, 3)    # Постельное бельё
]

# ============================================================
# ДОСТУПНЫЕ ТЕМПЕРАТУРЫ
# ============================================================

temperature_values = [
    20,
    30,
    40,
    50,
    60,
    70,
    80,
    90,
    95
]

# ============================================================
# ОБОРОТЫ
# ============================================================

spin_values = [
    0,
    400,
    600,
    800,
    1000,
    1200
]

# ============================================================
# ОТДЕЛЬНЫЕ НАСТРОЙКИ КАЖДОЙ ПРОГРАММЫ
# ============================================================
#
# Здесь хранятся текущие настройки каждой программы.
#
# Если изменить Хлопок на 70 градусов,
# потом перейти на Синтетику,
# а потом вернуться на Хлопок —
# там останется 70 градусов.
#

program_settings = []

for i in range(len(programs)):
    target_program, target_temp, target_spin, target_rinses = correct[i]

    if target_temp == 0:
        temp = 0
    else:
        temp = target_temp

    if target_spin in spin_values:
        spin = spin_values.index(target_spin)
    else:
        spin = 0

    program_settings.append({
        "temperature": temp,
        "spin_index": spin,
        "rinses": target_rinses
    })

# ============================================================
# СОСТОЯНИЕ ИГРЫ
# ============================================================

mission = 0
program = 0

running = False
stage = ""
start_time = 0

last_result = None
error_message = ""

error_time = 0

# ============================================================
# ТЕКУЩИЕ НАСТРОЙКИ
# ============================================================

def get_temperature():
    return program_settings[program]["temperature"]


def get_spin_index():
    return program_settings[program]["spin_index"]


def get_spin():
    return spin_values[get_spin_index()]


def get_rinses():
    return program_settings[program]["rinses"]


def set_temperature(value):
    program_settings[program]["temperature"] = value


def set_spin_index(value):
    program_settings[program]["spin_index"] = value


def set_rinses(value):
    program_settings[program]["rinses"] = value

# ============================================================
# ОШИБКА
# ============================================================

def show_error(message):
    global error_message
    global error_time

    error_message = message
    error_time = time.time()

# ============================================================
# ПРОВЕРКА ТЕМПЕРАТУРЫ
# ============================================================

def check_program_temperature():

    maximum = max_temperature[program]

    if maximum == 0:
        set_temperature(0)
        return

    current = get_temperature()

    if current == 0:
        set_temperature(20)

    elif current > maximum:
        # Ищем ближайшую допустимую температуру
        allowed = [
            value for value in temperature_values
            if value <= maximum
        ]

        if allowed:
            set_temperature(allowed[-1])
        else:
            set_temperature(0)

# ============================================================
# ПЕРЕКЛЮЧЕНИЕ ПРОГРАММЫ
# ============================================================

def change_program(direction):

    global program

    # Сохранять отдельно ничего не нужно —
    # настройки уже лежат в program_settings.

    program += direction

    if program < 0:
        program = len(programs) - 1

    if program >= len(programs):
        program = 0

    # Проверяем, подходит ли сохранённая температура
    check_program_temperature()

    show_error("")

# ============================================================
# ПРАВИЛЬНОСТЬ
# ============================================================

def calculate_correctness():

    target_program, target_temp, target_spin, target_rinses = correct[mission]

    score = 0

    # --------------------------------------------------------
    # ПРОГРАММА — 40 БАЛЛОВ
    # --------------------------------------------------------

    if program == target_program:
        score += 40

    # --------------------------------------------------------
    # ТЕМПЕРАТУРА — 25 БАЛЛОВ
    # --------------------------------------------------------

    temperature = get_temperature()

    difference = abs(temperature - target_temp)

    if difference == 0:
        score += 25

    elif difference <= 10:
        score += 21

    elif difference <= 20:
        score += 17

    elif difference <= 30:
        score += 12

    elif difference <= 40:
        score += 7

    # --------------------------------------------------------
    # ОБОРОТЫ — 20 БАЛЛОВ
    # --------------------------------------------------------

    spin = get_spin()

    difference = abs(spin - target_spin)

    if difference == 0:
        score += 20

    elif difference <= 200:
        score += 17

    elif difference <= 400:
        score += 14

    elif difference <= 600:
        score += 9

    elif difference <= 800:
        score += 5

    # --------------------------------------------------------
    # ПОЛОСКАНИЯ — 15 БАЛЛОВ
    # --------------------------------------------------------

    rinses = get_rinses()

    difference = abs(rinses - target_rinses)

    if difference == 0:
        score += 15

    elif difference == 1:
        score += 11

    elif difference == 2:
        score += 7

    elif difference == 3:
        score += 3

    return score

# ============================================================
# START
# ============================================================

def start_wash():

    global running
    global stage
    global start_time
    global last_result
    global error_message

    running = True

    stage = "НАБОР ВОДЫ"

    start_time = time.time()

    last_result = None
    error_message = ""

# ============================================================
# STOP
# ============================================================

def stop_wash():

    global running
    global stage

    running = False
    stage = "ОСТАНОВЛЕНО"

# ============================================================
# СТИРКА
# ============================================================

def update_wash():

    global running
    global stage
    global last_result
    global mission

    if not running:
        return

    elapsed = time.time() - start_time

    if elapsed < 1.5:
        stage = "НАБОР ВОДЫ"

    elif elapsed < 4:
        stage = "СТИРКА"

    elif elapsed < 6:
        stage = "ПОЛОСКАНИЕ"

    elif elapsed < 7.5:
        stage = "СЛИВ"

    elif elapsed < 9.5:
        stage = "ОТЖИМ"

    else:

        stage = "ЗАВЕРШЕНО"

        running = False

        # Получаем результат ДО смены задания
        last_result = calculate_correctness()

        # Следующее задание
        mission += 1

        if mission >= len(missions):
            mission = 0

# ============================================================
# ТЕКСТ
# ============================================================

def draw_text(text, x, y, font, color=BLACK, center=False):

    surface = font.render(str(text), True, color)

    if center:
        rect = surface.get_rect(center=(x, y))
    else:
        rect = surface.get_rect(topleft=(x, y))

    screen.blit(surface, rect)

# ============================================================
# КНОПКА
# ============================================================

def draw_button(rect, text, color, font=FONT, text_color=WHITE):

    pygame.draw.rect(
        screen,
        color,
        rect,
        border_radius=12
    )

    pygame.draw.rect(
        screen,
        BLACK,
        rect,
        2,
        border_radius=12
    )

    draw_text(
        text,
        rect.centerx,
        rect.centery,
        font,
        text_color,
        center=True
    )

# ============================================================
# ИНТЕРФЕЙС
# ============================================================

def draw_interface():

    screen.fill((225, 228, 232))

    # ========================================================
    # ЧТО СТИРАТЬ
    # ========================================================

    pygame.draw.rect(
        screen,
        WHITE,
        (30, 25, WIDTH - 60, 115),
        border_radius=16
    )

    pygame.draw.rect(
        screen,
        BLACK,
        (30, 25, WIDTH - 60, 115),
        2,
        border_radius=16
    )

    draw_text(
        "ЧТО СТИРАТЬ",
        55,
        42,
        FONT_BIG,
        BLACK
    )

    draw_text(
        missions[mission],
        55,
        88,
        FONT,
        BLUE
    )

    # ========================================================
    # ОСНОВНАЯ ПАНЕЛЬ
    # ========================================================

    pygame.draw.rect(
        screen,
        DARK,
        (30, 160, WIDTH - 60, 430),
        border_radius=18
    )

    # ========================================================
    # ЭКРАН
    # ========================================================

    pygame.draw.rect(
        screen,
        WHITE,
        (65, 190, WIDTH - 130, 190),
        border_radius=12
    )

    draw_text(
        "ПРОГРАММА",
        90,
        210,
        FONT_SMALL,
        GRAY
    )

    draw_text(
        programs[program],
        WIDTH // 2,
        255,
        FONT_BIG,
        BLACK,
        center=True
    )

    # ========================================================
    # ПАР
    # ========================================================

    if program == 12:

        draw_text(
            "ПОДДЕРЖИВАНИЕ ПАРА: ДА",
            WIDTH // 2,
            315,
            FONT,
            BLUE,
            center=True
        )

    else:

        draw_text(
            "ПОДДЕРЖИВАНИЕ ПАРА: НЕТ",
            WIDTH // 2,
            315,
            FONT,
            GRAY,
            center=True
        )

    # ========================================================
    # СТРЕЛКИ ПРОГРАММ
    # ========================================================

    draw_button(
        pygame.Rect(75, 400, 160, 70),
        "◀",
        BLUE,
        FONT_HUGE
    )

    draw_button(
        pygame.Rect(765, 400, 160, 70),
        "▶",
        BLUE,
        FONT_HUGE
    )

    # ========================================================
    # ТЕМПЕРАТУРА
    # ========================================================

    draw_text(
        "ТЕМПЕРАТУРА",
        270,
        405,
        FONT_SMALL,
        WHITE
    )

    draw_button(
        pygame.Rect(265, 440, 70, 60),
        "−",
        BLUE,
        FONT_BIG
    )

    draw_text(
        f"{get_temperature()} °C",
        410,
        470,
        FONT_BIG,
        WHITE,
        center=True
    )

    draw_button(
        pygame.Rect(485, 440, 70, 60),
        "+",
        BLUE,
        FONT_BIG
    )

    # ========================================================
    # ОБОРОТЫ
    # ========================================================

    draw_text(
        "ОБОРОТЫ",
        590,
        405,
        FONT_SMALL,
        WHITE
    )

    draw_button(
        pygame.Rect(575, 440, 70, 60),
        "−",
        BLUE,
        FONT_BIG
    )

    draw_text(
        f"{get_spin()}",
        700,
        470,
        FONT_BIG,
        WHITE,
        center=True
    )

    draw_button(
        pygame.Rect(755, 440, 70, 60),
        "+",
        BLUE,
        FONT_BIG
    )

    # ========================================================
    # ПОЛОСКАНИЯ
    # ========================================================

    draw_button(
        pygame.Rect(70, 505, 120, 55),
        "−",
        BLUE,
        FONT_BIG
    )

    draw_text(
        f"ПОЛОСКАНИЯ: {get_rinses()}",
        310,
        535,
        FONT,
        WHITE,
        center=True
    )

    draw_button(
        pygame.Rect(810, 505, 120, 55),
        "+",
        BLUE,
        FONT_BIG
    )

    # ========================================================
    # НИЖНЯЯ ПАНЕЛЬ
    # ========================================================

    pygame.draw.rect(
        screen,
        WHITE,
        (30, 610, WIDTH - 60, 160),
        border_radius=16
    )

    pygame.draw.rect(
        screen,
        BLACK,
        (30, 610, WIDTH - 60, 160),
        2,
        border_radius=16
    )

    # ========================================================
    # START
    # ========================================================

    draw_button(
        pygame.Rect(70, 650, 230, 80),
        "START",
        GREEN if not running else GRAY,
        FONT_BIG
    )

    # ========================================================
    # STOP
    # ========================================================

    draw_button(
        pygame.Rect(330, 650, 230, 80),
        "STOP",
        RED if running else GRAY,
        FONT_BIG
    )

    # ========================================================
    # СТАТУС
    # ========================================================

    if running:

        draw_text(
            f"СТАТУС: {stage}",
            600,
            635,
            FONT,
            BLACK
        )

        remaining = max(
            0,
            10 - int(time.time() - start_time)
        )

        draw_text(
            f"ОСТАЛОСЬ: {remaining} сек.",
            600,
            675,
            FONT_SMALL,
            GRAY
        )

    elif stage == "ЗАВЕРШЕНО" and last_result is not None:

        draw_text(
            "СТИРКА ЗАВЕРШЕНА",
            600,
            635,
            FONT,
            GREEN
        )

        draw_text(
            f"ПРАВИЛЬНОСТЬ: {last_result}%",
            600,
            675,
            FONT_BIG,
            BLUE
        )

    elif stage == "ОСТАНОВЛЕНО":

        draw_text(
            "СТИРКА ОСТАНОВЛЕНА",
            600,
            650,
            FONT,
            RED
        )

    else:

        draw_text(
            "ГОТОВ К СТИРКЕ",
            600,
            650,
            FONT,
            BLACK
        )

    # ========================================================
    # ОШИБКА
    # ========================================================

    if error_message:

        if time.time() - error_time < 2:

            draw_text(
                error_message,
                WIDTH // 2,
                785,
                FONT_SMALL,
                RED,
                center=True
            )


# ============================================================
# ОБРАБОТКА КЛИКОВ
# ============================================================

def handle_click(pos):

    global spin_index

    # ========================================================
    # ЕСЛИ СТИРКА ИДЁТ
    # ========================================================

    if running:

        # Разрешён только STOP
        if pygame.Rect(330, 650, 230, 80).collidepoint(pos):
            stop_wash()

        return

    # ========================================================
    # ПРОГРАММА ВЛЕВО
    # ========================================================

    if pygame.Rect(75, 400, 160, 70).collidepoint(pos):

        change_program(-1)

    # ========================================================
    # ПРОГРАММА ВПРАВО
    # ========================================================

    elif pygame.Rect(765, 400, 160, 70).collidepoint(pos):

        change_program(1)

    # ========================================================
    # ТЕМПЕРАТУРА МИНУС
    # ========================================================

    elif pygame.Rect(265, 440, 70, 60).collidepoint(pos):

        maximum = max_temperature[program]

        if maximum == 0:

            show_error(
                "ОШИБКА: ТЕМПЕРАТУРА НЕДОСТУПНА"
            )

            return

        current = get_temperature()

        if current in temperature_values:

            index = temperature_values.index(current)

            if index > 0:

                new_value = temperature_values[index - 1]

                if new_value <= maximum:

                    set_temperature(new_value)

    # ========================================================
    # ТЕМПЕРАТУРА ПЛЮС
    # ========================================================

    elif pygame.Rect(485, 440, 70, 60).collidepoint(pos):

        maximum = max_temperature[program]

        if maximum == 0:

            show_error(
                "ОШИБКА: ТЕМПЕРАТУРА НЕДОСТУПНА"
            )

            return

        current = get_temperature()

        if current in temperature_values:

            index = temperature_values.index(current)

            if index < len(temperature_values) - 1:

                new_value = temperature_values[index + 1]

                if new_value <= maximum:

                    set_temperature(new_value)

                else:

                    show_error(
                        f"ОШИБКА: МАКСИМУМ {maximum} °C"
                    )

    # ========================================================
    # ОБОРОТЫ МИНУС
    # ========================================================

    elif pygame.Rect(575, 440, 70, 60).collidepoint(pos):

        current = get_spin_index()

        if current > 0:

            set_spin_index(current - 1)

    # ========================================================
    # ОБОРОТЫ ПЛЮС
    # ========================================================

    elif pygame.Rect(755, 440, 70, 60).collidepoint(pos):

        current = get_spin_index()

        if current < len(spin_values) - 1:

            set_spin_index(current + 1)

    # ========================================================
    # ПОЛОСКАНИЯ МИНУС
    # ========================================================

    elif pygame.Rect(70, 505, 120, 55).collidepoint(pos):

        current = get_rinses()

        if current > 0:

            set_rinses(current - 1)

    # ========================================================
    # ПОЛОСКАНИЯ ПЛЮС
    # ========================================================

    elif pygame.Rect(810, 505, 120, 55).collidepoint(pos):

        current = get_rinses()

        if current < 5:

            set_rinses(current + 1)

    # ========================================================
    # START
    # ========================================================

    elif pygame.Rect(70, 650, 230, 80).collidepoint(pos):

        start_wash()

    # ========================================================
    # STOP
    # ========================================================

    elif pygame.Rect(330, 650, 230, 80).collidepoint(pos):

        stop_wash()


# ============================================================
# ГЛАВНЫЙ ЦИКЛ
# ============================================================

game_running = True

while game_running:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            game_running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:

            if event.button == 1:

                handle_click(event.pos)

    update_wash()

    draw_interface()

    pygame.display.flip()

    clock.tick(60)


pygame.quit()
sys.exit()