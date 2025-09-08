import requests
url = f"https://api.alquran.cloud/v1/ayah/2:255/quran-simple"
response = requests.get(url) #http git (ambil data)
data_json = response.json()

nama_surah = data_json["data"]
print(f"ayat al-kursi (2:225) -arab : {nama_surah["text"]}")


import requests
url = f"https://api.alquran.cloud/v1/ayah/2:255/en.asad"
response = requests.get
data_json = response.json()

nama_surah = data_json["data"]
print(f"terjemahan (EN) : {nama_surah["text"]}")