import os
import requests
import logging

def create_folder(path):
    if not os.path.exists(path):
        os.makedirs(path)
        logging.info(f"Složka {path} byla vytvořena.")

def load_file_list(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        raise requests.exceptions.RequestException(
            f"Načtení seznamu souborů se nezdařilo. Server vrátil stavový kód {response.status_code}"
        )

def download_file(file_url, save_path):
    response = requests.get(file_url)
    if response.status_code == 200:
        with open(save_path, "wb") as file:
            file.write(response.content)
            logging.info(f"Soubor {file_url} byl úspěšně stažen do {save_path}.")
    else:
        raise requests.exceptions.RequestException(
            f"Stažení souboru {file_url} se nezdařilo. Server vrátil stavový kód {response.status_code}"
        )