#nama: Sabrina
#Universitas Kristen Duta Wacana

#https://tutorallprogramming.blogspot.com/201/12/contoh-program-fungsi-pada-python.html

#Membuat fungsi untuk menghitung nilai total dari nilai quiz,uts,dan uas murid serta tingkat kerajinannya.
#quiz 20% , uts 40% , uas 40%

def jumlah_nilai (quiz, uts, uas):
    quiz= float (quiz) * 0.2
    uts= float (uts) * 0.4
    uas= float (uas) * 0.4

    nilai_total= quiz + uts + uas
    return nilai_total

def kerajinan (total_nilai):
    if total_nilai > 80:
        print ("Kerajinan A")
    elif total_nilai == 80:
        print ("Kerajinan B")
    else:
        print ("Kerajinan C")

quiz= float(input("Masukkan nilai quiz:"))
uts= float(input("Masukkan nilai uts: "))
uas= float(input("Masukkan nilai uas: "))
print ("total nilai: ", jumlah_nilai(quiz, uts, uas))
total_nilai = jumlah_nilai (quiz, uts, uas)
print (kerajinan(total_nilai))

