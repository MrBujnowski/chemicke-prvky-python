import csv
import json


class DataLoader:
    def __init__(self, csv_file=None, json_file=None):
        """
        Inicializuje DataLoader s volitelnými cestami k CSV a JSON souborům.
        """
        self.csv_file = "elements.csv"
        self.json_file = "groups.json"
        self.data_from_csv = []
        self.data_from_json = []

    def load_csv(self):
        """
        Načte data z CSV souboru do seznamu slovníků.
        """
        if not self.csv_file:
            print("Cesta k CSV souboru není nastavena.")
            return

        try:
            with open(self.csv_file, 'r', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                self.data_from_csv = [row for row in reader]
                print(f"Data z CSV byla úspěšně načtena. Načteno {len(self.data_from_csv)} řádků.")
        except FileNotFoundError:
            print(f"CSV soubor '{self.csv_file}' nebyl nalezen.")
        except Exception as e:
            print(f"Chyba při načítání CSV: {e}")

    def load_json(self):
        """
        Načte data z JSON souboru do seznamu slovníků.
        """
        if not self.json_file:
            print("Cesta k JSON souboru není nastavena.")
            return

        try:
            with open(self.json_file, 'r', encoding='utf-8') as f:
                self.data_from_json = json.load(f)
                print(f"Data z JSON byla úspěšně načtena. Načteno {len(self.data_from_json)} záznamů.")
        except FileNotFoundError:
            print(f"JSON soubor '{self.json_file}' nebyl nalezen.")
        except json.JSONDecodeError as e:
            print(f"Chyba při načítání JSON: {e}")

    def display_data(self):
        """
        Zobrazí data načtená z obou zdrojů.
        """
        print("\n--- Data z CSV souboru ---")
        for i, row in enumerate(self.data_from_csv, start=1):
            print(f"{i}: {row}")

        print("\n--- Data z JSON souboru ---")
        for i, item in enumerate(self.data_from_json, start=1):
            print(f"{i}: {item}")


# Příklad použití
loader = DataLoader(csv_file='elements.csv', json_file='groups.json')

# Načtení dat
loader.load_csv()
loader.load_json()

# Zobrazení načtených dat
loader.display_data()
