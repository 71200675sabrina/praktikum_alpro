#Nama: Sabrina
#Universitas Kristen Duta Wacana

#Buatlah suatu program yang dapat menghitung harga total buku yang dibeli,apabila
#daftar buku dan harga terdapat didalam dict dan urutkan
buku = {'Matematika':50000,'IPA':20000,'IPS':30000}
buku_ = list(buku.items())
buku1 = (buku_[0])
buku2 = (buku_[1])
buku3 = (buku_[2])

def hargatotal (jlh,namab) :
    if namab in buku1 :
        total = int(buku1[1]) * int(jlh)
        print ("Harga Total = ", total)
    elif namab in buku2 :
        total2 = int(buku2[1]) * int(jlh)
        print ("Harga Total = ", total2)
    elif namab in buku3 :
        total3 = int(buku3[1]) * int(jlh)
        print ("Harga Total = ", total3)
    else :
        print ("Buku tidak terdaftar, coba ulangi!!")

buku_.sort()
print (buku_)
hargatotal (5,'IPA')

