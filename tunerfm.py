import pylast
from colorama import Fore, Style, init
import time
import os
import json
import threading
import traceback

init(autoreset=True)

# Arquivos de configuração
CONFIG_FILE = 'config.json'
USER_CONFIG_FILE = 'user_config.json'

# Configurações padrão
DEFAULT_CONFIG = {
    'language': 'pt',
    'current_ascii_art': 'default',
    'primary_color': 'lightmagenta_ex',
    'secondary_color': 'magenta',
    'custom_ascii_art': ""
}

# Carregar configurações do usuário
def load_user_config():
    if os.path.exists(USER_CONFIG_FILE):
        try:
            with open(USER_CONFIG_FILE, 'r') as f:
                return json.load(f)
        except:
            return DEFAULT_CONFIG
    return DEFAULT_CONFIG

# Salvar configurações do usuário
def save_user_config(config):
    with open(USER_CONFIG_FILE, 'w') as f:
        json.dump(config, f)

# Carregar configurações iniciais
user_config = load_user_config()

# Variáveis globais com configurações do usuário
LANGUAGE = user_config.get('language', 'pt')
CURRENT_ASCII_ART = user_config.get('current_ascii_art', 'default')
PRIMARY_COLOR_NAME = user_config.get('primary_color', 'lightmagenta_ex')
SECONDARY_COLOR_NAME = user_config.get('secondary_color', 'magenta')

# Mapa de cores
COLOR_MAP = {
    'black': Fore.BLACK,
    'red': Fore.RED,
    'green': Fore.GREEN,
    'yellow': Fore.YELLOW,
    'blue': Fore.BLUE,
    'magenta': Fore.MAGENTA,
    'cyan': Fore.CYAN,
    'white': Fore.WHITE,
    'lightblack_ex': Fore.LIGHTBLACK_EX,
    'lightred_ex': Fore.LIGHTRED_EX,
    'lightgreen_ex': Fore.LIGHTGREEN_EX,
    'lightyellow_ex': Fore.LIGHTYELLOW_EX,
    'lightblue_ex': Fore.LIGHTBLUE_EX,
    'lightmagenta_ex': Fore.LIGHTMAGENTA_EX,
    'lightcyan_ex': Fore.LIGHTCYAN_EX,
    'lightwhite_ex': Fore.LIGHTWHITE_EX,
}

# Aplicar cores configuradas
PRIMARY_COLOR = COLOR_MAP.get(PRIMARY_COLOR_NAME, Fore.LIGHTMAGENTA_EX)
SECONDARY_COLOR = COLOR_MAP.get(SECONDARY_COLOR_NAME, Fore.MAGENTA)

