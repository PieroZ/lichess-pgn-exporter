import os
import json
import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv

# Wczytaj zmienne środowiskowe (TOKEN)
load_dotenv()
LICHESS_TOKEN = os.getenv("LICHESS_TOKEN")

# URL turnieju ChessManager
CHESSMANAGER_URL = os.getenv("CHESSMANAGER_URL")

# Folder wyjściowy
OUTPUT_DIR = "pgns"
os.makedirs(OUTPUT_DIR, exist_ok=True)

def get_lichess_usernames():
    """Pobiera listę nicków Lichess ze strony turnieju ChessManager."""
    print("🔍 Pobieram graczy z ChessManager...")
    r = requests.get(CHESSMANAGER_URL)
    r.raise_for_status()
    soup = BeautifulSoup(r.text, "html.parser")

    usernames = set()

    # Znajdujemy wszystkie <td class="mobile hidden"><em>nick</em></td>
    for td in soup.find_all("td", class_="mobile hidden"):
        em = td.find("em")
        if em:
            nick = em.get_text(strip=True)
            if nick:
                usernames.add(nick.lower())

    print(f"✅ Znaleziono {len(usernames)} graczy: {', '.join(sorted(usernames))}")
    return usernames


def download_games(username, player_list):
    """Pobiera partie danego użytkownika z Lichess API."""
    print(f"⬇️ Pobieram partie dla {username}...")

    url = f"https://lichess.org/api/games/user/{username}"
    params = {
        "max": 100,  # maksymalna liczba partii
        "pgnInJson": True,
        "clocks": False,
        "evals": False,
        "opening": True
    }

    headers = {
        "Accept": "application/x-ndjson"
    }

    if LICHESS_TOKEN:
        headers["Authorization"] = f"Bearer {LICHESS_TOKEN}"

    r = requests.get(url, headers=headers, params=params, timeout=30)

    if r.status_code != 200:
        print(f"⚠️ Nie udało się pobrać partii dla {username}: {r.status_code}")
        return

    for line in r.text.splitlines():
        try:
            data = json.loads(line)
        except json.JSONDecodeError:
            continue

        players = data.get("players", {})
        white_user = players.get("white", {}).get("user", {}).get("name", "").lower()
        black_user = players.get("black", {}).get("user", {}).get("name", "").lower()

        if not white_user or not black_user:
            continue

        # filtr: obaj gracze muszą być z listy turniejowej
        if white_user in player_list and black_user in player_list:
            pgn = data.get("pgn", "")
            if not pgn:
                continue

            game_id = data.get("id", "unknown")
            filename = f"{OUTPUT_DIR}/{white_user}_vs_{black_user}_{game_id}.pgn"

            with open(filename, "w", encoding="utf-8") as f:
                f.write(pgn)

            print(f"💾 Zapisano: {filename}")


def main():
    players = get_lichess_usernames()
    for p in players:
        download_games(p, players)


if __name__ == "__main__":
    main()
