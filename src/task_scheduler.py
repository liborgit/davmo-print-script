import subprocess
import time
import logging
from config import MAIN_PY_PATH, INTERVAL

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def run_main_script():
    logging.info(f"Spouštím main.py na cestě: {MAIN_PY_PATH}")

    try:
        process = subprocess.Popen(
            ["python", MAIN_PY_PATH],
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True
        )

        for line in process.stdout:
            logging.info(f"main.py: {line.strip()}")

        process.wait()
        logging.info("Proces kontroly souborů k tisku byl dokončen.")

    except Exception as e:
        logging.error(f"Chyba při spuštění main.py: {e}")

    finally:
        if process.stdout:
            process.stdout.close()

def schedule_main_script():
    try:
        while True:
            run_main_script()
            logging.info(
                f"Čekám {INTERVAL // 60} minut na další spuštění...\n--- Plánovač lze ukončit stisknutím Ctrl + C. ---")
            time.sleep(INTERVAL)

    except KeyboardInterrupt:
        logging.info("Plánovač byl ukončen uživatelem.")


if __name__ == "__main__":
    schedule_main_script()