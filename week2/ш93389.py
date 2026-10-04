import pygame
import sys

pygame.init()

screen = pygame.display.set_mode((720, 1280))
pygame.display.set_caption("Samsung 12 kg — Communication 2024 v1.3")
clock = pygame.time.Clock()

fonts = {}


def font(size):
    if size not in fonts:
        fonts[size] = pygame.font.Font(None, size)
    return fonts[size]


def text(value, x, y, size):
    img = font(size).render(str(value), True, (20, 20, 20))
    screen.blit(img, (x, y))


def button(x, y, w, h, name, color):
    pygame.draw.rect(screen, color, (x, y, w, h), border_radius=16)
    pygame.draw.rect(
        screen,
        (60, 60, 60),
        (x, y, w, h),
        3,
        border_radius=16
    )

    img = font(42).render(name, True, (20, 20, 20))
    rect = img.get_rect(center=(x + w // 2, y + h // 2))
    screen.blit(img, rect)


# ==========================================================
# ПРОГРАММЫ
# ==========================================================

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
    "Экономичная ECO",
    "Детские вещи + Постельное бельё + Пар"
]

# Максимальная температура каждой программы
max_temp = [
    95,
    60,
    40,
    60,
    60,
    60,
    40,
    0,
    40,
    40,
    60,
    60,
    60
]


# ==========================================================
# 16 ЗАДАНИЙ
# ==========================================================

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


# ==========================================================
# ПРАВИЛЬНЫЕ НАСТРОЙКИ
# ==========================================================
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
    (12, 40, 800, 3),   # новая программа с паром
    (1, 30, 800, 2),
    (4, 60, 1000, 2),
    (9, 30, 800, 2)
]


# ==========================================================
# ОБОРОТЫ
# ==========================================================

spin_values = [
    0,
    400,
    600,
    800,
    1000,
    1200,
    1400
]


# ==========================================================
# СОСТОЯНИЕ
# ==========================================================

mission = 0
program = 0
temperature = 40
spin_index = 4
rinses = 2

running = False
stage = "ГОТОВА"
start_time = 0

last_result = None
error_message = ""


# ==========================================================
# ПРАВИЛЬНОСТЬ
# ==========================================================

def calculate_score():

    right_program = correct[mission][0]
    right_temp = correct[mission][1]
    right_spin = correct[mission][2]
    right_rinses = correct[mission][3]

    score = 0

    # Программа — 40%
    if program == right_program:
        score += 40

    # Температура — 25%
    temp_difference = abs(temperature - right_temp)

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

    # Отжим — 20%
    spin_difference = abs(spin_values[spin_index] - right_spin)

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

    # Полоскания — 15%
    rinse_difference = abs(rinses - right_rinses)

    if rinse_difference == 0:
        score += 15
    elif rinse_difference == 1:
        score += 11
    elif rinse_difference == 2:
        score += 7
    elif rinse_difference == 3:
        score += 3

    return score


# ==========================================================
# ГЛАВНЫЙ ЦИКЛ
# ==========================================================

