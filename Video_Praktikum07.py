#Nama:Sabrina
#UniversitasKristenDutawacana

#program yang dapat meghitung kata yang terdapat dalam suatu kalimat.
#contoh kalimat:
#'Penggambaran para tokoh yang ada pada cerita tersebut cenderung sederhana dan tidak terlalu detail.' #=14
#text2='Penokohan yang dimaksud disini adalah suatu bentuk penggambaran tokoh beserta dengan sifat yang dimiliki. Dalam penokohan ini terdapat dua cara dalam menentukan penokohan, yaitu melalui metode analitik serta metode dramatik'#.= 30
#text3='Sudut pandang orang ketiga serbatahu (pengarang cerita biasanya menceritakan tokoh bernama dia dengan sangat detail sekali)' #= 16

def hitung_kata (kalimat):
    kalimat.lower
    hasil=kalimat.split(" ")
    print (len(hasil),"kata")
text= str(input("Masukkan kalimat: "))
hitung_kata(text)