# Arte ASCII
ASCII_ARTS = {
    'default': """⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡴⠲⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⣷⡄⠈⢢⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣄⠀⠀⠀⠀⠀⠀⢀⣾⡀⠀⠀⠀⠀⠹⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⡓⠦⢄⣀⠀⠀⡼⠻⠿⢶⡄⠀⠀⠀⠘⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢀⡤⠤⠤⣤⣤⣴⣶⣶⠶⠶⠶⠒⠒⠂⠙⠀⠀⠀⠉⠉⠓⠲⢤⣀⠀⠀⠀⠀⠀⢹⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢸⠀⠀⠀⠈⢿⠈⠳⣤⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠢⣄⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠈⡇⠀⠀⠀⠀⠀⢀⣿⡋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣟⠁⠀⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠸⡀⠀⠀⠀⠀⢈⡽⠁⠀⠀⠠⡄⠀⠀⠀⠀⠀⠀⠀⣄⠀⠀⠀⠀⠀⠀⠘⡆⠀⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠱⡀⠀⠀⣠⠞⠀⠀⠀⠀⣠⢧⠀⠀⠀⠀⠀⠀⠀⠘⣆⠀⠀⠀⠀⠀⠀⢹⠀⣸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢆⡴⠃⠀⠀⠀⢠⠞⠁⠈⢣⡀⣄⠀⠀⠀⠀⠀⠘⣆⠀⠀⠀⠀⠀⢸⣠⡇⠀⠀⠀⠀⠀⠀⠀⢀⡀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⢞⣓⣸⠀⢠⠰⣋⣀⣀⣳⢤⡙⢾⣟⠲⢤⣀⣠⠄⢯⠳⡀⠀⠀⠀⠸⠋⡇⠀⠀⠀⠀⠀⠀⢠⠏⠹⡄⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠉⣿⠀⢸⢰⠋⠀⣸⣿⣿⡆⠀⠈⠃⢤⣯⣿⡶⠾⣄⠘⡦⠀⠀⢀⣦⣿⠀⠀⠀⠀⠀⢠⠃⠀⠀⢳⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡄⢸⣼⣀⡀⠣⠽⠿⢃⠀⠀⠀⢾⣻⣿⡿⠀⣸⡸⠁⠀⢀⡼⡼⠉⠳⣄⠀⠀⣰⠁⠀⠀⠀⠀⢸⠇
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠟⣷⡘⣿⣛⡁⠀⠀⠀⠀⠁⠀⠀⠀⠉⠍⠡⣶⡿⠁⠀⣠⠟⣇⡇⠀⠀⠈⢦⣰⠁⠀⠀⠀⠀⢸⠂
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⠖⢻⣣⣈⣿⣤⠤⢒⠒⠦⠖⠢⠴⢄⣀⢬⣷⠞⢁⣠⠞⣡⠞⢹⡟⠀⠀⠀⠀⠃⠀⠀⠀⠀⢀⡞⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢏⣻⡶⠞⠉⠛⢉⣆⣴⡞⠻⠦⣾⢿⣊⣉⡴⣶⠁⠀⠀⠑⢄⡀⢀⢰⠋⢦⠀⠀⣠⠞⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢨⣿⣤⣶⣦⠀⠀⡇⠀⠀⣤⣄⠹⡟⠛⢷⠀⠁⠀⠀⠀⠀⠀⠙⠺⣏⣀⠈⢷⠚⠁⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⢿⣿⣿⣝⢿⡇⠀⣧⢠⣾⣿⣿⣿⡿⡄⢸⡄⠀⠀⠀⠀⠀⠀⠀⢸⠏⠉⠁⠈⡆⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡟⠀⠀⠀⠙⠃⠀⢸⣿⠈⠱⠟⠛⠛⠃⢹⢸⣿⡄⠀⠀⠀⣤⡀⢀⡿⠛⠛⠂⢀⢱⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣸⡀⠀⠀⠀⠀⠀⣠⢟⣸⠦⣄⣀⠀⠀⠀⠘⣸⠹⣟⡆⠀⡼⠁⠙⣾⣷⣦⣄⠀⠀⢸⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠞⠉⠀⠘⡇⠀⣀⣀⡠⠞⣱⠋⠀⠀⠀⠈⠙⢦⡀⠀⢹⡚⠉⠀⢰⠃⠀⠀⠘⣆⠀⠉⠀⠀⢸⡇⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢀⣜⠁⠀⠀⠀⠀⠙⠉⢹⣿⠁⢰⠃⠀⠀⠀⠀⠀⠀⠀⠑⣦⣬⠇⠀⢀⡏⠀⠀⠀⠀⠉⠀⠀⠀⢀⢸⡇⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⡠⠟⠛⠛⠷⠂⠀⠀⠀⠀⠈⣿⢠⡇⣠⣤⣤⣤⣀⠀⠀⠀⠀⠘⣿⣶⣶⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀⡞⢸⠃⠀⠀⠀
⠀⠀⠀⠀⠀⢀⣾⣷⣤⣤⠀⠀⠀⠀⠀⠀⠀⠀⠛⡼⢉⢉⣉⣉⠛⠻⢷⣄⠀⠀⠀⣸⣯⠙⢿⣧⠀⠀⠀⠀⠀⠀⢀⡼⠁⡼⠀⠀⠀⠀
⠀⠀⠀⠀⡰⠋⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡤⠀⡗⠛⠛⠻⠿⣷⣦⣀⠀⠀⠀⠀⠘⢻⠀⠀⠙⠃⠀⠀⠀⠀⡠⠊⠀⢠⠃⠀⠀⠀⠀
⠀⣠⣖⣟⣳⣒⣆⠀⠀⠀⠀⠀⠀⠀⠀⣠⣎⠀⢸⠁⠀⠀⠀⠀⠀⠉⠉⠀⢸⠀⠀⠀⣏⠀⠀⠀⠀⠀⠠⠒⠋⠀⠀⢠⠏⠀⠀⠀⠀⠀
⠰⣿⣿⣶⠿⠷⣾⠃⠀⠀⠀⠀⢀⡠⠚⠁⠈⠦⡞⠀⠀⠀⠀⠀⠀⠀⠀⢠⠏⠀⠀⡼⠉⠁⠀⠀⠀⠀⠀⠀⠀⣠⠔⠋⠀⠀⠀⠀⠀⠀
⠀⠹⣦⣓⡒⠋⠉⠀⠀⠀⣀⡴⠋⠀⠀⠀⠀⡼⠁⡀⠀⠀⠀⠀⠀⠀⣠⠏⢀⣠⢾⣁⣀⣀⣀⣀⣠⠤⠒⠚⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠉⠉⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠹⣦⣿⣯⣿⣷⣦⢀⡴⠋⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠉⠉⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
""",
    'communism': """⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⠏⠹⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⢶⣶⣶⣶⣶⣶⣾⠏⠀⠀⠹⣷⣶⣶⣶⣶⡶⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣦⣄⠀⠀⠀⠀⠀⠀⠀⣠⣴⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢙⣷⠀⠀⠀⠀⠀⢾⣏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⠀⠀⠀⠀⠀⠀⣼⣃⣠⣴⣶⣄⣀⢹⣧⠀⠀⠀⠀⠀⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢀⣠⣶⠟⠁⠀⠀⠀⠀⢠⣿⠟⠋⠀⠀⠀⠀⠙⢿⣿⡄⠀⠀⠀⠀⠹⣿⣷⣤⠀⠀⠀⠀⠀⠀
⠀⠀⠀⢀⣼⢻⡿⣫⠀⠀⠀⠀⠀⠀⠋⠀⠀⠀⠀⠀⡀⠀⠀⠀⠀⠙⠆⠀⠀⠀⠀⠀⢿⣿⣧⣷⣄⡀⠀⠀
⠀⠀⣰⢹⣟⣽⡾⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠳⣦⣄⡀⠀⠀⠀⠀⠀⠀⠀⠈⢻⣿⣽⡏⢳⡀⠀
⠀⢀⣿⢸⡿⣫⠆⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣀⣀⠀⠀⠀⠙⢿⣦⡄⠀⠀⠀⠀⠀⠀⠈⣯⡿⣇⢸⡇⠀
⠀⡜⣿⢸⣿⠏⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⣿⡿⠋⠀⠀⠀⠀⠈⢻⣿⣦⠀⠀⠀⠀⠀⠀⠘⣿⣮⢸⡟⡄
⢰⡇⢿⣿⢻⠆⠀⠀⠀⠀⠀⠀⠀⢴⣿⣿⡿⣿⣦⡀⠀⠀⠀⠀⠀⠀⢻⣿⣧⠀⠀⠀⠀⠀⠀⣯⢻⣿⢡⡇
⠘⣿⡘⢣⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⡋⠀⠈⠻⣿⣧⡀⠀⠀⠀⠀⢸⣿⣿⡄⠀⠀⠀⠀⠀⢹⣧⠛⣾⡇
⢿⣷⣼⡏⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣿⣦⡀⠀⠀⣸⣿⣿⠇⠀⠀⠀⠀⠀⡞⣿⣾⡿⢱
⠘⣧⡻⣿⢰⣧⠀⠀⠀⠀⠀⠀⠀⠀⣠⣄⡂⠀⠀⠀⠀⠈⠻⣿⣦⣠⣿⣿⡿⠀⠀⠀⠀⠀⢰⣇⢸⠟⣰⡏
⠀⠹⣷⣌⢸⣿⢠⡀⠀⠀⠀⠀⢀⣼⡿⠙⠿⣿⣶⣦⣤⣤⣤⣼⣿⣿⣿⡟⠁⠀⠀⠀⠀⣰⢺⡿⣨⣾⠟⠀
⠀⠀⢯⠻⣿⣿⡈⣷⡀⠀⢠⣾⣿⠋⠀⠀⠀⠀⠉⠛⠻⠿⠿⠿⠛⢿⣿⣦⡄⠀⠀⣸⡇⣼⣿⠟⣩⠂⠀
⠀⠀⠈⢿⣦⣙⡷⢻⣷⢦⡈⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠋⠀⣠⢶⣿⢑⣋⣴⡾⠋⠀⠀
⠀⠀⠀⠀⠉⡿⢿⣾⣿⣯⢿⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⢣⣿⣿⡿⢟⡏⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠈⠳⣶⣬⣭⣥⣽⣿⣦⡤⠄⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⡤⣴⣾⣿⣥⣭⣤⣶⠾⠋⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠻⣭⣉⣉⣡⣴⣾⡿⠟⣩⡶⠋⠉⠳⣮⣙⠿⣿⣶⣤⣭⣭⣭⠿⠃⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠉⠉⠉⢴⠟⠁⠀⠀⠀⠀⠀⠙⣷⠄⠉⠉⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
""",
    'the_eye': """⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡜⢣⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠎⡴⢦⠱⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⢎⣜⣉⣉⣧⡱⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⢃⡞⠒⣒⣒⠒⢳⡘⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⢡⣎⡩⠭⠤⠤⠭⢍⣱⡜⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡴⢡⡯⠴⢒⣈⣩⣉⣑⡒⠠⣹⡌⢦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡔⣡⣣⠔⡺⡋⡁⢀⡀⢈⠙⢟⠢⣝⣄⢢⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡜⣰⡟⠁⢰⡓⢎⣀⣸⣿⣷⡱⢚⡆⠈⢻⣆⢣⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠎⡼⣇⠣⡀⠸⡄⢊⢿⣿⣿⡿⡑⢠⠇⢀⠜⣸⢧⠱⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢠⢋⢼⡙⢌⠳⣍⠲⢽⣄⣁⠂⠐⣈⣠⡯⠔⣡⠞⡡⢊⣧⡙⡄⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣠⢃⣞⠣⡙⠦⡑⠦⣍⡒⠤⠬⠭⠭⠥⠤⢒⣩⠴⢊⠴⢋⠜⣳⡘⣄⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣰⣃⣛⣚⣓⣚⣓⣚⣓⣒⣛⣛⣓⣒⣒⣚⣛⣛⣒⣚⣓⣚⣓⣚⣒⣛⣘⣆⠀⠀
""",
    'afx': """⠀⠀⠀⠀⢀⣤⣴⠶⠶⠷⠶⠶⣦⣤⡀⠀⠀⠀⠀
⠀⠀⢠⡶⠟⠉⠀⠀⠀⠀⠀⠀⠀⠉⠻⢶⡄⠀⠀
⠀⣴⡟⣥⣤⣤⣤⣤⣤⣤⣤⣤⡀⠀⠀⠈⢻⣦⠀
⢰⡟⠀⠻⠿⠿⠟⠁⣼⣿⣿⣿⣷⡀⠀⠀⠀⢻⡆
⣿⠃⠀⠀⠀⠀⠀⣼⣿⡏⠙⣿⣿⣇⠀⠀⠀⠘⣿
⣿⡄⠀⠀⠀⠀⣴⣿⠟⠃⠀⠙⣿⣿⡆⠀⠀⢠⣿
⠹⣧⠀⠀⠀⢸⡟⠁⠀⠀⠀⠀⠘⢿⣷⡀⠀⣼⠏
⠀⠻⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⠃⣴⠟⠀
⠀⠀⠙⢷⣤⣀⠀⠀⠀⠀⠀⠀⠀⣀⣤⡾⠋⠀⠀
⠀⠀⠀⠀⠈⠛⠻⠶⠶⠶⠶⠶⠟⠛⠁⠀⠀⠀⠀
""",
    'andro': """⠀⠀⠀⠀⢀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠙⢷⣤⣤⣴⣶⣶⣦⣤⣤⡾⠋⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⠀⠀⠀⠀⠀
⠀⠀⠀⠀⣼⣿⣿⣉⣹⣿⣿⣿⣿⣏⣉⣿⣿⣧⠀⠀⠀⠀
⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀
⣠⣄⠀⢠⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⡄⠀⣠⣄
⣿⣿⡇⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⢸⣿⣿
⣿⣿⡇⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⢸⣿⣿
⣿⣿⡇⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⢸⣿⣿
⣿⣿⡇⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⢸⣿⣿
⠻⠟⠁⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠈⠻⠟
⠀⠀⠀⠀⠉⠉⣿⣿⣿⡏⠉⠉⢹⣿⣿⣿⠉⠉⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣿⣿⣿⡇⠀⠀⢸⣿⣿⣿⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣿⣿⣿⡇⠀⠀⢸⣿⣿⣿⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠈⠉⠉⠀⠀⠀⠀⠉⠉⠁⠀⠀⠀⠀⠀⠀
"""
}

