print('=====function======')
#function di awali dengan keyword def
def halo_ngab():
    print('halo ngab')
#function dengan parameter nama
def sapa_sapa(nama):
    print('halo bang',nama)
    print('halo juga bang',nama)
    print('==========')

print('cobain fungsinya')
halo_ngab()
sapa_sapa("fino")
sapa_sapa('azzam')
sapa_sapa('wildan')

#fungsi luas persegi panjang
def luas_presegi_panjang(panjang,lebar):
    print(">panjang:",panjang)
    print(">lebar:",lebar)
    rumus = panjang * lebar
    print("luas persegi panjang =",rumus)
   
luas_presegi_panjang(10,20)
luas_presegi_panjang(30,50 )
