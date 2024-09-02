import os
import requests

def vytvorit_slozku(cesta):
    if not os.path.exists(cesta):
        os.makedirs(cesta)

def nacti_seznam_souboru(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text.splitlines()
    else:
        raise Exception(f"Načtení seznamu souborů se nezdařilo. Server vrátil stavový kód {response.status_code}")

def stahni_soubor(file_url, uloz_cesta):
    response = requests.get(file_url)
    if response.status_code == 200:
        with open(uloz_cesta, "wb") as file:
            file.write(response.content)
    else:
        raise Exception(f"Stažení souboru {file_url} se nezdařilo. Server vrátil stavový kód {response.status_code}")

def smazat_soubor(cesta_k_souboru):
    os.remove(cesta_k_souboru)
    print(f"Soubor {cesta_k_souboru} byl úspěšně smazán.")