import sorting as sort

#bubblesort
mahasiswa =['andi', 'budi', 'ana', 'rina', 'uswa']
mahasiswa.sort()
print (f'{mahasiswa}')

#sort.SelectionSort()
angka = [23,7,32,99,4,15,11,20]
SelectionSort = sort.SelectionSort(angka)
print(angka)

#insert
list = [12, 23, 34, 52, 8, 44, 43, 45, 78]
print('Data sort :', list)
qs = sort.qs(list,0,len(list)-1)

#Mergesrt
print('Menggabungkan List', list)
list = [2,5,60,43,27,10,89,17]
ms = sort.ms(list)

#quick
list = [67,91,87,33,49,10,16,43,65,3]
print('Data yg akan di sort :', list)
print('Quick Sort :')
qs = sort.qs(list,0,len(list)-1)


