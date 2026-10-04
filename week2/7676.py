import pygame
import sys
import time

pygame.init()

WIDTH = 1000
HEIGHT = 800

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Communication 2024 v1.3 — Samsung 12 kg")

clock = pygame.time.Clock()

# =========================
# ШРИФТЫ
# =========================

def get_font(size, bold=False):
    return pygame.font.SysFont("arial", size, bold=bold)


FONT_SMALL = get_font(22)
FONT = get_font(28)
FONT_BIG = get_font(36, True)
FONT_HUGE = get_font(46, True)

# =========================
# ЦВЕТА
# =========================

WHITE = (245, 245, 245)
BLACK = (20, 20, 20)
DARK = (35, 38, 42)
GRAY = (110, 115, 120)
LIGHT_GRAY = (205, 208, 212)
GREEN = (50, 190, 90)
RED = (220, 55, 55)
BLUE = (65, 120, 210)
YELLOW = (230, 190, 45)

# =========================
# ПРОГРАММЫ
# =========================

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
    "Детские вещи + Постельное бельё + Пар"
]

# Максимальная температура каждой программы
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
    60   # Детские вещи + Постельное бельё + Пар
]

# =========================
# ЧТО СТИРАТЬ
# =========================

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

# =========================
# ПРАВИЛЬНЫЕ НАСТРОЙКИ
# =========================
# программа, температура, обороты, полоскания

correct = [
    (5, 60, 1200, 2),
    (0, 40, 1000, 3),
    (10, 40, 1000, 2),
    (9, 40, 800, 2),
    (1, 30, 800, 2),
    (1, 30, 800, 2),
    (9, 30, 800, 2),
    (0, 40, 1200, 2),
    (0, 40, 1000, 3),
    (3, 60, 1000, 3),
    (10, 40, 1000, 2),
    (9, 30, 800, 2),
    (12, 40, 800, 3),
    (1, 30, 800, 2),
    (4, 60, 1000, 2),
    (9, 30, 800, 2)
]

# =========================
# ТЕМПЕРАТУРА
# =========================

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

# =========================
# ОБОРОТЫ
# =========================

spin_values = [
    0,
    400,
    600,
    800,
    1000,
    1200
]

# =========================
# СОСТОЯНИЕ
# =========================

mission = 0
program = 0
temperature = 40
spin_index = 3
rinses = 2

running = False
stage = ""
start_time = 0
last_result = None
error_message = ""

# =========================
# ВСПОМОГАТЕЛЬНЫЕ ФУНКЦИИ
# =========================

def draw_text(text, x, y, font, color=BLACK, center=False):
    surface = font.render(str(text), True, color)

    if center:
        rect = surface.get_rect(center=(x, y))
    else:
        rect = surface.get_rect(topleft=(x, y))

    screen.blit(surface, rect)


def draw_button(rect, text, color, font=FONT, text_color=WHITE):
    pygame.draw.rect(screen, color, rect, border_radius=12)
    pygame.draw.rect(screen, BLACK, rect, 2, border_radius=12)

    draw_text(
        text,
        rect.centerx,
        rect.centery,
        font,
        text_color,
        center=True
    )


def show_error(message):
    global error_message
    error_message = message


def get_current_spin():
    return spin_values[spin_index]


def clamp_temperature_for_program():
    global temperature

    maximum = max_temperature[program]

    if maximum == 0:
        temperature = 0
        return

    if temperature > maximum:
        temperature = maximum

    if temperature == 0:
        temperature = 20


def calculate_correctness():
    target_program, target_temp, target_spin, target_rinses = correct[mission]

    score = 0

    # Программа — 40 баллов
    if program == target_program:
        score += 40

    # Температура — 25 баллов
    temp_difference = abs(temperature - target_temp)

    if temp_difference == 0:
        score += 25
    elif temp_difference <= 10:
        score += 21
    elif temp_difference <= 20:
        score += 17
    elif temp_difference <= 30:
        score += 12
    elif temp_difference <= 40:
        score += 7

    # Обороты — 20 баллов
    spin_difference = abs(get_current_spin() - target_spin)

    if spin_difference == 0:
        score += 20
    elif spin_difference <= 200:
        score += 17
    elif spin_difference <= 400:
        score += 14
    elif spin_difference <= 600:
        score += 9
    elif spin_difference <= 800:
        score += 5

    # Полоскания — 15 баллов
    rinse_difference = abs(rinses - target_rinses)

    if rinse_difference == 0:
        score += 15
    elif rinse_difference == 1:
        score += 11
    elif rinse_difference == 2:
        score += 7
    elif rinse_difference == 3:
        score += 3

    return score


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


def stop_wash():
    global running
    global stage

    running = False
    stage = "ОСТАНОВЛЕНО"


def update_wash():
    global running
    global stage
    global start_time
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

        last_result = calculate_correctness()

        # Следующее задание
        mission += 1

        if mission >= len(missions):
            mission = 0

# =========================
# ОТРИСОВКА
# =========================

