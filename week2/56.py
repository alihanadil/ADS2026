import tkinter as tk
from tkinter import ttk, messagebox
import math
import time

MODEL = "SAMSUNG WF60F4E2W2W"

PROGRAMS = {
    "Хлопок": {"temp": 40, "spin": 1200, "minutes": 120},
    "Синтетика": {"temp": 40, "spin": 800, "minutes": 85},
    "Смешанные ткани": {"temp": 40, "spin": 1200, "minutes": 80},
    "Быстрая стирка 15": {"temp": 30, "spin": 800, "minutes": 15},
    "Детские вещи": {"temp": 60, "spin": 1000, "minutes": 135},
    "Ежедневная": {"temp": 40, "spin": 1200, "minutes": 62},
    "Шерсть": {"temp": 30, "spin": 400, "minutes": 45},
    "Очистка барабана": {"temp": 70, "spin": 800, "minutes": 95},
}

PHASES = [
    ("Стирка", 0.55),
    ("Полоскание", 0.25),
    ("Слив", 0.08),
    ("Отжим", 0.12),
]


class WasherSimulator:
    def __init__(self, root):
        self.root = root
        self.root.title("Samsung Washer Simulator")
        self.root.geometry("900x650")
        self.root.minsize(800, 600)
        self.root.configure(bg="#e9edf2")

        self.running = False
        self.paused = False
        self.total_seconds = 0
        self.remaining_seconds = 0
        self.last_tick = None
        self.spin_angle = 0
        self.animation_job = None
        self.timer_job = None

        self.program_var = tk.StringVar(value="Ежедневная")
        self.temp_var = tk.IntVar(value=40)
        self.spin_var = tk.IntVar(value=1200)
        self.intensive_var = tk.BooleanVar(value=False)
        self.prewash_var = tk.BooleanVar(value=False)
        self.extra_rinse_var = tk.BooleanVar(value=False)

        self.status_var = tk.StringVar(value="ГОТОВА")
        self.time_var = tk.StringVar(value="01:02")
        self.phase_var = tk.StringVar(
            value="Выберите программу и нажмите СТАРТ"
        )
        self.door_var = tk.StringVar(value="Дверца закрыта")
        self.speed_var = tk.StringVar(value="0 об/мин")

        self.build_ui()
        self.update_program_defaults()
        self.draw_drum()

    def build_ui(self):
        header = tk.Frame(self.root, bg="#142b49", height=76)
        header.pack(fill="x")
        header.pack_propagate(False)

        tk.Label(
            header, text="SAMSUNG",
            font=("Arial", 21, "bold"),
            fg="white", bg="#142b49"
        ).pack(side="left", padx=(22, 10))

        tk.Label(
            header, text="WASHER SIMULATOR",
            font=("Arial", 11, "bold"),
            fg="#a9c6e8", bg="#142b49"
        ).pack(side="left", pady=(10, 0))

        tk.Label(
            header, text="6 kg  |  DIGITAL INVERTER",
            font=("Arial", 10),
            fg="white", bg="#142b49"
        ).pack(side="right", padx=22)

        body = tk.Frame(self.root, bg="#e9edf2")
        body.pack(fill="both", expand=True, padx=16, pady=16)

        left = tk.Frame(
            body, bg="#f8fafc", bd=1, relief="solid"
        )
        left.pack(
            side="left", fill="both", expand=True, padx=(0, 12)
        )

        tk.Label(
            left, text=MODEL,
            font=("Arial", 13, "bold"),
            bg="#f8fafc", fg="#142b49"
        ).pack(pady=(14, 3))

        tk.Label(
            left, text="СИМУЛЯЦИЯ СТИРАЛЬНОЙ МАШИНЫ",
            font=("Arial", 9),
            bg="#f8fafc", fg="#617084"
        ).pack()

        screen = tk.Frame(
            left, bg="#18232e", bd=3, relief="ridge"
        )
        screen.pack(fill="x", padx=20, pady=14)

        top = tk.Frame(screen, bg="#18232e")
        top.pack(fill="x", padx=12, pady=(8, 2))

        tk.Label(
            top, textvariable=self.status_var,
            bg="#18232e", fg="#6ef2b0",
            font=("Consolas", 11, "bold")
        ).pack(side="left")

        tk.Label(
            top, textvariable=self.speed_var,
            bg="#18232e", fg="#c9e3ff",
            font=("Consolas", 10)
        ).pack(side="right")

        tk.Label(
            screen, textvariable=self.time_var,
            bg="#18232e", fg="white",
            font=("Consolas", 30, "bold")
        ).pack(pady=2)

        tk.Label(
            screen, textvariable=self.phase_var,
            bg="#18232e", fg="#a9c6e8",
            font=("Arial", 9), wraplength=400
        ).pack(pady=(0,

        = tk.Canvas(
            left, width=350, height=250,
            bg="#f8fafc", highlightthickness=0
        )
        self.canvas.pack(fill="both", expand=True, padx=10)

        tk.Label(
            left, textvariable=self.door_var,
            bg="#f8fafc", fg="#617084",
            font=("Arial", 9)
        ).pack(pady=(0, 10))

        controls = tk.Frame(
            body, bg="white", bd=1,
            relief="solid", width=320
        )
        controls.pack(side="right", fill="y")
        controls.pack_propagate(False)

        tk.Label(
            controls, text="ПАНЕЛЬ УПРАВЛЕНИЯ",
            font=("Arial", 12, "bold"),
            bg="white", fg="#142b49"
        ).pack(anchor="w", padx=16, pady=(16, 10))

        tk.Label(
            controls, text="Программа",
            bg="white", fg="#334155"
        ).pack(anchor="w", padx=16)

        self.program_box = ttk.Combobox(
            controls,
            textvariable=self.program_var,
            values=list(PROGRAMS.keys()),
            state="readonly"
        )
        self.program_box.pack(
            fill="x", padx=16, pady=(4, 10)
        )
        self.program_box.bind(
            "<<ComboboxSelected>>",
            lambda _event: self.update_program_defaults()
        )

        tk.Label(
            controls, text="Температура",
            bg="white", fg="#334155"
        ).pack(anchor="w", padx=16)

        temp_row = tk.Frame(controls, bg="white")
        temp_row.pack(fill="x", padx=16)

        self.temp_label = tk.Label(
            temp_row, text="40 °C", width=8, anchor="w",
            bg="white", fg="#142b49",
            font=("Arial", 10, "bold")
        )
        self.temp_label.pack(side="left")

        self.temp_scale = ttk.Scale(
            temp_row, from_=0, to=95,
            command=self.change_temp
        )
        self.temp_scale.pack(
            side="right", fill="x", expand=True
        )
        self.temp_scale.set(40)

        tk.Label(
            controls, text="Отжим",
            bg="white", fg="#334155"
        ).pack(anchor="w", padx=16, pady=(10, 0))

        self.spin_box = ttk.Combobox(
            controls,
            textvariable=self.spin_var,
            values=[no, 400, 800, 1000, 1200],
            state="readonly"
        )
        self.spin_box.pack(
            fill="x", padx=16, pady=(4, 10)
        )

        options = tk.LabelFrame(
            controls, text="Дополнительные функции",
            bg="white", fg="#334155", padx=8, pady=5
        )
        options.pack(fill="x", padx=16, pady=4)

        tk.Checkbutton(
            options, text="Интенсивная",
            variable=self.intensive_var,
            bg="white", activebackground="white",
            anchor="w", command=self.update_duration_label
        ).pack(fill="x")

        tk.Checkbutton(
            options, text="Предварительная стирка",
            variable=self.prewash_var,
            bg="white", activebackground="white",
            anchor="w", command=self.update_duration_label
        ).pack(fill="x")

        tk.Checkbutton(
            options, text="Доп. полоскание",
            variable=self.extra_rinse_var,
            bg="white", activebackground="white",
            anchor="w", command=self.update_duration_label
        ).pack(fill="x")

        self.duration_label = tk.Label(
            controls,
            text="Примерная длительность: 01:02",
            bg="white", fg="#475569",
            font=("Arial", 9)
        )
        self.duration_label.pack(
            anchor="w", padx=16, pady=(8, 3)
        )

        buttons = tk.Frame(controls, bg="white")
        buttons.pack(fill="x", padx=16, pady=(10, 6))

        self.start_button = tk.Button(
            buttons, text="▶ СТАРТ",
            command=self.start_or_pause,
            bg="#087f5b", fg="white",
            activebackground="#066649",
            activeforeground="white",
            font=("Arial", 10, "bold"),
            relief="flat", padx=8, pady=9
        )
        self.start_button.pack(
            side="left", fill="x", expand=True, padx=(0, 4)
        )

        tk.Button(
            buttons, text="■ СТОП",
            command=self.stop_cycle,
            bg="#c2413b", fg="white",
            activebackground="#9f302b",
            activeforeground="white",
            font=("Arial", 10, "bold"),
            relief="flat", padx=8, pady=9
        ).pack(
            side="left", fill="x", expand=True, padx=(4, 0)
        )

        tk.Button(
            controls, text="↻ СБРОС",
            command=self.reset_cycle,
            bg="#e2e8f0", fg="#142b49",
            relief="flat", font=("Arial", 10, "bold"),
            pady=7
        ).pack(fill="x", padx=16, pady=(2, 12))

        tk.Label(
            self.root,
            text="Ускоренный режим: 1 секунда ≈ 1 минута программы. "
                 "Не управляет реальной машиной.",
            bg="#e9edf2", fg="#64748b",
            font=("Arial", 9)
        ).pack(pady=(0, 8))

    def change_temp(self, value):
        temp = int(round(float(value) / 5) * 5)
        self.temp_var.set(temp)
        self.temp_label.config(text=f"{temp} °C")
        self.update_duration_label()

    def update_program_defaults(self):
        if self.running:
            return

        program = PROGRAMS[self.program_var.get()]
        self.temp_var.set(program["temp"])
        self.temp_scale.set(program["temp"])
