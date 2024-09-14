# Skript pro automatický tisk PDF souborů

Tento program je určen k automatickému stahování a tisku PDF souborů z daného seznamu, který je uložen ve formátu JSON. Skript také zaznamenává, které soubory byly úspěšně vytištěny, aby se zabránilo jejich opakovanému tisku. Byl vytvořen pro soukromého klienta na zakázku pod **MIT licencí**.

## Struktura projektu

- `task_scheduler.py`: Plánovač, který opakovaně spouští hlavní skript `main.py` v předem definovaném časovém intervalu. Slouží pro plnou automatizaci tiskových úloh.
- `main.py`: Hlavní skript, který zpracovává seznam souborů, stahuje PDF soubory a odesílá je k tisku.
- `config.py`: Obsahuje konfigurační proměnné, jako jsou URL pro seznam souborů, umístění PDF souborů k tisku apod. Je nutné jej nastavit dle potřeb uživatele.
- `file_operations.py`: Obsahuje funkce pro práci se soubory.
- `printer.py`: Obsahuje funkce pro odesílání souborů k tisku a zaznamenávání vytištěných souborů do logu.
- `printed_files.json`: Soubor ve formátu JSON, kde jsou zaznamenány již vytištěné soubory. Slouží jako log pro potřeby skriptu.


- `order_list.json`: Soubor ve formátu JSON obsahující seznam PDF souborů k tisku. V reálném nasazení projektu jde o externí soubor na severu.

## Použití

### Předpoklady

- Python 3.x
- Knihovna `requests`

### Nastavení

1. Naklonujte tento repozitář do svého lokálního zařízení (nutné mít **Git**):
   ```bash
   git clone https://github.com/liborgit/davmo-print-script.git

2. Vytvořte virtuální prostředí a aktivujte ho:
   ```bash
   python -m venv .venv
   .venv\Scripts\activate

3. Nainstalujte potřebné závislosti:
   ```bash
   pip install requests

### Upravte soubor `config.py` dle vašich potřeb:

- `MAIN_PY_PATH`: Vložte cestu k souboru `main.py` Důležité pro použití `task_scheduler.py`.
- `INTERVAL`: Interval v sekundách, po kterém se bude znovu spouštět `main.py`. Upravte dle potřeby.
- `LIST_URL`: URL adresa k externímu souboru JSON, který obsahuje seznam PDF souborů k tisku.
- `BASE_URL`: Základní URL adresa k externímu adresáři, kde jsou uloženy PDF soubory (objednávky) k tisku.
- `DOWNLOAD_FOLDER`: Složka, kam se budou stahovat PDF soubory před tiskem.
- `LOG_FILE`: Název souboru, ve kterém jsou zaznamenány již vytištěné soubory.

## Spuštění

Pro automatickou kontrolu nových souborů ke stažení a tisku je nutné spustit skript `task_scheduler.py`. Tento skript zajišťuje plánované spouštění hlavního skriptu `main.py` v pravidelných intervalech, jak jsou definovány v konfiguračním souboru `config.py`.

### Postup spuštění:
1. Otevřete terminál nebo příkazový řádek.
2. Přejděte do adresáře zdrojového kódu projektu `src/`.
3. Spusťte plánovač `task_scheduler.py`. Tímto příkazem se spustí plánovač, který bude opakovaně kontrolovat nové soubory ke stažení a tisku.
   ```bash
   python task_scheduler.py

### Po spuštění plánovače:

Program bude automaticky v pravidelném intervalu (např. každých 30 minut) spouštět skript `main.py`.  V každém běhu bude skript zpracovávat a porovnávat seznam souborů, stahovat nové PDF soubory a odesílat je k tisku.
Plánovač bude vypisovat do konzole informace o běhu programu.


Pokud chcete plánovač ukončit, můžete bezpečně zastavit běh programu stisknutím kombinace kláves **Ctrl + C**.

### Jak to funguje

- **Načítání seznamu souborů**: Skript načte seznam PDF souborů z URL definované v `config.py`.
- **Kontrola vytištěných souborů**: Skript zkontroluje, které soubory již byly vytištěny, a vytiskne pouze nové soubory.
- **Stahování a tisk**: Každý nový soubor je stažen a následně odeslán k tisku.
- **Zaznamenávání**: Po úspěšném tisku je soubor zaznamenán do logu `printed_files.json`, aby se zabránilo jeho opakovanému tisku.

### Omezení

- Skript je navržen pro použití na systémech Windows, kde využívá funkci `os.startfile` pro odesílání souborů k tisku.
- Pro tisk souborů je nutné mít na systému nainstalovanou výchozí aplikaci, která podporuje příkaz tisku (např. Adobe Reader pro PDF).
