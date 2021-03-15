#Nama:Sabrina
#Universitas Kristen Duta Wacana

#Membuat program yang dapat menentukan titik awal segitiga berada di tengah,kanan atau kiri dan dapat menentukan ukurannya juga.

print ("""
Pilih bentuk segitiga:
1.Tengah
2.Kanan
3.Kiri
4.Exit
""")
a = 1
while a >= 1 :
    z=int(input("Maukkan pilihan: "))
    if z == 1:
        n=int(input("ukuran: "))
        for i in range (1,n+1):
            jumlah_spasi= n - i
            for j in range (jumlah_spasi):
                print (" ",end ='')
            jumlah_bintang= i
            for j in range (jumlah_bintang):
                print ("*",end=' ')
            print ()
    elif z == 2:
        n=int(input("ukuran: "))
        for i in range (1,n+1):
            jumlah_spasi= n - i
            for j in range (jumlah_spasi):
                print (" ",end =' ')
            jumlah_bintang= i
            for j in range (jumlah_bintang):
                print ("*",end=' ')
            print ()
    elif z == 3:
        n=int(input("ukuran: "))
        for i in range (1,n+1):
            jumlah_spasi= i
            for j in range (jumlah_spasi):
                print ("",end ='')
            jumlah_bintang= i
            for j in range (jumlah_bintang):
                print ("*",end=' ')
            print ()
    else:
        break