# Adicionar arte personalizada se existir
if 'custom_ascii_art' in user_config and user_config['custom_ascii_art']:
    ASCII_ARTS['custom'] = user_config['custom_ascii_art']

class ColorConfig:
    def __init__(self):
        self.primary = PRIMARY_COLOR
        self.secondary = SECONDARY_COLOR

    def set_colors(self, primary, secondary):  
        self.primary = primary  
        self.secondary = secondary  

    def print_primary(self, text):  
        print(self.primary + text + Style.RESET_ALL)  

    def print_secondary(self, text):  
        print(self.secondary + text + Style.RESET_ALL)

color_manager = ColorConfig()

def save_credentials(api_key, api_secret, username, password_hash):
    credentials = {
        'api_key': api_key,
        'api_secret': api_secret,
        'username': username,
        'password_hash': password_hash
    }
    with open(CONFIG_FILE, 'w') as f:
        json.dump(credentials, f)
    color_manager.print_primary("Credenciais salvas com sucesso!")

def load_credentials():
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, 'r') as f:
            return json.load(f)
    return None

class LastfmScrobbler:
    def __init__(self):
        self.network = None

    def authenticate(self):  
        color_manager.print_primary("\n--- Autenticação Last.fm ---")  
        credentials = load_credentials()  

        if credentials:  
            color_manager.print_secondary("Tentando autenticar com credenciais salvas...")  
            try:  
                self.network = pylast.LastFMNetwork(  
                    api_key=credentials['api_key'],  
                    api_secret=credentials['api_secret'],  
                    username=credentials['username'],  
                    password_hash=credentials['password_hash']  
                )  
                self.network.get_authenticated_user()  
                color_manager.print_primary("Autenticação bem-sucedida com credenciais salvas!")  
                return True  
            except pylast.PyLastError as e:  
                color_manager.print_secondary(f"Erro de autenticação com credenciais salvas: {e}")  
                color_manager.print_secondary("Por favor, insira suas credenciais novamente.")  
            except Exception as e:  
                color_manager.print_secondary(f"Ocorreu um erro inesperado ao carregar credenciais: {e}")  
                color_manager.print_secondary("Por favor, insira suas credenciais novamente.")  

        api_key = input(f"{color_manager.secondary}Digite sua API Key: {Style.RESET_ALL}").strip()  
        api_secret = input(f"{color_manager.secondary}Digite seu API Secret: {Style.RESET_ALL}").strip()  
        username = input(f"{color_manager.secondary}Digite seu nome de usuário Last.fm: {Style.RESET_ALL}").strip()  
        password_hash = input(f"{color_manager.secondary}Digite seu password hash Last.fm: {Style.RESET_ALL}").strip()  

        try:  
            self.network = pylast.LastFMNetwork(  
                api_key=api_key,  
                api_secret=api_secret,  
                username=username,  
                password_hash=password_hash  
            )  
            self.network.get_authenticated_user()  
            color_manager.print_primary("Autenticação bem-sucedida!")  
            save_credentials(api_key, api_secret, username, password_hash)  
            return True  
        except pylast.PyLastError as e:  
            color_manager.print_secondary(f"Erro de autenticação: {e}")  
            return False  
        except Exception as e:  
            color_manager.print_secondary(f"Ocorreu um erro inesperado durante a autenticação: {e}")  
            return False  

    def get_album_tracks(self, artist_name, album_name):  
        try:  
            album = self.network.get_album(artist_name, album_name)  
            return album.get_tracks()  
        except pylast.PyLastError as e:  
            color_manager.print_secondary(f"Erro ao buscar faixas do álbum: {e}")  
            return []  
        except Exception as e:  
            color_manager.print_secondary(f"Ocorreu um erro inesperado ao buscar faixas do álbum: {e}")  
            return []  

    def get_artist_albums(self, artist_name):  
        try:  
            time.sleep(0.3)  # Delay pra evitar rate limiting
            artist = self.network.get_artist(artist_name)  
            return artist.get_top_albums(limit=None)  
        except pylast.PyLastError as e:  
            color_manager.print_secondary(f"Erro ao buscar álbuns do artista: {e}")  
            return []  
        except Exception as e:  
            color_manager.print_secondary(f"Ocorreu um erro inesperado ao buscar álbuns do artista: {e}")  
            return []  

    def scrobble_track(self, artist, title, timestamp):  
        try:  
            self.network.scrobble(artist=artist, title=title, timestamp=timestamp)  
            color_manager.print_primary(f"Scrobbled: {title} de {artist} em {time.ctime(timestamp)}")  
            return True  
        except pylast.PyLastError as e:  
            color_manager.print_secondary(f"Erro ao scrobble: {e}")  
            return False  
        except Exception as e:  
            color_manager.print_secondary(f"Ocorreu um erro inesperado ao scrobble: {e}")  
            return False

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def configure_ascii_art():
    global CURRENT_ASCII_ART, user_config
    clear_screen()
    color_manager.print_primary("\n--- Configurações de ASCII Art ---")
    color_manager.print_secondary("ASCII Arts disponíveis:")
    for art_name in ASCII_ARTS.keys():
        print(f"- {art_name}")

    while True:  
        choice = input(f"{color_manager.secondary}Escolha uma ASCII Art (digite o nome): {Style.RESET_ALL}").strip().lower()  
        if choice in ASCII_ARTS:  
            CURRENT_ASCII_ART = choice
            user_config['current_ascii_art'] = choice
            save_user_config(user_config)
            color_manager.print_primary(f"ASCII Art atualizada para: {choice}!")  
            break  
        else:  
            color_manager.print_secondary("Nome de ASCII Art inválido. Tente novamente.")  
    time.sleep(2)