while True:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:

            x, y = event.pos

            # ==================================================
            # START
            # ==================================================

            if 40 <= x <= 330 and 950 <= y <= 1070:

                if not running:

                    running = True
                    start_time = pygame.time.get_ticks()
                    stage = "НАБОР ВОДЫ"
                    last_result = None
                    error_message = ""

            # ==================================================
            # STOP
            # ==================================================

            elif 390 <= x <= 680 and 950 <= y <= 1070:

                if running:
                    running = False
                    stage = "ОСТАНОВЛЕНО"

            # ==================================================
            # НАСТРОЙКИ
            # ==================================================

            elif not running:

                # ПРОГРАММА -

                if 40 <= x <= 170 and 300 <= y <= 390:

                    program -= 1

                    if program < 0:
                        program = len(programs) - 1

                    if temperature > max_temp[program]:
                        temperature = max_temp[program]

                    error_message = ""

                # ПРОГРАММА +

                elif 550 <= x <= 680 and 300 <= y <= 390:

                    program += 1

                    if program >= len(programs):
                        program = 0

                    if temperature > max_temp[program]:
                        temperature = max_temp[program]

                    error_message = ""

                # ТЕМПЕРАТУРА -

                elif 40 <= x <= 170 and 470 <= y <= 550:

                    if max_temp[program] == 0:
                        temperature = 0
                    else:
                        temperature -= 10

                        if temperature < 20:
                            temperature = 20

                    error_message = ""

                # ТЕМПЕРАТУРА +

                elif 550 <= x <= 680 and 470 <= y <= 550:

                    if max_temp[program] == 0:

                        error_message = (
                            "ОШИБКА: ТЕМПЕРАТУРА НЕДОСТУПНА"
                        )

                    else:

                        new_temp = temperature + 10

                        if new_temp > max_temp[program]:

                            error_message = (
                                "ОШИБКА: МАКСИМУМ "
                                + str(max_temp[program])
                                + " °C"
                            )

                        else:
                            temperature = new_temp
                            error_message = ""

                # ОТЖИМ -

                elif 40 <= x <= 170 and 580 <= y <= 660:

                    spin_index -= 1

                    if spin_index < 0:
                        spin_index = len(spin_values) - 1

                # ОТЖИМ +

                elif 550 <= x <= 680 and 580 <= y <= 660:

                    spin_index += 1

                    if spin_index >= len(spin_values):
                        spin_index = 0

                # ПОЛОСКАНИЯ -

                elif 40 <= x <= 170 and 690 <= y <= 770:

                    rinses -= 1

                    if rinses < 0:
                        rinses = 5

                # ПОЛОСКАНИЯ +

                elif 550 <= x <= 680 and 690 <= y <= 770:

                    rinses += 1

                    if rinses > 5:
                        rinses = 0


    # ==========================================================
    # СТИРКА
    # ==========================================================

    if running:

        elapsed = pygame.time.get_ticks() - start_time

        if elapsed < 1500:
            stage = "НАБОР ВОДЫ"

        elif elapsed < 5000:
            stage = "СТИРКА"

        elif elapsed < 6500:
            stage = "ПОЛОСКАНИЕ"

        elif elapsed < 8000:
            stage = "СЛИВ"

        elif elapsed < 10000:
            stage = "ОТЖИМ"

        else:

            running = False
            stage = "ЗАВЕРШЕНО"

            last_result = calculate_score()

            # Следующее задание
            if mission < len(missions) - 1:
                mission += 1
            else:
                mission = 0


    # ==========================================================
    # ЭКРАН
    # ==========================================================

    screen.fill((235, 235, 235))

    text("SAMSUNG 12 kg", 40, 20, 52)

    text("ЧТО СТИРАТЬ", 40, 85, 58)

    text(missions[mission], 40, 150, 32)

    pygame.draw.line(
        screen,
        (70, 70, 70),
        (30, 220),
        (690, 220),
        3
    )

    # ==========================================================
    # ПРОГРАММА
    # ==========================================================

    text("ПРОГРАММА", 40, 250, 42)

    button(
        40, 300, 130, 90,
        "<",
        (220, 220, 220)
    )

    button(
        550, 300, 130, 90,
        ">",
        (220, 220, 220)
    )

    pygame.draw.rect(
        screen,
        (255, 255, 255),
        (190, 290, 340, 110),
        border_radius=16
    )

    program_name = programs[program]

    # Чтобы длинное название не вылезало
    if len(program_name) > 22:
        program_size = 25
    elif len(program_name) > 15:
        program_size = 31
    else:
        program_size = 38

    img = font(program_size).render(
        program_name,
        True,
        (20, 20, 20)
    )

    rect = img.get_rect(
        center=(360, 345)
    )

    screen.blit(img, rect)

    # ==========================================================
    # ТЕМПЕРАТУРА
    # ==========================================================

    text("ТЕМПЕРАТУРА", 40, 430, 42)

    button(
        40, 470, 130, 80,
        "-",
        (220, 220, 220)
    )

    button(
        550, 470, 130, 80,
        "+",
        (220, 220, 220)
    )

    text(
        str(temperature) + " °C",
        300,
        485,
        50
    )

    # ==========================================================
    # ОТЖИМ
    # ==========================================================

    text("ОТЖИМ", 40, 560, 42)

    button(
        40, 580, 130, 80,
        "-",
        (220, 220, 220)
    )

    button(
        550, 580, 130, 80,
        "+",
        (220, 220, 220)
    )

    text(
        str(spin_values[spin_index]) + " ОБ/МИН",
        235,
        595,
        42
    )

    # ==========================================================
    # ПОЛОСКАНИЯ
    # ==========================================================

    text("ПОЛОСКАНИЯ", 40, 670, 42)

    button(
        40, 690, 130, 80,
        "-",
        (220, 220, 220)
    )

    button(
        550, 690, 130, 80,
        "+",
        (220, 220, 220)
    )

    text(
        str(rinses),
        350,
        705,
        52
    )

    # ==========================================================
    # ОШИБКА
    # ==========================================================

    if error_message:
        text(
            error_message,
            45,
            790,
            27
        )

    # ==========================================================
    # РЕЗУЛЬТАТ
    # ==========================================================

    if last_result is not None:

        text(
            "ПРАВИЛЬНОСТЬ: "
            + str(last_result)
            + "%",
            205,
            825,
            42
        )

    # ==========================================================
    # START
    # ==========================================================

    if running:
        start_color = (70, 210, 90)
    else:
        start_color = (180, 235, 180)

    button(
        40,
        950,
        290,
        110,
        "START",
        start_color
    )

    # ==========================================================
    # STOP
    # ==========================================================

    if running:
        stop_color = (235, 70, 70)
    else:
        stop_color = (220, 220, 220)

    button(
        390,
        950,
        290,
        110,
        "STOP",
        stop_color
    )

    # ==========================================================
    # СТАТУС
    # ==========================================================

    text(
        stage,
        285,
        1100,
        42
    )

    pygame.display.flip()
    clock.tick(30)
