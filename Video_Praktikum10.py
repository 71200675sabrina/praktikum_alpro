#Nama: Sabrina
#Universitas Kristen Duta Wacana

#Permasalahan buatlah pemograman kamus offline indonesia bahasa inggris

print ("Selamat datang di Kamus Offline")
print ("===============================")
ind2eng = dict ()
a = 1
while a>= 1:
    print ("""
Kamus Indonesia -> Inggris
1.Tambah kosa kata
2.Translate
3.Daftar kosa kata
4.Menghapus kosa kata
5.Exit
""")
    input1 = int(input("Masukkan Pilihan Anda: "))
    if input1 == 1:
        x = str(input("Masukkan kata Bahasa Indonesia : "))
        y =str(input("Masukkan kata Bahasa Inggris : "))
        ind2eng [x] = y
    elif input1 == 2:
        kata2 = str(input("Masukkan kata Bahasa Indonesia : "))
        if kata2 in ind2eng :
            print (ind2eng[kata2])
        else:
            print ("Kata tidak ditemukan,silahkan ulangi kembali")
    elif input1 == 3:
        print (ind2eng)
    elif input1 == 4:
        kata3 = str(input("Masukkan Kata Bahasa Indonesia: "))
        del (ind2eng[kata3])
        print ("Kata berhasil dihapus")
    else:
        print ("Terimakasih!!")
        break
    
