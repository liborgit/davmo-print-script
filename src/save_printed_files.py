import os

# Načtení seznamu již vytisknutých souborů
printed_files = []
if os.path.exists("printed_files.txt"):
    with open("printed_files.txt", "r") as f:
        printed_files = f.read().splitlines()

# Výpis seznamu vytisknutých souborů
print("Seznam vytisknutých souborů:", printed_files)