#contoh Buble Sort
#membandingkan masing-masing item secara berpasangan, menukar item jika diperlukan, 
#dan mengulaginya sampai akhir list secara berurutan hingga tidak ada item yang dapat ditukar
mahasiswa =['andi', 'budi', 'ana', 'rina', 'uswa']
print(f'sebelum: {mahasiswa}')
mahasiswa.sort()
print (f'sesudah: {mahasiswa}')

#contoh insertion sort
#memilah data yg akan diurutkan menjd dua bagian, yg belum diurutkan dan yg sudah diurutkan. 
# Elemen pertama diambil dr bagian array yg blm diurutkan dan lalu diletakkan sesuai posisinya 
# pada bagian lain dari array yg telah diurutkan. Langkah ini dilakukan secara berulang hingga 
# tidak ada lagi elemen yang tersisa pada bagian array yang belum diurutkan
list = [12, 23, 34, 52, 8, 44, 43, 45, 78]
for i in range(1,len(list)):
    currentvalue=list[i]
    possition=i
    while(possition>0 and list[possition-1]>currentvalue):
        list[possition]=list[possition-1]
        possition=possition-1
    list[possition]=currentvalue
    print(list)

#contoh Selection Sort
#memilih elemen dengan nilai paling rendah dan menukar elemen yang terpilih dengan elemen ke-i. 
#Nilai dari i dimulai dari 1 ke n, dimana n adalah jumlah total elemen dikurangi 1.
def SelectionSort(val):
   for isi in range(len(val)-1,0,-1):
       Max=0
       for lokasi in range(1,isi+1):
           if val[lokasi]>val[Max]:
               Max = lokasi
 
       temp = val[isi]
       val[isi] = val[Max]
       val[Max] = temp
 
DaftarAngka = [23,7,32,99,4,15,11,20]
SelectionSort(DaftarAngka)
print(DaftarAngka)

#algoritma yang stau jenis dengan insertion sort, dimana pada setiap nilai i dalam n/i item 
#diurutkan. Pada setiap pergantian nilai, i dikurangi sampai 1 sebagai nilai terakhir
def Mergesrt(alist):
    print("Memisahkan", alist)
    if len(alist)>1:
        mid = len(alist)//2
        setkiri = alist[:mid]
        setkanan = alist[mid:]
        Mergesrt(setkiri)
        Mergesrt(setkanan)
        i=0
        j=0
        k=0
        while i < len(setkiri) and j < len(setkanan):
            if setkiri[i] < setkanan[j]:
                alist[k]=setkiri[i]
                i=i+1
            else:
                alist[k]=setkanan[j]
                j=j+1
            k=k+1
        while i < len(setkiri):
            alist[k]=setkiri[1]
            i=i+1
            k=k+1
        while j < len(setkanan):
            alist[k]=setkanan[j]
            j=j+1
            k=k+1
        print("Menggabungkan",alist)
    m = [54,67,99,34,32,8]
    Mergesrt(m)
    print(m)

#metode pertambahan menurun (diminishing increment)
#Metode ini mengurutkan data dengan cara membandingkan suatu data dengan data lain yang 
# memiliki jarak tertentu, kemudian dilakukan penukaran bila diperlukan
def shellsrt(alist):
    sublst = len(alist)//2
    while sublst > 0:
        for startposition in range(sublst):
            gapInsertionSort(alist,startposition,sublst)
        print("abis di increment", "listnya jadi",alist)
        sublst = sublst // 2
def gapInsertionSort(alist,start,gap):
    for i in range(start+gap,len(alist),gap):
        Value = alist[i]
        position = i
        while position>=gap and alist[position-gap]>Value:
            alist[position]=alist[position-gap]
            position = position-gap
        alist[position]=Value
alist = [47,43,54,54,75,78,42,78,56]
shellsrt(alist)
print(alist)


print ("Merge Sort")
def ms (list):
    print('Memecah List', list)
    n = len(list)
    if n < 2:
        return list
    else:
        mid=n//2
        left=list[:mid]
        right=list[mid:]
        ms(left)
        ms(right)
        i=0
        j=0
        k=0
        while i < len (left) and j < len (right):
            if left[i]>right[j]:
                list[k]=left[i]
                i=i+1
            else:
                list[k]=right[j]
                j=j+1
            k=k+1
            while i < len (left):
                list[k]=left[i]
                i=i+1
                k=k+1
            while j < len (right):
                list[k]=right[j]
                j=j+1
                k=k+1
    print('Menggabungkan List', list)
list = [2,5,60,43,27,10,89,17]
ms(list)


print("Quick Sort") 
def qs(list,awal,akhir):
    if awal < akhir:
            pindex = partisi(list,awal,akhir)
            qs(list,awal,pindex-1)
            qs(list,pindex+1,akhir)

def partisi(list,awal,akhir):
    tengah = int(akhir/2)
    pivot = list[tengah]
    pindex = awal
    for i in range(awal,tengah):
        if list[i]>=pivot:
            list[i],list[pindex]=list[pindex],list[i]
            pindex = pindex + 1
    list[pindex],list[tengah]=list[tengah],list[pindex]
    print(list)
    return pindex
    
list = [67,91,87,33,49,10,16,43,65,3]
print('Data yang akan di sort :', list)
print('Quick Sort :')
qs(list,0,len(list)-1)