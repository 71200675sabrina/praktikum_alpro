#Nama: Sabrina
#Universitas Kristen Duta Wacana

#Buatlah sebuah fungsi yang dapat menghapus nama satu siswa yang batal ikut
#lomba cerdas cermat.

Matematika = {'Budi','Andi','Rahel','Lisa','Rose'}
Fisika = {'Andi','Ridwan','Budi','Daya','Lisa'}

def batal_ikut (set1,set2,batal,batal2):
    gabung = set1 | set2
    gabung.remove (batal)
    gabung.remove (batal2)
    print (gabung)
    total = len(gabung)
    print ("Total Siswa yang ikut =" , total)
batal_ikut (Matematika,Fisika,'Lisa','Ridwan')

