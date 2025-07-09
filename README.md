# TunerFM
Last.fm Scrobbler but a way cooler




# 🎛️ TunerFM

**O scrobbler farmer mais rápido (deve ser o único x3) para Last.fm — milhares de scrobbles em minutos!**  
The fastest, wildest Last.fm scrobbler—thousands of scrobbles in minutes! :3


## 🇧🇷 Português

### 🚀 Descrição
TunerFM é um “scrobbler farmer” que planta **milhares de scrobbles** na sua conta Last.fm em tempo recorde.  
Ele automatiza desde um único track até discografias inteiras, com delay customizável ou “turbo mode” (intervalo = 0).  

  - `main_menu()`: menu principal multilíngue (PT/EN).  
  - `settings_menu()`: muda idioma, cores, ASCII art, exibe credenciais.  
  - `configure_ascii_art()`, `change_language()`, `configure_colors()`, `configure_custom_ascii()`, `view_credentials()`: customizações variadas.  

### 📦 Pré-requisitos
- Python 3.7+  
- Última versão de `pip`  
- Libs Python (instalar via `requirements.txt`):

  ```txt
  pylast
  colorama

📁 Estrutura

TunerFM/
├── tunerfm.py         # seu script principal
├── requirements.txt   # lista de dependências
└── README.md          # este arquivo

🛠️ Instalação & Uso em Todas as Plataformas

> Dica geral: crie sempre um virtualenv para isolamento:

python3 -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate



💻 PC (Windows, Linux, macOS)

1. Clone o repositório e entre na pasta:

git clone https://github.com/macinttosh/TunerFM.git
cd TunerFM


2. Instale dependências:

pip install --upgrade pip
pip install -r requirements.txt


3. Execute:

python3 tunerfm.py



📱 Termux (Android)

1. Atualize e instale Python:

pkg update && pkg install python git


2. Clone e instale:

git clone https://github.com/macinttosh/TunerFM.git
cd TunerFM
pip install --upgrade pip
pip install -r requirements.txt


3. Execute:

python3 tunerfm.py



🤖 Pydroid 3 (Android)

1. Abra o Pydroid 3 e copie a pasta TunerFM para o armazenamento interno.


2. No menu lateral, acesse PIP e instale manualmente:

pylast

colorama



3. Abra tunerfm.py no editor do Pydroid 3 e toque em Run.


🇺🇸 English

🚀 Description

TunerFM is a Last.fm “scrobbler farmer” that plants thousands of scrobbles on your account in record time.
It automates everything from a single track up to entire discographies, with custom delays or full “turbo mode” (interval = 0).


Menus & Helpers

main_menu(): multilanguage main menu (EN/PT).

settings_menu(): change language, colors, ASCII art, reveal creds.

Customization helpers: ASCII art, language, colors, credentials view.



📦 Prerequisites

Python 3.7+

Latest pip

Python libs (install via requirements.txt):

pylast
colorama


📁 Structure

TunerFM/
├── tunerfm.py         # main script
├── requirements.txt   # dependencies list
└── README.md          # this file

Install & Run on Any Platform



 PC (Windows, Linux, macOS)

1. Clone & cd:

git clone https://github.com/macinttosh/TunerFM.git
cd TunerFM


2. Install deps:

pip install --upgrade pip
pip install -r requirements.txt


3. Run:

python3 tunerfm.py



📱 Termux (Android)

1. Setup:

pkg update && pkg install python git


2. Clone, install:

git clone https://github.com/macinttosh/TunerFM.git
cd TunerFM
pip install --upgrade pip
pip install -r requirements.txt


3. Run:

python3 tunerfm.py



🤖 Pydroid 3 (Android)

1. Copy TunerFM folder to Pydroid 3 storage.


2. In Pydroid’s PIP, install:

pylast

colorama



3. Open tunerfm.py and hit Run.





🎉 Contribuições

Issues, PRs e forks são muito bem-vindos! Vamos deixar esse scrobbler cada vez mais louco e eficiente. O⁠_⁠o




> License: MIT
(funny enough idk even why did i put a license 0_0)





