#set -> {} -> tidak berurutan,berubah,tidak berubah
game_azka = {'valorant','delta','roblox'}
game_zaky = {'minecraf','roblox'}
game_azka.add('minecraf')
game_zaky.add('roblox')
game_azka.remove('valorant')
=
print("game_azka:",game_azka)
print("game_zaky:",game_zaky)
game_gabungan = game_azka | game_zaky # | -> (or) atau
print('daftar game:',game_gabungan) 

for game in game_gabungan:
    print(game)
    print('---> transfer data game', game,'ke ps5') 

#dictionary (dict) --> {key:value} / {kunci:isi}
kamus_anime = {
    "demon_slayer":" tanjiro",
    "blue_lock":"isagi ren",
     "waifu": {
         "one_piece":"big mom",
         "demon_slayer":"nezuko",    
     }      
} 

print("kamus_anime:",kamus_anime)
print("MC demon slayer:",kamus_anime["demon_slayer"])
print("waifu one piece:",kamus_anime["waifu"]["one_piece"])
#menambah item baru ke dictionary
kamus_anime["naruto"] = "shikamarau"
print('MC naruto:',kamus_anime["demon_slayer"])
#mengubah item dari dictionary
kamus_anime["demon_slayer"] = "zenitsu"
#menghapus item dari dictionary
del(kamus_anime["blue_lock"])
print('kamus anime terbaru:',kamus_anime)

#merojaah dict
print('=======dictionary=======')
wildan_6 ={
    'umur':'16',
    'asal': 'wonosobo',
    'kelas':'10',
}

print(wildan_6["asal"])

for item in wildan_6:
    print(item)

#menambah nilai
wildan_6['berat badan'] = 75
print(wildan_6)

#mengubah nilai
wildan_6['berat badan'] = 65
print(wildan_6)

#menghapus nilai
del(wildan_6["berat badan"])
print(wildan_6)

#mengecek key
print("umur"in wildan_6)

#mendapatkan semua key dan valuenya
#cara mengecek ada key apa aja
print(wildan_6.keys())

#cara mengecek value apa aja
print(wildan_6.values())

#LOOPING LAGII
for key in wildan_6:
    print(key)

for value in wildan_6.values():
    print(value)

for key, value in wildan_6.items():
    print(f"{key} --> {value}")    


#nested dictionary

# kelas =[
#     "siswa1":{
#         'nama':'harun',
#         'umur':'20',
#         'asal':'bogor',
#         'hobi':{
#             'hobi1':'makan',
#             'hobi2':'joget',
#             'hobi3':'marah',
#             'hobi4':{
#                 'bola1':'bola sepak',
#                 'bola2':'bola basket',
#                 'bola3':'bola voli',
#             }
#         }
        
#     }
#     'siswa2':{
#         'nama':'wildan',
#         'umur':'16',
#         'asal':'wonosobo'
#     }
#     'siswa3':{
#         'nama':'opet',
#         'umur':'34',
#         'asal':'london',
#     }
# ]

# print(f"{key}.{value}")