def settings_menu():
    while True:
        clear_screen()
        color_manager.print_primary("\n--- Menu de Configurações ---")
        color_manager.print_secondary("1. Alterar Idioma (PT/EN)")
        color_manager.print_secondary("2. Configurar Arte ASCII Personalizada")
        color_manager.print_secondary("3. Ver Credenciais Last.fm")
        color_manager.print_secondary("4. Configurações de Cores")
        color_manager.print_secondary("5. Voltar")

        choice = input(f"{color_manager.primary}Escolha uma opção: {Style.RESET_ALL}").strip()

        if choice == '1':
            change_language()
        elif choice == '2':
            configure_custom_ascii()
        elif choice == '3':
            view_credentials()
        elif choice == '4':
            configure_colors()
        elif choice == '5':
            return
        else:
            color_manager.print_secondary("Opção inválida. Tente novamente.")
            time.sleep(1)

def change_language():
    global LANGUAGE, user_config
    clear_screen()
    color_manager.print_primary("\n--- Alterar Idioma ---")
    color_manager.print_secondary("1. Português (PT)")
    color_manager.print_secondary("2. English (EN)")
    
    lang_choice = input(f"{color_manager.primary}Escolha o idioma: {Style.RESET_ALL}").strip()
    
    if lang_choice == '1':
        LANGUAGE = 'pt'
        user_config['language'] = 'pt'
        save_user_config(user_config)
        color_manager.print_primary("\nIdioma alterado para Português!")
    elif lang_choice == '2':
        LANGUAGE = 'en'
        user_config['language'] = 'en'
        save_user_config(user_config)
        color_manager.print_primary("\nLanguage changed to English!")
    else:
        color_manager.print_secondary("Opção inválida. Idioma não alterado.")
    
    time.sleep(2)

