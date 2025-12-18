import requests
from tabulate import tabulate

print("=== PokeAPI Project ===")
pokemon_name = input("Masukkan nama Pokemon: ")

target_url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}"
print(f"Target URL: {target_url}")
response = requests.get(target_url)

if response.status_code != 200:
    print("Pokemon tidak ditemukan")
else:
    data_json = response.json()


    name = data_json["name"]
    height = data_json["height"]
    weight = data_json["weight"]
    abilities = data_json["abilities"]
    print("\n=== HASIL DATA POKEMON ===")
    print(f"|  Nama  |  Tinggi  |  Berat  |  Ability  |")
    print(f"{name}")
    print(f"{height}")
    print(f"{weight}")
    print("Ability:")

    for ability in abilities:
        ability_name = ability["ability"]["name"]
        print(f"- {ability_name}")

# Siapkan data untuk tabel info utama
info_table = [
    ["Name", name],
    ["Height", height],
    ["Weight", weight],
]

print("\n=== INFO POKEMON ===")
print(tabulate(info_table, tablefmt="grid"))

# Siapkan tabel abilities
abilities_table = []
for idx, ability in enumerate(abilities, start=1):
    ability_name = ability["ability"]["name"]
    abilities_table.append([idx, ability_name])

print("\n=== ABILITIES ===")
print(tabulate(abilities_table, headers=["No", "Ability"], tablefmt="grid"))
