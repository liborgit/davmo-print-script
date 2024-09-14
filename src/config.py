# Cesta k souboru main.py (důležité pro task_scheduler.py)
MAIN_PY_PATH = "C:\\Users\\libor\\Desktop\\davmo-print-script\\davmo-print-script\\src\\main.py"

# Interval v sekundách, po kterém se bude znovu spouštět main.py
# Například 1800 sekund = 30 minut
INTERVAL = 1800

# URL adresa k souboru TXT, který obsahuje seznam PDF souborů k tisku
LIST_URL = "https://raw.githubusercontent.com/liborgit/davmo-print-script/master/model_order_list/order_list.json"

# Základní URL adresa ke složce, kde jsou uloženy PDF soubory
BASE_URL = "https://raw.githubusercontent.com/liborgit/davmo-print-script/master/model_pdf_files/"

# Složka, kam se budou stahovat PDF soubory před tiskem
DOWNLOAD_FOLDER = "downloaded_pdf_files"

# Název souboru, ve kterém jsou zaznamenány již vytisknuté soubory
LOG_FILE = "printed_files.json"