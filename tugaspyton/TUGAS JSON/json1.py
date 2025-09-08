import json

file_path = r"C:\tugas python\tugaspyton.py\tugas json\data.json"

with open(file_path, "r") as file_materi:
    data_materi = json.load(file_materi)

print("data materi")

total_pinjam = 0
belum_kembali = 0

print("belum kembali:")
for anggota in data_materi["anggota:"]:
    for buku_pinjaman in anggota["pinjam"]:
        total_pinjam += 1
        if buku_pinjaman["kembali"] == False:
            buku_kembali += 1
            print(f"- {anggota['nama']} : {buku_pinjaman['judul']} ({buku_kembali['tanggal']})")

print(f"total pinjaman: {total_pinjam} | belum kembali: {belum_kembali}")
