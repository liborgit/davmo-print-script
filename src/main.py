import os
import json
from config import TXT_URL, BASE_URL, DOWNLOAD_FOLDER, LOG_FILE
from file_operations import vytvorit_slozku, nacti_seznam_souboru, stahni_soubor
from printer import tiskni_soubor, zaznamenej_tisknuty_soubor

def zpracuj_soubory():
    vytvorit_slozku(DOWNLOAD_FOLDER)

    try:
        seznam_souboru = nacti_seznam_souboru(TXT_URL)
    except Exception as e:
        print(f"Chyba při načítání seznamu souborů: {e}")
        return

    try:
        with open(LOG_FILE, "r") as f:
            vytistene_soubory = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        vytistene_soubory = []

    soubory_vytištěny = False

    for soubor in seznam_souboru:
        if soubor not in vytistene_soubory:
            print(f"Stahuji soubor: {soubor}")
            soubory_vytištěny = True

            file_url = BASE_URL + soubor
            cesta_k_souboru = os.path.join(DOWNLOAD_FOLDER, soubor)

            try:
                stahni_soubor(file_url, cesta_k_souboru)

                if os.path.exists(cesta_k_souboru):
                    print(f"Soubor {soubor} byl úspěšně stažen. Odesílám k tisku.")
                    tiskni_soubor(cesta_k_souboru)
                    zaznamenej_tisknuty_soubor(soubor, LOG_FILE)
                else:
                    print(f"Soubor {soubor} nebyl nalezen po stažení.")
            except Exception as e:
                print(f"Chyba při zpracování souboru {soubor}: {e}")

    if not soubory_vytištěny:
        print("Žádné nové soubory k tisku.")

    print("Zpracování dokončeno.")

if __name__ == "__main__":
    zpracuj_soubory()