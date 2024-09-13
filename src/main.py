import os
import json
import logging
import requests
from config import TXT_URL, BASE_URL, DOWNLOAD_FOLDER, LOG_FILE
from file_operations import create_folder, load_file_list, download_file
from printer import print_file, record_printed_file

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def process_files():
    create_folder(DOWNLOAD_FOLDER)

    file_list = get_file_list()
    if file_list is None:
        return

    printed_files = get_printed_files()

    files_printed = download_and_print_files(file_list, printed_files)

    if not files_printed:
        logging.info("Žádné nové soubory k tisku.")
    logging.info("Zpracování dokončeno.")

def get_file_list():
    try:
        return load_file_list(TXT_URL)
    except requests.exceptions.RequestException as e:
        logging.error(f"Chyba při načítání seznamu souborů: {e}")
        return None

def get_printed_files():
    try:
        with open(LOG_FILE, "r") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def download_and_print_files(file_list, printed_files):
    files_printed = False

    for file in file_list:
        if file not in printed_files:
            logging.info(f"Stahuji soubor: {file}")
            files_printed = True

            file_url = BASE_URL + file
            file_path = os.path.join(DOWNLOAD_FOLDER, file)

            if download_file_and_handle(file_url, file_path):
                print_file(file_path)
                record_printed_file(file, LOG_FILE)
            else:
                logging.warning(f"Soubor {file} nebyl nalezen po stažení.")
    
    return files_printed

def download_file_and_handle(file_url, file_path):
    try:
        download_file(file_url, file_path)
        return os.path.exists(file_path)
    except requests.exceptions.RequestException as e:
        logging.error(f"Chyba při stahování souboru {file_url}: {e}")
        return False

if __name__ == "__main__":
    process_files()