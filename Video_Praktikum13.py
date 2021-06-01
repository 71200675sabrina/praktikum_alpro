#Nama : Sabrina
#Universitas Kristen Duta Wacana
#link:https://jagongoding.com/python/latihan-logika/mencari-nilai-maksimum-dan-minimum/#menggunakan-perulangan-rekursi
#program yang dapat menampilkan nilai terkecil!

angka = [3, 0.5 , 3, 4, 67,2 , 20]

def nilai_min (list):
    nilai_kecil = list[0]
    
    print (f'{list} -> {nilai_kecil}')
    if len(list) > 1 :
        nilai_kecil2 = nilai_min(list[1:5])

        if nilai_kecil2 < nilai_kecil:
            nilai_kecil = nilai_kecil2
    print (f'{list} -> {nilai_kecil}')
    return nilai_kecil
print (angka)
print ('Nilai terkecil: ',nilai_min(angka))

