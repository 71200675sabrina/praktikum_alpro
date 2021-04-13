#Nama:Sabrina
#Universitas Kristen Duta Wacana

#Rani seorang guru baru di SD8 ingin mengumpulkan nilai siswanya yang berisikan
#Nama,Nilai Matematika,kimia dan fisika
#bantulah rani membuat program tersebut dan dalam file.

print("Program Pengumpulan Nilai")
print ("============================")
print ("""
1.Menambahkan Nilai
2.Daftar Nilai
3.Jumlah Siswa yang terdaftar
4.Exit
""")
a=1
while a >= 1:
    inp = int(input("Masukkan pilihan anda: "))
    if inp == 1:
        nama = str(input("Nama: "))
        mat = int(input("Matematika: "))
        kimia = int (input ("Kimia: "))
        fisika = int(input("Fisika: "))

        teks = "\nNama: {}\nMatematika: {}\nKimia: {}\nFisika: {} \n---".format(nama,mat,kimia,fisika)

        file = open('daftarnilai.txt',"a")
        file.write(teks)
        file.close()
    elif inp == 2:
        file2= open('daftarnilai.txt')
        print (file2.read())
        file2.close()
    elif inp == 3:
        file3= open('daftarnilai.txt',"r")
        c = 0
        for line in file3:
            if line.find("Nama") != -1:
                c += 1
        print ("jumlah: ",c)
    elif inp == 4 :
        print ("Terimakasih telah menggunakan program ini!")
        break
    else:
        print ("pilihan anda tidak terdaftar,silahkan coba lagi")
        
