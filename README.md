# 🎧 **TunerFM**  
*A ridiculously fast Last.fm scrobbler farmer — thousands of scrobbles in minutes!*

---

### 🚀 **Description**

TunerFM is a turbocharged scrobbler farmer that injects **thousands of scrobbles** into your Last.fm account in record time.  
It automates **everything from single tracks to entire discographies**, with custom delay support or full **turbo mode** (`interval = 0`).

---

### ⚙️ **Key Functions**

```python
main_menu()            # Multilanguage interface (EN/PT)
settings_menu()        # Customize language, colors, ASCII art, reveal credentials

# Customization helpers:
configure_ascii_art()
change_language()
configure_colors()
configure_custom_ascii()
view_credentials()
```

---
### 🔐 **Last.fm API Credentials**

To use TunerFM, you’ll need 3 essential pieces of information:

1. **API Key**  
2. **Shared Secret**  
3. **Your password in MD5 hash format**

---

#### How to get them:

🔸 **API Key & Shared Secret**  
1. Go to: [https://www.last.fm/api/account/create](https://www.last.fm/api/account/create)  
2. Create a new application  
3. Copy your **API Key** and **Shared Secret**

🔸 **Generate your MD5 password hash**  
You can generate your MD5 password hash using Python:

```import pylast
password = input("Insert your Last.fm Actual Password: ")
password_hash = pylast.md5(password)
print(f"your password hash is: {password_hash}")
```

Or use a trusted MD5 hash generator like:  
[https://www.md5hashgenerator.com/](https://www.md5hashgenerator.com/)

---

#### Inserting your credentials into TunerFM

When you launch the program for the first time, it will ask for your credentials.  
You can also view them later from the settings menu:

```python
settings_menu() ➜ view_credentials()
```

### 📦 **Requirements**

- Python `3.7+`
- Latest version of `pip`

**Install dependencies:**

```bash
pip install -r requirements.txt
```

<details>
<summary>Or manually install:</summary>

```bash
pip install pylast colorama
```
</details>

---

### 📁 **Project Structure**

```
TunerFM/
├── tunerfm.py         # Main script
├── requirements.txt   # Dependencies list
└── README.md          # This file
```

---

### 💻 **Installation & Usage**

#### 🖥️ PC (Windows / Linux / macOS)

```bash
git clone https://github.com/macinttosh/TunerFM.git
cd TunerFM

python3 -m venv venv
# Activate virtual environment:
source venv/bin/activate      # On Windows: venv\Scripts\activate

pip install --upgrade pip
pip install -r requirements.txt

python3 tunerfm.py
```

---

#### 📱 Termux (Android)

```bash
pkg update && pkg install python git

git clone https://github.com/macinttosh/TunerFM.git
cd TunerFM

pip install --upgrade pip
pip install -r requirements.txt

python3 tunerfm.py
```

---

#### 🤖 Pydroid 3 (Android)

1. Download `tunerfm.py` manually.  
2. Open **PIP menu** and install the following packages:
   - `pylast`
   - `colorama`  
3. Open the script and hit **Run**.

---

# 🎛️ TunerFM

**Last.fm Scrobbler Farmer — absurdamente rápido!**  
Plante milhares de scrobbles em minutos com o TunerFM :3

---

## 🇧🇷 Português

### 🚀 **Descrição**

TunerFM é um *scrobbler farmer* que injeta **milhares de scrobbles** na sua conta Last.fm em tempo recorde.  
Ele automatiza desde faixas únicas até discografias inteiras, com delays personalizáveis ou o insano **turbo mode** (`interval = 0`).

---

### ⚙️ **Funções Principais**

```python
main_menu()              # Menu principal multilíngue (PT/EN)
settings_menu()          # Ajustes de idioma, cores, ASCII art, visualização de credenciais

# Funções auxiliares:
configure_ascii_art()
change_language()
configure_colors()
configure_custom_ascii()
view_credentials()
```

---

### 🔐 **Credenciais da API do Last.fm**

Para usar o TunerFM, você precisará de 3 dados importantes:

1. **API Key**
2. **Shared Secret**
3. **Senha em hash MD5**

#### Como conseguir:

🔸 **API Key & Shared Secret**  
1. Acesse: [https://www.last.fm/api/account/create](https://www.last.fm/api/account/create)  
2. Crie uma nova aplicação  
3. Copie a **API Key** e o **Shared Secret**

🔸 **Gerar senha em hash MD5**  
Você pode gerar sua senha em formato MD5 usando Python:

```import pylast
password = input("Digite sua senha do Last.fm: ")
password_hash = pylast.md5(password)
print(f"Seu password hash é: {password_hash}")
```

Ou use algum gerador online confiável de MD5 (ex: [https://www.md5hashgenerator.com/](https://www.md5hashgenerator.com/)).
( na verdade eu não faço ideia se isso funciona alem do gerador hash do proprio pylast )
#### Inserir credenciais no TunerFM

Quando o programa for iniciado pela primeira vez, ele pedirá suas credenciais. Você também pode visualizá-las depois em:

```python
settings_menu() ➜ view_credentials()
```

### 📦 **Requisitos**

- Python **3.7+**
- Última versão do `pip`

**Instalar dependências automaticamente:**

```bash
pip install -r requirements.txt
```

<details>
<summary>Ou manualmente:</summary>

```bash
pip install pylast colorama
```
</details>

---

### 📁 **Estrutura do Projeto**

```
TunerFM/
├── tunerfm.py         # Script principal
├── requirements.txt   # Lista de dependências
└── README.md          # Este arquivo
```

---

### 💻 **Instalação & Uso**

#### 🖥️ PC (Windows, Linux, macOS)

```bash
# Clone o repositório
git clone https://github.com/macinttosh/TunerFM.git
cd TunerFM

# (Opcional) Crie um ambiente virtual
python3 -m venv venv
# Ative o ambiente virtual:
source venv/bin/activate      # No Windows: venv\Scripts\activate

# Instale as dependências
pip install --upgrade pip
pip install -r requirements.txt

# Execute o script
python3 tunerfm.py
```

---

#### 📱 Termux (Android)

```bash
pkg update && pkg install python git

git clone https://github.com/macinttosh/TunerFM.git
cd TunerFM

pip install --upgrade pip
pip install -r requirements.txt

python3 tunerfm.py
```

---

#### 🤖 Pydroid 3 (Android)

1. Baixe o arquivo `tunerfm.py` manualmente.  
2. No menu lateral do Pydroid, vá até **PIP** e instale os pacotes:
   - `pylast`
   - `colorama`  
3. Abra `tunerfm.py` no editor e toque em **Run**.

---

🎉 Contribuições

Issues e forks, todos são muito bem-vindos
Vamos deixar esse scrobbler cada vez mais rapido O⁠_⁠o



📄 Licença

MIT
(funny enough, I don’t even know why I put a license 0_0)
