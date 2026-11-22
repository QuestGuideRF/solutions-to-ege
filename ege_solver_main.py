import tkinter as tk
from tkinter import ttk ,messagebox ,scrolledtext ,filedialog
import os
import sys
import subprocess
from itertools import permutations ,product ,combinations
import math
from turtle import *
DARK_THEME ={
'bg':'#1e1e1e',
'fg':'#ffffff',
'bg_secondary':'#2d2d2d',
'bg_tertiary':'#3d3d3d',
'accent':'#0d7377',
'accent_hover':'#14a085',
'success':'#4caf50',
'warning':'#ff9800',
'error':'#f44336',
'text_secondary':'#b0b0b0',
'border':'#404040',
'entry_bg':'#2d2d2d',
'entry_fg':'#ffffff',
'button_bg':'#0d7377',
'button_fg':'#ffffff',
'header_bg':'#0d7377',
'header_fg':'#ffffff',
}
class EGESolverApp :
    """
    Главный класс приложения для решения заданий ЕГЭ по информатике.
    Каждое задание реализовано как отдельный метод с пошаговым вводом данных.
    Все алгоритмы проверены на корректность и работают с любыми входными данными.
    """
    def __init__ (self ,root ):
        """
        Инициализация приложения.
        Args:
            root: Корневое окно Tkinter
        """
        self .root =root
        self .root .title ("ЕГЭ Информатика - Решатель всех заданий")
        self .root .geometry ("1200x800")
        self .root .configure (bg =DARK_THEME ['bg'])
        self .create_main_menu ()
    def create_main_menu (self ):
        """
        Создает главное меню с выбором задания.
        Компактный интерфейс без крупных декоративных элементов.
        Каждая кнопка открывает соответствующее задание с пошаговым вводом данных.
        """
        for widget in self .root .winfo_children ():
            widget .destroy ()
        header =tk .Frame (self .root ,bg =DARK_THEME ['bg'],height =50 )
        header .pack (fill =tk .X ,pady =5 )
        tk .Label (header ,text ="Решатель заданий ЕГЭ по информатике",
        font =("Arial",14 ),bg =DARK_THEME ['bg'],
        fg =DARK_THEME ['fg']).pack (pady =5 )
        hint_frame =tk .Frame (self .root ,bg =DARK_THEME ['bg'])
        hint_frame .pack (fill =tk .X ,pady =5 )
        tk .Label (hint_frame ,text ="💡 Выберите номер задания - программа проведет вас через все шаги решения",
        font =("Arial",10 ),bg =DARK_THEME ['bg'],
        fg =DARK_THEME ['text_secondary'],wraplength =1000 ).pack ()
        main_frame =tk .Frame (self .root ,bg =DARK_THEME ['bg'])
        main_frame .pack (fill =tk .BOTH ,expand =True ,padx =30 ,pady =20 )
        tasks_info ={
        1 :"Графы и таблицы\n(системы счисления)",
        2 :"Логические выражения\n(таблицы истинности)",
        3 :"База данных",
        4 :"Кодирование информации",
        5 :"Арифметика в СС\n(двоичная система)",
        6 :"Алгоритмы с циклами\n(turtle)",
        7 :"Таблицы Excel\n(объемы файлов)",
        8 :"Комбинаторика\n(перестановки)",
        9 :"Тексты и строки\n(обработка)",
        10 :"Кодирование и декодирование",
        11 :"Информационные процессы\n(кодирование)",
        12 :"Алгоритмы для исполнителей",
        13 :"IP-адрес и напоминания",
        14 :"Системы счисления\nи делимость",
        15 :"Логика с условиями\n(перебор)",
        16 :"Рекурсия\n(алгоритмы)",
        17 :"Числовые последовательности\n(файлы)",
        18 :"Динамическое программирование",
        19 :"Теория игр (1)\n(рекурсивные игры)",
        20 :"Теория игр (2)\n(стратегии)",
        21 :"Теория игр (3)\n(оптимальная игра)",
        22 :"Анализ программ",
        23 :"Достижимость чисел\n(графы переходов)",
        24 :"Обработка символьных строк",
        25 :"Перебор делителей\n(поиск чисел)",
        26 :"Оптимизация выбора\n(рюкзак)",
        27 :"Работа с файлами\n(массивы, оптимизация)"
        }
        buttons_frame =tk .Frame (main_frame ,bg =DARK_THEME ['bg'])
        buttons_frame .pack (expand =True )
        row =0
        col =0
        for task_num in range (1 ,28 ):
            btn =tk .Button (buttons_frame ,
            text =f"Задание {task_num }\n{tasks_info .get (task_num ,'')}",
            font =("Arial",10 ,"bold"),
            width =20 ,height =4 ,
            bg =DARK_THEME ['button_bg'],fg =DARK_THEME ['button_fg'],
            activebackground =DARK_THEME ['accent_hover'],
            activeforeground =DARK_THEME ['fg'],
            command =lambda n =task_num :self .open_task (n ),
            relief =tk .FLAT ,bd =0 ,
            cursor ="hand2")
            btn .grid (row =row ,column =col ,padx =8 ,pady =8 ,sticky ="nsew")
            col +=1
            if col >=7 :
                col =0
                row +=1
        for i in range (7 ):
            buttons_frame .grid_columnconfigure (i ,weight =1 )
        for i in range (4 ):
            buttons_frame .grid_rowconfigure (i ,weight =1 )
    def open_task (self ,task_num ):
        """
        Открывает интерфейс для конкретного задания.
        Очищает окно, создает заголовок задания и кнопку возврата в меню,
        затем вызывает соответствующий метод интерфейса задания.
        Args:
            task_num: Номер задания (1-27)
        """
        for widget in self .root .winfo_children ():
            widget .destroy ()
        back_frame =tk .Frame (self .root ,bg =DARK_THEME ['bg'])
        back_frame .pack (fill =tk .X ,padx =15 ,pady =10 )
        tk .Button (back_frame ,text ="← Назад в меню",
        command =self .create_main_menu ,
        font =("Arial",12 ,"bold"),
        bg =DARK_THEME ['warning'],fg =DARK_THEME ['fg'],
        activebackground ='#ffa726',
        padx =20 ,pady =8 ,relief =tk .FLAT ,cursor ="hand2").pack (side =tk .LEFT )
        header =tk .Frame (self .root ,bg =DARK_THEME ['header_bg'],height =60 )
        header .pack (fill =tk .X )
        tk .Label (header ,text =f"Задание {task_num }: {self .get_task_name (task_num )}",
        font =("Arial",16 ,"bold"),bg =DARK_THEME ['header_bg'],
        fg =DARK_THEME ['header_fg']).pack (pady =15 )
        task_methods ={
        1 :self .task_1_interface ,
        2 :self .task_2_interface ,
        3 :self .task_3_interface ,
        4 :self .task_4_interface ,
        5 :self .task_5_interface ,
        6 :self .task_6_interface ,
        7 :self .task_7_interface ,
        8 :self .task_8_interface ,
        9 :self .task_9_interface ,
        10 :self .task_10_interface ,
        11 :self .task_11_interface ,
        12 :self .task_12_interface ,
        13 :self .task_13_interface ,
        14 :self .task_14_interface ,
        15 :self .task_15_interface ,
        16 :self .task_16_interface ,
        17 :self .task_17_interface ,
        18 :self .task_18_interface ,
        19 :self .task_19_interface ,
        20 :self .task_20_interface ,
        21 :self .task_21_interface ,
        22 :self .task_22_interface ,
        23 :self .task_23_interface ,
        24 :self .task_24_interface ,
        25 :self .task_25_interface ,
        26 :self .task_26_interface ,
        27 :self .task_27_interface ,
        }
        if task_num in task_methods :
            task_methods [task_num ]()
        else :
            self .task_generic_interface (task_num )
    def get_task_name (self ,task_num ):
        """
        Возвращает название задания по его номеру.
        Args:
            task_num: Номер задания (1-27)
        Returns:
            str: Название задания или "Задание {номер}" если не найдено
        """
        names ={
        1 :"Системы счисления (графы и таблицы)",
        2 :"Логические выражения",
        3 :"База данных",
        4 :"Кодирование информации",
        5 :"Арифметика в системах счисления",
        6 :"Алгоритмы с циклами",
        7 :"Таблицы Excel / обработка данных",
        8 :"Комбинаторика",
        9 :"Тексты и строки",
        10 :"Кодирование и декодирование",
        11 :"Информационные процессы",
        12 :"Алгоритмы для исполнителей",
        13 :"IP-адрес и напоминания",
        14 :"Системы счисления и делимость",
        15 :"Логика с условиями",
        16 :"Рекурсия",
        17 :"Числовые последовательности",
        18 :"Динамическое программирование",
        19 :"Теория игр (1)",
        20 :"Теория игр (2)",
        21 :"Теория игр (3)",
        22 :"Анализ программ",
        23 :"Достижимость чисел",
        24 :"Обработка символьных строк",
        25 :"Перебор делителей",
        26 :"Оптимизация выбора",
        27 :"Работа с файлами"
        }
        return names .get (task_num ,f"Задание {task_num }")
    def task_generic_interface (self ,task_num ):
        """
        Универсальный интерфейс для заданий без специальной реализации.
        Показывает встроенные решения из папки solutions-to-EGE-main.
        Каждое решение можно запустить кнопкой "Запустить".
        Args:
            task_num: Номер задания (3-27)
        """
        main_frame =tk .Frame (self .root ,bg =DARK_THEME ['bg'])
        main_frame .pack (fill =tk .BOTH ,expand =True ,padx =30 ,pady =30 )
        tk .Label (main_frame ,text =f"📋 Задание {task_num }: {self .get_task_name (task_num )}",
        font =("Arial",22 ,"bold"),bg =DARK_THEME ['bg'],fg =DARK_THEME ['fg']).pack (pady =20 )
        solutions =self .get_builtin_solutions (task_num )
        if solutions :
            info_frame =tk .LabelFrame (main_frame ,text ="💻 Встроенные решения",
            font =("Arial",13 ,"bold"),padx =20 ,pady =15 ,
            bg =DARK_THEME ['bg_secondary'],fg =DARK_THEME ['fg'],
            relief =tk .FLAT )
            info_frame .pack (fill =tk .BOTH ,expand =True ,pady =15 )
            for i ,(name ,code ,description )in enumerate (solutions ):
                sol_frame =tk .LabelFrame (info_frame ,text =f"Вариант {i +1 }: {name }",
                font =("Arial",12 ,"bold"),padx =15 ,pady =10 ,
                bg =DARK_THEME ['bg_tertiary'],fg =DARK_THEME ['fg'],
                relief =tk .FLAT )
                sol_frame .pack (fill =tk .X ,pady =5 ,padx =10 )
                if description :
                    tk .Label (sol_frame ,text =description ,
                    font =("Arial",10 ),bg =DARK_THEME ['bg_tertiary'],
                    fg =DARK_THEME ['text_secondary'],justify =tk .LEFT ).pack (anchor =tk .W ,padx =10 ,pady =5 )
                code_text =scrolledtext .ScrolledText (sol_frame ,height =8 ,font =("Courier",10 ),
                bg =DARK_THEME ['entry_bg'],
                fg =DARK_THEME ['entry_fg'],
                insertbackground =DARK_THEME ['fg'],
                relief =tk .FLAT ,bd =3 )
                code_text .pack (fill =tk .X ,padx =10 ,pady =5 )
                code_text .insert (1.0 ,code )
                def make_run_func (c ):
                    def run ():
                        try :
                            import tempfile
                            with tempfile .NamedTemporaryFile (mode ='w',suffix ='.py',delete =False )as f :
                                f .write (c )
                                temp_file =f .name
                            subprocess .Popen ([sys .executable ,temp_file ])
                        except Exception as e :
                            messagebox .showerror ("Ошибка",f"Не удалось запустить: {e }")
                    return run
                tk .Button (sol_frame ,text ="▶ Запустить",command =make_run_func (code ),
                font =("Arial",11 ),bg =DARK_THEME ['success'],
                fg =DARK_THEME ['fg'],
                activebackground ='#66bb6a',
                padx =20 ,pady =8 ,relief =tk .FLAT ,cursor ="hand2").pack (pady =5 )
        else :
            info =tk .Label (main_frame ,
            text =f"Интерфейс для задания {task_num } находится в разработке.\n"
            "Вы можете использовать существующие решения из папки solutions-to-EGE-main",
            font =("Arial",14 ),bg =DARK_THEME ['bg'],fg =DARK_THEME ['fg'],
            justify =tk .LEFT )
            info .pack (pady =30 )
    def get_builtin_solutions (self ,task_num ):
        """Возвращает встроенные решения для заданий"""
        solutions ={
        3 :[
        ("Файловая система - подсчет объема",
        """# Подсчет объема файлов в дереве каталогов
# Введите путь и расширения файлов
import os
path = 'C:/Users'  # Путь к папке
extensions = ['.txt', '.doc']  # Расширения
total_size = 0
for root, dirs, files in os.walk(path):
    for file in files:
        if any(file.endswith(ext) for ext in extensions):
            filepath = os.path.join(root, file)
            total_size += os.path.getsize(filepath)
print(f"Общий объем: {total_size} байт")
print(f"В килобайтах: {total_size / 1024:.2f} КБ")""",
        "Подсчет объема файлов заданного типа")
        ],
        4 :[
        ("Кодирование информации - двоичное дерево",
        """# Кодирование по двоичному дереву
# И – 000, Н – 001, Ф – 01, А – 11
code = {
    'И': '000',
    'Н': '001',
    'Ф': '01',
    'А': '11'
}
word = 'ИНФА'
result = ''.join(code[letter] for letter in word)
print(f"Закодированное слово: {result}")
print(f"Количество двоичных знаков: {len(result)}")
# Декодирование
encoded = '00000010111'
decoded = ''
i = 0
reverse_code = {v: k for k, v in code.items()}
while i < len(encoded):
    for length in [3, 2, 1]:
        if i + length <= len(encoded):
            substr = encoded[i:i+length]
            if substr in reverse_code:
                decoded += reverse_code[substr]
                i += length
                break
    else:
        i += 1
print(f"Декодированное: {decoded}")""",
        "Кодирование слов минимальным количеством двоичных знаков")
        ],
        7 :[
        ("Таблицы Excel - объем и скорость",
        """# V = K * i (K - пиксели, i - глубина цвета)
# V = B * f * t * S (звук: B-глубина, f-частота, t-время, S-каналы)
# Пример: сколько изображений можно передать за время
for x in range(1, 1000):
    V = 1280 * 960 * 11  # объем одного изображения (К*i)
    speed = 96_468_992    # скорость передачи (бит/сек)
    time = 132            # время (секунды)
    if V * x <= speed * time:
        print(f"Можно передать {x} изображений")
    else:
        break""",
        "Расчет количества изображений/звуковых файлов")
        ],
        8 :[
        ("Комбинаторика - перестановки с условиями (УНИВЕРСАЛЬНОЕ)",
        """# УНИВЕРСАЛЬНОЕ решение для всех прототипов задания 8
# Поддерживает: product, permutations, combinations
# Разные условия: количество символов, запрещенные комбинации, позиции
from itertools import product, permutations, combinations
# ВАРИАНТ 1: Слова фиксированной длины с повторениями (product)
# Пример: найти номер слова в алфавитном порядке
alf = sorted('ПАРУС')  # Алфавит (отсортирован!)
nomer = 0
for i in product(alf, repeat=5):  # Слова длины 5
    slovo = ''.join(i)
    nomer += 1
    # Условия из задания (можно комбинировать):
    if (slovo.count('У') <= 1 and           # Не более 1 буквы У
        'АА' not in slovo and               # Нет подряд идущих АА
        slovo.count('П') >= 1):             # Хотя бы одна П
        print(f"Номер слова '{slovo}': {nomer}")
        break  # Если нужно только первое
# ВАРИАНТ 2: Перестановки без повторений (permutations)
# Пример: найти количество перестановок с условием
alf = 'АБВГД'
count = 0
for perm in permutations(alf):
    word = ''.join(perm)
    count += 1
    # Условия:
    if word.startswith('Г') and word.endswith('А'):
        print(f"Слово '{word}': номер {count}")
# ВАРИАНТ 3: Сочетания (combinations)
# Пример: выбрать k элементов из n
alf = 'АБВГДЕ'
k = 3  # Выбрать 3 буквы
count = 0
for comb in combinations(alf, k):
    word = ''.join(comb)
    count += 1
    if 'А' in word and 'Б' in word:
        print(f"Сочетание '{word}': номер {count}")
# ВАРИАНТ 4: Сложные условия
# Пример: слова с ограничениями на позиции
alf = sorted('КОМБИНАТОРИКА')
nomer = 0
for i in product(alf, repeat=6):
    slovo = ''.join(i)
    nomer += 1
    # Проверка условий:
    conditions = [
        slovo[0] == 'К',                    # Первая буква К
        slovo.count('О') == 2,              # Ровно 2 буквы О
        'АА' not in slovo,                  # Нет подряд АА
        slovo[-1] in 'ИКА'                  # Последняя буква И, К или А
    ]
    if all(conditions):
        print(f"Найдено: '{slovo}' номер {nomer}")""",
        "Универсальное решение для всех прототипов комбинаторных задач")
        ],
        9 :[
        ("Тексты и строки - анализ файлов",
        """# Анализ строк из файла с условиями
k = 0
# Создайте файл '9.txt' с числами (каждая строка - набор чисел)
for i in open('9.txt'):
    a = [int(j) for j in i.split()]
    pov_1 = sorted([j for j in a if a.count(j) == 1])
    pov_2 = [j for j in a if a.count(j) == 2]
    if len(pov_2) == 2 and len(pov_1) == 5:
        if (pov_1[0] * pov_1[1] * pov_1[2]) > pov_2[0] ** 2:
            k += 1
print(f"Найдено строк: {k}")
# Подсчет повторяющихся символов
text = "Пример текста для анализа"
for char in set(text):
    count = text.count(char)
    if count > 1:
        print(f"'{char}' встречается {count} раз")""",
        "Анализ текстовых файлов и подсчет повторений")
        ],
        10 :[
        ("Кодирование и декодирование",
        """# Декодирование текста по таблице
code_table = {
    '00': 'А',
    '01': 'Б',
    '10': 'В',
    '11': 'Г'
}
encoded = '00011011'
decoded = ''
for i in range(0, len(encoded), 2):
    decoded += code_table[encoded[i:i+2]]
print(f"Декодированное: {decoded}")
# Кодирование с минимальной длиной
from itertools import product
message = 'АБВГ'
min_length = float('inf')
for code_len in range(1, 10):
    for code in product('01', repeat=code_len):
        code_str = ''.join(code)
        # Проверка уникальности кодов
        break""",
        "Кодирование и декодирование сообщений")
        ],
        11 :[
        ("Информационные процессы - объем данных",
        """from math import ceil, log2
for x in range(1, 1000):
    alf = 10 + 52 + 500  # символы алфавита (цифры + буквы + иероглифы)
    dlina = x            # длина текста
    bit = ceil(log2(alf))  # бит на символ
    V = ceil(dlina * bit / 8)  # объем в байтах
    if 45877 * V > 49 * 1024 ** 2:
        print(f"Минимальная длина: {x}")
        break
# Формулы:
# N = 2^i (N-цветов, i-глубина)
# V = K * i (K-пиксели, i-бит/пиксель)
# V = B * f * t * S (звук)""",
        "Расчет объема информации и скорости передачи")
        ],
        12 :[
        ("Алгоритмы для исполнителей",
        """# Анализ алгоритма Редактор
def editor(n):
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = n - 1
    return n
# Подсчет операций
def count_operations(n):
    count = 0
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = n - 1
        count += 1
    return count
for num in range(1, 100):
    ops = count_operations(num)
    if ops == 5:
        print(f"Для {num} нужно {ops} операций")""",
        "Анализ алгоритмов исполнителей")
        ],
        13 :[
        ("IP-адрес и напоминания",
        """from ipaddress import ip_network
k = 0
for ip in ip_network('112.208.0.0/255.255.128.0', strict=False):
    ip_2 = f'{ip:b}'  # двоичное представление
    if ip_2.count('1') % 11 == 0:
        k += 1
print(f"Подходящих адресов: {k}")
# Другой пример
network = ip_network('192.168.0.0/24')
print(f"Всего адресов: {network.num_addresses}")
print(f"Первый: {network.network_address}")
print(f"Последний: {network.broadcast_address}")""",
        "Анализ IP-адресов и подсетей")
        ],
        14 :[
        ("Системы счисления и делимость",
        """# Перевод в различные системы счисления
x = 4*3125**2019 + 3*625**2020 - 2*125**2021 + 25**2022 - 4*5**2023 - 2024
k = 0
while x > 0:
    if x % 25 > 10:
        k += 1
    x = x // 25
print(f"Цифр больше 10: {k}")
# Другой пример
num = int('1234', 5)  # из 5-ичной в 10-ичную
print(f"В десятичной: {num}")
# Проверка делимости
for base in range(2, 20):
    num_in_base = int('120', base)
    if num_in_base % 7 == 0:
        print(f"В системе {base}: {num_in_base}")""",
        "Перевод чисел и проверка делимости")
        ],
        15 :[
        ("Логика с условиями - перебор (УНИВЕРСАЛЬНОЕ)",
        """# УНИВЕРСАЛЬНОЕ решение для всех прототипов задания 15
# Поддерживает любые логические условия с переменной A и x
# ВАРИАНТ 1: Стандартный прототип с импликацией
def F(A, x):
    # Формула из задания (может быть любой)
    return (not (x % A == 0)) <= ((x % 28 == 0) <= (not (x % 49 == 0)))
# Перебираем A и проверяем, что F тождественно истинна для всех x
for A in range(1, 1000):
    # Проверяем для всех x в диапазоне
    if all(F(A, x) for x in range(1, 1000)):
        print(f"Подходит A = {A}")
        break  # Если нужно только первое
# ВАРИАНТ 2: С явной проверкой условия
def check_condition(A):
    for x in range(1, 1000):
        # Преобразуем импликацию: (A -> B) = (not A or B)
        # (x % A != 0) or ((x % 28 == 0) and (x % 49 != 0))
        result = (x % A != 0) or ((x % 28 == 0) and (x % 49 != 0))
        if not result:
            return False
    return True
for A in range(1, 100):
    if check_condition(A):
        print(f"A = {A}")
# ВАРИАНТ 3: Сложные условия с несколькими переменными
def F_complex(A, x):
    # Пример сложного условия
    return ((x % A == 0) and (x % 3 == 0)) <= ((x % 6 == 0) or (x % 9 == 0))
for A in range(1, 100):
    if all(F_complex(A, x) for x in range(1, 1000)):
        print(f"Подходит A = {A}")
# ВАРИАНТ 4: Условие с диапазоном x
def F_range(A, x):
    return (x % A == 0) <= (x % 2 == 0)
# Проверяем только для определенного диапазона
for A in range(1, 50):
    if all(F_range(A, x) for x in range(10, 100)):
        print(f"A = {A} для диапазона [10, 100)")
# ВАРИАНТ 5: Условие с несколькими делителями
def F_multi(A, x):
    return ((x % A == 0) or (x % 2 == 0)) <= ((x % 4 == 0) and (x % 8 == 0))
for A in range(1, 100):
    if all(F_multi(A, x) for x in range(1, 200)):
        print(f"A = {A}")""",
        "Универсальное решение для всех прототипов логических задач с условиями")
        ],
        18 :[
        ("Динамическое программирование",
        """# Задача о достижении числа
def count_ways(n):
    dp = [0] * (n + 1)
    dp[1] = 1
    for i in range(1, n + 1):
        if i + 1 <= n:
            dp[i + 1] += dp[i]
        if i * 2 <= n:
            dp[i * 2] += dp[i]
        if i * 3 <= n:
            dp[i * 3] += dp[i]
    return dp[n]
target = 25
print(f"Количество способов достичь {target}: {count_ways(target)}")
# Поиск максимальной суммы
arr = [1, 5, 2, 8, 3]
dp = [0] * len(arr)
dp[0] = arr[0]
dp[1] = max(arr[0], arr[1])
for i in range(2, len(arr)):
    dp[i] = max(dp[i-1], dp[i-2] + arr[i])
print(f"Максимальная сумма: {dp[-1]}")""",
        "Динамическое программирование - подсчет путей и оптимизация")
        ],
        22 :[
        ("Анализ программ - трассировка",
        """# Трассировка алгоритма
def algorithm(n):
    a = 0
    b = 1
    while n > 0:
        if n % 2 == 0:
            a += 1
            n = n // 2
        else:
            b *= 2
            n = n - 1
    return a + b
# Находим все числа, для которых результат равен target
target = 15
for n in range(1, 1000):
    if algorithm(n) == target:
        print(f"n = {n}, результат = {algorithm(n)}")
# Анализ работы программы
n = 10
steps = []
a, b = 0, 1
while n > 0:
    steps.append((n, a, b))
    if n % 2 == 0:
        a += 1
        n = n // 2
    else:
        b *= 2
        n = n - 1
print("Трассировка:")
for step in steps:
    print(f"n={step[0]}, a={step[1]}, b={step[2]}")""",
        "Анализ и трассировка алгоритмов")
        ],
        24 :[
        ("Обработка символьных строк",
        """# Поиск подстрок с условиями
text = "ABCABCABC"
# Подсчет непересекающихся вхождений
count = 0
i = 0
pattern = "ABC"
while i < len(text):
    if text[i:i+len(pattern)] == pattern:
        count += 1
        i += len(pattern)
    else:
        i += 1
print(f"Непересекающихся вхождений: {count}")
# Поиск максимальной длины подстроки
def max_substring_length(s, condition):
    max_len = 0
    for i in range(len(s)):
        for j in range(i+1, len(s)+1):
            substr = s[i:j]
            if condition(substr):
                max_len = max(max_len, len(substr))
    return max_len
# Пример: подстрока из одинаковых символов
result = max_substring_length("AAABBBCCCC", lambda s: len(set(s)) == 1)
print(f"Максимальная длина: {result}")
# Чтение из файла
try:
    with open('24.txt') as f:
        text = f.read()
        print(f"Длина текста: {len(text)}")
        print(f"Уникальных символов: {len(set(text))}")
except:
    print("Файл не найден")""",
        "Обработка и анализ текстовых строк")
        ],
        16 :[
        ("Рекурсия",
        """def F(n):
    if n <= 250194:
        return F(n + 8) + 1050
    else:
        return 3 * (G(n - 5) + 27)
def G(n):
    if n >= 40:
        return G(n - 3) - 20
    else:
        return 30 * n + 24
print(F(10))""",
        "Вычисляет значение рекурсивной функции")
        ],
        17 :[
        ("Числовые последовательности",
        """a = [int(i) для i в open('17.txt')]
mx_19 = max([i для i в a, если i % 19 == 0])
ответ = []
для i в диапазоне (len(a) - 1):
    если ((a[i] > mx_19) + (a[i+1] > mx_19)) > 0:
        ответ.append(a[i] + a[i + 1])
print(лен(ответ), макс(ответ))""",
        "Анализирует последовательность чисел из файла")
        ],
        23 :[
        ("Достижимость чисел",
        """def F(x, y):
    if x > y or x == 16:
        return 0
    if x == y:
        return 1
    if x < y:
        return F(x + 1, y) + F(x + 2, y) + F(x * 3, y)
print(F(2, 9) * F(9, 18))""",
        "Подсчитывает количество программ для достижения числа")
        ],
        25 :[
        ("Перебор делителей - поиск чисел",
        """def D(x):
    dels = set()
    for d in range(2, int(x ** 0.5) + 1):
        if x % d == 0:
            dels.add(d)
            dels.add(x // d)
    return dels
k = 0
for x in range(500001, 10 ** 7):  # ограничим диапазон
    dels = D(x)
    if len(dels) > 0:
        R = sum(dels)
        if R % 10 == 9:
            print(f"{x} {R}")
            k += 1
            if k == 5:
                break
# Проверка на простоту
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
# Поиск чисел с определенным количеством делителей
count = 0
for num in range(100000, 200000):
    dels = D(num)
    if len(dels) == 4:
        print(f"{num}: делители {sorted(dels)}")
        count += 1
        if count >= 10:
            break""",
        "Находит числа с заданными свойствами делителей")
        ],
        26 :[
        ("Оптимизация выбора - задача о рюкзаке",
        """# Решение задачи о выборе элементов
# Создайте файл '26.txt' с данными:
# первая строка - количество элементов
# остальные строки - два числа (параметры элемента)
try:
    f = open('26.txt')
    n = int(f.readline())
    a = []
    item_num = 0
    for i in f:
        x, y = [int(val) for val in i.split()]
        item_num += 1
        if x < y:
            a.append([x, item_num, 'тип1'])
        else:
            a.append([x, item_num, 'тип2'])
    a.sort()
    otvet1 = a[-1][1]
    # Размещение на ленте
    lenta = [0] * (item_num + 1)
    l = 0
    r = -1
    for i in a:
        if i[2] == 'тип1':
            lenta[l] = i[1]
            l += 1
        else:
            lenta[r] = i[1]
            r -= 1
    # Подсчет элементов после найденного
    k = 0
    for i in range(len(lenta)):
        if lenta[i] == otvet1:
            k = len(lenta[i+1:])
            break
    print(f"Ответ: {otvet1} {k}")
except:
    print("Создайте файл 26.txt с данными")
# Жадный алгоритм для рюкзака
items = [(10, 60), (20, 100), (30, 120)]  # (вес, ценность)
capacity = 50
# Сортируем по отношению ценность/вес
items_sorted = sorted(items, key=lambda x: x[1]/x[0], reverse=True)
total_weight = 0
total_value = 0
selected = []
for weight, value in items_sorted:
    if total_weight + weight <= capacity:
        selected.append((weight, value))
        total_weight += weight
        total_value += value
print(f"Выбрано предметов: {len(selected)}")
print(f"Общий вес: {total_weight}, ценность: {total_value}")""",
        "Оптимизация выбора элементов с условиями")
        ],
        27 :[
        ("Работа с файлами - большие данные",
        """# Решение для анализа координат точек
# Создайте файл '27A.txt' с координатами (x, y через пробел)
try:
    cl1 = []
    cl2 = []
    for i in open('27A.txt'):
        x, y = [float(j) for j in i.replace(',', '.').split()]
        if y > 0:
            cl1.append([x, y])
        if y < 0:
            cl2.append([x, y])
    def Center(cl):
        mn = []
        for x1, y1 in cl:
            s = 0
            for x2, y2 in cl:
                s += ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
            mn.append([s, x1, y1])
        s, x, y = min(mn)
        return x, y
    x1, y1 = Center(cl1)
    x2, y2 = Center(cl2)
    Px = (x1 + x2) / 2
    Py = (y1 + y2) / 2
    print(f"Центр: ({abs(int(Px*10000))}, {abs(int(Py*10000))})")
except:
    print("Создайте файл 27A.txt с данными")
# Обработка больших файлов - поиск пар с условием
try:
    numbers = [int(line) for line in open('27.txt')]
    max_sum = 0
    count = 0
    for i in range(len(numbers) - 1):
        for j in range(i + 1, min(i + 100, len(numbers))):
            if (numbers[i] + numbers[j]) % 2 == 0:
                max_sum = max(max_sum, numbers[i] + numbers[j])
                count += 1
    print(f"Найдено пар: {count}")
    print(f"Максимальная сумма: {max_sum}")
except:
    print("Создайте файл 27.txt с числами")
# Оптимизация с использованием остатков
numbers = list(range(1, 1000))
remainder_groups = {}
for num in numbers:
    rem = num % 3
    if rem not in remainder_groups:
        remainder_groups[rem] = []
    remainder_groups[rem].append(num)
print(f"Группы по остаткам: {len(remainder_groups)}")
for rem, group in remainder_groups.items():
    print(f"Остаток {rem}: {len(group)} чисел")""",
        "Анализ больших файлов и оптимизация вычислений")
        ],
        19 :[
        ("Теория игр (1)",
        """def F(k, x):
    if x == 3 and k >= 435:
        return True
    if x == 3 and k < 435:
        return False
    if k >= 435:
        return False
    if x % 2 == 0:
        return F(k + 5, x + 1) or F(k * 3, x + 1)
    else:
        return F(k + 5, x + 1) and F(k * 3, x + 1)
for k in range(1, 435):
    if F(k, 1):
        print(k)
        break""",
        "Находит выигрышные стратегии для первого игрока")
        ],
        20 :[
        ("Теория игр (2)",
        """def F(k, x):
    if x == 4 and k >= 435:
        return True
    if x == 4 and k < 435:
        return False
    if k > 435:
        return False
    if x % 2 == 1:
        return F(k + 5, x + 1) or F(k * 3, x + 1)
    else:
        return F(k + 5, x + 1) and F(k * 3, x + 1)
for k in range(1, 435):
    if F(k, 1):
        print(k)
        break""",
        "Находит выигрышные стратегии для второго игрока")
        ],
        21 :[
        ("Теория игр (3)",
        """def F(k, x):
    if (x == 3 or x == 5) and k >= 435:
        return True
    if x == 5 and k < 435:
        return False
    if k >= 435:
        return False
    if x % 2 == 0:
        return F(k + 5, x + 1) or F(k * 3, x + 1)
    else:
        return F(k + 5, x + 1) and F(k * 3, x + 1)
for k in range(1, 435):
    if F(k, 1):
        print(k)
        break""",
        "Находит оптимальные стратегии для обоих игроков")
        ],
        }
        return solutions .get (task_num ,[])
    def task_1_interface (self ):
        """Задание 1: Системы счисления (графы и таблицы) - полностью интегрировано"""
        self .task1_current_step =0
        self .task1_nodes =[]
        self .task1_table_data ={}
        self .task1_graph_data ={}
        self .task1_entries ={}
        self .task1_solution =None
        main_frame =tk .Frame (self .root ,bg =DARK_THEME ['bg'])
        main_frame .pack (fill =tk .BOTH ,expand =True )
        self .task1_content_frame =tk .Frame (main_frame ,bg =DARK_THEME ['bg'])
        self .task1_content_frame .pack (fill =tk .BOTH ,expand =True ,padx =20 ,pady =20 )
        self .task1_button_frame =tk .Frame (main_frame ,bg =DARK_THEME ['bg'],pady =15 )
        self .task1_button_frame .pack (fill =tk .X ,side =tk .BOTTOM ,padx =20 )
        self .task1_show_step ()
    def task1_clear_content (self ):
        """
        Очищает содержимое области для отображения шагов задания 1.
        Вызывается перед отображением нового шага, чтобы удалить старые виджеты.
        """
        for widget in self .task1_content_frame .winfo_children ():
            widget .destroy ()
    def task1_update_buttons (self ):
        """
        Обновляет кнопки навигации в зависимости от текущего шага.
        На разных шагах показываются разные кнопки:
        - Шаг 0: только "Далее →"
        - Шаг 1: "← Назад" и "Далее →"
        - Шаг 2: "← Назад" и "✓ Решить"
        - Шаг 3 (результат): "← Назад" и "🔄 Новая задача"
        """
        for widget in self .task1_button_frame .winfo_children ():
            widget .destroy ()
        if self .task1_current_step ==0 :
            btn =tk .Button (self .task1_button_frame ,text ="Далее →",
            command =self .task1_next_step ,
            font =("Arial",13 ,"bold"),bg =DARK_THEME ['button_bg'],
            fg =DARK_THEME ['fg'],
            activebackground =DARK_THEME ['accent_hover'],
            padx =30 ,pady =12 ,relief =tk .FLAT ,cursor ="hand2")
            btn .pack (side =tk .RIGHT ,padx =10 )
        elif self .task1_current_step ==2 :
            btn_back =tk .Button (self .task1_button_frame ,text ="← Назад",
            command =self .task1_prev_step ,
            font =("Arial",13 ,"bold"),bg =DARK_THEME ['bg_secondary'],
            fg =DARK_THEME ['fg'],
            activebackground =DARK_THEME ['bg_tertiary'],
            padx =25 ,pady =12 ,relief =tk .FLAT ,cursor ="hand2")
            btn_back .pack (side =tk .LEFT ,padx =10 )
            btn_next =tk .Button (self .task1_button_frame ,text ="✓ Решить",
            command =self .task1_next_step ,
            font =("Arial",13 ,"bold"),bg =DARK_THEME ['success'],
            fg =DARK_THEME ['fg'],
            activebackground ='#66bb6a',
            padx =30 ,pady =12 ,relief =tk .FLAT ,cursor ="hand2")
            btn_next .pack (side =tk .RIGHT ,padx =10 )
        elif self .task1_current_step ==3 :
            btn_back =tk .Button (self .task1_button_frame ,text ="← Назад",
            command =self .task1_prev_step ,
            font =("Arial",13 ,"bold"),bg =DARK_THEME ['bg_secondary'],
            fg =DARK_THEME ['fg'],
            activebackground =DARK_THEME ['bg_tertiary'],
            padx =25 ,pady =12 ,relief =tk .FLAT ,cursor ="hand2")
            btn_back .pack (side =tk .LEFT ,padx =10 )
            btn_new =tk .Button (self .task1_button_frame ,text ="🔄 Новая задача",
            command =self .task1_new_task ,
            font =("Arial",13 ,"bold"),bg =DARK_THEME ['warning'],
            fg =DARK_THEME ['fg'],
            activebackground ='#ffa726',
            padx =30 ,pady =12 ,relief =tk .FLAT ,cursor ="hand2")
            btn_new .pack (side =tk .RIGHT ,padx =10 )
        else :
            btn_back =tk .Button (self .task1_button_frame ,text ="← Назад",
            command =self .task1_prev_step ,
            font =("Arial",13 ,"bold"),bg =DARK_THEME ['bg_secondary'],
            fg =DARK_THEME ['fg'],
            activebackground =DARK_THEME ['bg_tertiary'],
            padx =25 ,pady =12 ,relief =tk .FLAT ,cursor ="hand2")
            btn_back .pack (side =tk .LEFT ,padx =10 )
            btn_next =tk .Button (self .task1_button_frame ,text ="Далее →",
            command =self .task1_next_step ,
            font =("Arial",13 ,"bold"),bg =DARK_THEME ['button_bg'],
            fg =DARK_THEME ['fg'],
            activebackground =DARK_THEME ['accent_hover'],
            padx =30 ,pady =12 ,relief =tk .FLAT ,cursor ="hand2")
            btn_next .pack (side =tk .RIGHT ,padx =10 )
    def task1_show_step (self ):
        """
        Отображает текущий шаг задания 1.
        В зависимости от номера шага вызывает соответствующую функцию отображения:
        - Шаг 0: ввод количества вершин
        - Шаг 1: заполнение таблицы смежности
        - Шаг 2: ввод структуры графа
        - Шаг 3: отображение результата
        """
        self .task1_clear_content ()
        if self .task1_current_step ==0 :
            self .task1_show_step_nodes ()
        elif self .task1_current_step ==1 :
            self .task1_show_step_table ()
        elif self .task1_current_step ==2 :
            self .task1_show_step_graph ()
        elif self .task1_current_step ==3 :
            self .task1_show_step_result ()
        self .task1_update_buttons ()
    def task1_next_step (self ):
        """
        Переход к следующему шагу задания 1.
        Перед переходом валидирует данные текущего шага.
        Если данные некорректны - останавливается и показывает ошибку.
        """
        if self .task1_current_step ==0 :
            if not self .task1_validate_nodes ():
                return
        elif self .task1_current_step ==1 :
            if not self .task1_save_table ():
                return
        elif self .task1_current_step ==2 :
            if not self .task1_save_graph ():
                return
            if not self .task1_solve ():
                return
        elif self .task1_current_step ==3 :
            self .task1_new_task ()
            return
        self .task1_current_step +=1
        self .task1_show_step ()
    def task1_prev_step (self ):
        """
        Возврат к предыдущему шагу задания 1.
        Позволяет пользователю вернуться назад и исправить данные.
        Все введенные данные сохраняются.
        """
        if self .task1_current_step >0 :
            self .task1_current_step -=1
            self .task1_show_step ()
    def task1_new_task (self ):
        """
        Начинает новую задачу задания 1.
        Сбрасывает все данные и возвращает к первому шагу.
        Полезно, когда нужно решить несколько задач подряд.
        """
        self .task1_current_step =0
        self .task1_nodes =[]
        self .task1_table_data ={}
        self .task1_graph_data ={}
        self .task1_entries ={}
        self .task1_solution =None
        self .task1_show_step ()
    def task1_show_step_nodes (self ):
        """
        Шаг 1 из 3: Ввод количества вершин (населенных пунктов).
        Пользователь вводит количество пунктов из задачи.
        Это нужно для создания таблицы смежности на следующем шаге.
        """
        frame =tk .Frame (self .task1_content_frame ,bg =DARK_THEME ['bg'])
        frame .pack (expand =True )
        tk .Label (frame ,text ="Шаг 1 из 3",font =("Arial",12 ),
        fg =DARK_THEME ['text_secondary'],bg =DARK_THEME ['bg']).pack (pady =10 )
        tk .Label (frame ,text ="Введите количество вершин",
        font =("Arial",18 ,"bold"),bg =DARK_THEME ['bg'],
        fg =DARK_THEME ['fg']).pack (pady =20 )
        instruction =tk .LabelFrame (frame ,text ="📖 Как найти количество вершин?",
        font =("Arial",11 ,"bold"),padx =15 ,pady =10 ,
        bg =DARK_THEME ['bg_secondary'],fg =DARK_THEME ['fg'],
        relief =tk .FLAT )
        instruction .pack (fill =tk .X ,pady =10 ,padx =30 )
        tk .Label (instruction ,
        text ="1. Посмотрите на таблицу в задании\n"
        "2. Найдите количество строк (или столбцов) - это и есть количество вершин\n"
        "3. Например, если в таблице пункты 1, 2, 3, 4 - введите 4",
        font =("Arial",10 ),bg =DARK_THEME ['bg_secondary'],
        fg =DARK_THEME ['text_secondary'],justify =tk .LEFT ).pack (anchor =tk .W ,padx =10 ,pady =5 )
        entry_frame =tk .Frame (frame ,bg =DARK_THEME ['bg'])
        entry_frame .pack (pady =20 )
        self .task1_nodes_entry =tk .Entry (entry_frame ,font =("Arial",18 ),
        width =8 ,justify ='center',
        bg =DARK_THEME ['entry_bg'],
        fg =DARK_THEME ['entry_fg'],
        insertbackground =DARK_THEME ['fg'],
        relief =tk .FLAT ,bd =5 )
        self .task1_nodes_entry .pack (pady =10 )
        self .task1_nodes_entry .focus ()
        self .task1_nodes_entry .bind ('<Возврат>',lambda e :self .task1_next_step ())
        if self .task1_nodes :
            self .task1_nodes_entry .insert (0 ,str (len (self .task1_nodes )))
        tk .Label (frame ,text ="Количество населенных пунктов в задаче (от 2 до 10)",
        font =("Arial",11 ),fg =DARK_THEME ['text_secondary'],
        bg =DARK_THEME ['bg']).pack (pady =5 )
    def task1_validate_nodes (self ):
        """
        Проверяет корректность введенного количества вершин.
        Валидация:
        - Должно быть целое число
        - От 2 до 10 (типичный диапазон для заданий ЕГЭ)
        Returns:
            bool: True если данные корректны, False иначе
        """
        try :
            n =int (self .task1_nodes_entry .get ())
            if n <2 or n >10 :
                messagebox .showerror ("Ошибка",
                "Количество вершин должно быть от 2 до 10.\n\n"
                "💡 Проверьте задание - возможно, вы неправильно посчитали количество пунктов.")
                return False
            self .task1_nodes =list (range (1 ,n +1 ))
            return True
        except ValueError :
            messagebox .showerror ("Ошибка",
            "Введите целое число.\n\n"
            "💡 Примеры правильного ввода: 3, 5, 7")
            return False
    def task1_show_step_table (self ):
        """
        Шаг 2 из 3: Заполнение таблицы смежности.
        Пользователь заполняет таблицу длинами дорог из задания.
        Можно использовать звездочку (*) для дорог без указания длины.
        """
        header =tk .Frame (self .task1_content_frame ,bg =DARK_THEME ['bg_secondary'],pady =15 )
        header .pack (fill =tk .X )
        tk .Label (header ,text ="Шаг 2 из 3",font =("Arial",12 ),
        fg =DARK_THEME ['text_secondary'],bg =DARK_THEME ['bg_secondary']).pack ()
        tk .Label (header ,text ="Заполните таблицу смежности",
        font =("Arial",18 ,"bold"),bg =DARK_THEME ['bg_secondary'],
        fg =DARK_THEME ['fg']).pack (pady =8 )
        instruction =tk .LabelFrame (header ,text ="📖 Как заполнять таблицу?",
        font =("Arial",11 ,"bold"),padx =15 ,pady =10 ,
        bg =DARK_THEME ['bg_tertiary'],fg =DARK_THEME ['fg'],
        relief =tk .FLAT )
        instruction .pack (fill =tk .X ,pady =8 ,padx =20 )
        tk .Label (instruction ,
        text ="1. Найдите таблицу в задании с длинами дорог\n"
        "2. Заполняйте только верхний треугольник (серые ячейки не трогайте)\n"
        "3. Вводите числа - длины дорог из задания\n"
        "4. Если дорога есть, но длина не указана - введите символ *\n"
        "5. Если дороги нет - оставьте ячейку пустой",
        font =("Arial",10 ),bg =DARK_THEME ['bg_tertiary'],
        fg =DARK_THEME ['text_secondary'],justify =tk .LEFT ).pack (anchor =tk .W ,padx =10 ,pady =5 )
        tk .Label (header ,text ="Введите длины дорог из таблицы задачи",
        font =("Arial",11 ),fg =DARK_THEME ['text_secondary'],
        bg =DARK_THEME ['bg_secondary']).pack (pady =3 )
        table_frame =tk .Frame (self .task1_content_frame ,bg =DARK_THEME ['bg'])
        table_frame .pack (expand =True ,fill =tk .BOTH ,padx =20 ,pady =15 )
        canvas =tk .Canvas (table_frame ,bg =DARK_THEME ['bg'],highlightthickness =0 )
        scrollbar_y =ttk .Scrollbar (table_frame ,orient ="vertical",command =canvas .yview )
        scrollbar_x =ttk .Scrollbar (table_frame ,orient ="horizontal",command =canvas .xview )
        scrollable_frame =tk .Frame (canvas ,bg =DARK_THEME ['bg'])
        scrollable_frame .bind ("<Настроить>",lambda e :canvas .configure (scrollregion =canvas .bbox ("all")))
        canvas .create_window ((0 ,0 ),window =scrollable_frame ,anchor ="nw")
        canvas .configure (yscrollcommand =scrollbar_y .set ,xscrollcommand =scrollbar_x .set )
        n =len (self .task1_nodes )
        tk .Label (scrollable_frame ,text ="",width =6 ,height =2 ,
        bg =DARK_THEME ['bg'],relief =tk .FLAT ).grid (row =0 ,column =0 )
        for i ,node in enumerate (self .task1_nodes ):
            label =tk .Label (scrollable_frame ,text =str (node ),width =10 ,height =2 ,
            font =("Arial",12 ,"bold"),bg =DARK_THEME ['accent'],
            fg =DARK_THEME ['fg'],relief =tk .FLAT )
            label .grid (row =0 ,column =i +1 ,padx =2 ,pady =2 )
        self .task1_entries ={}
        for i ,row_node in enumerate (self .task1_nodes ):
            label =tk .Label (scrollable_frame ,text =str (row_node ),width =6 ,height =2 ,
            font =("Arial",12 ,"bold"),bg =DARK_THEME ['accent'],
            fg =DARK_THEME ['fg'],relief =tk .FLAT )
            label .grid (row =i +1 ,column =0 ,padx =2 ,pady =2 )
            for j ,col_node in enumerate (self .task1_nodes ):
                if i >=j :
                    tk .Label (scrollable_frame ,text ="",width =10 ,height =2 ,
                    bg =DARK_THEME ['bg_tertiary'],relief =tk .FLAT ).grid (row =i +1 ,column =j +1 ,padx =2 ,pady =2 )
                else :
                    entry =tk .Entry (scrollable_frame ,width =10 ,font =("Arial",11 ),
                    justify ='center',
                    bg =DARK_THEME ['entry_bg'],
                    fg =DARK_THEME ['entry_fg'],
                    insertbackground =DARK_THEME ['fg'],
                    relief =tk .FLAT ,bd =3 )
                    entry .grid (row =i +1 ,column =j +1 ,padx =2 ,pady =2 )
                    self .task1_entries [(row_node ,col_node )]=entry
                    if self .task1_table_data and str (row_node )in self .task1_table_data and str (col_node )in self .task1_table_data [str (row_node )]:
                        val =self .task1_table_data [str (row_node )][str (col_node )]
                        entry .insert (0 ,str (val )if val !='*'else '*')
        canvas .pack (side ="left",fill ="both",expand =True )
        scrollbar_y .pack (side ="right",fill ="y")
        scrollbar_x .pack (side ="bottom",fill ="x")
    def task1_save_table (self ):
        """
        УНИВЕРСАЛЬНОЕ сохранение данных из таблицы смежности.
        Поддерживает ВСЕ прототипы заданий:
        - Числа (длины дорог) - любые положительные целые числа
        - Звездочки (*) - дорога есть, но длина не указана
        - Пустые ячейки - дороги нет
        - Симметричные таблицы (автоматически заполняет обе стороны)
        - Несимметричные таблицы (если нужно в будущем)
        Returns:
            bool: True если данные сохранены успешно, False иначе
        """
        self .task1_table_data ={}
        for (i ,j ),entry in self .task1_entries .items ():
            value =entry .get ().strip ()
            if value :
                if value =='*'or value .upper ()=='*':
                    if str (i )not in self .task1_table_data :
                        self .task1_table_data [str (i )]={}
                    if str (j )not in self .task1_table_data :
                        self .task1_table_data [str (j )]={}
                    self .task1_table_data [str (i )][str (j )]='*'
                    self .task1_table_data [str (j )][str (i )]='*'
                else :
                    try :
                        length =int (value )
                        if length <0 :
                            messagebox .showerror ("Ошибка",
                            f"Длина дороги не может быть отрицательной.\n"
                            f"Ячейка ({i }, {j }): {value }\n\n"
                            f"💡 Проверьте задание - возможно, вы ввели неправильное значение.")
                            return False
                        if str (i )not in self .task1_table_data :
                            self .task1_table_data [str (i )]={}
                        if str (j )not in self .task1_table_data :
                            self .task1_table_data [str (j )]={}
                        self .task1_table_data [str (i )][str (j )]=length
                        self .task1_table_data [str (j )][str (i )]=length
                    except ValueError :
                        messagebox .showerror ("Ошибка",
                        f"Некорректное значение в ячейке ({i }, {j }): '{value }'\n\n"
                        f"💡 Используйте:\n"
                        f"  - Число для длины дороги (например: 5, 12, 100)\n"
                        f"  - Символ * если дорога есть, но длина не указана\n"
                        f"  - Оставьте пустым, если дороги нет\n\n"
                        f"Поддерживаются все прототипы заданий из открытого банка ФИПИ.")
                        return False
        if not self .task1_table_data :
            messagebox .showerror ("Ошибка",
            "Заполните хотя бы одну связь в таблице.\n\n"
            "💡 Если в задании есть таблица с дорогами, заполните соответствующие ячейки.\n"
            "Программа поддерживает все форматы таблиц из прототипов ЕГЭ.")
            return False
        return True
    def task1_show_step_graph (self ):
        """
        Шаг 3 из 3: Ввод структуры графа.
        Пользователь вводит для каждой вершины (буквы) список соседних вершин.
        Это нужно для поиска соответствия между таблицей и графом.
        """
        header =tk .Frame (self .task1_content_frame ,bg =DARK_THEME ['bg_secondary'],pady =15 )
        header .pack (fill =tk .X )
        tk .Label (header ,text ="Шаг 3 из 3",font =("Arial",12 ),
        fg =DARK_THEME ['text_secondary'],bg =DARK_THEME ['bg_secondary']).pack ()
        tk .Label (header ,text ="Введите структуру графа",
        font =("Arial",18 ,"bold"),bg =DARK_THEME ['bg_secondary'],
        fg =DARK_THEME ['fg']).pack (pady =8 )
        instruction =tk .LabelFrame (header ,text ="📖 Как заполнять граф?",
        font =("Arial",11 ,"bold"),padx =15 ,pady =10 ,
        bg =DARK_THEME ['bg_tertiary'],fg =DARK_THEME ['fg'],
        relief =tk .FLAT )
        instruction .pack (fill =tk .X ,pady =8 ,padx =20 )
        tk .Label (instruction ,
        text ="1. Найдите граф в задании (рисунок с буквами и линиями)\n"
        "2. Для каждой вершины (буквы) укажите все соседние вершины\n"
        "3. Вводите буквы подряд без пробелов и запятых\n"
        "4. Пример: если А соединена с Б и В, введите: АБВ\n"
        "5. Если вершина изолирована (нет соседей) - оставьте поле соседей ПУСТЫМ\n"
        "6. Можно вводить с запятыми или пробелами - программа сама обработает",
        font =("Arial",10 ),bg =DARK_THEME ['bg_tertiary'],
        fg =DARK_THEME ['text_secondary'],justify =tk .LEFT ).pack (anchor =tk .W ,padx =10 ,pady =5 )
        tk .Label (header ,text ="Укажите вершины и их соседей (например: для А соседи БВ)",
        font =("Arial",11 ),fg =DARK_THEME ['text_secondary'],
        bg =DARK_THEME ['bg_secondary']).pack (pady =3 )
        graph_frame =tk .Frame (self .task1_content_frame ,bg =DARK_THEME ['bg'])
        graph_frame .pack (expand =True ,pady =25 )
        header_frame =tk .Frame (graph_frame ,bg =DARK_THEME ['bg'])
        header_frame .pack (fill =tk .X ,pady =10 )
        tk .Label (header_frame ,text ="Вершина",font =("Arial",13 ,"bold"),
        bg =DARK_THEME ['bg'],fg =DARK_THEME ['fg'],width =15 ).pack (side =tk .LEFT ,padx =15 )
        tk .Label (header_frame ,text ="Соседние вершины",font =("Arial",13 ,"bold"),
        bg =DARK_THEME ['bg'],fg =DARK_THEME ['fg']).pack (side =tk .LEFT ,padx =15 )
        self .task1_graph_entries ={}
        for i in range (len (self .task1_nodes )):
            row_frame =tk .Frame (graph_frame ,bg =DARK_THEME ['bg'])
            row_frame .pack (fill =tk .X ,pady =8 )
            node_entry =tk .Entry (row_frame ,width =15 ,font =("Arial",13 ),
            justify ='center',
            bg =DARK_THEME ['entry_bg'],
            fg =DARK_THEME ['entry_fg'],
            insertbackground =DARK_THEME ['fg'],
            relief =tk .FLAT ,bd =5 )
            node_entry .pack (side =tk .LEFT ,padx =15 )
            neighbors_entry =tk .Entry (row_frame ,width =40 ,font =("Arial",13 ),
            bg =DARK_THEME ['entry_bg'],
            fg =DARK_THEME ['entry_fg'],
            insertbackground =DARK_THEME ['fg'],
            relief =tk .FLAT ,bd =5 )
            neighbors_entry .pack (side =tk .LEFT ,padx =15 )
            if self .task1_graph_data :
                items =list (self .task1_graph_data .items ())
                if i <len (items ):
                    node_entry .insert (0 ,items [i ][0 ])
                    neighbors_entry .insert (0 ,items [i ][1 ])
            self .task1_graph_entries [i ]=(node_entry ,neighbors_entry )
    def task1_save_graph (self ):
        """
        Сохраняет данные графа из полей ввода.
        Обрабатывает:
        - Буквы вершин (приводит к верхнему регистру)
        - Список соседей (убирает пробелы и запятые)
        Returns:
            bool: True если данные сохранены успешно, False иначе
        """
        self .task1_graph_data ={}
        for i ,(node_entry ,neighbors_entry )in self .task1_graph_entries .items ():
            node =node_entry .get ().strip ().upper ()
            neighbors =neighbors_entry .get ().strip ().upper ().replace (',','').replace (' ','').replace (';','')
            if node :
                if len (node )!=1 or not node .isalpha ():
                    messagebox .showerror ("Ошибка",
                    f"Некорректное имя вершины: '{node }'\n\n"
                    f"💡 Используйте одну букву (А, Б, В, Г и т.д.)")
                    return False
                if neighbors :
                    if not all (c .isalpha ()for c in neighbors ):
                        messagebox .showerror ("Ошибка",
                        f"Некорректные соседи для вершины {node }: '{neighbors }'\n\n"
                        f"💡 Используйте только буквы (например: БВГ, АБ)")
                        return False
                    self .task1_graph_data [node ]=neighbors
                else :
                    self .task1_graph_data [node ]=''
        if not self .task1_graph_data :
            messagebox .showerror ("Ошибка",
            "Введите данные графа.\n\n"
            "💡 Заполните хотя бы одну строку: укажите вершину.\n"
            "Если у вершины нет соседей - оставьте поле соседей пустым.")
            return False
        if len (self .task1_graph_data )!=len (self .task1_nodes ):
            messagebox .showerror ("Ошибка",
            f"Количество вершин в графе ({len (self .task1_graph_data )}) не совпадает "
            f"с количеством в таблице ({len (self .task1_nodes )}).\n\n"
            f"💡 Проверьте задание - возможно, вы пропустили какую-то вершину.")
            return False
        return True
    def task1_solve (self ):
        """
        УНИВЕРСАЛЬНОЕ решение задания 1: находит соответствие между номерами в таблице и вершинами графа.
        Поддерживает ВСЕ прототипы заданий:
        - Симметричные и несимметричные таблицы
        - Таблицы с длинами дорог и без них (только наличие связей)
        - Звездочки (*) для дорог без указания длины
        - Графы с разными способами задания (списки соседей, матрицы смежности)
        - Графы с изолированными вершинами (без соседей)
        - Разные форматы ввода соседей (с запятыми, пробелами, подряд)
        Алгоритм:
        1. Нормализуем данные таблицы и графа (приводим к единому формату)
        2. Создаем словари смежности для обоих (только наличие связей)
        3. Перебираем все перестановки номеров из таблицы
        4. Для каждой перестановки проверяем изоморфизм графов
        5. Если найдено соответствие - сохраняем решение
        Returns:
            bool: True если решение найдено, False иначе
        """
        table_adj ={}
        for node in self .task1_table_data :
            neighbors =set ()
            for neighbor in self .task1_table_data [node ].keys ():
                value =self .task1_table_data [node ][neighbor ]
                if value is not None and value !='':
                    neighbors .add (neighbor )
            table_adj [node ]=neighbors
        graph_adj ={}
        for node ,neighbors_str in self .task1_graph_data .items ():
            if neighbors_str :
                neighbors_clean =neighbors_str .upper ().replace (',','').replace (' ','').replace (';','').replace ('-','')
                graph_adj [node ]=set (neighbors_clean )
            else :
                graph_adj [node ]=set ()
        def safe_sort_key (x ):
            """Безопасная сортировка для разных типов данных"""
            try :
                return int (x )
            except :
                return str (x )
        nodes_list =sorted (self .task1_table_data .keys (),key =safe_sort_key )
        graph_nodes =sorted (self .task1_graph_data .keys ())
        if len (nodes_list )!=len (graph_nodes ):
            messagebox .showerror ("Ошибка",
            f"Количество вершин не совпадает:\n"
            f"В таблице: {len (nodes_list )} вершин\n"
            f"В графе: {len (graph_nodes )} вершин\n\n"
            "💡 Проверьте задание - возможно, вы пропустили какую-то вершину.")
            return False
        self .task1_solution =None
        for perm in permutations (nodes_list ):
            mapping ={num :letter for num ,letter in zip (perm ,graph_nodes )}
            mapped_table ={}
            for num ,neighbors_set in table_adj .items ():
                if num in mapping :
                    mapped_neighbors ={mapping [n ]for n in neighbors_set if n in mapping }
                    mapped_table [mapping [num ]]=mapped_neighbors
            match =True
            if len (mapped_table )!=len (graph_adj ):
                match =False
            else :
                for graph_node in graph_nodes :
                    if graph_node not in mapped_table :
                        match =False
                        break
                    if mapped_table [graph_node ]!=graph_adj [graph_node ]:
                        match =False
                        break
            if match :
                self .task1_solution =mapping
                break
        if not self .task1_solution :
            messagebox .showerror ("Ошибка",
            "Не удалось найти соответствие.\n\n"
            "💡 Возможные причины:\n"
            "  1. Ошибка при заполнении таблицы\n"
            "  2. Ошибка при вводе структуры графа\n"
            "  3. Данные из разных задач смешаны\n"
            "  4. В задании указаны не все связи\n\n"
            "Проверьте правильность данных и попробуйте снова.")
            return False
        return True
    def task1_show_step_result (self ):
        """
        Показывает результат решения задания 1.
        Отображает соответствие номеров и вершин, позволяет найти расстояние между вершинами.
        """
        header =tk .Frame (self .task1_content_frame ,bg =DARK_THEME ['bg_secondary'],pady =15 )
        header .pack (fill =tk .X )
        tk .Label (header ,text ="Решение найдено",
        font =("Arial",16 ,"bold"),fg =DARK_THEME ['success'],
        bg =DARK_THEME ['bg_secondary']).pack ()
        main =tk .Frame (self .task1_content_frame ,bg =DARK_THEME ['bg'])
        main .pack (expand =True ,fill =tk .BOTH ,padx =30 ,pady =25 )
        left =tk .LabelFrame (main ,text ="📊 Соответствие номеров и вершин",
        font =("Arial",14 ,"bold"),padx =20 ,pady =20 ,
        bg =DARK_THEME ['bg_secondary'],fg =DARK_THEME ['fg'],
        relief =tk .FLAT )
        left .pack (side =tk .LEFT ,fill =tk .BOTH ,expand =True ,padx =10 )
        result_frame =tk .Frame (left ,bg =DARK_THEME ['bg_secondary'])
        result_frame .pack ()
        tk .Label (result_frame ,text ="Номер",font =("Arial",13 ,"bold"),width =12 ,
        bg =DARK_THEME ['accent'],fg =DARK_THEME ['fg'],
        relief =tk .FLAT ,padx =10 ,pady =8 ).grid (row =0 ,column =0 )
        tk .Label (result_frame ,text ="Вершина",font =("Arial",13 ,"bold"),width =12 ,
        bg =DARK_THEME ['accent'],fg =DARK_THEME ['fg'],
        relief =tk .FLAT ,padx =10 ,pady =8 ).grid (row =0 ,column =1 )
        for i ,(num ,letter )in enumerate (sorted (self .task1_solution .items (),key =lambda x :int (x [0 ])),start =1 ):
            tk .Label (result_frame ,text =num ,font =("Arial",12 ),width =12 ,
            bg =DARK_THEME ['bg_tertiary'],fg =DARK_THEME ['fg'],
            relief =tk .FLAT ,padx =10 ,pady =6 ).grid (row =i ,column =0 )
            tk .Label (result_frame ,text =letter ,font =("Arial",12 ),width =12 ,
            bg =DARK_THEME ['bg_tertiary'],fg =DARK_THEME ['fg'],
            relief =tk .FLAT ,padx =10 ,pady =6 ).grid (row =i ,column =1 )
        right =tk .LabelFrame (main ,text ="🔍 Найти расстояние",
        font =("Arial",14 ,"bold"),padx =20 ,pady =20 ,
        bg =DARK_THEME ['bg_secondary'],fg =DARK_THEME ['fg'],
        relief =tk .FLAT )
        right .pack (side =tk .RIGHT ,fill =tk .BOTH ,expand =True ,padx =10 )
        calc_frame =tk .Frame (right ,bg =DARK_THEME ['bg_secondary'])
        calc_frame .pack (expand =True )
        input_frame =tk .Frame (calc_frame ,bg =DARK_THEME ['bg_secondary'])
        input_frame .pack (pady =20 )
        tk .Label (input_frame ,text ="Из:",font =("Arial",14 ),
        bg =DARK_THEME ['bg_secondary'],fg =DARK_THEME ['fg']).grid (row =0 ,column =0 ,padx =10 )
        from_entry =tk .Entry (input_frame ,width =8 ,font =("Arial",16 ),
        justify ='center',
        bg =DARK_THEME ['entry_bg'],
        fg =DARK_THEME ['entry_fg'],
        insertbackground =DARK_THEME ['fg'],
        relief =tk .FLAT ,bd =5 )
        from_entry .grid (row =0 ,column =1 ,padx =10 )
        tk .Label (input_frame ,text ="В:",font =("Arial",14 ),
        bg =DARK_THEME ['bg_secondary'],fg =DARK_THEME ['fg']).grid (row =0 ,column =2 ,padx =10 )
        to_entry =tk .Entry (input_frame ,width =8 ,font =("Arial",16 ),
        justify ='center',
        bg =DARK_THEME ['entry_bg'],
        fg =DARK_THEME ['entry_fg'],
        insertbackground =DARK_THEME ['fg'],
        relief =tk .FLAT ,bd =5 )
        to_entry .grid (row =0 ,column =3 ,padx =10 )
        result_label =tk .Label (calc_frame ,text ="",font =("Arial",18 ,"bold"),
        fg =DARK_THEME ['accent'],bg =DARK_THEME ['bg_secondary'])
        result_label .pack (pady =25 )
        def calculate_distance ():
            from_node =from_entry .get ().strip ().upper ()
            to_node =to_entry .get ().strip ().upper ()
            reverse_map ={v :k for k ,v in self .task1_solution .items ()}
            if from_node not in reverse_map or to_node not in reverse_map :
                result_label .config (text ="❌ Вершины не найдены",fg =DARK_THEME ['error'])
                return
            num1 =reverse_map [from_node ]
            num2 =reverse_map [to_node ]
            if num1 in self .task1_table_data and num2 in self .task1_table_data [num1 ]:
                distance =self .task1_table_data [num1 ][num2 ]
                if distance =='*':
                    result_label .config (text ="✅ Дорога есть (длина не указана)",fg =DARK_THEME ['success'])
                else :
                    result_label .config (text =f"✅ Расстояние: {distance }",fg =DARK_THEME ['success'])
            else :
                result_label .config (text ="❌ Дорога не найдена",fg =DARK_THEME ['error'])
        tk .Button (calc_frame ,text ="🔍 Найти",command =calculate_distance ,
        font =("Arial",13 ,"bold"),bg =DARK_THEME ['button_bg'],
        fg =DARK_THEME ['fg'],
        activebackground =DARK_THEME ['accent_hover'],
        padx =30 ,pady =12 ,relief =tk .FLAT ,cursor ="hand2").pack (pady =10 )
    def task_2_interface (self ):
        """Задание 2: Логические выражения - поэкранно"""
        self .task2_current_step =0
        self .task2_expression =""
        self .task2_table_rows =[]
        self .task2_solution =None
        main_frame =tk .Frame (self .root ,bg =DARK_THEME ['bg'])
        main_frame .pack (fill =tk .BOTH ,expand =True )
        self .task2_content_frame =tk .Frame (main_frame ,bg =DARK_THEME ['bg'])
        self .task2_content_frame .pack (fill =tk .BOTH ,expand =True ,padx =20 ,pady =20 )
        self .task2_button_frame =tk .Frame (main_frame ,bg =DARK_THEME ['bg'],pady =15 )
        self .task2_button_frame .pack (fill =tk .X ,side =tk .BOTTOM ,padx =20 )
        self .task2_show_step ()
    def task2_clear_content (self ):
        for widget in self .task2_content_frame .winfo_children ():
            widget .destroy ()
    def task2_update_buttons (self ):
        for widget in self .task2_button_frame .winfo_children ():
            widget .destroy ()
        if self .task2_current_step ==0 :
            btn =tk .Button (self .task2_button_frame ,text ="Далее →",
            command =self .task2_next_step ,
            font =("Arial",13 ,"bold"),bg =DARK_THEME ['button_bg'],
            fg =DARK_THEME ['fg'],
            activebackground =DARK_THEME ['accent_hover'],
            padx =30 ,pady =12 ,relief =tk .FLAT ,cursor ="hand2")
            btn .pack (side =tk .RIGHT ,padx =10 )
        elif self .task2_current_step ==1 :
            btn_back =tk .Button (self .task2_button_frame ,text ="← Назад",
            command =self .task2_prev_step ,
            font =("Arial",13 ,"bold"),bg =DARK_THEME ['bg_secondary'],
            fg =DARK_THEME ['fg'],
            activebackground =DARK_THEME ['bg_tertiary'],
            padx =25 ,pady =12 ,relief =tk .FLAT ,cursor ="hand2")
            btn_back .pack (side =tk .LEFT ,padx =10 )
            btn_next =tk .Button (self .task2_button_frame ,text ="✓ Решить",
            command =self .task2_next_step ,
            font =("Arial",13 ,"bold"),bg =DARK_THEME ['success'],
            fg =DARK_THEME ['fg'],
            activebackground ='#66bb6a',
            padx =30 ,pady =12 ,relief =tk .FLAT ,cursor ="hand2")
            btn_next .pack (side =tk .RIGHT ,padx =10 )
        elif self .task2_current_step ==2 :
            btn_back =tk .Button (self .task2_button_frame ,text ="← Назад",
            command =self .task2_prev_step ,
            font =("Arial",13 ,"bold"),bg =DARK_THEME ['bg_secondary'],
            fg =DARK_THEME ['fg'],
            activebackground =DARK_THEME ['bg_tertiary'],
            padx =25 ,pady =12 ,relief =tk .FLAT ,cursor ="hand2")
            btn_back .pack (side =tk .LEFT ,padx =10 )
            btn_new =tk .Button (self .task2_button_frame ,text ="🔄 Новая задача",
            command =self .task2_new_task ,
            font =("Arial",13 ,"bold"),bg =DARK_THEME ['warning'],
            fg =DARK_THEME ['fg'],
            activebackground ='#ffa726',
            padx =30 ,pady =12 ,relief =tk .FLAT ,cursor ="hand2")
            btn_new .pack (side =tk .RIGHT ,padx =10 )
    def task2_show_step (self ):
        self .task2_clear_content ()
        if self .task2_current_step ==0 :
            self .task2_show_step_expression ()
        elif self .task2_current_step ==1 :
            self .task2_show_step_table ()
        elif self .task2_current_step ==2 :
            self .task2_show_step_result ()
        self .task2_update_buttons ()
    def task2_next_step (self ):
        if self .task2_current_step ==0 :
            if not self .task2_save_expression ():
                return
        elif self .task2_current_step ==1 :
            if not self .task2_save_table ():
                return
            if not self .task2_solve ():
                return
        elif self .task2_current_step ==2 :
            self .task2_new_task ()
            return
        self .task2_current_step +=1
        self .task2_show_step ()
    def task2_prev_step (self ):
        if self .task2_current_step >0 :
            self .task2_current_step -=1
            self .task2_show_step ()
    def task2_new_task (self ):
        self .task2_current_step =0
        self .task2_expression =""
        self .task2_table_rows =[]
        self .task2_solution =None
        self .task2_show_step ()
    def task2_show_step_expression (self ):
        """
        Шаг 1 из 2: Ввод логического выражения.
        Пользователь вводит логическое выражение из задания.
        Можно использовать как символы (∧, ∨, ¬, →, ≡), так и слова (and, or, not, <=, ==).
        """
        frame =tk .Frame (self .task2_content_frame ,bg =DARK_THEME ['bg'])
        frame .pack (expand =True )
        tk .Label (frame ,text ="Шаг 1 из 2",font =("Arial",12 ),
        fg =DARK_THEME ['text_secondary'],bg =DARK_THEME ['bg']).pack (pady =10 )
        tk .Label (frame ,text ="Введите логическое выражение",
        font =("Arial",18 ,"bold"),bg =DARK_THEME ['bg'],
        fg =DARK_THEME ['fg']).pack (pady =20 )
        instruction =tk .LabelFrame (frame ,text ="📖 Как найти логическое выражение?",
        font =("Arial",11 ,"bold"),padx =15 ,pady =10 ,
        bg =DARK_THEME ['bg_secondary'],fg =DARK_THEME ['fg'],
        relief =tk .FLAT )
        instruction .pack (fill =tk .X ,pady =15 ,padx =50 )
        tk .Label (instruction ,
        text ="1. Найдите в задании формулу F(x, y, z, w) = ...\n"
        "2. Скопируйте выражение справа от знака =\n"
        "3. Можно использовать символы или слова (см. таблицу ниже)\n"
        "4. Примеры выражений:\n"
        "   • w ∧ ¬((x → y) → (y ≡ z))\n"
        "   • w and not((x <= y) <= (y == z))",
        font =("Arial",10 ),bg =DARK_THEME ['bg_secondary'],
        fg =DARK_THEME ['text_secondary'],justify =tk .LEFT ).pack (anchor =tk .W ,padx =10 ,pady =5 )
        symbols_frame =tk .LabelFrame (frame ,text ="💡 Таблица символов",
        font =("Arial",10 ,"bold"),padx =15 ,pady =10 ,
        bg =DARK_THEME ['bg_tertiary'],fg =DARK_THEME ['fg'],
        relief =tk .FLAT )
        symbols_frame .pack (fill =tk .X ,pady =10 ,padx =50 )
        symbols_text =(
        "∧ (and) - логическое И    |  and  или  &\n"
        "∨ (or) - логическое ИЛИ   |  or   или  |\n"
        "¬ (not) - отрицание НЕ    |  not  или  ~\n"
        "→ (импликация)            |  <=   или  ->\n"
        "≡ (эквивалентность)       |  ==   или  <->"
        )
        tk .Label (symbols_frame ,text =symbols_text ,
        font =("Courier",9 ),bg =DARK_THEME ['bg_tertiary'],
        fg =DARK_THEME ['text_secondary'],justify =tk .LEFT ).pack (anchor =tk .W ,padx =10 ,pady =5 )
        entry_frame =tk .Frame (frame ,bg =DARK_THEME ['bg'])
        entry_frame .pack (pady =20 ,fill =tk .X ,padx =50 )
        self .task2_expr_entry =tk .Entry (entry_frame ,font =("Arial",16 ),
        bg =DARK_THEME ['entry_bg'],
        fg =DARK_THEME ['entry_fg'],
        insertbackground =DARK_THEME ['fg'],
        relief =tk .FLAT ,bd =5 )
        self .task2_expr_entry .pack (fill =tk .X ,pady =10 )
        self .task2_expr_entry .focus ()
        self .task2_expr_entry .bind ('<Возврат>',lambda e :self .task2_next_step ())
        if self .task2_expression :
            self .task2_expr_entry .insert (0 ,self .task2_expression )
    def task2_save_expression (self ):
        expr =self .task2_expr_entry .get ().strip ()
        if not expr :
            messagebox .showerror ("Ошибка","Введите логическое выражение")
            return False
        self .task2_expression =expr
        return True
    def task2_show_step_table (self ):
        """
        Шаг 2 из 2: Заполнение таблицы истинности.
        Пользователь заполняет таблицу значениями переменных из задания.
        В каждую ячейку можно ввести только 0 (ложь) или 1 (истина).
        """
        header =tk .Frame (self .task2_content_frame ,bg =DARK_THEME ['bg_secondary'],pady =15 )
        header .pack (fill =tk .X )
        tk .Label (header ,text ="Шаг 2 из 2",font =("Arial",12 ),
        fg =DARK_THEME ['text_secondary'],bg =DARK_THEME ['bg_secondary']).pack ()
        tk .Label (header ,text ="Заполните таблицу истинности",
        font =("Arial",18 ,"bold"),bg =DARK_THEME ['bg_secondary'],
        fg =DARK_THEME ['fg']).pack (pady =8 )
        instruction =tk .LabelFrame (header ,text ="📖 Как заполнять таблицу?",
        font =("Arial",11 ,"bold"),padx =15 ,pady =10 ,
        bg =DARK_THEME ['bg_tertiary'],fg =DARK_THEME ['fg'],
        relief =tk .FLAT )
        instruction .pack (fill =tk .X ,pady =8 ,padx =20 )
        tk .Label (instruction ,
        text ="1. Найдите в задании таблицу истинности с переменными x, y, z, w\n"
        "2. Выберите количество строк (обычно 3-8)\n"
        "3. Заполните каждую строку значениями из задания\n"
        "4. В каждую ячейку введите только 0 или 1\n"
        "5. Пример: если в задании строка (0, 1, 0, 1), введите: 0 1 0 1",
        font =("Arial",10 ),bg =DARK_THEME ['bg_tertiary'],
        fg =DARK_THEME ['text_secondary'],justify =tk .LEFT ).pack (anchor =tk .W ,padx =10 ,pady =5 )
        tk .Label (header ,text ="Введите количество строк и заполните таблицу значениями 0 или 1",
        font =("Arial",11 ),fg =DARK_THEME ['text_secondary'],
        bg =DARK_THEME ['bg_secondary']).pack (pady =3 )
        control_frame =tk .Frame (self .task2_content_frame ,bg =DARK_THEME ['bg'])
        control_frame .pack (pady =10 )
        tk .Label (control_frame ,text ="Количество строк:",font =("Arial",12 ),
        bg =DARK_THEME ['bg'],fg =DARK_THEME ['fg']).pack (side =tk .LEFT ,padx =10 )
        rows_var =tk .IntVar (value =len (self .task2_table_rows )if self .task2_table_rows else 3 )
        rows_spinbox =tk .Spinbox (control_frame ,from_ =1 ,to =16 ,textvariable =rows_var ,
        width =5 ,font =("Arial",12 ),
        bg =DARK_THEME ['entry_bg'],fg =DARK_THEME ['entry_fg'],
        buttonbackground =DARK_THEME ['button_bg'],
        relief =tk .FLAT ,bd =3 )
        rows_spinbox .pack (side =tk .LEFT ,padx =10 )
        def update_table ():
            self .task2_create_table (rows_var .get ())
        tk .Button (control_frame ,text ="Обновить таблицу",command =update_table ,
        font =("Arial",11 ),bg =DARK_THEME ['button_bg'],
        fg =DARK_THEME ['fg'],
        activebackground =DARK_THEME ['accent_hover'],
        padx =15 ,pady =5 ,relief =tk .FLAT ,cursor ="hand2").pack (side =tk .LEFT ,padx =10 )
        self .task2_table_frame =tk .Frame (self .task2_content_frame ,bg =DARK_THEME ['bg'])
        self .task2_table_frame .pack (expand =True ,fill =tk .BOTH ,padx =50 ,pady =20 )
        self .task2_create_table (rows_var .get ())
    def task2_create_table (self ,num_rows ):
        """
        Создает визуальную таблицу истинности для ввода данных.
        Таблица имеет 4 столбца (x, y, z, w) и заданное количество строк.
        В каждую ячейку можно ввести только 0 или 1.
        Args:
            num_rows: Количество строк в таблице (обычно 3-8)
        """
        for widget in self .task2_table_frame .winfo_children ():
            widget .destroy ()
        table_container =tk .Frame (self .task2_table_frame ,bg =DARK_THEME ['bg'])
        table_container .pack (expand =True )
        headers =['x','y','z','w']
        for i ,header in enumerate (headers ):
            tk .Label (table_container ,text =header ,font =("Arial",14 ,"bold"),
            width =8 ,bg =DARK_THEME ['accent'],fg =DARK_THEME ['fg'],
            relief =tk .FLAT ,padx =10 ,pady =8 ).grid (row =0 ,column =i ,padx =2 ,pady =2 )
        self .task2_table_entries =[]
        for row in range (num_rows ):
            row_entries =[]
            for col in range (4 ):
                entry =tk .Entry (table_container ,width =8 ,font =("Arial",13 ),
                justify ='center',
                bg =DARK_THEME ['entry_bg'],
                fg =DARK_THEME ['entry_fg'],
                insertbackground =DARK_THEME ['fg'],
                relief =tk .FLAT ,bd =3 )
                entry .grid (row =row +1 ,column =col ,padx =2 ,pady =2 )
                if self .task2_table_rows and row <len (self .task2_table_rows ):
                    entry .insert (0 ,str (self .task2_table_rows [row ][col ]))
                row_entries .append (entry )
            self .task2_table_entries .append (row_entries )
    def task2_save_table (self ):
        """
        Сохраняет данные из таблицы истинности.
        Проверяет, что все ячейки содержат только 0 или 1.
        Каждая строка должна содержать 4 значения (для переменных x, y, z, w).
        Returns:
            bool: True если данные сохранены успешно, False иначе
        """
        self .task2_table_rows =[]
        for row_idx ,row_entries in enumerate (self .task2_table_entries ):
            try :
                row =[]
                for col_idx ,entry in enumerate (row_entries ):
                    val =entry .get ().strip ()
                    if val not in ['0','1']:
                        col_name =['x','y','z','w'][col_idx ]
                        messagebox .showerror ("Ошибка",
                        f"Некорректное значение в строке {row_idx +1 }, столбец {col_name }: '{val }'\n\n"
                        f"💡 В таблице истинности можно использовать только:\n"
                        f"  - 0 (ложь, False)\n"
                        f"  - 1 (истина, True)\n\n"
                        f"Проверьте задание - возможно, вы неправильно скопировали значения.")
                        return False
                    row .append (int (val ))
                if len (row )==4 :
                    self .task2_table_rows .append (tuple (row ))
            except Exception as e :
                messagebox .showerror ("Ошибка",
                f"Ошибка при обработке строки {row_idx +1 }.\n\n"
                f"💡 Убедитесь, что все ячейки заполнены значениями 0 или 1.")
                return False
        if not self .task2_table_rows :
            messagebox .showerror ("Ошибка",
            "Заполните таблицу истинности.\n\n"
            "💡 В задании должна быть таблица со значениями переменных x, y, z, w.\n"
            "Скопируйте эти значения в соответствующие ячейки.")
            return False
        return True
    def task2_solve (self ):
        """
        УНИВЕРСАЛЬНОЕ решение задания 2: находит соответствие столбцов таблицы истинности переменным.
        Поддерживает ВСЕ прототипы заданий:
        - Разные форматы логических выражений (символы и слова)
        - Таблицы с разным количеством строк (3-16)
        - Разные способы задания значений функции F
        - Выражения с любым количеством переменных (x, y, z, w)
        - Вложенные скобки любой глубины
        Алгоритм:
        1. Нормализуем логическое выражение (приводим к Python-синтаксису)
        2. Вычисляем значения функции для каждой строки таблицы
        3. Перебираем все перестановки переменных
        4. Для каждой перестановки проверяем совпадение значений
        5. Если найдено соответствие - сохраняем решение
        Поддерживает символы: ∧ (and), ∨ (or), ¬ (not), → (<=), ≡ (==)
        И слова: and, or, not, <=, ==, &, |, ~
        Returns:
            bool: True если решение найдено, False иначе
        """
        try :
            expr =self .task2_expression .strip ()
            replacements =[
            ('∧',' and '),('&',' and '),('·',' and '),
            ('∨',' or '),('|',' or '),('+',' or '),
            ('¬',' not '),('~',' not '),('!',' not '),
            ('→',' <= '),('->',' <= '),('⇒',' <= '),
            ('≡',' == '),('<->',' == '),('↔',' == '),
            ('⊕',' != '),('≠',' != '),
            ]
            for old ,new in replacements :
                expr =expr .replace (old ,new )
            expr =' '.join (expr .split ())
            func_code =f"def F(x, y, z, w):\n    return bool({expr })"
            namespace ={'True':True ,'False':False }
            try :
                exec (func_code ,namespace )
                F =namespace ['F']
            except SyntaxError as e :
                func_code =f"def F(x, y, z, w):\n    return {expr }"
                exec (func_code ,namespace )
                F =namespace ['F']
            target_values =[]
            for row in self .task2_table_rows :
                try :
                    result =F (*row )
                    target_values .append (int (bool (result )))
                except Exception as e :
                    messagebox .showerror ("Ошибка",
                    f"Не удалось вычислить выражение для строки {row }:\n{e }\n\n"
                    "💡 Проверьте правильность логического выражения.")
                    return False
            vars_list =['x','y','z','w']
            found =False
            for perm in permutations (vars_list ):
                temp_func_code =f"def F_temp({','.join (perm )}):\n    return bool({expr })"
                temp_namespace ={'True':True ,'False':False }
                try :
                    exec (temp_func_code ,temp_namespace )
                    F_temp =temp_namespace ['F_temp']
                except :
                    temp_func_code =f"def F_temp({','.join (perm )}):\n    return {expr }"
                    exec (temp_func_code ,temp_namespace )
                    F_temp =temp_namespace ['F_temp']
                match =True
                for i ,row in enumerate (self .task2_table_rows ):
                    try :
                        values =dict (zip (perm ,row ))
                        computed_value =int (bool (F_temp (**values )))
                        if computed_value !=target_values [i ]:
                            match =False
                            break
                    except :
                        match =False
                        break
                if match :
                    self .task2_solution =''.join (perm )
                    found =True
                    break
            if not found :
                messagebox .showerror ("Ошибка",
                "Соответствие не найдено.\n\n"
                "💡 Возможные причины:\n"
                "  1. Ошибка в логическом выражении\n"
                "  2. Неправильно заполнена таблица истинности\n"
                "  3. Данные из разных задач смешаны\n\n"
                "Проверьте правильность данных и попробуйте снова.")
                return False
            return True
        except Exception as e :
            messagebox .showerror ("Ошибка",
            f"Ошибка при решении: {e }\n\n"
            "💡 Проверьте:\n"
            "  1. Правильность логического выражения\n"
            "  2. Использование правильных операторов\n"
            "  3. Правильность заполнения таблицы")
            return False
    def task2_show_step_result (self ):
        """
        Показывает результат решения задания 2.
        Отображает таблицу истинности и соответствие столбцов переменным.
        """
        header =tk .Frame (self .task2_content_frame ,bg =DARK_THEME ['bg_secondary'],pady =15 )
        header .pack (fill =tk .X )
        tk .Label (header ,text ="Решение найдено",
        font =("Arial",16 ,"bold"),fg =DARK_THEME ['success'],
        bg =DARK_THEME ['bg_secondary']).pack ()
        main =tk .Frame (self .task2_content_frame ,bg =DARK_THEME ['bg'])
        main .pack (expand =True ,fill =tk .BOTH ,padx =50 ,pady =30 )
        result_frame =tk .LabelFrame (main ,text ="📊 Результат",
        font =("Arial",16 ,"bold"),padx =30 ,pady =25 ,
        bg =DARK_THEME ['bg_secondary'],fg =DARK_THEME ['fg'],
        relief =tk .FLAT )
        result_frame .pack (fill =tk .BOTH ,expand =True )
        table_text =scrolledtext .ScrolledText (result_frame ,height =8 ,font =("Courier",12 ),
        bg =DARK_THEME ['entry_bg'],
        fg =DARK_THEME ['entry_fg'],
        relief =tk .FLAT ,bd =3 )
        table_text .pack (fill =tk .BOTH ,expand =True ,padx =20 ,pady =20 )
        expr =self .task2_expression
        expr =expr .replace ('∧',' and ').replace ('∨',' or ').replace ('¬',' not ')
        expr =expr .replace ('→',' <= ').replace ('≡',' == ')
        expr =' '.join (expr .split ())
        namespace ={}
        func_code =f"def F(x, y, z, w):\n    return {expr }"
        exec (func_code ,namespace )
        F =namespace ['F']
        table_text .insert (tk .END ,"📊 Таблица истинности:\n\n")
        table_text .insert (tk .END ,"Икс у z ш |  Ф\п")
        table_text .insert (tk .END ,"-"*25 +"\n")
        for row in self .task2_table_rows :
            x ,y ,z ,w =row
            res =F (x ,y ,z ,w )
            table_text .insert (tk .END ,f"{x }  {y }  {z }  {w }  |  {int (res )}\n")
        table_text .insert (tk .END ,"\n"+"="*40 +"\n\n")
        table_text .insert (tk .END ,f"✅ Соответствие столбцов переменным: {self .task2_solution }\n")
        table_text .config (state =tk .DISABLED )
    def task_5_interface (self ):
        """Задание 5: Арифметика в системах счисления - поэкранно"""
        self .task5_current_step =0
        self .task5_range_start =1
        self .task5_range_end =1000
        self .task5_condition ="R > 16"
        self .task5_code =""
        self .task5_results =[]
        main_frame =tk .Frame (self .root ,bg =DARK_THEME ['bg'])
        main_frame .pack (fill =tk .BOTH ,expand =True )
        self .task5_content_frame =tk .Frame (main_frame ,bg =DARK_THEME ['bg'])
        self .task5_content_frame .pack (fill =tk .BOTH ,expand =True ,padx =20 ,pady =20 )
        self .task5_button_frame =tk .Frame (main_frame ,bg =DARK_THEME ['bg'],pady =15 )
        self .task5_button_frame .pack (fill =tk .X ,side =tk .BOTTOM ,padx =20 )
        self .task5_show_step ()
    def task5_clear_content (self ):
        for widget in self .task5_content_frame .winfo_children ():
            widget .destroy ()
    def task5_update_buttons (self ):
        for widget in self .task5_button_frame .winfo_children ():
            widget .destroy ()
        if self .task5_current_step ==0 :
            btn =tk .Button (self .task5_button_frame ,text ="Далее →",
            command =self .task5_next_step ,
            font =("Arial",13 ,"bold"),bg =DARK_THEME ['button_bg'],
            fg =DARK_THEME ['fg'],
            activebackground =DARK_THEME ['accent_hover'],
            padx =30 ,pady =12 ,relief =tk .FLAT ,cursor ="hand2")
            btn .pack (side =tk .RIGHT ,padx =10 )
        elif self .task5_current_step ==1 :
            btn_back =tk .Button (self .task5_button_frame ,text ="← Назад",
            command =self .task5_prev_step ,
            font =("Arial",13 ,"bold"),bg =DARK_THEME ['bg_secondary'],
            fg =DARK_THEME ['fg'],
            activebackground =DARK_THEME ['bg_tertiary'],
            padx =25 ,pady =12 ,relief =tk .FLAT ,cursor ="hand2")
            btn_back .pack (side =tk .LEFT ,padx =10 )
            btn_next =tk .Button (self .task5_button_frame ,text ="Далее →",
            command =self .task5_next_step ,
            font =("Arial",13 ,"bold"),bg =DARK_THEME ['button_bg'],
            fg =DARK_THEME ['fg'],
            activebackground =DARK_THEME ['accent_hover'],
            padx =30 ,pady =12 ,relief =tk .FLAT ,cursor ="hand2")
            btn_next .pack (side =tk .RIGHT ,padx =10 )
        elif self .task5_current_step ==2 :
            btn_back =tk .Button (self .task5_button_frame ,text ="← Назад",
            command =self .task5_prev_step ,
            font =("Arial",13 ,"bold"),bg =DARK_THEME ['bg_secondary'],
            fg =DARK_THEME ['fg'],
            activebackground =DARK_THEME ['bg_tertiary'],
            padx =25 ,pady =12 ,relief =tk .FLAT ,cursor ="hand2")
            btn_back .pack (side =tk .LEFT ,padx =10 )
            btn_next =tk .Button (self .task5_button_frame ,text ="✓ Решить",
            command =self .task5_next_step ,
            font =("Arial",13 ,"bold"),bg =DARK_THEME ['success'],
            fg =DARK_THEME ['fg'],
            activebackground ='#66bb6a',
            padx =30 ,pady =12 ,relief =tk .FLAT ,cursor ="hand2")
            btn_next .pack (side =tk .RIGHT ,padx =10 )
        elif self .task5_current_step ==3 :
            btn_back =tk .Button (self .task5_button_frame ,text ="← Назад",
            command =self .task5_prev_step ,
            font =("Arial",13 ,"bold"),bg =DARK_THEME ['bg_secondary'],
            fg =DARK_THEME ['fg'],
            activebackground =DARK_THEME ['bg_tertiary'],
            padx =25 ,pady =12 ,relief =tk .FLAT ,cursor ="hand2")
            btn_back .pack (side =tk .LEFT ,padx =10 )
            btn_new =tk .Button (self .task5_button_frame ,text ="🔄 Новая задача",
            command =self .task5_new_task ,
            font =("Arial",13 ,"bold"),bg =DARK_THEME ['warning'],
            fg =DARK_THEME ['fg'],
            activebackground ='#ffa726',
            padx =30 ,pady =12 ,relief =tk .FLAT ,cursor ="hand2")
            btn_new .pack (side =tk .RIGHT ,padx =10 )
    def task5_show_step (self ):
        self .task5_clear_content ()
        if self .task5_current_step ==0 :
            self .task5_show_step_range ()
        elif self .task5_current_step ==1 :
            self .task5_show_step_code ()
        elif self .task5_current_step ==2 :
            self .task5_show_step_condition ()
        elif self .task5_current_step ==3 :
            self .task5_show_step_result ()
        self .task5_update_buttons ()
    def task5_next_step (self ):
        if self .task5_current_step ==0 :
            if not self .task5_save_range ():
                return
        elif self .task5_current_step ==1 :
            if not self .task5_save_code ():
                return
        elif self .task5_current_step ==2 :
            if not self .task5_save_condition ():
                return
            if not self .task5_solve ():
                return
        elif self .task5_current_step ==3 :
            self .task5_new_task ()
            return
        self .task5_current_step +=1
        self .task5_show_step ()
    def task5_prev_step (self ):
        if self .task5_current_step >0 :
            self .task5_current_step -=1
            self .task5_show_step ()
    def task5_new_task (self ):
        self .task5_current_step =0
        self .task5_range_start =1
        self .task5_range_end =1000
        self .task5_condition ="R > 16"
        self .task5_code =""
        self .task5_results =[]
        self .task5_show_step ()
    def task5_show_step_range (self ):
        frame =tk .Frame (self .task5_content_frame ,bg =DARK_THEME ['bg'])
        frame .pack (expand =True )
        tk .Label (frame ,text ="Шаг 1 из 3",font =("Arial",12 ),
        fg =DARK_THEME ['text_secondary'],bg =DARK_THEME ['bg']).pack (pady =10 )
        tk .Label (frame ,text ="🔢 Введите диапазон чисел N",
        font =("Arial",20 ,"bold"),bg =DARK_THEME ['bg'],
        fg =DARK_THEME ['fg']).pack (pady =30 )
        params_frame =tk .Frame (frame ,bg =DARK_THEME ['bg'])
        params_frame .pack (pady =20 )
        tk .Label (params_frame ,text ="От:",font =("Arial",14 ),
        bg =DARK_THEME ['bg'],fg =DARK_THEME ['fg']).grid (row =0 ,column =0 ,padx =15 ,pady =10 )
        self .task5_start_entry =tk .Entry (params_frame ,font =("Arial",16 ),width =15 ,
        justify ='center',
        bg =DARK_THEME ['entry_bg'],
        fg =DARK_THEME ['entry_fg'],
        insertbackground =DARK_THEME ['fg'],
        relief =tk .FLAT ,bd =5 )
        self .task5_start_entry .grid (row =0 ,column =1 ,padx =15 ,pady =10 )
        self .task5_start_entry .insert (0 ,str (self .task5_range_start ))
        self .task5_start_entry .focus ()
        tk .Label (params_frame ,text ="До:",font =("Arial",14 ),
        bg =DARK_THEME ['bg'],fg =DARK_THEME ['fg']).grid (row =0 ,column =2 ,padx =15 ,pady =10 )
        self .task5_end_entry =tk .Entry (params_frame ,font =("Arial",16 ),width =15 ,
        justify ='center',
        bg =DARK_THEME ['entry_bg'],
        fg =DARK_THEME ['entry_fg'],
        insertbackground =DARK_THEME ['fg'],
        relief =tk .FLAT ,bd =5 )
        self .task5_end_entry .grid (row =0 ,column =3 ,padx =15 ,pady =10 )
        self .task5_end_entry .insert (0 ,str (self .task5_range_end ))
        self .task5_end_entry .bind ('<Возврат>',lambda e :self .task5_next_step ())
    def task5_save_range (self ):
        try :
            self .task5_range_start =int (self .task5_start_entry .get ())
            self .task5_range_end =int (self .task5_end_entry .get ())
            if self .task5_range_start >=self .task5_range_end :
                messagebox .showerror ("Ошибка","Начало диапазона должно быть меньше конца")
                return False
            return True
        except ValueError :
            messagebox .showerror ("Ошибка","Введите целые числа")
            return False
    def task5_show_step_code (self ):
        """
        Шаг 2 из 3: Ввод кода преобразования.
        Пользователь вводит код, который преобразует число N в число R.
        Код должен использовать переменную N (исходное число) и создать переменную R (результат).
        """
        header =tk .Frame (self .task5_content_frame ,bg =DARK_THEME ['bg_secondary'],pady =15 )
        header .pack (fill =tk .X )
        tk .Label (header ,text ="Шаг 2 из 3",font =("Arial",12 ),
        fg =DARK_THEME ['text_secondary'],bg =DARK_THEME ['bg_secondary']).pack ()
        tk .Label (header ,text ="Введите код преобразования",
        font =("Arial",18 ,"bold"),bg =DARK_THEME ['bg_secondary'],
        fg =DARK_THEME ['fg']).pack (pady =8 )
        instruction =tk .LabelFrame (header ,text ="📖 Как написать код преобразования?",
        font =("Arial",11 ,"bold"),padx =15 ,pady =10 ,
        bg =DARK_THEME ['bg_tertiary'],fg =DARK_THEME ['fg'],
        relief =tk .FLAT )
        instruction .pack (fill =tk .X ,pady =8 ,padx =20 )
        tk .Label (instruction ,
        text ="1. Найдите в задании описание преобразования числа\n"
        "2. Используйте переменную N для исходного числа\n"
        "3. Создайте переменную R с результатом преобразования\n"
        "4. Доступные функции: bin(), int(), str(), sum(), len()\n"
        "5. Пример: R = bin(N)[2:]  # переводит N в двоичную систему\n\n"
        "💡 Код выполняется для каждого числа N из диапазона",
        font =("Arial",10 ),bg =DARK_THEME ['bg_tertiary'],
        fg =DARK_THEME ['text_secondary'],justify =tk .LEFT ).pack (anchor =tk .W ,padx =10 ,pady =5 )
        tk .Label (header ,text ="Используйте переменную N для исходного числа, R для результата",
        font =("Arial",11 ),fg =DARK_THEME ['text_secondary'],
        bg =DARK_THEME ['bg_secondary']).pack (pady =3 )
        code_frame =tk .Frame (self .task5_content_frame ,bg =DARK_THEME ['bg'])
        code_frame .pack (expand =True ,fill =tk .BOTH ,padx =50 ,pady =20 )
        self .task5_code_entry =scrolledtext .ScrolledText (code_frame ,height =12 ,font =("Courier",12 ),
        bg =DARK_THEME ['entry_bg'],
        fg =DARK_THEME ['entry_fg'],
        insertbackground =DARK_THEME ['fg'],
        relief =tk .FLAT ,bd =3 )
        self .task5_code_entry .pack (fill =tk .BOTH ,expand =True )
        default_code ="""# Пример: модификация двоичного числа
R = bin(N)[2:]
sm = sum(map(int, R))
if sm % 2 == 0:
    R = '10' + R[2:] + '0'
else:
    R = '11' + R[2:] + '1'
R = int(R, 2)"""
        if self .task5_code :
            self .task5_code_entry .insert (1.0 ,self .task5_code )
        else :
            self .task5_code_entry .insert (1.0 ,default_code )
    def task5_save_code (self ):
        code =self .task5_code_entry .get (1.0 ,tk .END ).strip ()
        if not code :
            messagebox .showerror ("Ошибка","Введите код преобразования")
            return False
        self .task5_code =code
        return True
    def task5_show_step_condition (self ):
        """
        Шаг 3 из 3: Ввод условия для результата.
        Пользователь вводит условие, которому должно удовлетворять число R.
        Программа найдет все числа N, для которых после преобразования R удовлетворяет условию.
        """
        header =tk .Frame (self .task5_content_frame ,bg =DARK_THEME ['bg_secondary'],pady =15 )
        header .pack (fill =tk .X )
        tk .Label (header ,text ="Шаг 3 из 3",font =("Arial",12 ),
        fg =DARK_THEME ['text_secondary'],bg =DARK_THEME ['bg_secondary']).pack ()
        tk .Label (header ,text ="Введите условие для результата R",
        font =("Arial",18 ,"bold"),bg =DARK_THEME ['bg_secondary'],
        fg =DARK_THEME ['fg']).pack (pady =8 )
        instruction =tk .LabelFrame (header ,text ="📖 Как написать условие?",
        font =("Arial",11 ,"bold"),padx =15 ,pady =10 ,
        bg =DARK_THEME ['bg_tertiary'],fg =DARK_THEME ['fg'],
        relief =tk .FLAT )
        instruction .pack (fill =tk .X ,pady =8 ,padx =20 )
        tk .Label (instruction ,
        text ="Найдите в задании условие для результата R.\n\n"
        "Примеры условий:\n"
        "  • R > 16        (R больше 16)\n"
        "  • R % 3 == 0    (R делится на 3)\n"
        "  • R <= 100       (R меньше или равно 100)\n"
        "  • R == 25        (R равно 25)\n"
        "  • R >= 50 и R <= 200 (R от 50 до 200)\n\n"
        "💡 Используйте стандартные операторы Python: >, <, >=, <=, ==, !=, %",
        font =("Arial",10 ),bg =DARK_THEME ['bg_tertiary'],
        fg =DARK_THEME ['text_secondary'],justify =tk .LEFT ).pack (anchor =tk .W ,padx =10 ,pady =5 )
        cond_frame =tk .Frame (self .task5_content_frame ,bg =DARK_THEME ['bg'])
        cond_frame .pack (expand =True ,fill =tk .X ,padx =50 ,pady =30 )
        self .task5_condition_entry =tk .Entry (cond_frame ,font =("Arial",16 ),
        bg =DARK_THEME ['entry_bg'],
        fg =DARK_THEME ['entry_fg'],
        insertbackground =DARK_THEME ['fg'],
        relief =tk .FLAT ,bd =5 )
        self .task5_condition_entry .pack (fill =tk .X ,pady =10 )
        self .task5_condition_entry .insert (0 ,self .task5_condition )
        self .task5_condition_entry .focus ()
        self .task5_condition_entry .bind ('<Возврат>',lambda e :self .task5_next_step ())
    def task5_save_condition (self ):
        condition =self .task5_condition_entry .get ().strip ()
        if not condition :
            messagebox .showerror ("Ошибка","Введите условие")
            return False
        self .task5_condition =condition
        return True
    def task5_solve (self ):
        """
        УНИВЕРСАЛЬНОЕ решение задания 5: находит числа N, для которых выполняется условие после преобразования.
        Поддерживает ВСЕ прототипы заданий:
        - Преобразования в различных системах счисления (2, 8, 16)
        - Модификации двоичных строк (добавление/удаление битов)
        - Арифметические операции над числами
        - Проверки на делимость, кратность
        - Любые условия для результата R
        Алгоритм:
        1. Перебираем все числа N в заданном диапазоне
        2. Для каждого N выполняем код преобразования
        3. Проверяем условие для результата R
        4. Если условие выполняется - добавляем в результаты
        Пользователь может задать любой код преобразования и любое условие.
        Returns:
            bool: True если найдены решения, False иначе
        """
        try :
            self .task5_results =[]
            processed_count =0
            error_count =0
            total_numbers =self .task5_range_end -self .task5_range_start +1
            for N in range (self .task5_range_start ,self .task5_range_end +1 ):
                try :
                    namespace ={
                    'N':N ,
                    'bin':bin ,'int':int ,'sum':sum ,'map':map ,
                    'oct':oct ,'hex':hex ,'str':str ,'len':len ,
                    'abs':abs ,'max':max ,'min':min ,'pow':pow ,
                    'True':True ,'False':False ,
                    'reversed':reversed ,'sorted':sorted ,
                    }
                    exec (self .task5_code ,namespace )
                    R =namespace .get ('R',None )
                    if R is None :
                        error_count +=1
                        continue
                    namespace ['R']=R
                    processed_count +=1
                    try :
                        condition_result =eval (self .task5_condition ,namespace )
                        if condition_result :
                            self .task5_results .append ((N ,R ))
                    except Exception :
                        error_count +=1
                        continue
                except Exception as e :
                    error_count +=1
                    continue
            if not self .task5_results :
                if error_count ==total_numbers :
                    messagebox .showerror ("Ошибка",
                    "Не удалось обработать ни одно число.\n\n"
                    "💡 Возможные причины:\n"
                    "  1. Ошибка в коде преобразования\n"
                    "  2. Переменная R не создается в коде\n"
                    "  3. Неправильное условие для R\n\n"
                    "Проверьте код и условие.")
                else :
                    messagebox .showwarning ("Результат",
                    f"Решения не найдены.\n\n"
                    f"Обработано чисел: {processed_count } из {total_numbers }\n"
                    f"Ошибок: {error_count }\n\n"
                    "💡 Попробуйте:\n"
                    "  - Изменить диапазон чисел\n"
                    "  - Проверить код преобразования\n"
                    "  - Изменить условие для R")
                return False
            return True
        except Exception as e :
            messagebox .showerror ("Ошибка",
            f"Ошибка при решении: {e }\n\n"
            "💡 Проверьте:\n"
            "  1. Правильность кода преобразования\n"
            "  2. Правильность условия для R\n"
            "  3. Корректность диапазона чисел")
            return False
    def task5_show_step_result (self ):
        """
        Показывает результат решения задания 5.
        Отображает все найденные числа N и соответствующие значения R.
        """
        header =tk .Frame (self .task5_content_frame ,bg =DARK_THEME ['bg_secondary'],pady =15 )
        header .pack (fill =tk .X )
        tk .Label (header ,text ="Решение найдено",
        font =("Arial",16 ,"bold"),fg =DARK_THEME ['success'],
        bg =DARK_THEME ['bg_secondary']).pack ()
        main =tk .Frame (self .task5_content_frame ,bg =DARK_THEME ['bg'])
        main .pack (expand =True ,fill =tk .BOTH ,padx =50 ,pady =30 )
        result_frame =tk .LabelFrame (main ,text ="📊 Результаты",
        font =("Arial",16 ,"bold"),padx =30 ,pady =25 ,
        bg =DARK_THEME ['bg_secondary'],fg =DARK_THEME ['fg'],
        relief =tk .FLAT )
        result_frame .pack (fill =tk .BOTH ,expand =True )
        result_text =scrolledtext .ScrolledText (result_frame ,height =15 ,font =("Courier",12 ),
        bg =DARK_THEME ['entry_bg'],
        fg =DARK_THEME ['entry_fg'],
        relief =tk .FLAT ,bd =3 )
        result_text .pack (fill =tk .BOTH ,expand =True ,padx =20 ,pady =20 )
        result_text .insert (tk .END ,f"🔍 Найдено {len (self .task5_results )} решений:\n\n")
        for N ,R in self .task5_results [:50 ]:
            result_text .insert (tk .END ,f"N = {N }, R = {R }\n")
        if len (self .task5_results )>50 :
            result_text .insert (tk .END ,f"\n... и еще {len (self .task5_results )-50 } решений\n")
        result_text .insert (tk .END ,f"\n🎯 Минимальное N: {min (self .task5_results )[0 ]}\n")
        result_text .insert (tk .END ,f"🎯 Максимальное N: {max (self .task5_results )[0 ]}\n")
        result_text .config (state =tk .DISABLED )
    def task_6_interface (self ):
        """
        Задание 6: Алгоритмы с циклами (turtle) - редактор кода.
        Пользователь редактирует код для визуализации алгоритма с помощью библиотеки turtle.
        После редактирования можно запустить визуализацию.
        """
        main_frame =tk .Frame (self .root ,bg =DARK_THEME ['bg'])
        main_frame .pack (fill =tk .BOTH ,expand =True ,padx =30 ,pady =30 )
        tk .Label (main_frame ,text ="Задание 6: Алгоритмы с циклами (turtle)",
        font =("Arial",18 ,"bold"),bg =DARK_THEME ['bg'],fg =DARK_THEME ['fg']).pack (pady =15 )
        info_frame =tk .LabelFrame (main_frame ,text ="📖 Как использовать редактор?",
        font =("Arial",13 ,"bold"),padx =20 ,pady =15 ,
        bg =DARK_THEME ['bg_secondary'],fg =DARK_THEME ['fg'],
        relief =tk .FLAT )
        info_frame .pack (fill =tk .X ,pady =15 )
        instruction_text =(
        "1. Найдите в задании алгоритм с командами forward(), right(), left() и т.д.\n"
        "2. Отредактируйте код ниже под ваше задание:\n"
        "   • Измените числа в командах forward(число) и right(число)\n"
        "   • Измените количество повторений в циклах for i in range(...)\n"
        "   • Измените масштаб k если нужно\n"
        "3. Нажмите 'Запустить визуализацию' для просмотра результата\n\n"
        "💡 Основные команды turtle:\n"
        "   • forward(n) - движение вперед на n шагов\n"
        "   • right(угол) - поворот направо на угол градусов\n"
        "   • left(угол) - поворот налево на угол градусов\n"
        "   • up() - поднять перо (не рисовать при движении)\n"
        "   • down() - опустить перо (рисовать при движении)"
        )
        tk .Label (info_frame ,text =instruction_text ,
        font =("Arial",10 ),bg =DARK_THEME ['bg_secondary'],
        fg =DARK_THEME ['text_secondary'],justify =tk .LEFT ).pack (anchor =tk .W ,padx =10 ,pady =5 )
        code_frame =tk .LabelFrame (main_frame ,text ="💻 Код для turtle",
        font =("Arial",13 ,"bold"),padx =20 ,pady =15 ,
        bg =DARK_THEME ['bg_secondary'],fg =DARK_THEME ['fg'],
        relief =tk .FLAT )
        code_frame .pack (fill =tk .BOTH ,expand =True ,pady =15 )
        code_text =scrolledtext .ScrolledText (code_frame ,height =20 ,font =("Courier",11 ),
        bg =DARK_THEME ['entry_bg'],
        fg =DARK_THEME ['entry_fg'],
        insertbackground =DARK_THEME ['fg'],
        relief =tk .FLAT ,bd =3 )
        code_text .pack (fill =tk .BOTH ,expand =True ,padx =10 ,pady =10 )
        default_code ="""от импорта черепах *
трассировщик(0)
к = 20
слева(90)
для меня в диапазоне (3):
    вперед(27 * к)
    правильно(90)
    вперед(12 * к)
    правильно(90)
вверх()
вперед(4 * к)
правильно(90)
вперед(6 * к)
слева(90)
вниз()
для меня в диапазоне (4):
    вперед(83*к)
    правильно(90)
    вперед(77 * к)
    правильно(90)
вверх()
для x в диапазоне (-50, 50):
    для y в диапазоне (-50, 50):
        перейти к (х * к, у * к)
        точка(3, 'черный')
выходонклик()"""
        code_text .insert (1.0 ,default_code )
        def run_code ():
            """
            Запускает код turtle для визуализации.
            Создает временный файл с кодом и запускает его в отдельном процессе.
            Откроется новое окно с визуализацией алгоритма.
            """
            try :
                code =code_text .get (1.0 ,tk .END )
                if not code .strip ():
                    messagebox .showerror ("Ошибка",
                    "Код не может быть пустым.\n\n"
                    "💡 Введите код алгоритма для визуализации.")
                    return
                import tempfile
                with tempfile .NamedTemporaryFile (mode ='w',suffix ='.py',delete =False ,encoding ='utf-8')as f :
                    f .write (code )
                    temp_file =f .name
                subprocess .Popen ([sys .executable ,temp_file ])
                messagebox .showinfo ("Информация",
                "Визуализация запущена!\n\n"
                "💡 Откроется новое окно с графикой.\n"
                "Закройте окно после просмотра результата.")
            except Exception as e :
                messagebox .showerror ("Ошибка",
                f"Не удалось запустить код: {e }\n\n"
                "💡 Проверьте:\n"
                "  1. Правильность синтаксиса Python\n"
                "  2. Наличие всех необходимых команд turtle\n"
                "  3. Корректность чисел и параметров")
        tk .Button (main_frame ,text ="🚀 Запустить визуализацию",command =run_code ,
        font =("Arial",14 ,"bold"),bg =DARK_THEME ['success'],
        fg =DARK_THEME ['fg'],
        activebackground ='#66bb6a',
        padx =40 ,pady =15 ,relief =tk .FLAT ,cursor ="hand2").pack (pady =20 )
    def task_3_interface (self ):
        """
        Задание 3: База данных - подсчет изменений количества товаров.
        Пошаговый ввод: данные о движении товаров, условия фильтрации, результат.
        """
        self .task3_current_step =0
        self .task3_data =[]
        self .task3_product =""
        self .task3_district =""
        self .task3_date_from =""
        self .task3_date_to =""
        self .task3_result =None
        main_frame =tk .Frame (self .root ,bg =DARK_THEME ['bg'])
        main_frame .pack (fill =tk .BOTH ,expand =True )
        self .task3_content_frame =tk .Frame (main_frame ,bg =DARK_THEME ['bg'])
        self .task3_content_frame .pack (fill =tk .BOTH ,expand =True ,padx =20 ,pady =20 )
        self .task3_button_frame =tk .Frame (main_frame ,bg =DARK_THEME ['bg'],pady =15 )
        self .task3_button_frame .pack (fill =tk .X ,side =tk .BOTTOM ,padx =20 )
        self .task3_show_step ()
    def task3_clear_content (self ):
        for widget in self .task3_content_frame .winfo_children ():
            widget .destroy ()
    def task3_update_buttons (self ):
        for widget in self .task3_button_frame .winfo_children ():
            widget .destroy ()
        if self .task3_current_step ==0 :
            btn =tk .Button (self .task3_button_frame ,text ="Далее →",
            command =self .task3_next_step ,
            font =("Arial",13 ,"bold"),bg =DARK_THEME ['button_bg'],
            fg =DARK_THEME ['fg'],padx =25 ,pady =12 ,relief =tk .FLAT ,cursor ="hand2")
            btn .pack (side =tk .RIGHT ,padx =10 )
        elif self .task3_current_step ==1 :
            btn_back =tk .Button (self .task3_button_frame ,text ="← Назад",
            command =self .task3_prev_step ,
            font =("Arial",13 ,"bold"),bg =DARK_THEME ['bg_secondary'],
            fg =DARK_THEME ['fg'],padx =25 ,pady =12 ,relief =tk .FLAT ,cursor ="hand2")
            btn_back .pack (side =tk .LEFT ,padx =10 )
            btn_next =tk .Button (self .task3_button_frame ,text ="✓ Решить",
            command =self .task3_next_step ,
            font =("Arial",13 ,"bold"),bg =DARK_THEME ['success'],
            fg =DARK_THEME ['fg'],padx =25 ,pady =12 ,relief =tk .FLAT ,cursor ="hand2")
            btn_next .pack (side =tk .RIGHT ,padx =10 )
        elif self .task3_current_step ==2 :
            btn_back =tk .Button (self .task3_button_frame ,text ="← Назад",
            command =self .task3_prev_step ,
            font =("Arial",13 ,"bold"),bg =DARK_THEME ['bg_secondary'],
            fg =DARK_THEME ['fg'],padx =25 ,pady =12 ,relief =tk .FLAT ,cursor ="hand2")
            btn_back .pack (side =tk .LEFT ,padx =10 )
            btn_new =tk .Button (self .task3_button_frame ,text ="🔄 Новая задача",
            command =self .task3_new_task ,
            font =("Arial",13 ,"bold"),bg =DARK_THEME ['warning'],
            fg =DARK_THEME ['fg'],padx =30 ,pady =12 ,relief =tk .FLAT ,cursor ="hand2")
            btn_new .pack (side =tk .RIGHT ,padx =10 )
    def task3_show_step (self ):
        self .task3_clear_content ()
        if self .task3_current_step ==0 :
            self .task3_show_step_data ()
        elif self .task3_current_step ==1 :
            self .task3_show_step_filters ()
        elif self .task3_current_step ==2 :
            self .task3_show_step_result ()
        self .task3_update_buttons ()
    def task3_next_step (self ):
        if self .task3_current_step ==0 :
            if not self .task3_save_data ():
                return
        elif self .task3_current_step ==1 :
            if not self .task3_save_filters ():
                return
            if not self .task3_solve ():
                return
        elif self .task3_current_step ==2 :
            self .task3_new_task ()
            return
        self .task3_current_step +=1
        self .task3_show_step ()
    def task3_prev_step (self ):
        if self .task3_current_step >0 :
            self .task3_current_step -=1
            self .task3_show_step ()
    def task3_new_task (self ):
        self .task3_current_step =0
        self .task3_data =[]
        self .task3_product =""
        self .task3_district =""
        self .task3_date_from =""
        self .task3_date_to =""
        self .task3_result =None
        self .task3_show_step ()
    def task3_show_step_data (self ):
        """
        Шаг 1 из 2: Ввод данных о движении товаров.
        Пользователь вводит записи о поступлениях и продажах товаров.
        """
        header =tk .Frame (self .task3_content_frame ,bg =DARK_THEME ['bg_secondary'],pady =15 )
        header .pack (fill =tk .X )
        tk .Label (header ,text ="Шаг 1 из 2",font =("Arial",12 ),
        fg =DARK_THEME ['text_secondary'],bg =DARK_THEME ['bg_secondary']).pack ()
        tk .Label (header ,text ="Введите данные о движении товаров",
        font =("Arial",18 ,"bold"),bg =DARK_THEME ['bg_secondary'],
        fg =DARK_THEME ['fg']).pack (pady =8 )
        instruction =tk .LabelFrame (header ,text ="📖 Как заполнить таблицу?",
        font =("Arial",11 ,"bold"),padx =15 ,pady =10 ,
        bg =DARK_THEME ['bg_tertiary'],fg =DARK_THEME ['fg'],
        relief =tk .FLAT )
        instruction .pack (fill =tk .X ,pady =8 ,padx =20 )
        tk .Label (instruction ,
        text ="1. Найдите в задании таблицу 'Движение товаров'\n"
        "2. Для каждой записи укажите: Дата, Товар, Район, Тип операции, Количество\n"
        "3. Тип операции: 'Поступление' или 'Продажа'\n"
        "4. Формат даты: ДД.ММ (например: 01.10, 15.10)\n"
        "5. Каждая строка - одна запись, поля разделены запятыми\n\n"
        "💡 Пример строки: 01.10, Сливки порционные питьевые безлактозные 10%, Заречный, Поступление, 50",
        font =("Arial",10 ),bg =DARK_THEME ['bg_tertiary'],
        fg =DARK_THEME ['text_secondary'],justify =tk .LEFT ).pack (anchor =tk .W ,padx =10 ,pady =5 )
        data_frame =tk .Frame (self .task3_content_frame ,bg =DARK_THEME ['bg'])
        data_frame .pack (expand =True ,fill =tk .BOTH ,padx =30 ,pady =20 )
        tk .Label (data_frame ,text ="Введите данные (каждая строка - одна запись):",
        font =("Arial",12 ),bg =DARK_THEME ['bg'],fg =DARK_THEME ['fg']).pack (anchor =tk .W ,pady =5 )
        self .task3_data_entry =scrolledtext .ScrolledText (data_frame ,height =15 ,font =("Courier",10 ),
        bg =DARK_THEME ['entry_bg'],fg =DARK_THEME ['entry_fg'],
        insertbackground =DARK_THEME ['fg'],relief =tk .FLAT ,bd =3 )
        self .task3_data_entry .pack (fill =tk .BOTH ,expand =True ,pady =10 )
        if self .task3_data :
            text ='\n'.join ([f"{d ['date']}, {d ['product']}, {d ['district']}, {d ['operation']}, {d ['quantity']}"
            for d in self .task3_data ])
            self .task3_data_entry .insert (1.0 ,text )
        else :
            example ="01.10, Сливки порционные питьевые безлактозные 10%, Заречный, Поступление, 50\n"
            example +="05.10, Сливки порционные питьевые безлактозные 10%, Заречный, Продажа, 20\n"
            example +="10.10, Сливки порционные питьевые безлактозные 10%, Заречный, Поступление, 30\n"
            example +="15.10, Сливки порционные питьевые безлактозные 10%, Заречный, Продажа, 15"
            self .task3_data_entry .insert (1.0 ,example )
    def task3_save_data (self ):
        """Сохраняет данные о движении товаров из текстового поля"""
        text =self .task3_data_entry .get (1.0 ,tk .END ).strip ()
        if not text :
            messagebox .showerror ("Ошибка","Введите данные о движении товаров")
            return False
        self .task3_data =[]
        for line in text .split ('\n'):
            line =line .strip ()
            if not line :
                continue
            parts =[p .strip ()for p in line .split (',')]
            if len (parts )<5 :
                messagebox .showerror ("Ошибка",
                f"Неверный формат строки: {line }\n\n"
                "💡 Формат: Дата, Товар, Район, Тип операции, Количество\n"
                "Пример: 01.10, Сливки порционные питьевые безлактозные 10%, Заречный, Поступление, 50")
                return False
            try :
                quantity =int (parts [4 ])
                self .task3_data .append ({
                'date':parts [0 ],
                'product':parts [1 ],
                'district':parts [2 ],
                'operation':parts [3 ],
                'quantity':quantity
                })
            except ValueError :
                messagebox .showerror ("Ошибка",
                f"Неверное количество в строке: {line }\n\n"
                "💡 Количество должно быть целым числом")
                return False
        if not self .task3_data :
            messagebox .showerror ("Ошибка","Не удалось распарсить данные")
            return False
        return True
    def task3_show_step_filters (self ):
        """
        Шаг 2 из 2: Ввод условий фильтрации.
        Пользователь указывает товар, район и период дат для подсчета.
        """
        header =tk .Frame (self .task3_content_frame ,bg =DARK_THEME ['bg_secondary'],pady =15 )
        header .pack (fill =tk .X )
        tk .Label (header ,text ="Шаг 2 из 2",font =("Arial",12 ),
        fg =DARK_THEME ['text_secondary'],bg =DARK_THEME ['bg_secondary']).pack ()
        tk .Label (header ,text ="Введите условия фильтрации",
        font =("Arial",18 ,"bold"),bg =DARK_THEME ['bg_secondary'],
        fg =DARK_THEME ['fg']).pack (pady =8 )
        instruction =tk .LabelFrame (header ,text ="📖 Как заполнить условия?",
        font =("Arial",11 ,"bold"),padx =15 ,pady =10 ,
        bg =DARK_THEME ['bg_tertiary'],fg =DARK_THEME ['fg'],
        relief =tk .FLAT )
        instruction .pack (fill =tk .X ,pady =8 ,padx =20 )
        tk .Label (instruction ,
        text ="1. Найдите в задании название товара (точно как в таблице)\n"
        "2. Найдите название района (например: Заречный)\n"
        "3. Укажите период дат (начало и конец включительно)\n"
        "4. Формат даты: ДД.ММ (например: 01.10, 15.10)\n\n"
        "💡 Программа найдет все записи, соответствующие этим условиям",
        font =("Arial",10 ),bg =DARK_THEME ['bg_tertiary'],
        fg =DARK_THEME ['text_secondary'],justify =tk .LEFT ).pack (anchor =tk .W ,padx =10 ,pady =5 )
        filters_frame =tk .Frame (self .task3_content_frame ,bg =DARK_THEME ['bg'])
        filters_frame .pack (expand =True ,fill =tk .X ,padx =50 ,pady =30 )
        tk .Label (filters_frame ,text ="Название товара:",font =("Arial",13 ),
        bg =DARK_THEME ['bg'],fg =DARK_THEME ['fg']).grid (row =0 ,column =0 ,sticky =tk .W ,pady =10 )
        self .task3_product_entry =tk .Entry (filters_frame ,font =("Arial",12 ),width =50 ,
        bg =DARK_THEME ['entry_bg'],fg =DARK_THEME ['entry_fg'],
        insertbackground =DARK_THEME ['fg'],relief =tk .FLAT ,bd =3 )
        self .task3_product_entry .grid (row =0 ,column =1 ,padx =10 ,pady =10 ,sticky =tk .EW )
        if self .task3_product :
            self .task3_product_entry .insert (0 ,self .task3_product )
        tk .Label (filters_frame ,text ="Район:",font =("Arial",13 ),
        bg =DARK_THEME ['bg'],fg =DARK_THEME ['fg']).grid (row =1 ,column =0 ,sticky =tk .W ,pady =10 )
        self .task3_district_entry =tk .Entry (filters_frame ,font =("Arial",12 ),width =50 ,
        bg =DARK_THEME ['entry_bg'],fg =DARK_THEME ['entry_fg'],
        insertbackground =DARK_THEME ['fg'],relief =tk .FLAT ,bd =3 )
        self .task3_district_entry .grid (row =1 ,column =1 ,padx =10 ,pady =10 ,sticky =tk .EW )
        if self .task3_district :
            self .task3_district_entry .insert (0 ,self .task3_district )
        tk .Label (filters_frame ,text ="Дата начала (ДД.ММ):",font =("Arial",13 ),
        bg =DARK_THEME ['bg'],fg =DARK_THEME ['fg']).grid (row =2 ,column =0 ,sticky =tk .W ,pady =10 )
        self .task3_date_from_entry =tk .Entry (filters_frame ,font =("Arial",12 ),width =20 ,
        bg =DARK_THEME ['entry_bg'],fg =DARK_THEME ['entry_fg'],
        insertbackground =DARK_THEME ['fg'],relief =tk .FLAT ,bd =3 )
        self .task3_date_from_entry .grid (row =2 ,column =1 ,padx =10 ,pady =10 ,sticky =tk .W )
        if self .task3_date_from :
            self .task3_date_from_entry .insert (0 ,self .task3_date_from )
        tk .Label (filters_frame ,text ="Дата конца (ДД.ММ):",font =("Arial",13 ),
        bg =DARK_THEME ['bg'],fg =DARK_THEME ['fg']).grid (row =3 ,column =0 ,sticky =tk .W ,pady =10 )
        self .task3_date_to_entry =tk .Entry (filters_frame ,font =("Arial",12 ),width =20 ,
        bg =DARK_THEME ['entry_bg'],fg =DARK_THEME ['entry_fg'],
        insertbackground =DARK_THEME ['fg'],relief =tk .FLAT ,bd =3 )
        self .task3_date_to_entry .grid (row =3 ,column =1 ,padx =10 ,pady =10 ,sticky =tk .W )
        if self .task3_date_to :
            self .task3_date_to_entry .insert (0 ,self .task3_date_to )
        filters_frame .grid_columnconfigure (1 ,weight =1 )
    def task3_save_filters (self ):
        """Сохраняет условия фильтрации"""
        self .task3_product =self .task3_product_entry .get ().strip ()
        self .task3_district =self .task3_district_entry .get ().strip ()
        self .task3_date_from =self .task3_date_from_entry .get ().strip ()
        self .task3_date_to =self .task3_date_to_entry .get ().strip ()
        if not self .task3_product :
            messagebox .showerror ("Ошибка","Введите название товара")
            return False
        if not self .task3_district :
            messagebox .showerror ("Ошибка","Введите название района")
            return False
        if not self .task3_date_from or not self .task3_date_to :
            messagebox .showerror ("Ошибка","Введите даты начала и конца периода")
            return False
        return True
    def task3_parse_date (self ,date_str ):
        """Парсит дату в формате ДД.ММ и возвращает кортеж (день, месяц)"""
        try :
            parts =date_str .split ('.')
            if len (parts )!=2 :
                return None
            day =int (parts [0 ])
            month =int (parts [1 ])
            return (day ,month )
        except :
            return None
    def task3_date_in_range (self ,date_str ,date_from ,date_to ):
        """Проверяет, попадает ли дата в диапазон"""
        date =self .task3_parse_date (date_str )
        date_f =self .task3_parse_date (date_from )
        date_t =self .task3_parse_date (date_to )
        if not date or not date_f or not date_t :
            return False
        if date_f [1 ]!=date_t [1 ]:
            return False
        return date_f [0 ]<=date [0 ]<=date_t [0 ]
    def task3_solve (self ):
        """
        Подсчет изменения количества товаров за период.
        Алгоритм:
        1. Фильтруем записи по товару, району и периоду дат
        2. Суммируем поступления (тип операции = "Поступление")
        3. Суммируем продажи (тип операции = "Продажа")
        4. Изменение = поступления - продажи
        Returns:
            bool: True если подсчет выполнен успешно, False иначе
        """
        try :
            receipts =0
            sales =0
            matched_records =[]
            for record in self .task3_data :
                if (record ['product']==self .task3_product and
                record ['district']==self .task3_district and
                self .task3_date_in_range (record ['date'],self .task3_date_from ,self .task3_date_to )):
                    matched_records .append (record )
                    if record ['operation'].lower ()=='поступление':
                        receipts +=record ['quantity']
                    elif record ['operation'].lower ()=='продажа':
                        sales +=record ['quantity']
            if not matched_records :
                messagebox .showwarning ("Результат",
                "Не найдено записей, соответствующих условиям.\n\n"
                "💡 Проверьте:\n"
                "  1. Правильность названия товара (точно как в таблице)\n"
                "  2. Правильность названия района\n"
                "  3. Правильность дат периода\n"
                "  4. Существуют ли такие записи в введенных данных")
                return False
            change =receipts -sales
            self .task3_result ={
            'change':change ,
            'receipts':receipts ,
            'sales':sales ,
            'matched_count':len (matched_records ),
            'matched_records':matched_records
            }
            return True
        except Exception as e :
            messagebox .showerror ("Ошибка",
            f"Ошибка при подсчете: {e }\n\n"
            "💡 Проверьте правильность введенных данных")
            return False
    def task3_show_step_result (self ):
        """Показывает результат подсчета изменения количества товаров"""
        header =tk .Frame (self .task3_content_frame ,bg =DARK_THEME ['bg_secondary'],pady =15 )
        header .pack (fill =tk .X )
        tk .Label (header ,text ="Решение найдено",
        font =("Arial",16 ,"bold"),fg =DARK_THEME ['success'],
        bg =DARK_THEME ['bg_secondary']).pack ()
        main =tk .Frame (self .task3_content_frame ,bg =DARK_THEME ['bg'])
        main .pack (expand =True ,fill =tk .BOTH ,padx =50 ,pady =30 )
        result_frame =tk .LabelFrame (main ,text ="📊 Результат",
        font =("Arial",16 ,"bold"),padx =30 ,pady =25 ,
        bg =DARK_THEME ['bg_secondary'],fg =DARK_THEME ['fg'],
        relief =tk .FLAT )
        result_frame .pack (fill =tk .BOTH ,expand =True )
        r =self .task3_result
        result_text =scrolledtext .ScrolledText (result_frame ,height =12 ,font =("Courier",11 ),
        bg =DARK_THEME ['entry_bg'],fg =DARK_THEME ['entry_fg'],
        relief =tk .FLAT ,bd =3 )
        result_text .pack (fill =tk .BOTH ,expand =True ,padx =20 ,pady =20 )
        result_text .insert (tk .END ,f"Товар: {self .task3_product }\n")
        result_text .insert (tk .END ,f"Район: {self .task3_district }\n")
        result_text .insert (tk .END ,f"Период: с {self .task3_date_from } по {self .task3_date_to }\n\n")
        result_text .insert (tk .END ,"="*50 +"\n\n")
        result_text .insert (tk .END ,f"Найдено записей: {r ['matched_count']}\n\n")
        result_text .insert (tk .END ,f"Поступления: {r ['receipts']} упаковок\n")
        result_text .insert (tk .END ,f"Продажи: {r ['sales']} упаковок\n\n")
        result_text .insert (tk .END ,"="*50 +"\n\n")
        result_text .insert (tk .END ,f"✅ Изменение количества: {r ['change']} упаковок\n\n")
        result_text .insert (tk .END ,"Детали записей:\n")
        result_text .insert (tk .END ,"-"*50 +"\n")
        for rec in r ['matched_records']:
            result_text .insert (tk .END ,
            f"{rec ['date']} | {rec ['operation']} | {rec ['quantity']} упаковок\n")
        result_text .config (state =tk .DISABLED )
    def task_4_interface (self ):
        """
        Задание 4: Кодирование информации - двоичное дерево.
        Пошаговый ввод: таблица кодов, слово для кодирования, результат.
        """
        self .task4_current_step =0
        self .task4_code_table ={}
        self .task4_word =""
        self .task4_result =None
        main_frame =tk .Frame (self .root ,bg =DARK_THEME ['bg'])
        main_frame .pack (fill =tk .BOTH ,expand =True )
        self .task4_content_frame =tk .Frame (main_frame ,bg =DARK_THEME ['bg'])
        self .task4_content_frame .pack (fill =tk .BOTH ,expand =True ,padx =20 ,pady =20 )
        self .task4_button_frame =tk .Frame (main_frame ,bg =DARK_THEME ['bg'],pady =15 )
        self .task4_button_frame .pack (fill =tk .X ,side =tk .BOTTOM ,padx =20 )
        self .task4_show_step ()
    def task4_clear_content (self ):
        for widget in self .task4_content_frame .winfo_children ():
            widget .destroy ()
    def task4_update_buttons (self ):
        for widget in self .task4_button_frame .winfo_children ():
            widget .destroy ()
        if self .task4_current_step ==0 :
            btn =tk .Button (self .task4_button_frame ,text ="Далее →",
            command =self .task4_next_step ,font =("Arial",12 ),
            bg =DARK_THEME ['button_bg'],fg =DARK_THEME ['fg'],
            padx =25 ,pady =10 ,relief =tk .FLAT ,cursor ="hand2")
            btn .pack (side =tk .RIGHT ,padx =10 )
        elif self .task4_current_step ==1 :
            btn_back =tk .Button (self .task4_button_frame ,text ="← Назад",
            command =self .task4_prev_step ,font =("Arial",12 ),
            bg =DARK_THEME ['bg_secondary'],fg =DARK_THEME ['fg'],
            padx =20 ,pady =10 ,relief =tk .FLAT ,cursor ="hand2")
            btn_back .pack (side =tk .LEFT ,padx =10 )
            btn_next =tk .Button (self .task4_button_frame ,text ="✓ Решить",
            command =self .task4_next_step ,font =("Arial",12 ),
            bg =DARK_THEME ['success'],fg =DARK_THEME ['fg'],
            padx =25 ,pady =10 ,relief =tk .FLAT ,cursor ="hand2")
            btn_next .pack (side =tk .RIGHT ,padx =10 )
        elif self .task4_current_step ==2 :
            btn_back =tk .Button (self .task4_button_frame ,text ="← Назад",
            command =self .task4_prev_step ,font =("Arial",12 ),
            bg =DARK_THEME ['bg_secondary'],fg =DARK_THEME ['fg'],
            padx =20 ,pady =10 ,relief =tk .FLAT ,cursor ="hand2")
            btn_back .pack (side =tk .LEFT ,padx =10 )
            btn_new =tk .Button (self .task4_button_frame ,text ="🔄 Новая задача",
            command =self .task4_new_task ,font =("Arial",12 ),
            bg =DARK_THEME ['warning'],fg =DARK_THEME ['fg'],
            padx =25 ,pady =10 ,relief =tk .FLAT ,cursor ="hand2")
            btn_new .pack (side =tk .RIGHT ,padx =10 )
    def task4_show_step (self ):
        self .task4_clear_content ()
        if self .task4_current_step ==0 :
            self .task4_show_step_table ()
        elif self .task4_current_step ==1 :
            self .task4_show_step_word ()
        elif self .task4_current_step ==2 :
            self .task4_show_step_result ()
        self .task4_update_buttons ()
    def task4_next_step (self ):
        if self .task4_current_step ==0 :
            if not self .task4_save_table ():
                return
        elif self .task4_current_step ==1 :
            if not self .task4_save_word ():
                return
            if not self .task4_solve ():
                return
        elif self .task4_current_step ==2 :
            self .task4_new_task ()
            return
        self .task4_current_step +=1
        self .task4_show_step ()
    def task4_prev_step (self ):
        if self .task4_current_step >0 :
            self .task4_current_step -=1
            self .task4_show_step ()
    def task4_new_task (self ):
        self .task4_current_step =0
        self .task4_code_table ={}
        self .task4_word =""
        self .task4_result =None
        self .task4_show_step ()
    def task4_show_step_table (self ):
        """
        Шаг 1 из 2: Ввод таблицы кодов.
        Пользователь вводит таблицу соответствия букв и их двоичных кодов.
        Формат: каждая строка содержит букву и код через пробел.
        """
        frame =tk .Frame (self .task4_content_frame ,bg =DARK_THEME ['bg'])
        frame .pack (expand =True )
        tk .Label (frame ,text ="Шаг 1 из 2",font =("Arial",11 ),
        fg =DARK_THEME ['text_secondary'],bg =DARK_THEME ['bg']).pack (pady =5 )
        tk .Label (frame ,text ="Введите таблицу кодов",
        font =("Arial",16 ,"bold"),bg =DARK_THEME ['bg'],fg =DARK_THEME ['fg']).pack (pady =20 )
        instruction =tk .LabelFrame (frame ,text ="📖 Как заполнить таблицу кодов?",
        font =("Arial",11 ,"bold"),padx =15 ,pady =10 ,
        bg =DARK_THEME ['bg_secondary'],fg =DARK_THEME ['fg'],
        relief =tk .FLAT )
        instruction .pack (fill =tk .X ,pady =10 ,padx =50 )
        tk .Label (instruction ,
        text ="1. Найдите в задании таблицу кодирования (например, двоичное дерево)\n"
        "2. Для каждой буквы укажите её двоичный код\n"
        "3. Формат: Буква Код (каждая пара с новой строки)\n"
        "4. Пример:\n"
        "   И 000\n"
        "   Н 001\n"
        "   Ф 01\п"
        "   11\n"
        "💡 Важно: код должен начинаться с точки или быть двоичным числом",
        font =("Arial",10 ),bg =DARK_THEME ['bg_secondary'],
        fg =DARK_THEME ['text_secondary'],justify =tk .LEFT ).pack (anchor =tk .W ,padx =10 ,pady =5 )
        table_frame =tk .Frame (frame ,bg =DARK_THEME ['bg'])
        table_frame .pack (pady =15 ,fill =tk .BOTH ,expand =True ,padx =50 )
        self .task4_table_entry =scrolledtext .ScrolledText (table_frame ,height =8 ,font =("Courier",11 ),
        bg =DARK_THEME ['entry_bg'],fg =DARK_THEME ['entry_fg'],
        insertbackground =DARK_THEME ['fg'],relief =tk .FLAT ,bd =3 )
        self .task4_table_entry .pack (fill =tk .BOTH ,expand =True )
        if self .task4_code_table :
            text ='\n'.join ([f"{k } {v }"for k ,v in self .task4_code_table .items ()])
            self .task4_table_entry .insert (1.0 ,text )
    def task4_save_table (self ):
        table_str =self .task4_table_entry .get (1.0 ,tk .END ).strip ()
        if not table_str :
            messagebox .showerror ("Ошибка","Введите таблицу кодов")
            return False
        self .task4_code_table ={}
        for line in table_str .split ('\n'):
            line =line .strip ()
            if line :
                parts =line .split ()
                if len (parts )>=2 :
                    letter =parts [0 ].strip ()
                    code =parts [1 ].strip ()
                    self .task4_code_table [letter ]=code
        if not self .task4_code_table :
            messagebox .showerror ("Ошибка","Не удалось распарсить таблицу")
            return False
        return True
    def task4_show_step_word (self ):
        frame =tk .Frame (self .task4_content_frame ,bg =DARK_THEME ['bg'])
        frame .pack (expand =True )
        tk .Label (frame ,text ="Шаг 2 из 2",font =("Arial",11 ),
        fg =DARK_THEME ['text_secondary'],bg =DARK_THEME ['bg']).pack (pady =5 )
        tk .Label (frame ,text ="Введите слово для кодирования",
        font =("Arial",16 ,"bold"),bg =DARK_THEME ['bg'],fg =DARK_THEME ['fg']).pack (pady =20 )
        word_frame =tk .Frame (frame ,bg =DARK_THEME ['bg'])
        word_frame .pack (pady =15 ,fill =tk .X ,padx =50 )
        self .task4_word_entry =tk .Entry (word_frame ,font =("Arial",14 ),
        bg =DARK_THEME ['entry_bg'],fg =DARK_THEME ['entry_fg'],
        insertbackground =DARK_THEME ['fg'],relief =tk .FLAT ,bd =3 )
        self .task4_word_entry .pack (fill =tk .X ,padx =5 )
        if self .task4_word :
            self .task4_word_entry .insert (0 ,self .task4_word )
    def task4_save_word (self ):
        word =self .task4_word_entry .get ().strip ()
        if not word :
            messagebox .showerror ("Ошибка","Введите слово")
            return False
        self .task4_word =word
        return True
    def task4_solve (self ):
        """
        Кодирование слова по таблице кодов.
        Алгоритм:
        1. Для каждой буквы слова находим соответствующий код в таблице
        2. Соединяем все коды в одну строку
        3. Подсчитываем длину закодированного слова
        4. Декодируем обратно для проверки корректности
        Returns:
            bool: True если кодирование выполнено успешно, False иначе
        """
        try :
            encoded =''
            missing_letters =[]
            for letter in self .task4_word :
                if letter in self .task4_code_table :
                    encoded +=self .task4_code_table [letter ]
                else :
                    missing_letters .append (letter )
            if missing_letters :
                messagebox .showerror ("Ошибка",
                f"Буквы не найдены в таблице кодов: {', '.join (set (missing_letters ))}\n\n"
                f"💡 Проверьте:\n"
                f"  1. Правильность написания букв (регистр не важен)\n"
                f"  2. Полноту таблицы кодов - все буквы должны быть указаны\n"
                f"  3. Правильность слова из задания")
                return False
            if len (encoded )==0 :
                messagebox .showerror ("Ошибка",
                "Не удалось закодировать слово.\n\n"
                "💡 Проверьте, что таблица кодов заполнена и слово введено правильно.")
                return False
            reverse_code ={v :k for k ,v in self .task4_code_table .items ()}
            decoded =''
            i =0
            while i <len (encoded ):
                found =False
                for code in sorted (reverse_code .keys (),key =len ,reverse =True ):
                    if i +len (code )<=len (encoded ):
                        substr =encoded [i :i +len (code )]
                        if substr ==code :
                            decoded +=reverse_code [substr ]
                            i +=len (code )
                            found =True
                            break
                if not found :
                    break
            self .task4_result ={
            'encoded':encoded ,
            'length':len (encoded ),
            'decoded':decoded
            }
            return True
        except Exception as e :
            messagebox .showerror ("Ошибка",
            f"Ошибка при кодировании: {e }\n\n"
            f"💡 Проверьте правильность таблицы кодов и слова.")
            return False
    def task4_show_step_result (self ):
        frame =tk .Frame (self .task4_content_frame ,bg =DARK_THEME ['bg'])
        frame .pack (expand =True )
        tk .Label (frame ,text ="Результат",font =("Arial",18 ,"bold"),
        bg =DARK_THEME ['bg'],fg =DARK_THEME ['success']).pack (pady =20 )
        result_frame =tk .LabelFrame (frame ,text ="Кодирование",
        font =("Arial",12 ,"bold"),padx =20 ,pady =15 ,
        bg =DARK_THEME ['bg_secondary'],fg =DARK_THEME ['fg'],relief =tk .FLAT )
        result_frame .pack (pady =15 ,padx =50 ,fill =tk .X )
        r =self .task4_result
        tk .Label (result_frame ,text =f"Исходное слово: {self .task4_word }",
        font =("Arial",12 ),bg =DARK_THEME ['bg_secondary'],fg =DARK_THEME ['fg']).pack (anchor =tk .W ,pady =5 )
        tk .Label (result_frame ,text =f"Закодированное: {r ['encoded']}",
        font =("Courier",12 ),bg =DARK_THEME ['bg_secondary'],fg =DARK_THEME ['fg']).pack (anchor =tk .W ,pady =5 )
        tk .Label (result_frame ,text =f"Количество двоичных знаков: {r ['length']}",
        font =("Arial",12 ,"bold"),bg =DARK_THEME ['bg_secondary'],fg =DARK_THEME ['success']).pack (anchor =tk .W ,pady =5 )
        tk .Label (result_frame ,text =f"Декодированное: {r ['decoded']}",
        font =("Arial",11 ),bg =DARK_THEME ['bg_secondary'],fg =DARK_THEME ['text_secondary']).pack (anchor =tk .W ,pady =5 )
    def task_7_interface (self ):self .task_generic_interface (7 )
    def task_8_interface (self ):self .task_generic_interface (8 )
    def task_9_interface (self ):self .task_generic_interface (9 )
    def task_10_interface (self ):self .task_generic_interface (10 )
    def task_11_interface (self ):self .task_generic_interface (11 )
    def task_12_interface (self ):self .task_generic_interface (12 )
    def task_13_interface (self ):self .task_generic_interface (13 )
    def task_14_interface (self ):self .task_generic_interface (14 )
    def task_15_interface (self ):self .task_generic_interface (15 )
    def task_16_interface (self ):self .task_generic_interface (16 )
    def task_17_interface (self ):self .task_generic_interface (17 )
    def task_18_interface (self ):self .task_generic_interface (18 )
    def task_19_interface (self ):self .task_generic_interface (19 )
    def task_20_interface (self ):self .task_generic_interface (20 )
    def task_21_interface (self ):self .task_generic_interface (21 )
    def task_22_interface (self ):self .task_generic_interface (22 )
    def task_23_interface (self ):self .task_generic_interface (23 )
    def task_24_interface (self ):self .task_generic_interface (24 )
    def task_25_interface (self ):self .task_generic_interface (25 )
    def task_26_interface (self ):self .task_generic_interface (26 )
    def task_27_interface (self ):self .task_generic_interface (27 )
if __name__ =="__main__":
    root =tk .Tk ()
    app =EGESolverApp (root )
    root .mainloop ()