#
daftar_belanja = ['teh','nasi','pisang']

#
print('isi tas belanja:',daftar_belanja)
print('item ke-1:',daftar_belanja[0])
print('item ke-2:',daftar_belanja[2])

#append() menambah item baru ke akhir list
daftar_belanja.append('ayam')
daftar_belanja.append('susu')
print('isi tas belanja skrg:',daftar_belanja)
print('item ke-4:',daftar_belanja[3])
#remove()menghapus item dari list
daftar_belanja.remove('pisang')
print('isi tas belanja akhir:',daftar_belanja)
#insert menambah item terserah,mau di taro dimana
daftar_belanja.insert(1,'gorengan')
print(daftar_belanja)
#menghapus berdasarkan index
daftar_belanja.pop(0)
print(daftar_belanja)
# panjang list
print(len(daftar_belanja))
#mencetak seluruh list menggunakan looping
for item in daftar_belanja:
    print(item)

print('======tuple======')
#tuple (berurut,tdk bisa di ubah,boleh di duplikat)
#penulisan menggunakan ()

ttl= ('wonosobo', 25, 'juli',2009)
print("tanggal lahir ujang:",ttl)
 
 #[no_index]akses data tupl
print('tempat lahir:',ttl[0])
print("tanggal:",ttl[1])
print("bulan:",ttl[2])
print('tahun:',ttl[3])
#
print('bulan tahun:',ttl[2:4])
#
tempat_lahir, tgl_lahir ,bulan_lahir, tahun_lahir = ttl
print(tempat_lahir)

#manipulasi list lanjutan
jajan_dihya = ['bakso','susu']
jajan_wildan = ['tahu','gabin']
jajan_dihya_dan_wildan = jajan_dihya + jajan_wildan 
print(jajan_dihya_dan_wildan)
#list multi-dimensi
list_minuman = [
   ['kopi','susu','doger'],
   ['jus apel''es teh','teler'],
   ['campur','dawet','es'],]
print(list_minuman)   
print(list_minuman[0][1]) 

#merojaah list
print('=======list=======')
list_buah = [] 
