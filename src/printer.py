import os

def tiskni_soubor(cesta_k_souboru):
    try:
        os.startfile(cesta_k_souboru, "print")
        print(f"Soubor {cesta_k_souboru} byl úspěšně odeslán k tisku.")
    except OSError as e:
        raise Exception(f"Chyba při tisku souboru {cesta_k_souboru}: {e}")

def zaznamenej_tisknuty_soubor(jmeno_souboru, log_soubor):
    with open(log_soubor, "a") as f:
        f.write(jmeno_souboru + "\n")