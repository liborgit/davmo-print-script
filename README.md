# Davmo.cz Print Script

## Popis
Tento projekt je automatizační skript pro stahování a tisk PDF souborů z WWW. Skript stahuje seznam souborů z určeného TXT souboru, který je uložen na WWW, a poté jednotlivé PDF soubory automaticky stáhne, vytiskne a po úspěšném tisku odstraní z lokálního úložiště.

## Funkce
- Automatické stahování seznamu PDF souborů z WWW.
- Ukládání stažených PDF souborů do specifikované složky.
- Automatický tisk PDF souborů.
- Mazání PDF souborů po úspěšném tisku.
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
1. Klonujte repozitář: `git clone https://www.davmo.cz/print-script`
2. Nainstalujte požadované knihovny: `pip install -r requirements.txt`

## Licence
Tento projekt je licencován pod licencí MIT.
