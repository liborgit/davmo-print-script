import os
import requests


def create_directory(path):
    if not os.path.exists(path):
        os.makedirs(path)


def fetch_file_list(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text.splitlines()
    else:
        raise Exception(f"Failed to fetch file list. Server returned status code {response.status_code}")


def download_file(file_url, save_path):
    response = requests.get(file_url)
    if response.status_code == 200:
        with open(save_path, "wb") as file:
            file.write(response.content)
    else:
        raise Exception(f"Failed to download file {file_url}. Server returned status code {response.status_code}")


def print_file(file_path):
    try:
        os.startfile(file_path, "print")
        print(f"Soubor {file_path} byl úspěšně odeslán k tisku.")
    except OSError as e:
        raise Exception(f"Chyba při tisku souboru {file_path}: {e}")


def log_printed_file(file_name, log_file):
    with open(log_file, "a") as f:
        f.write(file_name + "\n")


def delete_file(file_path):
    os.remove(file_path)
    print(f"Soubor {file_path} byl úspěšně smazán.")


def process_files(txt_url, base_url, download_folder, log_file):
    create_directory(download_folder)

    try:
        seznam_souboru = fetch_file_list(txt_url)
    except Exception as e:
        print(e)
        return

    if os.path.exists(log_file):
        with open(log_file, "r") as f:
            printed_files = f.read().splitlines()
    else:
        printed_files = []

    files_printed = False

    for file in seznam_souboru:
        if file not in printed_files:
            print(f"Stahuji a tisknu soubor: {file}")
            files_printed = True

            file_url = base_url + file
            file_path = os.path.join(download_folder, file)

            try:
                download_file(file_url, file_path)
                print_file(file_path)
                log_printed_file(file, log_file)
                delete_file(file_path)
            except Exception as e:
                print(e)

    if not files_printed:
        print("Žádné nové soubory k tisku.")

    print("Zpracování dokončeno.")


# Parametry
txt_url = "https://raw.githubusercontent.com/liborgit/davmo-print-script/master/model_order_list/order_list.txt"
base_url = "https://raw.githubusercontent.com/liborgit/davmo-print-script/master/model-pdf-files/"
download_folder = "downloaded-pdf-files"
log_file = "printed_files.txt"

# Spuštění procesu
process_files(txt_url, base_url, download_folder, log_file)