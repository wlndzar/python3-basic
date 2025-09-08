#TUGAS DARI MAS HAMKA!!!

print('======jadwal piket harian======')

piket_hari_ini = ["ali","budi","aisyah"]
print("jadwal piket hari:")
for item in piket_hari_ini:
    print("-",item)

print("=======rukun islam========")
rukun_islam = ("syahadat","sholat","pausa","bayar zakat","haji dan umroh")
print('rukun islam')
for i in range(len(rukun_islam)):
    print(f"{i + 1}.{rukun_islam[i]}")

print("=======kitab pelajaran=====")
kitab_pelajaran = {"kitab tajwid","kitab fiqih","kitab aqidah"} 
print("kitab kitab yang di pelajari:")
for i in kitab_pelajaran:
    print("-",i)

print("=======biodata santri========")    
biodata = {
    'nama':'wildan',
    'kelas':'10-A',
    'hafalan juz':20
}

print("biodata santri:")
for keys, Value in biodata.items():
    print(f"{keys}.{Value}") 



