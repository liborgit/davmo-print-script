import os
import json
import logging

def print_file(file_path):
    try:
        os.startfile(file_path, "print")
        logging.info(f"Soubor {file_path} byl úspěšně odeslán k tisku.")
    except OSError as e:
        raise Exception(f"Chyba při tisku souboru {file_path}: {e}")

def record_printed_file(file_name, log_file):
    try:
        with open(log_file, "r") as f:
            data = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        data = []

    if file_name not in data:
        data.append(file_name)

    with open(log_file, "w") as f:
        json.dump(data, f, indent=4)
        logging.info(f"Soubor {file_name} byl zaznamenán do logu {log_file}.")