def configure_custom_ascii():
    global ASCII_ARTS, user_config
    clear_screen()
    color_manager.print_primary("\n--- Arte ASCII Personalizada ---")
    color_manager.print_secondary("1. Colar nova arte ASCII")
    color_manager.print_secondary("2. Voltar")
    
    choice = input(f"{color_manager.primary}Escolha uma opção: {Style.RESET_ALL}").strip()
    
    if choice == '1':
        clear_screen()
        color_manager.print_primary("\nCole sua arte ASCII abaixo (Ctrl+D ou Ctrl+Z para finalizar):")
        color_manager.print_secondary("Dica: Cole uma arte com no máximo 40 linhas e 100 caracteres por linha")
        
        lines = []
        try:
            while True:
                line = input()
                if len(line) > 100:
                    color_manager.print_secondary("Linha muito longa! Máximo 100 caracteres.")
                    return
                lines.append(line)
                
                if len(lines) > 40:
                    color_manager.print_secondary("Máximo de linhas excedido! (40 linhas)")
                    return
        except EOFError:
            pass
        
        if lines:
            custom_art = "\n".join(lines)
            ASCII_ARTS['custom'] = custom_art
            global CURRENT_ASCII_ART
            CURRENT_ASCII_ART = 'custom'
            user_config['current_ascii_art'] = 'custom'
            user_config['custom_ascii_art'] = custom_art
            save_user_config(user_config)
            color_manager.print_primary("\nArte ASCII personalizada salva e ativada!")
        else:
            color_manager.print_secondary("Nenhuma arte fornecida.")
        
        time.sleep(2)
    elif choice != '2':
        color_manager.print_secondary("Opção inválida.")

