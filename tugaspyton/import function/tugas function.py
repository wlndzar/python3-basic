print('====tugas pertama===')
import doa_harian
import hitung_uang
import rangking
import emoji


doa_setalah_makan = doa_harian.doa_setalah_makan()
print(f"doa setelah makan:{doa_setalah_makan}")

doa_sebelum_makan = doa_harian.doa_sebelum_makan()
print(f"doa sebelum makan:{doa_sebelum_makan}")

doa_mandi_wajib = doa_harian.doa_mandi_wajib()
print(f"doa mandi wajib:{doa_mandi_wajib}")

print('===tugas kedua===')

uang_jajan = [5000,6000,7000.8000,9000]
print (hitung_uang.tambah_bonus(uang_jajan))

print("-----tugas ketiga-----")
print("<===================>") 
nilai_rangking = [75,90,60,88,100,55]
mood = ["senang","biasa","sedih","semnagat"]

print(rangking.urutkan_nilai(nilai_rangking))