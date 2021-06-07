#Nama: Sabrina
#Universitas Kristen Duta Wacana

#Untuk menjadi selebgram dina harus menambahkan 10 hashtag disetiap foto


def hashtag (string):
    import re
    k = string
    x = re.sub('\s','#',k)
    print ("Hashtag for caption :", x)
    import re
    k1 = x
    x1 = re.findall('#',k1)
    print (x1)
    print ("Jumlah Hashtag terbentuk: ",(len(x1)))

hashtag(' mantap cool keren fff lfl sfs good like fav food pictfun')
        
    
