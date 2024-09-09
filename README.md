Poznámka: nyní pracuji na rozšíření funkce automatizace a převodu CLI aplikace do GUI formy

# Skript pro automatický tisk PDF souborů

Tento projekt je určen k automatickému stahování a tisku PDF souborů z daného seznamu, který je uložen ve formátu JSON. Skript také zaznamenává, které soubory byly úspěšně vytištěny, aby se zabránilo jejich opakovanému tisku.

## Struktura projektu

- **main.py**: Hlavní skript, který zpracovává seznam souborů, stahuje PDF soubory a odesílá je k tisku.
- **config.py**: Obsahuje konfigurační proměnné, jako jsou URL pro seznam souborů a umístění PDF souborů.
- **file_operations.py**: Obsahuje funkce pro práci se soubory, jako je stahování souborů a vytváření složek.
- **printer.py**: Obsahuje funkce pro odesílání souborů k tisku a zaznamenávání vytištěných souborů.
- **order_list.json**: Soubor ve formátu JSON obsahující seznam PDF souborů k tisku.
- **printed_files.json**: Soubor ve formátu JSON, kde jsou zaznamenány již vytištěné soubory.

## Použití

### Předpoklady

- Python 3.x
- Knihovna `requests`

### Nastavení

1. Naklonujte tento repozitář do svého lokálního stroje.
2. Vytvořte virtuální prostředí a aktivujte ho:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # Na Windows použijte .venv\Scripts\activate
### Nainstalujte potřebné závislosti:

```bash
pip install requests
```
### Upravte soubor `config.py` dle vašich potřeb:

- **TXT_URL**: URL adresa k souboru JSON, který obsahuje seznam PDF souborů k tisku.
- **BASE_URL**: Základní URL adresa ke složce, kde jsou uloženy PDF soubory.
- **DOWNLOAD_FOLDER**: Složka, kam se budou stahovat PDF soubory před tiskem.
- **LOG_FILE**: Název souboru, ve kterém jsou zaznamenány již vytištěné soubory.


### Spuštění

Spusťte hlavní skript:

```bash
python src/main.py
```
Skript automaticky načte seznam PDF souborů z order_list.json, stáhne je, vytiskne a zaznamená do printed_files.json.

### Jak to funguje

- **Načítání seznamu souborů**: Skript načte seznam PDF souborů z URL definované v `config.py`.
- **Kontrola vytištěných souborů**: Skript zkontroluje, které soubory již byly vytištěny, a vytiskne pouze nové soubory.
- **Stahování a tisk**: Každý nový soubor je stažen a následně odeslán k tisku.
- **Zaznamenávání**: Po úspěšném tisku je soubor zaznamenán do `printed_files.json`, aby se zabránilo jeho opakovanému tisku.

### Omezení

- Skript je navržen pro použití na systémech Windows, kde využívá funkci `os.startfile` pro odesílání souborů k tisku.
- Pro tisk souborů je nutné mít na systému nainstalovanou výchozí aplikaci, která podporuje příkaz tisku (např. Adobe Reader pro PDF).
