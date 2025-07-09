 🎛️ TunerFM

**Last.fm Scrobbler Farmer — absurdamente rápido!**  
Plante milhares de scrobbles em minutos com o TunerFM :3


## 🇧🇷 Português

### 🚀 Descrição

TunerFM é um *scrobbler farmer* que injeta **milhares de scrobbles** na sua conta Last.fm em tempo recorde.  
Ele automatiza desde faixas únicas até discografias inteiras, com delays personalizáveis ou o insano **turbo mode** (`interval = 0`).

### ⚙️ Funções Principais

- `main_menu()`: menu principal multilíngue (PT/EN)  
- `settings_menu()`: ajustes de idioma, cores, ASCII art, visualização de credenciais  
- Helpers:  
  - `configure_ascii_art()`  
  - `change_language()`  
  - `configure_colors()`  
  - `configure_custom_ascii()`  
  - `view_credentials()`

---

### 📦 Requisitos

- Python **3.7+**
- Última versão do `pip`
- Dependências (instalar com `requirements.txt`):

```txt
pylast
colorama



📁 Estrutura do Projeto

TunerFM/
├── tunerfm.py         # Script principal
├── requirements.txt   # Lista de dependências
└── README.md          # Este arquivo



💻 Instalação & Uso

🖥️ PC (Windows, Linux, macOS)

# Clone o repositório
git clone https://github.com/macinttosh/TunerFM.git
cd TunerFM

# (Recomendado) Crie um ambiente virtual
python3 -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate

# Instale as dependências
pip install --upgrade pip
pip install -r requirements.txt

# Execute
python3 tunerfm.py

📱 Termux (Android)

pkg update && pkg install python git

git clone https://github.com/macinttosh/TunerFM.git
cd TunerFM

pip install --upgrade pip
pip install -r requirements.txt

python3 tunerfm.py

🤖 Pydroid 3 (Android)

1. Baixe o tunerfm.py


2. No menu lateral do Pydroid, vá até PIP e instale:



pylast
colorama

3. Abra tunerfm.py no editor e toque em Run.




🇺🇸 English

🚀 Description

TunerFM is a scrobbler farmer that injects thousands of scrobbles into your Last.fm account in record time.
It automates anything from a single track to full discographies, with custom delay or full turbo mode (interval = 0).

⚙️ Key Functions

main_menu(): multilanguage interface (EN/PT)

settings_menu(): tweak language, colors, ASCII art, reveal credentials

Customization helpers:

configure_ascii_art()

change_language()

configure_colors()

configure_custom_ascii()

view_credentials()




---

📦 Requirements

Python 3.7+

Latest pip

Install with requirements.txt:


pylast
colorama


---

📁 Project Structure

TunerFM/
├── tunerfm.py         # Main script
├── requirements.txt   # Dependencies list
└── README.md          # This file


---

💻 Installation & Usage

🖥️ PC (Windows, Linux, macOS)

git clone https://github.com/macinttosh/TunerFM.git
cd TunerFM

python3 -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

pip install --upgrade pip
pip install -r requirements.txt

python3 tunerfm.py

📱 Termux (Android)

pkg update && pkg install python git

git clone https://github.com/macinttosh/TunerFM.git
cd TunerFM

pip install --upgrade pip
pip install -r requirements.txt

python3 tunerfm.py

🤖 Pydroid 3 (Android)

1. download tunerfm.py


2. In PIP menu, install:



pylast
colorama

3. Open tunerfm.py and hit Run



🎉 Contribuições

Issues e forks, todos são muito bem-vindos
Vamos deixar esse scrobbler cada vez mais rapido O⁠_⁠o



📄 Licença

MIT
(funny enough, I don’t even know why I put a license 0_0)
