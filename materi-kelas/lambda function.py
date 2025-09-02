print('======lambda function======')
print('---------------------------')
#function tidak akan di eksekusi jika tidak pri
def say_hello(name):
    print(f"halo mas.{name}")
    print('baik baik yaaa')


#lambda untuk di sebut menulis fungsi yg ringkas dgn satu baris saja
#sering di sebut juga fungsi anomim (tanpa nama)
say_hello_mini = lambda name:print(f'hello mas.{name}')

#panggil fungsi2nya di bawah sini
say_hello('ibrohim')
say_hello('ghozy')
print('====================')
say_hello_mini('rosyid')
say_hello_mini('harun')
say_hello_mini('dihyah')

#contoh penerapan lambda dgn higher-
jajan_mingguan = [50000,30000,70000,10000,45000,15000]
#sofred()--> mengurutkan data
urutkan_uang =sorted(jajan_mingguan)
urutan_uang_terbalik = sorted(jajan_mingguan,reverse=True)
print(f'ururtan uang:{urutkan_uang}')
print(f'urutan uang terbalik:{urutan_uang_terbalik}')
#map()-> mentransformasi data
kurangi_uang = map(lambda uang:uang - 5000, jajan_mingguan)

list_kurangin_uang = list(kurangi_uang)
print(f"map uang berkurang: {list_kurangin_uang}")

#filter()-> menyaring / memfilter data
filter_jajan_banyak  = filter(lambda uang: uang > 30000,jajan_mingguan)
list_jajan_banyak = list(filter_jajan_banyak)
print(f"filter jajan diatas 30rb:{list_jajan_banyak}")

#panggil module kumpulan doa
import doa
import random
import math
#import math(module matematika)
doa_mandi = doa.doa_mandi_wajib()
print(f'doa mandi wajib: {doa_mandi}')
tebak_angka = random.randint(1, 1000)
print(f'tebak angka: {tebak_angka}')
jari_jari = 14
luas_lingkaran = math.pi * jari_jari * jari_jari
print(f'niali pi: {math.pi}')
print(f'luas lingkaran: {luas_lingkaran}')