def view_credentials():
    credentials = load_credentials()
    if not credentials:
        color_manager.print_secondary("Nenhuma credencial salva encontrada.")
        time.sleep(2)
        return
    
    clear_screen()
    color_manager.print_primary("\n--- Credenciais Last.fm ---")
    color_manager.print_secondary("Pressione ENTER para revelar as credenciais (manter pressionado para ver)")
    color_manager.print_secondary("Solta a tecla para ocultar automaticamente")
    
    # Aguardar confirmacao do usuário
    input()
    
    # Mostrar credenciais enquanto ENTER estiver pressionado
    color_manager.print_primary("\nCredenciais Reveladas:")
    color_manager.print_secondary(f"API Key: {credentials['api_key']}")
    color_manager.print_secondary(f"API Secret: {credentials['api_secret']}")
    color_manager.print_secondary(f"Usuário: {credentials['username']}")
    color_manager.print_secondary(f"Password Hash: {credentials['password_hash']}")
    color_manager.print_primary("\nSolta ENTER para ocultar...")
    
    # Aguardar ate que o usuário solte a tecla
    input()
    
    # replace com espaços em branco para "ocultar" nao sei programar isso
    print("\n" * 10)
    color_manager.print_primary("Credenciais ocultadas com segurança!")

def scrobble_loop(scrobbler, tracks, interval, stop_event=None):
    if not tracks:
        color_manager.print_secondary("Nenhuma faixa encontrada para scrobble.")
        time.sleep(2)
        return

    if interval < 0:  
        interval = 0  

    if stop_event is None:
        stop_event = threading.Event()

    color_manager.print_primary(f"Iniciando scrobbling de {len(tracks)} faixas com intervalo de {interval} segundos...")  
    color_manager.print_secondary("Pressione ENTER a qualquer momento para parar.")  
      
    def wait_for_enter():  
        input()  
        stop_event.set()  
        color_manager.print_primary("\nInterrupção solicitada. Finalizando operação...")
      
    input_thread = threading.Thread(target=wait_for_enter, daemon=True)  
    input_thread.start()  
      
    try:  
        while not stop_event.is_set():  
            for track in tracks:  
                if stop_event.is_set():  
                    break  
                      
                timestamp = int(time.time())  
                scrobbler.scrobble_track(track.artist.name, track.title, timestamp)  
                  
                if interval == 0:  
                    continue  
                  
                start_time = time.time()  
                while (time.time() - start_time) < interval:  
                    if stop_event.is_set():  
                        break  
                    time.sleep(0.1)  
                      
                if stop_event.is_set():  
                    break  
                      
    finally:  
        if stop_event.is_set():  
            color_manager.print_primary("Scrobbling interrompido pelo usuário. Voltando ao menu...")  
            time.sleep(2)

