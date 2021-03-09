#Nama:Sabrina
#UniversitasKristenDutaWacana

#Program untuk menambahkan atau menghapus daftar koleksi buku yang dipunya

print ("""
===DAFTAR BUKU===
1.Tambah Buku
2.Hapus Buku
3.Koleksi Buku
4.Exit
""")
koleksi= ['Matematika','IPA','IPS']
a=0
while a >= 0:
    a= int(input("Masukan Pilihan: "))
    if a == 1:
        nama1=input("Nama Buku: ")
        koleksi.append(nama1)
        print ("Buku", nama1, "berhasil ditambahkan")
    elif a == 2:
        nama2=input("Nama Buku: ")
        koleksi.remove(nama2)
        print ("buku", nama2, "berhasil dihapus")
    elif a == 3:
        z= ",". join(koleksi)
        print (z)
    else:
        break