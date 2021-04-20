#Nama: Sabrina
#Universitas kristen Duta Wacana

#Membuat suatu sistem pendaftaran pekan olimpiade sekolah, agar siswa bisa
#berpartisipasi dalam POS


print (" Pekan Olimpiade Sekolah")
print ("===========================")
username =['budi','andi','putri','diva']
pelajaran = ['matematika','fisika','kimia','biologi']
a=1
while a>=1:
    print ("""
1.Pendaftaran
2.Daftar pelajaran
3.Daftar peserta
4.Pembatalan peserta
5.Exit""")
    inp = int(input("Masukkan pilihan anda: "))
    if inp == 1:
        nama = input("Nama: ")
        username.append(nama)
        kelas = input("Kelas: ")
        mapel = input ("Mata pelajaran: ")
        print ("Pendaftaran berhasil!")
    elif inp == 2:
        print ("Mata pelajaran yang diujikan")
        pelajaran.sort()
        bu = ",".join(pelajaran)
        print (bu)
    elif inp == 3:
        print ("Daftar peserta")
        username.sort()
        go = "|".join(username)
        print (go)
    elif inp == 4:
        delt = input("Nama: ")
        if delt not in username:
            print ("Data", delt,"tidak ditemukan")
        else:
            username.remove(delt)
            print ("Data",delt,"berhasil di hapus")
    else:
        print ("Terimakasih!")
        break
