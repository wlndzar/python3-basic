import csv

file_uang = r"C:\study\tugaspyton.py\tugas.csv"

with open(file_uang,"r")as file_baru:
    next(file_baru)
    read = csv.reader(file_baru)
    list_read = list(read)

    print("SEMUA DATA")
    print("tanggal | keterangan | kategori |jumlah")
    print("-" * 20)
    for baris in list_read:
        tanggal = baris[0]
        keterangan = baris[1]
        kategori = baris[2]
        jumlah = baris[3]

        print(f"{tanggal} | {keterangan} | {kategori} | {jumlah}")






    
