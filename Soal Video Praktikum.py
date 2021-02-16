#Nama:Sabrina
#NIM: 71200675

#Seorang guru ingin mengetahui jumlah nilai, rata - rata, dan nilai tertinggi pada 5 orang muridnya

Banyak_murid= int(input("Masukkan Jumlah Murid: "))

N1=float(input("Masukkan Nilai 1: "))
N2=float(input("Masukkan Nilai 2: "))
N3=float(input("Masukkan Nilai 3: "))
N4=float(input("Masukkan Nilai 4: "))
N5=float(input("Masukkan Nilai 5: "))

jumlah= N1 + N2 + N3 + N4 + N5
print ("Jumlah total nilai semua murid", jumlah)

mean= jumlah / Banyak_murid
print("Rata - rata Nilai murid adalah: ", mean)

tertinggi= max(N1, N2, N3, N4, N5)
print ("Nilai tertinggi adalah: ", tertinggi)