def scrobble_by_album(scrobbler):
    color_manager.print_primary("\n--- Scrobble por Álbum ---")
    artist_name = input(f"{color_manager.secondary}Digite o nome do artista: {Style.RESET_ALL}").strip()
    album_name = input(f"{color_manager.secondary}Digite o nome do álbum: {Style.RESET_ALL}").strip()

    if not artist_name or not album_name:
        color_manager.print_secondary("Artista e álbum são obrigatórios!")
        time.sleep(2)
        return

    try:  
        tracks = scrobbler.get_album_tracks(artist_name, album_name)  
        if not tracks:  
            color_manager.print_secondary("Não foi possível encontrar faixas para este álbum.")  
            time.sleep(2)  
            return  
              
        color_manager.print_primary(f"Encontradas {len(tracks)} faixas para o álbum {album_name} de {artist_name}.")  
        
        try:
            interval = float(input(f"{color_manager.secondary}Intervalo entre scrobbles (segundos, 0 para o mais rápido): {Style.RESET_ALL}").strip())
        except ValueError:
            interval = 0
            color_manager.print_secondary("Valor inválido. Usando intervalo 0.")
            
        scrobble_loop(scrobbler, tracks, interval)  
    except Exception as e:  
        color_manager.print_secondary(f"Erro ao buscar faixas do álbum: {e}")  
        time.sleep(2)

def scrobble_by_artist_discography(scrobbler):
    color_manager.print_primary("\n--- Scrobble por Discografia do Artista ---")
    artist_name = input(f"{color_manager.secondary}Digite o nome do artista: {Style.RESET_ALL}").strip()

    if not artist_name:
        color_manager.print_secondary("Nome do artista é obrigatório!")
        time.sleep(2)
        return

    # Evento e thread específicos para a fase de coleta
    collect_stop_event = threading.Event()
    input_thread = None

    def check_for_enter():
        input()  # Espera Enter
        collect_stop_event.set()
        color_manager.print_primary("\nInterrupção solicitada. Finalizando operação...")

    # Inicia thread para capturar Enter durante a coleta
    input_thread = threading.Thread(target=check_for_enter, daemon=True)
    input_thread.start()

    try:
        albums = scrobbler.get_artist_albums(artist_name)
        if not albums:
            color_manager.print_secondary("Não foi possível encontrar álbuns para este artista.")
            time.sleep(2)
            collect_stop_event.set()
            return

        all_tracks = []
        color_manager.print_primary(f"Encontrados {len(albums)} álbuns para o artista {artist_name}. Coletando faixas...")
        
        for album_obj in albums:
            if collect_stop_event.is_set():
                color_manager.print_primary("Coleta interrompida pelo usuário!")
                return
                
            try:
                album_title = album_obj.item.get_title()
                time.sleep(0.5)  # Delay pra evitar rate limit
                
                album_tracks = scrobbler.get_album_tracks(artist_name, album_title)
                if album_tracks:
                    all_tracks.extend(album_tracks)
                    color_manager.print_secondary(f"  - Adicionadas {len(album_tracks)} faixas do álbum: {album_title}")
                else:
                    color_manager.print_secondary(f"  - Álbum sem faixas: {album_title} (pulando)")
            except pylast.PyLastError as e:
                color_manager.print_secondary(f"  - Erro no álbum: {str(e)} (pulando)")
            except Exception as e:
                color_manager.print_secondary(f"  - Erro inesperado: {str(e)} (pulando)")

        # verificar
        if collect_stop_event.is_set():
            color_manager.print_primary("Operação cancelada pelo usuário!")
            return

        if not all_tracks:
            color_manager.print_secondary("Nenhuma faixa encontrada na discografia do artista.")
            time.sleep(2)
            return

        color_manager.print_primary(f"Total de {len(all_tracks)} faixas encontradas na discografia de {artist_name}.")
        
        # intervalo
        try:
            interval = float(input(f"{color_manager.secondary}Intervalo entre scrobbles (segundos, 0 para o mais rápido): {Style.RESET_ALL}").strip())
        except ValueError:
            interval = 0
            color_manager.print_secondary("Valor inválido. Usando intervalo 0.")
            
        # esqueci oq era
        scrobble_loop(scrobbler, all_tracks, interval)

    except Exception as e:
        color_manager.print_secondary(f"Erro fatal ao processar discografia: {e}")
        traceback.print_exc()
        time.sleep(2)
    finally:
        collect_stop_event.set()

