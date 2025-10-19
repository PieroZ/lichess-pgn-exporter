# ♟️ Lichess Tournament Game Downloader

A simple Python script to download chess games from [Lichess.org](https://lichess.org) played between participants of a tournament registered on [ChessManager.com](https://www.chessmanager.com).

Each game is saved as a separate `.pgn` file.

---

## 🧰 Requirements

- **Python 3.10+**  
  (check with `python --version` or `python3 --version`)
- A **Lichess.org account**
- Access to the tournament page on **ChessManager** (e.g., `https://www.chessmanager.com/pl-pl/tournaments/xxxxx/players`)

---

## 🚀 Step-by-step Setup

### 1️⃣ Clone the repository or download the files

With Git:
```bash
git clone https://github.com/PieroZ/lichess-pgn-exporter.git
cd lichess-pgn-exporter
```

2️⃣ Create and activate a virtual environment

This isolates the project dependencies.

💻 Windows (PowerShell or CMD):
```
python -m venv venv
venv\Scripts\activate
```

🐧 Linux / macOS:
```
python3 -m venv venv
source venv/bin/activate
```

You should see (venv) in your terminal prompt.

3️⃣ Install required Python libraries

```
pip install -r requirements.txt
```

4️⃣ Configure the .env file
The script uses a .env file to store configuration.
There is a template file .env.example in the repository. Copy it and fill in your values:
```
cp .env.example .env
```
Edit .env with:
```
LICHESS_TOKEN=lip_xxxxxxxxxxxxxxxxxxxxxxxxxx
CHESSMANAGER_URL=https://www.chessmanager.com/pl-pl/tournaments/1234567890123456/players
```

🔐 How to get your LICHESS_TOKEN

Log in to Lichess.org
Go to Personal API Tokens
Click "Create a new token", and copy the generated token without adding any additional permissions.
Paste it into .env.

5️⃣ Run the script

After activating the virtual environment:
```
python main.py
```

6️⃣ Output

The script fetches the list of players from ChessManager (Lichess nicknames column).

Then it downloads all games where both players are tournament participants.

Each game is saved in the pgns/ folder, for example:
```
pgns/
├── pieroz_vs_khahethel_gv82xF9.pgn
├── kasparov_vs_karpov_Hyq7z9D2.pgn
```

⚙️ Project files

```
File	Description
main.py	Main script to download games
requirements.txt	Python libraries required for the project
.env.example	Template configuration file
.gitignore	Ignores .env and .idea/
pgns/	Folder where downloaded .pgn files are stored
```
