import os
import json

def tiskni_soubor(cesta_k_souboru):
    try:
        os.startfile(cesta_k_souboru, "print")
        print(f"Soubor {cesta_k_souboru} byl úspěšně odeslán k tisku.")
    except OSError as e:
        raise Exception(f"Chyba při tisku souboru {cesta_k_souboru}: {e}")

def zaznamenej_tisknuty_soubor(jmeno_souboru, log_soubor):
    try:
        with open(log_soubor, "r") as f:
            data = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        data = []

    if jmeno_souboru not in data:
        data.append(jmeno_souboru)

    with open(log_soubor, "w") as f:
        json.dump(data, f, indent=4)