import requests

# URL k vašemu TXT souboru na GitHubu
txt_url = "https://raw.githubusercontent.com/liborgit/davmo-print-scrip/main/model_order_list/order_list.txt"

try:
    # Načtení seznamu souborů ze serveru
    response = requests.get(txt_url)

    # Ověření, zda server vrátil úspěšnou odpověď
    if response.status_code == 200:
        # Rozdělení obsahu TXT souboru na seznam souborů
        seznam_souboru = response.text.splitlines()
        print("TXT data byla úspěšně načtena:", seznam_souboru)
    else:
        print(f"Chyba: Server vrátil stavový kód {response.status_code}")
except requests.exceptions.RequestException as e:
    print(f"Došlo k chybě při odesílání požadavku: {e}")