# davmo.cz/print-script

## Popis
Tento projekt je automatizační skript pro stahování a tisk PDF souborů z webu. Skript stahuje seznam souborů z určeného TXT souboru, který je uložen na webu, a poté jednotlivé PDF soubory automaticky stáhne, vytiskne a po úspěšném tisku odstraní z lokálního úložiště.

## Funkce
- Automatické stahování seznamu PDF souborů z webu.
- Ukládání stažených PDF souborů do specifikované složky.
- Automatický tisk PDF souborů.
- Mazání PDF souborů z lokálního úložiště po úspěšném tisku.
- Záznam již vytisknutých souborů, aby nedocházelo k jejich opakovanému tisku.

## Použití
1. Naklonujte tento repozitář do svého lokálního prostředí.
2. Upravte konfigurační soubor `config.py` podle svých potřeb (např. cesty k souborům, URL adresy).
3. Spusťte hlavní skript `main.py`.
4. Skript automaticky stáhne a vytiskne nové PDF soubory a po úspěšném tisku je smaže.

## Požadavky
- Python 3.x
- Nainstalované knihovny: `requests`

## Instalace
1. Klonujte repozitář: `git clone https://github.com/liborgit/davmo-print-script`
3. Nainstalujte požadované knihovny: `pip install -r requirements.txt`