def scrobble_by_track(scrobbler):
    color_manager.print_primary("\n--- Scrobble por Faixa ---")
    artist_name = input(f"{color_manager.secondary}Digite o nome do artista: {Style.RESET_ALL}").strip()
    track_title = input(f"{color_manager.secondary}Digite o título da faixa: {Style.RESET_ALL}").strip()

    if not artist_name or not track_title:
        color_manager.print_secondary("Artista e faixa são obrigatórios!")
        time.sleep(2)
        return

    class DummyTrack:  
        def __init__(self, artist, title):  
            self.artist = type('Artist', (object,), {'name': artist})()  
            self.title = title  

    track = DummyTrack(artist_name, track_title)  
    tracks = [track]  

    try:  
        interval = float(input(f"{color_manager.secondary}Intervalo entre scrobbles (segundos, 0 para o mais rápido): {Style.RESET_ALL}").strip())  
        scrobble_loop(scrobbler, tracks, interval)  
    except ValueError:  
        color_manager.print_secondary("Intervalo inválido. Usando 0.")  
        scrobble_loop(scrobbler, tracks, 0)

def configure_colors():
    global user_config
    clear_screen()  
    color_manager.print_primary("\n--- Configurações de Cores ---")  
    color_manager.print_secondary("Cores disponíveis:")  
    for color_name in COLOR_MAP.keys():  
        print(f"- {COLOR_MAP[color_name]}{color_name}{Style.RESET_ALL}")  

    while True:  
        primary_choice = input(f"{color_manager.secondary}Escolha a cor primária (ex: lightmagenta_ex): {Style.RESET_ALL}").strip().lower()  
        if primary_choice in COLOR_MAP:  
            break  
        else:  
            color_manager.print_secondary("Cor inválida. Tente novamente.")  

    while True:  
        secondary_choice = input(f"{color_manager.secondary}Escolha a cor secundária (ex: magenta): {Style.RESET_ALL}").strip().lower()  
        if secondary_choice in COLOR_MAP:  
            break  
        else:  
            color_manager.print_secondary("Cor inválida. Tente novamente.")  

    color_manager.set_colors(COLOR_MAP[primary_choice], COLOR_MAP[secondary_choice])  
    user_config['primary_color'] = primary_choice
    user_config['secondary_color'] = secondary_choice
    save_user_config(user_config)
    color_manager.print_primary("Cores atualizadas e salvas com sucesso!")  
    time.sleep(2)

def main_menu():
    scrobbler = LastfmScrobbler()
    if not scrobbler.authenticate():
        return

    while True:  
        clear_screen()  
        color_manager.print_primary(ASCII_ARTS[CURRENT_ASCII_ART])
        
        # Menu com suporte a idiomas
        menu_text = {
            'pt': {
                'title': "\n--- Menu Principal Last.fm Scrobbler ---",
                'options': [
                    "1. Scrobble por álbum",
                    "2. Scrobble por faixa",
                    "3. Scrobble por discografia do artista",
                    "4. Configurações",
                    "5. Sair"
                ]
            },
            'en': {
                'title': "\n--- Last.fm Scrobbler Main Menu ---",
                'options': [
                    "1. Scrobble by album",
                    "2. Scrobble by track",
                    "3. Scrobble artist discography",
                    "4. Settings",
                    "5. Exit"
                ]
            }
        }
        
        lang = menu_text[LANGUAGE]
        color_manager.print_primary(lang['title'])  
        for option in lang['options']:
            color_manager.print_secondary(option)

        choice = input(f"{color_manager.primary}Escolha uma opção: {Style.RESET_ALL}").strip()  

        if choice == '1':  
            scrobble_by_album(scrobbler)  
        elif choice == '2':  
            scrobble_by_track(scrobbler)  
        elif choice == '3':  
            scrobble_by_artist_discography(scrobbler)  
        elif choice == '4':  
            settings_menu()
        elif choice == '5':  
            if LANGUAGE == 'pt':
                color_manager.print_primary("Saindo... Até mais!")
            else:
                color_manager.print_primary("Exiting... Goodbye!")
            break  
        else:  
            if LANGUAGE == 'pt':
                color_manager.print_secondary("Opção inválida. Tente novamente.")  
            else:
                color_manager.print_secondary("Invalid option. Try again.")  
            time.sleep(2)

if __name__ == "__main__":
    main_menu()