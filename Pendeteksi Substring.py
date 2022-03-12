
x = input("String 1: ")
y = input("String 2: ")

def polastring(x,y):
    counter  = 0
    cek2 = True
    if(len(x)>len(y)):
        i1 = 0
        i2 = 0
        while((i1 <= len(x) - len(y)) and cek2):
            cek = True
            i2 = i1
            z = 0
            counter = counter + 1
            while((z<len(y)) and cek):

                if(y[z]!= x[i2]):
                    cek = False

                elif(y[z] == x[i2] and (z == (len(y)-1))):
                    print(i2 - z)
                    cek2 =  False

                i2 = i2+1
                z =z + 1
            i1 = i1+1
            if (i1 > len(x) - len(y)):
                print("Jumlah Perbandingan: ",counter)
            

polastring(x,y)


