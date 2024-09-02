import os
from config import TXT_URL, BASE_URL, DOWNLOAD_FOLDER, LOG_FILE
from file_operations import vytvorit_slozku, nacti_seznam_souboru, stahni_soubor, smazat_soubor
from printer import tiskni_soubor, zaznamenej_tisknuty_soubor


def zpracuj_soubory():
    vytvorit_slozku(DOWNLOAD_FOLDER)

    try:
        seznam_souboru = nacti_seznam_souboru(TXT_URL)
    except Exception as e:
        print(e)
        return

    if os.path.exists(LOG_FILE):
        with open(LOG_FILE, "r") as f:
            vytistene_soubory = f.read().splitlines()
    else:
        vytistene_soubory = []

    soubory_vytištěny = False

    for soubor in seznam_souboru:
        if soubor not in vytistene_soubory:
            print(f"Stahuji a tisknu soubor: {soubor}")
            soubory_vytištěny = True

            file_url = BASE_URL + soubor
            cesta_k_souboru = os.path.join(DOWNLOAD_FOLDER, soubor)

            try:
                stahni_soubor(file_url, cesta_k_souboru)
                tiskni_soubor(cesta_k_souboru)
                zaznamenej_tisknuty_soubor(soubor, LOG_FILE)
                smazat_soubor(cesta_k_souboru)
            except Exception as e:
                print(e)

    if not soubory_vytištěny:
        print("Žádné nové soubory k tisku.")

    print("Zpracování dokončeno.")


# Spuštění procesu
if __name__ == "__main__":
    zpracuj_soubory()