import json
print("===materi 12 - json file handling===")
print("===read json===")
file_path_json = r"C:\study\materi-kelas\materi.json"
with open(file_path_json, "r")as file_materi:
    #json.load() -> membaca isi file json
    data_materi = json.load(file_materi)
    print(f"judul berkas: {data_materi["title"]}")
    print(f"total kelas A: {data_materi['total']}")
    print(f"status santri: {data_materi['status_santri']}")
    print(f"status kelulusan: {data_materi['status_lulus']}")
    #ekstrak data list dengan for loop
    for pelajaran in data_materi['pelajaran']:
        print(f"--> {pelajaran}")

    print("-" * 50)
    print("|no|nama surah|ayat|tempat turun|")
    print("-" * 50)
    for surah in data_materi['surah']:
        print(f"| {surah['no']} | {surah['nama']} | {surah['ayat']} | {surah['turun']} | ")
            

