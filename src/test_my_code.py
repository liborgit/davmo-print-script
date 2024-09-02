import os
import requests

# URL k vašemu TXT souboru na GitHubu
txt_url = "https://raw.githubusercontent.com/liborgit/davmo-print-scrip/main/model_order_list/order_list.txt"

# Načtení seznamu souborů ze serveru
response = requests.get(txt_url)
if response.status_code == 200:
    print("Seznam souborů úspěšně načten.")
    # Rozdělení obsahu TXT souboru na seznam souborů
    seznam_souboru = response.text.splitlines()

    # Načtení seznamu již vytisknutých souborů
    printed_files = []
    if os.path.exists("printed_files.txt"):
        with open("printed_files.txt", "r") as f:
            printed_files = f.read().splitlines()

    # Základní URL k PDF souborům
    base_url = "https://raw.githubusercontent.com/liborgit/davmo-print-scrip/main/model-pdf-files/"

    # Ukazatel, zda se nějaký soubor tisknul
    files_printed = False

    for file in seznam_souboru:
        if file not in printed_files:
            print(f"Stahuji a tisknu soubor: {file}")
            files_printed = True  # Zaznamenejte, že byl nějaký soubor zpracován
            # Stažení souboru
            file_url = base_url + file
            print(f"URL ke stažení: {file_url}")
            response = requests.get(file_url)
            if response.status_code == 200:
                with open(file, "wb") as f:
                    f.write(response.content)

                # Pokus o tisk souboru (pro Windows)
                try:
                    os.startfile(file, "print")
                    print(f"Soubor {file} byl úspěšně odeslán k tisku.")

                    # Po úspěšném tisku přidat soubor do seznamu vytisknutých
                    with open("printed_files.txt", "a") as f:
                        f.write(file + "\n")
                except OSError as e:
                    print(f"Chyba při tisku souboru {file}: {e}")
                    # Volitelně můžeme přidat logiku pro opakovaný pokus o tisk
            else:
                print(f"Chyba: Soubor {file} se nepodařilo stáhnout.")

    if not files_printed:
        print("Žádné nové soubory k tisku.")

    print("Zpracování dokončeno.")
else:
    print(f"Chyba: Server vrátil stavový kód {response.status_code}")