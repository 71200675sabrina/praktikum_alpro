#Nama: Sabrina
#Nim:71200675

#buatlah program yang dapat menhitung luas dan keliling persegi

print ("Selamat datang di program menghitung luas dan keliling persegi")
print ("1.Menghitung Luas")
print ("2.Menghitung Keliling")
a= int(input("Apa yang ingin anda proses: "))
b= float(input("Masukkan sisi:"))
if a == 1:
    luas= b**2
    print ("Luas persegi adalah", luas)
else:
    keliling= 4*b
    print ("Keliling persegi adalah", keliling)
print ("Terimakasih telah menggunakan program ini")