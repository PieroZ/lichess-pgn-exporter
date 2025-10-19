
import requests
from bs4 import BeautifulSoup


# URL turnieju ChessManager
CHESSMANAGER_URL = "#####################"


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



def main():
    players = get_lichess_usernames()


if __name__ == "__main__":
    main()