def draw_interface():

    screen.fill((225, 228, 232))

    # =================================
    # ВЕРХНЯЯ ПАНЕЛЬ — ЧТО СТИРАТЬ
    # =================================

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

    # =================================
    # ОСНОВНОЙ БЛОК
    # =================================

    pygame.draw.rect(
        screen,
        DARK,
        (30, 160, WIDTH - 60, 430),
        border_radius=18
    )

    # Белый экран
    pygame.draw.rect(
        screen,
        WHITE,
        (65, 190, WIDTH - 130, 190),
        border_radius=12
    )

    # Название программы
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

    # Пар
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

    # =================================
    # СТРЕЛКИ ПРОГРАММ
    # =================================

    left_program = pygame.Rect(75, 400, 160, 70)
    right_program = pygame.Rect(765, 400, 160, 70)

    draw_button(
        left_program,
        "◀",
        BLUE,
        FONT_HUGE
    )

    draw_button(
        right_program,
        "▶",
        BLUE,
        FONT_HUGE
    )

    # =================================
    # ТЕМПЕРАТУРА
    # =================================

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
        f"{temperature} °C",
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

    # =================================
    # ОБОРОТЫ
    # =================================

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
        f"{get_current_spin()}",
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

    # =================================
    # ПОЛОСКАНИЯ
    # =================================

    draw_button(
        pygame.Rect(70, 505, 120, 55),
        "−",
        BLUE,
        FONT_BIG
    )

    draw_text(
        f"ПОЛОСКАНИЯ: {rinses}",
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

    # =================================
    # НИЖНЯЯ ПАНЕЛЬ
    # =================================

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

    # START
    start_button = pygame.Rect(70, 650, 230, 80)

    draw_button(
        start_button,
        "START",
        GREEN if not running else GRAY,
        FONT_BIG
    )

    # STOP
    stop_button = pygame.Rect(330, 650, 230, 80)

    draw_button(
        stop_button,
        "STOP",
        RED if running else GRAY,
        FONT_BIG
    )

    # Статус
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

    # =================================
    # ОШИБКА
    # =================================

    if error_message:
        draw_text(
            error_message,
            WIDTH // 2,
            785,
            FONT_SMALL,
            RED,
            center=True
        )


# =========================
# ОБРАБОТКА КЛИКОВ
# =========================

def handle_click(pos):

    global program
    global temperature
    global spin_index
    global rinses

    if running:
        # Во время стирки работает только STOP
        if pygame.Rect(330, 650, 230, 80).collidepoint(pos):
            stop_wash()

        return

    # =================================
    # ПРОГРАММА ВЛЕВО
    # =================================

    if pygame.Rect(75, 400, 160, 70).collidepoint(pos):

        program -= 1

        if program < 0:
            program = len(programs) - 1

        clamp_temperature_for_program()

    # =================================
    # ПРОГРАММА ВПРАВО
    # =================================

    elif pygame.Rect(765, 400, 160, 70).collidepoint(pos):

        program += 1

        if program >= len(programs):
            program = 0

        clamp_temperature_for_program()

    # =================================
    # ТЕМПЕРАТУРА МИНУС
    # =================================

    elif pygame.Rect(265, 440, 70, 60).collidepoint(pos):

        if max_temperature[program] == 0:
            show_error("ОШИБКА: ТЕМПЕРАТУРА НЕДОСТУПНА")
            return

        current_index = temperature_values.index(temperature)

        if current_index > 0:
            temperature = temperature_values[current_index - 1]

    # =================================
    # ТЕМПЕРАТУРА ПЛЮС
    # =================================

    elif pygame.Rect(485, 440, 70, 60).collidepoint(pos):

        if max_temperature[program] == 0:
            show_error("ОШИБКА: ТЕМПЕРАТУРА НЕДОСТУПНА")
            return

        current_index = temperature_values.index(temperature)

        if current_index < len(temperature_values) - 1:

            new_temperature = temperature_values[current_index + 1]

            if new_temperature <= max_temperature[program]:
                temperature = new_temperature
            else:
                show_error(
                    f"ОШИБКА: МАКСИМУМ {max_temperature[program]} °C"
                )

    # =================================
    # ОБОРОТЫ МИНУС
    # =================================

    elif pygame.Rect(575, 440, 70, 60).collidepoint(pos):

        if spin_index > 0:
            spin_index -= 1

    # =================================
    # ОБОРОТЫ ПЛЮС
    # =================================

    elif pygame.Rect(755, 440, 70, 60).collidepoint(pos):

        if spin_index < len(spin_values) - 1:
            spin_index += 1

    # =================================
    # ПОЛОСКАНИЯ МИНУС
    # =================================

    elif pygame.Rect(70, 505, 120, 55).collidepoint(pos):

        if rinses > 0:
            rinses -= 1

    # =================================
    # ПОЛОСКАНИЯ ПЛЮС
    # =================================

    elif pygame.Rect(810, 505, 120, 55).collidepoint(pos):

        if rinses < 5:
            rinses += 1

    # =================================
    # START
    # =================================

    elif pygame.Rect(70, 650, 230, 80).collidepoint(pos):

        start_wash()

    # =================================
    # STOP
    # =================================

    elif pygame.Rect(330, 650, 230, 80).collidepoint(pos):

        stop_wash()


# =========================
# ГЛАВНЫЙ ЦИКЛ
# =========================

running_program = True

while running_program:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running_program = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                handle_click(event.pos)

    update_wash()

    # Ошибка показывается недолго
    if error_message:
        # Убираем её через 2 секунды
        pass

    draw_interface()

    pygame.display.flip()

    clock.tick(60)

pygame.quit()
sys.exit()