import csv
print('=========file=======')
print("--------------------")

#merojaah csv

file_jajan = r"C:\study\materi-kelas\jajan.csv"

with open(file_jajan,"r")as file_baru:
    next(file_baru)
    read = csv.reader(file_baru)
    list_read = list(read)

    print("semua data")
    print("-" * 20)
    for baris in list_read:
        nomor = baris[0]
        nama = baris[1]
        kelas = baris[2]

        print(f"{nomor} | {nama} | {kelas}")

#tmabah data
with open(file_jajan, "a",newline="")as file_baru:
    write = csv.writer(file_baru)
    write.writerow(["5","ucok","10"])

